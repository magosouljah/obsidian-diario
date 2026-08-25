# Tarea 5.1 — Delete cross-bot y cleanup Direct

**Estado:** M0-F reciente probado; cleanup físico cross-bot >48 h diferido como deuda futura de GC de baja prioridad.  
**Fecha:** 2026-08-25, `America/Mexico_City`.  
**Tarea propietaria:** Fase 0, Tarea 5.1 — límites de confianza Direct.  
**No cierra 5.1:** ningún checkbox pasa a `[x]` por esta nota.

> Objetivo de esta nota: conservar la arquitectura y evidencia de cleanup Direct sin volver a convertir MASTER en worker por archivo ni hacer del cleanup físico histórico un requisito de corrección del producto.

## 1. Problema real

BeatGaler usa un pool de transport bots. Un vault puede haber sido atendido por distintos transport bots a lo largo del tiempo, por lo que puede contener media creada por bots anteriores.

La corrección funcional de Replace/Delete **no puede depender de borrar primero el mensaje físico viejo**. El orden autoritativo es:

```text
nuevo asset -> nuevo INDEX confirmado -> asset viejo queda obsoleto -> cleanup oportunista
```

Si el cleanup físico falla, el INDEX nuevo sigue siendo la autoridad y el asset viejo no reaparece en BeatGaler.

## 2. Evidencia M0-F ya obtenida

### 2.1 Miembro normal: delete propio sí, cross-bot no

El probe negativo aislado confirmó:

```text
own_delete_without_admin_proven=true
cross_bot_delete_without_admin_denied=true
bot_a_admin=false
bot_b_admin=false
permission_churn_used=false
production_runtime_changed=false
```

Conclusión: un transport bot miembro normal puede borrar su propio mensaje, pero no debe esperarse que borre el de otro bot.

CI normal #180 (`32831177470`) terminó PASS.

### 2.2 Vault privado + admin estable: cross-bot reciente sí

En el rerun final del workflow M0-F `32877055196`, job `97900929779`:

1. Lorenzo inició su sesión MTProto antes de pertenecer al vault.
2. Después fue añadido al vault privado como admin con `delete_messages`.
3. La **misma sesión MTProto** aprendió el peer/access hash privado.
4. Federico creó un mensaje reciente.
5. Lorenzo ejecutó `channels.deleteMessages` y lo borró.

Evidencia:

```text
cross_bot_delete_mtproto_proven=true
mtproto_session_started_before_vault_membership=true
private_peer_learned_by_same_mtproto_session=true
current_transport_identity_is_bot_a=true
message_author_is_bot_b=true
delete_messages_baseline_required=true
mtproto_channels_delete_messages_used=true
public_vault_required=false
master_per_file_cleanup_used=false
production_runtime_changed=false
token_rotation_or_revoke=false
```

Esto prueba que un vault **no necesita ser público** y que MASTER no necesita entregar un access hash ni ejecutar el delete rutinario por archivo.

## 3. Evidencia >48 h y decisión del RO

Se ejecutó un probe sobre un mensaje real que el RO garantizó como:

- mayor a 48 horas;
- creado por otro bot;
- seguro de borrar.

Workflow `32880457856`, job `97908382881`.

El transport bot actual llegó correctamente hasta:

```text
channels.deleteMessages
```

pero Telegram respondió:

```text
MESSAGE_DELETE_FORBIDDEN
```

Por tanto:

```text
over_48h_proven=false
```

### Decisión vigente

El RO decidió que **el borrado físico cross-bot >48 h es un problema futuro de baja prioridad y NO bloquea Tarea 5.1**.

La corrección del producto depende del INDEX autoritativo, no de que todos los objetos físicos obsoletos desaparezcan inmediatamente del storage subyacente.

La deuda física se resolverá después mediante reconciliación/garbage journal/GC, enlazada con Tarea 5.2.

## 4. División correcta de responsabilidades

### MASTER / control plane

MASTER puede encargarse de:

- resolver/asignar vault;
- introducir/promover transport bots cuando cambie membership/lease;
- conceder permisos baseline mínimos y estables;
- recovery administrativo excepcional.

MASTER **no** debe ser worker central de cleanup de media por archivo.

### Transport bot actual / data plane

Durante una sesión normal puede encargarse de:

- upload directo;
- operaciones de INDEX;
- delete propio;
- delete cross-bot cuando Telegram lo permita y tenga `delete_messages` baseline;
- registrar/emitir deuda de cleanup cuando el delete físico no sea posible.

## 5. Flujo definitivo de Replace/Delete

```text
1. Subir nueva media directamente.
2. Obtener/persistir IDs nuevos.
3. Construir/publicar INDEX nuevo.
4. Confirmar INDEX nuevo como autoridad.
5. Calcular referencias obsoletas = INDEX anterior - INDEX nuevo.
6. Intentar cleanup físico post-commit con el transport bot actual.
7. Si cleanup falla: mantener INDEX nuevo, registrar deuda y continuar.
```

Nunca:

```text
borrar viejo -> después intentar confirmar nuevo INDEX
```

porque un fallo intermedio podría causar pérdida real.

## 6. Permisos: baseline estable, no churn

La Tarea 5.1 ya probó que churn administrativo frecuente puede disparar `FLOOD_WAIT` e incluso impedir restauración inmediata.

Queda fuera:

```text
grant delete -> borrar -> revoke delete
```

También queda fuera promote/demote por cada operación/chunk.

M0-F confirmó que `delete_messages` es necesario para cross-bot reciente; por tanto puede permanecer como **baseline mínimo estable** mientras el transport bot sea admin del vault durante su membership/lease.

La reducción de blast radius debe venir de:

- temporary auth;
- membership acotada;
- aislamiento tenant/vault;
- sesiones/leases acotadas;
- permisos baseline mínimos;
- admission control;

no de permission churn por operación.

## 7. Relación con temporary auth

M0-B2/M0-E1/M0-E2 ya demostraron que la identidad bot puede operar por MTProto directo sin entregar permanent auth/token/API hash al cliente en el modelo temporal propuesto.

Target:

```text
transport bot actual
+ temporary auth válida
+ membership del vault
+ delete_messages baseline
-> operaciones normales MTProto directas
```

Los bytes de archivos siguen:

```text
dispositivo <-> storage subyacente
```

Galer Cloud no se convierte en relay de archivos.

## 8. Garbage journal / GC futuro

Si el INDEX nuevo ya es autoritativo y falla el cleanup:

- no revertir INDEX;
- no volver a presentar el asset viejo como actual;
- registrar `vault + message_id + asset/beat + reason + attempts + next_retry` sin secretos;
- hacer retries acotados/backoff cuando tenga sentido;
- tratar `already absent` como éxito idempotente;
- permitir mantenimiento/GC posterior sin bloquear la UX normal.

La persistencia durable y reconciliación de esta deuda pertenece a **Tarea 5.2**, que ya exige reconciliación INDEX/storage + garbage journal.

## 9. Qué queda pendiente dentro de 5.1

La parte delete propio/cross-bot **ya no es el siguiente subgate**. El siguiente subgate principal es:

```text
aislamiento cross-vault/shared-bot
```

Debe probar que un mismo transport bot que tenga membership en varios vaults no pueda usar una sesión/tenant para operar el vault equivocado.

Después siguen:

- escalabilidad/admission control;
- decidir si expiración server-side/natural sigue siendo requisito;
- migración del runtime productivo sin credenciales compartidas;
- discovery/hardening restante;
- revisión independiente requerida por el gate global.

**No iniciar Tarea 5.2 todavía.**

## 10. Qué NO volver a implementar

No usar como arquitectura final:

- MASTER borrando rutinariamente toda media reemplazada;
- traer de vuelta al bot autor viejo para cleanup normal;
- grant/revoke `delete_messages` por Replace;
- hacer público un vault para resolver peers;
- relay de archivos por Galer Cloud;
- delete destructivo antes de confirmar INDEX nuevo;
- bloquear Replace/Delete porque un objeto físico obsoleto >48 h no pudo borrarse.

## 11. Estado de evidencia vigente

```text
own_delete_without_admin_proven=true
cross_bot_delete_without_admin_denied=true
cross_bot_recent_mtproto_proven=true
private_peer_learned_by_same_mtproto_session=true
public_vault_required=false
delete_messages_baseline_required=true
master_per_file_cleanup_used=false
over_48h_delete_proven=false
over_48h_cleanup_blocks_task_5_1=false
index_is_authority=true
garbage_journal_deferred_to_task_5_2=true
production_runtime_changed=false
task_5_1_closed=false
```

`!!!PLAN/Plan Maestro 2208 copy DONT TOUCH .md` **no se modifica**.