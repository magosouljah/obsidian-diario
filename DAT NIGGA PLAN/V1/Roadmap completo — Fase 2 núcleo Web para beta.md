# Roadmap completo — Fase 2: núcleo Web para beta

## Objetivo

Llegar cuanto antes a una beta Web rápida, estable y confiable con cinco cuentas simultáneas.

La prioridad es rendimiento. Durante toda la fase se preservan estas garantías:

- No pérdida de datos.
- No corrupción de archivos, metadata ni INDEX.
- Ninguna cuenta puede modificar o borrar contenido de otra.
- Las operaciones retenidas se liberan tras un error, crash o reinicio.

Quedan fuera: UX y pulido, uploads o downloads resumibles, features nuevas, refactors grandes y trabajo operativo de producción.

## Definiciones de medición

**Biblioteca caliente**

Tiempo desde una apertura normal con sesión existente o un Reload con sesión activa hasta que la **biblioteca autoritativa queda utilizable**: índice confirmado, cards correctas y acciones principales disponibles.

Objetivo: `p95 ≤ 5 s`.

**Primer audio**

Tiempo desde el clic en Play hasta que el audio está sonando y su posición avanza.

Objetivo: `p95 ≤ 2 s`.

**Muestra válida**

Cada métrica se medirá con cinco cuentas simultáneas, en el build Web de producción, con al menos:

- 20 muestras válidas por métrica.
- Tres corridas independientes.
- Registro de p95, máximo, promedio, número de muestras y errores.

Una corrida abortada, una cuenta sin completar el flujo o una medición sin trazas no cuenta como éxito.

---

## Task 0 — Preparar el protocolo de medición

**Propósito:** impedir que los resultados de Vite, un build viejo o condiciones diferentes se mezclen con la aceptación de beta.

**Alcance**

- Usar la misma revisión de Web y Cloud por corrida.
- Ejecutar aceptación sobre `vite preview` o el modo equivalente al artefacto de producción.
- Mantener Vite dev sólo para diagnóstico local.
- Etiquetar cada medición como:
    - apertura fría;
    - reapertura caliente;
    - Reload caliente;
    - Play después de biblioteca autoritativa utilizable.
- Conservar versión, hora, número de cuentas, condición, muestras y resultado.

**Salida**

Un harness y formato de reporte repetible que pueda comparar corridas sin ambigüedad.

---

## Task 1 — Atribuir la causa de los 25–45 s

**Propósito:** demostrar dónde se consume el tiempo antes de cambiar el diseño.

**Alcance**

Trazar, por cuenta y por operación:

```
abrir / Reload
→ auth/session
→ Cloud/control
→ conexión Direct
→ get_index
→ lectura del INDEX
→ procesamiento Web
→ biblioteca autoritativa utilizable
```

Y para reproducción:

```
click Play
→ prioridad/conexión Direct
→ solicitud de media
→ primeros bytes
→ buffer reproducible
→ audio.playing con progreso
```

Separar el tiempo de cada tramo. No atribuir la demora a Telegram, caché, Cloud o Web sin evidencia.

**No hacer**

- No implementar una caché nueva.
- No cambiar arquitectura por intuición.
- No ajustar presupuestos para hacer pasar una corrida.

**Salida**

Una causa o conjunto de causas demostradas que expliquen el retraso de biblioteca caliente, con el cambio mínimo propuesto para corregirlas.

---

## Task 2 — Corregir biblioteca caliente

**Propósito:** llevar la biblioteca autoritativa utilizable a `p95 ≤ 5 s` con cinco cuentas.

**Alcance**

Aplicar sólo las correcciones justificadas por Task 1. Según la evidencia, pueden afectar:

- espera innecesaria entre auth, Direct y `get_index`;
- operaciones seriales que pueden coordinarse o ejecutarse en paralelo;
- conexión Direct no reutilizada;
- lectura o reconciliación del INDEX;
- procesamiento o render Web;
- prioridades entre biblioteca, prefetch y reproducción;
- una caché existente cuyo uso sea seguro y medible.

Toda optimización debe preservar que el INDEX y Cloud/vault siguen siendo la autoridad.

**Criterio de aceptación**

- Biblioteca caliente `p95 ≤ 5 s`.
- Cinco cuentas simultáneas.
- Cards, metadata, orden y archivos corresponden a la lectura autoritativa.
- No se introduce corrupción, duplicación ni cruces entre vaults.

---

## Task 3 — Corregir primer audio y seek

**Propósito:** lograr reproducción rápida sin empeorar biblioteca ni operaciones de otras cuentas.

**Alcance**

Medir y corregir sólo el tramo que limite el primer audio:

- conexión Direct;
- obtención de metadata de media;
- prioridad de transferencias;
- prefetch existente;
- streaming;
- MSE/Blob;
- contención entre playback y operaciones de fondo.

Si la evidencia demuestra que caché o prefetch ayudan, se implementan aquí. No existe una Task separada de “estrategia de caché”.

Toda caché de bytes debe estar ligada a una versión concreta del archivo. En el sistema actual, el `messageId` de media es el candidato natural; un reemplazo de MP3 debe producir una identidad de media distinta antes de que bytes anteriores puedan reutilizarse.

**Criterio de aceptación**

- Primer audio `p95 ≤ 2 s`.
- Cinco cuentas simultáneas.
- Seek cambia realmente la posición y la reproducción continúa.
- Playback sigue funcionando mientras otras cuentas suben, editan metadata, recargan o descargan.

---

## Task 4 — Integridad de upload y metadata

**Propósito:** confirmar que las operaciones de escritura existentes son confiables.

**Alcance**

Cubrir el flujo:

```
upload
→ publicación de metadata
→ Reload
→ lectura autoritativa
```

Cubrir también:

```
upload interrumpido
→ sin publicación parcial
→ operación liberada
→ retry desde cero
→ lectura autoritativa correcta
```

Verificar que:

- un archivo no aparece como válido antes de estar confirmado;
- no queda un INDEX huérfano;
- no se pierden beats existentes;
- metadata editada persiste después de Reload;
- otras cuentas siguen operando;
- una cuenta no puede editar ni borrar datos ajenos.

**No hacer**

- No resumable upload.
- No reanudación automática.
- No nuevos tipos de operación.

**Criterio de aceptación**

Los flujos completos pasan y ningún fallo deja corrupción, pérdida o permisos cruzados de modificación/borrado.

---

## Task 5 — Downloads y Trash existentes

**Propósito:** verificar los recorridos ya presentes en el producto sin ampliar su alcance.

**Downloads**

- WAV íntegro mediante hash.
- ZIP íntegro mediante hash.
- MP3 descargado válido y reproducible.
- Fallo limpio.
- Retry desde cero permitido.

**Trash**

Auditar el comportamiento que existe y comprobar:

```
enviar a Trash
→ Reload
→ estado autoritativo correcto
→ purge existente, si aplica
→ Reload
→ no resurrección
```

Verificar que una cuenta no puede ver, restaurar, purgar, modificar o borrar contenido de otra.

**Criterio de aceptación**

Downloads y Trash existentes funcionan según su comportamiento actual y persisten correctamente tras Reload.

---

## Task 6 — Reload, relogin, fallos y recuperación

**Propósito:** asegurar que el núcleo se recupera sin estado inconsistente.

**Alcance**

Completar y reutilizar cobertura de:

- Reload.
- Logout → login.
- Corte de red durante upload.
- Crash de navegador.
- Reconexión.
- Reinicio controlado de Cloud.
- Liberación de sesiones, leases y operaciones.

Tras cada recuperación:

- biblioteca autoritativa correcta;
- archivos correctos;
- metadata correcta;
- orden correcto;
- vault correcto;
- ninguna operación retenida permanentemente;
- ningún doble writer;
- ningún INDEX inconsistente;
- las otras cuentas siguen funcionando.

### Test informativo: caché A → B en el mismo perfil

Incluir un test pequeño que haga:

```
Cuenta A
→ logout
→ login de Cuenta B en el mismo perfil
→ observar estado temporal y estado autoritativo final
```

Registrar si aparecen temporalmente cards, nombres, rutas o audio cacheados de A.

Este resultado **no bloquea Fase 2** si sólo afecta presentación temporal y la lectura autoritativa final de B es correcta.

Sí bloquea si B puede usar ese estado para modificar o borrar contenido de A, o si hay exposición funcional persistente de contenido ajeno.

**Criterio de aceptación**

Los fallos recuperables no causan pérdida, corrupción, escrituras dobles ni permisos cruzados.

---

## Task 7 — Aceptación final de cinco cuentas

**Propósito:** demostrar que el núcleo completo aguanta uso simultáneo real.

**Escenario**

Cinco cuentas durante 30 minutos, rotando para que todas ejecuten:

- Play.
- Seek.
- Upload.
- Metadata + Reload.
- Download.
- Trash.
- Una transferencia grande.

Al finalizar:

```
Reload autoritativo de las cinco cuentas
→ comparar usuario, vault, beats, metadata, orden y archivos
→ verificar operaciones, sesiones y locks
```

**Gates**

- Biblioteca caliente `p95 ≤ 5 s`.
- Primer audio `p95 ≤ 2 s`.
- Cinco cuentas simultáneas.
- Soak completo de 30 minutos.
- Rotación completa de roles.
- Cero pérdida, corrupción o cruce de datos.
- Cero capacidad cruzada de modificar o borrar contenido.
- Cero operaciones graves abandonadas.
- Las cuentas ajenas no se congelan durante una transferencia grande.

---

## Task 8 — Regresión breve y backlog posterior

**Propósito:** preservar las garantías sin crear una suite inmanejable.

Dejar cuatro comandos o modos canónicos:

```
1 cuenta → core flow
2 cuentas → aislamiento y permisos cruzados
5 cuentas → startup, playback y operaciones mixtas
1 fallo controlado → recuperación
```

Mantener debajo los unit e integration tests existentes.

Documentar defectos menores observados durante Fase 2 en:

```
POST-V1-UX-RELIABILITY-BACKLOG.md
```

Este documento no crea trabajo adicional dentro de la fase.

---

# Criterio de salida de Fase 2

Fase 2 está cerrada cuando, en el build Web de producción:

- Cinco cuentas completan el soak de 30 minutos y la rotación de operaciones.
- Biblioteca autoritativa caliente cumple `p95 ≤ 5 s`.
- Primer audio cumple `p95 ≤ 2 s`.
- Abrir, escuchar, seek, subir, editar, descargar, Trash, Reload, logout/login y recuperación funcionan.
- No hay pérdida de datos, corrupción, INDEX inconsistente ni operaciones graves abandonadas.
- Ninguna cuenta puede modificar o borrar contenido de otra.
- Los resultados temporales de caché A→B quedan registrados; sólo bloquean si generan una capacidad real de acceso, modificación o borrado entre cuentas.
- Queda una batería corta que protege estas garantías.

No se ejecutarán cambios, pruebas nuevas, refactors ni ampliaciones de producto hasta recibir las órdenes para iniciar la Fase 2.