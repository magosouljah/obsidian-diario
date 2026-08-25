# Tarea 5.1 — Delete cross-bot y cleanup Direct

**Estado:** decisión/evidencia documental; prueba live cross-bot pendiente.  
**Fecha:** 2026-08-25, `America/Mexico_City`.  
**Tarea propietaria:** Fase 0, Tarea 5.1 — límites de confianza Direct.  
**No cierra 5.1:** ningún checkbox pasa a `[x]` por esta nota.

> Objetivo de esta nota: conservar en un solo lugar la arquitectura que BeatGaler ya había diseñado parcialmente y evitar volver a confundir el rol de MASTER, Bot API y transport bots durante reemplazos de media.

## 1. Problema real que debe resolver BeatGaler

BeatGaler usa un pool de **transport bots**. Un vault puede haber sido atendido por distintos transport bots a lo largo del tiempo, aunque en una sesión dada exista un transport bot actual.

Por tanto, dentro de un mismo vault pueden coexistir mensajes de media creados por transport bots de sesiones anteriores. Un MASTER/MP3 que hoy debe reemplazarse puede haber sido enviado por otro transport bot y puede tener mucho más de 48 horas.

Caso obligatorio:

```text
Sesión vieja
Bot A -> vault -> MASTER viejo, message_id=100

pasan días/semanas

Sesión actual
Bot B -> mismo vault -> reemplaza MASTER
```

Bot B debe poder dejar el MASTER nuevo como autoridad y eliminar el mensaje 100 aunque:

- Bot B no sea su autor;
- Bot A ya no sea el bot de la sesión;
- el mensaje tenga más de 48 horas;
- MASTER no ejecute el borrado rutinario.

## 2. Lo que aprendimos de Telegram

### 2.1 Bot API NO sirve como mecanismo correcto para cleanup histórico

La Bot API documenta para `deleteMessage` que un mensaje solo puede borrarse si fue enviado hace menos de 48 horas. `deleteMessages` hereda las limitaciones de `deleteMessage`.

Referencias oficiales:

- https://core.telegram.org/bots/api#deletemessage
- https://core.telegram.org/bots/api#deletemessages

Conclusión BeatGaler:

**Bot API puede seguir siendo útil donde corresponda, pero no puede ser la dependencia de corrección para borrar media obsoleta histórica.** Un Replace no puede asumir que el asset sustituido tiene menos de 48 horas.

### 2.2 MTProto sí tiene el primitivo que necesitamos

Telegram expone `channels.deleteMessages` para borrar mensajes de un channel/supergroup. La documentación oficial indica que **users y bots pueden usar este método**, exige ser admin cuando corresponda y no documenta el límite de 48 horas de Bot API.

Referencia oficial:

- https://core.telegram.org/method/channels.deleteMessages

El método trabaja con:

```text
channel/supergroup + message IDs
```

No necesita que el bot autor original siga siendo el transport bot activo.

### 2.3 `delete_messages` cubre el caso Bot B -> mensaje de Bot A

`chatAdminRights.delete_messages` permite al admin borrar también mensajes de otros admins en el channel/supergroup.

Referencia oficial:

- https://core.telegram.org/constructor/chatAdminRights

Esto encaja con el caso BeatGaler:

```text
Bot A creó el mensaje viejo
Bot B es el transport bot actual
Bot B tiene delete_messages baseline
Bot B usa channels.deleteMessages(vault, [old_message_id])
```

## 3. BeatGaler YA tenía la mitad importante implementada

En el baseline Cloud auditado `626efe933cb61130d5f7d20bcdd398f53b61d434`, `cloud-server/direct-transport-control.js` ya hace que MASTER invite y promueva al transport bot con derechos de data plane estables:

```text
deleteMessages: true
pinMessages: true
other: true
```

El comentario del propio código dice que esos derechos existen para que el transport bot mantenga el índice único y elimine media reemplazada.

Por tanto, **la idea original no era que MASTER cargara con todos los deletes de media**. MASTER ya preparaba al transport bot para hacer ese trabajo.

Lo que quedó mal/incompleto en el runtime posterior fue la ruta concreta de borrado: el helper de Desktop terminó dependiendo de Bot API para eliminar media obsoleta, y Bot API choca con el límite de 48 horas.

## 4. División correcta de responsabilidades

### MASTER / control plane

MASTER debe encargarse de operaciones administrativas/control plane necesarias, por ejemplo:

- resolver/asignar vault;
- introducir el transport bot cuando la lease lo requiera;
- conceder los **permisos baseline mínimos y estables** necesarios;
- administrar membership/roles cuando realmente cambie la lease;
- recovery administrativo excepcional.

MASTER **NO debe ser el worker central de cleanup de MP3/WAV/artwork/project de todas las sesiones**.

### Transport bot actual / data plane

El transport bot actual debe ejecutar las operaciones normales de la sesión contra su vault, incluyendo:

- upload directo;
- operaciones de INDEX que le correspondan;
- delete de media obsoleta propia;
- **delete cross-bot de media obsoleta creada por transport bots anteriores**, mediante MTProto cuando Bot API no sea suficiente.

Esto distribuye el trabajo por sesión/bot en vez de concentrarlo en MASTER.

## 5. Flujo correcto de Replace

Orden de seguridad obligatorio:

```text
1. Bot B sube el nuevo MASTER/media directamente a Telegram.
2. BeatGaler obtiene y persiste los IDs nuevos.
3. BeatGaler construye/publica el INDEX nuevo.
4. El INDEX nuevo queda confirmado como autoridad.
5. BeatGaler calcula referencias obsoletas = INDEX anterior - INDEX nuevo.
6. Bot B, usando su identidad MTProto y delete_messages baseline,
   llama channels.deleteMessages(vault, obsolete_message_ids).
7. Si cleanup falla, el INDEX nuevo NO se revierte: queda deuda de cleanup para retry.
```

Nunca hacer:

```text
borrar asset viejo -> luego intentar publicar INDEX nuevo
```

porque un fallo intermedio podría dejar pérdida real.

## 6. Regla de permisos: estable, no churn

Tarea 5.1 ya probó que cambios administrativos frecuentes pueden disparar `FLOOD_WAIT`, incluso impidiendo una restauración inmediata del permiso.

Por eso queda fuera de la arquitectura:

```text
grant delete -> borrar -> revoke delete
```

También queda fuera promote/demote por cada operación o chunk.

Si la prueba live confirma que `delete_messages` es necesario para cross-bot —la documentación oficial indica que sí es el derecho adecuado— debe quedar como **baseline mínimo estable** mientras el transport bot sea admin del vault durante su lease/membership.

La reducción de blast radius se obtiene con:

- temporary auth;
- membership acotada;
- aislamiento tenant/vault;
- sesión/lease acotada;
- permisos baseline mínimos;
- admission control;

no con permission churn por operación.

## 7. Relación con temporary auth de 5.1

M0-B2 ya demostró que una identidad bot puede ejecutar RPC MTProto directo usando la frontera temporary-auth propuesta sin entregar permanent bot credentials al cliente.

Por tanto, el target productivo no debe reintroducir `bot_token`, API hash o permanent auth key en el cliente solo para poder borrar.

La operación final a demostrar es conceptualmente:

```text
transport bot actual
+ temporary auth válida
+ membership del vault
+ delete_messages baseline
-> channels.deleteMessages(old_message_ids)
```

Los bytes de los archivos siguen siendo:

```text
dispositivo <-> Telegram
```

Galer Cloud no se convierte en relay.

## 8. Escalabilidad

La arquitectura buscada es horizontal:

```text
sesión A -> transport bot asignado -> cleanup de su vault
sesión B -> transport bot asignado -> cleanup de su vault
sesión C -> transport bot asignado -> cleanup de su vault
```

MASTER no debe procesar todos los deletes rutinarios de todas las sesiones.

MASTER sigue siendo control plane. Los transport bots ejecutan el trabajo normal del data plane.

Antes de producción deben medirse:

- deletes por bot/vault;
- `FLOOD_WAIT`/rate behavior de RPCs necesarios;
- joins/leaves administrativos;
- número de vaults/bots concurrentes;
- cola/admission control;
- aislamiento cuando un transport bot pueda pertenecer a más de un vault.

## 9. Cleanup debt / garbage journal

Si el INDEX nuevo ya quedó autoritativo y Telegram rechaza temporalmente el delete de uno o más mensajes viejos:

- no revertir el INDEX;
- no volver a presentar el asset viejo como actual;
- registrar `vault + message_id + asset/beat + reason + attempts + next_retry` sin secretos;
- reintentar de forma acotada/backoff;
- permitir que un transport bot futuro autorizado para ese vault liquide esa deuda;
- hacer la operación idempotente: `already absent` cuenta como cleanup satisfecho.

La persistencia durable/reconciliación de esta deuda debe enlazarse con **Tarea 5.2**, que ya exige definir reconciliación Telegram/INDEX y garbage journal.

## 10. Prueba live obligatoria antes de declarar esto resuelto

Crear un probe aislado de 5.1, sin tocar primero el runtime productivo.

### Caso mínimo positivo

```text
1. Bot A crea un mensaje de prueba en un vault de prueba.
2. El mensaje debe ser realmente viejo (>48 h) o usarse evidencia equivalente que demuestre la frontera; preferencia: >48 h real.
3. Bot B pasa a ser el transport bot actual y queda admin con delete_messages.
4. Bot B usa MTProto channels.deleteMessages para borrar el mensaje de Bot A.
5. Verificar realmente que el mensaje desapareció.
```

Debe registrarse explícitamente:

```text
cross_bot_delete_proven=true
over_48h_delete_proven=true
current_transport_performed_delete=true
master_performed_media_delete=false
old_transport_required=false
bot_api_required_for_cleanup=false
```

### Negativos obligatorios

- sin `delete_messages`, el cross-bot delete debe fallar cerrado;
- un usuario/sesión no puede cambiar `vault/chat_id` y borrar en otro tenant;
- si el mismo transport bot pertenece a varios vaults, autorización BeatGaler debe impedir usar una sesión para operar el vault incorrecto;
- IDs inválidos/ya borrados deben ser idempotentes y no producir corrupción;
- ningún secreto permanente debe aparecer en cliente/logs/artefactos.

### Repetición bajo arquitectura final

Después del probe aislado, repetir con temporary auth y luego en:

- Windows;
- macOS;
- Web pura.

Solo entonces puede cerrarse la parte delete propio/cross-bot de Tarea 5.1.

## 11. Qué NO debemos volver a implementar

No usar como arquitectura final:

- MASTER borrando rutinariamente toda media reemplazada de todos los usuarios;
- Bot API como única ruta de cleanup de mensajes históricos;
- traer de vuelta al bot autor viejo para borrar su mensaje;
- grant/revoke `delete_messages` por cada Replace;
- relay de archivos por Galer Cloud;
- delete destructivo antes de confirmar el INDEX nuevo;
- declarar solucionado solo porque un mensaje reciente (<48 h) pudo borrarse.

## 12. Relación con el parche experimental v0.7.4

El parche experimental de la rama `fix-v0.7.4-runtime-master-audit`/PR #22 que hace cleanup post-commit mediante MASTER **no representa la arquitectura objetivo de 5.1**.

Puede haber servido para confirmar el problema y explorar seguridad post-commit, pero no debe convertirse por accidente en la implementación definitiva de cleanup cross-bot.

La parte útil que debe conservarse conceptualmente es:

```text
INDEX nuevo primero -> delete destructivo después
```

La identidad que ejecuta el delete normal debe ser el **transport bot actual**, no MASTER.

## 13. Dónde debe reflejarse cuando avancemos

Esta nota es la referencia de recuperación completa. Además, el protocolo obligatorio del Plan Maestro exige actualizar estos tres lugares con cada avance real:

1. `!!!PLAN/Plan Maestro.md`
   - `Estado vivo del plan`;
   - próximo subgate/bloqueos/evidencia 5.1.
2. `!!!PLAN/Fase 0 - Contención e integración.md`
   - Tarea 5.1;
   - evidencia de delete propio/cross-bot y decisión final de baseline rights.
3. `!!!PLAN/Registro de avances.md`
   - entrada fechada con PR/SHA/workflow/resultados exactos.

Además, en el repo BeatGaler deben mantenerse alineados:

- `docs/ADR-0051-TRUST-BOUNDARIES.md`;
- `docs/THREAT-MODEL-0051.md`, especialmente TM-11 y matriz de privilegios;
- `docs/MIGRATION-0051-ROLLBACK.md` para rollout/rollback/cleanup debt;
- Tarea 5.2 cuando se concrete el garbage journal durable.

`!!!PLAN/Plan Maestro 2208 copy DONT TOUCH .md` **no se modifica**.

## 14. Estado de evidencia al crear esta nota

```text
telegram_bot_api_48h_limit_documented=true
mtproto_channels_delete_messages_available_to_bots=true
mtproto_delete_messages_admin_right_documented=true
existing_transport_admin_permission_path=true
permission_churn_rejected_by_plan=true
cross_bot_live_proven=false
over_48h_live_proven=false
temporary_auth_cross_bot_delete_proven=false
master_required_for_routine_cleanup=false
bot_api_sufficient_for_historical_cleanup=false
task_5_1_closed=false
```

Hasta tener la prueba live y los negativos correspondientes, esta arquitectura queda **diseño respaldado por documentación + código histórico, pero NO evidencia funcional completa**.