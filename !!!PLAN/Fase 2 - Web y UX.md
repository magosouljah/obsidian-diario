# Fase 2 — Flujos Web completos y rediseño de alto impacto

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 7–11 de septiembre  
**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

## Día 11 — 7 de septiembre — Foundations y AccountGate

**Resultado:** primitives compartidos y adquisición de cuenta coherente.

### Tarea 11.1 [P1 · FE/DL] — Design foundations

- [ ] Tokens, tipografía, iconos, focus, buttons, fields, feedback, Dialog y reduced motion.
- [ ] Documentar todos los estados; retirar duplicación inline empezando por AccountGate.
- [ ] Corregir autofill, contraste, loading y layout 390–430 px.

### Tarea 11.2 [P1 · FE/QA] — Auth UI completa

- [ ] Login/register/MFA/verify/reset/recovery/error/offline.
- [ ] OAuth con popup reservado o redirect, blocked/cancel/retry.
- [ ] Tests teclado, lector, zoom, móvil y errores de red.

**Dependencias:** APIs de Día 8.  
**Evidencia:** catálogo visual, axe/manual keyboard y E2E auth.  
**Gate de salida:** todas las variantes de cuenta son alcanzables, legibles y recuperables.

## Día 12 — 8 de septiembre — Library, cards y primera cuenta Web

**Resultado:** una cuenta Web nueva entra a una biblioteca autoritativa y puede orientarse.

### Tarea 12.1 [P1 · BE/FE] — Bootstrap y load

- [ ] Aprovisionar índice vacío atómicamente en control plane.
- [ ] Separar empty, no-results, offline, auth y cloud failure.
- [ ] Añadir thumbnails/lazy artwork, paginación o ventana y presupuesto de memoria.
- [ ] **Corregir regresión de rendimiento reportada por el owner:** la librería llegó a aparecer rápidamente tras una optimización previa y posteriormente volvió a aumentar el tiempo de espera. Instrumentar startup por fases (cache/render, auth/session, index, hydration/artwork), comparar cold/warm start y restaurar el comportamiento rápido sin sacrificar consistencia.

**Observación activa de rendimiento 12.1:** no asumir que el tiempo actual es aceptable solo porque la librería termina cargando. Debe existir medición antes/después y un presupuesto de startup acordado; el objetivo es recuperar la sensación de aparición rápida que ya se consiguió previamente.

### Tarea 12.2 [P1/P2 · FE/DL] — Rediseñar biblioteca

- [ ] Header/search/sort/tags/selection con iconos y nombres accesibles.
- [ ] Card con jerarquía fija y estados cloud/playback/download sin salto.
- [ ] Grid para 390, 768, 1024 y desktop; touch no depende de hover.

**Dependencias:** data plane y foundations.  
**Evidencia:** E2E cuenta limpia + screenshots baseline + performance trace.  
**Gate de salida:** registro → empty gallery → Add Beat es posible sin Desktop previo.

## Día 13 — 9 de septiembre — Import, Review y bulk edit

**Resultado:** importar y editar en Web nunca cae en Tauri ni produce éxito falso.

### Tarea 13.1 [P1 · FE/BE] — Persistencia Web correcta

- [ ] `Save All` comitea cada candidato con expectativas de índice y resume parciales.
- [ ] Bulk edit usa una transacción Web conflict-safe o queda deshabilitado con explicación hasta completarla.
- [ ] Garbage journal limpia uploads huérfanos tras fallo/cancel.

### Tarea 13.2 [P1 · FE/DL/QA] — ReviewShell

- [ ] Modos Import/Edit/Bulk explícitos, CTA fija, close visible y progreso N/N.
- [ ] Errores por item, retry/skip/cancel y confirmación durable.
- [ ] E2E multi-file, conflicto, refresh simultáneo y rollback.

**Dependencias:** biblioteca y data plane.  
**Evidencia:** tests de Save All/bulk y reconciliación posterior al refresh.  
**Gate de salida:** ninguna acción visible Web llama Tauri; 0 pérdida silenciosa.

## Día 14 — 10 de septiembre — Playback, queue y descargas

**Resultado:** reproducción y archivos funcionan dentro de límites conocidos por navegador.

### Tarea 14.1 [P1/P2 · FE/BE] — Streaming/memoria

- [ ] Definir soporte MediaSource/Range y fallback seguro por navegador.
- [ ] Evitar ensamblar archivos gigantes en RAM; imponer límites y comunicar alternativa.
- [ ] Cancelar/reanudar donde sea seguro y liberar object URLs/buffers.

### Tarea 14.2 [P2 · FE/DL/QA] — Player/queue

- [ ] Corregir índice activo, shortcuts, seek, shuffle/repeat y error recoverable.
- [ ] Queue/volumen como popover desktop y sheet Web móvil.
- [ ] Probar Safari/Firefox/Chrome/iPhone con archivo pequeño/grande y red degradada.

**Dependencias:** biblioteca estable.  
**Evidencia:** matriz browser, perfiles de memoria y E2E playback/download.  
**Gate de salida:** no hay crash por fallback soportado y la pista activa siempre es inequívoca.

## Día 15 — 11 de septiembre — Settings, Trash, accesibilidad y YouTube Web

**Resultado:** configuración y recuperación tienen estados completos y lenguaje veraz; YouTube deja de ser una capacidad exclusiva de Desktop en la implementación Web.

### Tarea 15.1 [P1 · FE/DL] — SettingsShell

- [ ] Sidebar desktop y navegación apilada móvil; Account/Plan/Preferences/Trash/legal por secciones.
- [ ] State machines reales para catálogo, cache, Trash y updater; error + retry.
- [ ] Acciones peligrosas separadas, confirmadas y con reautenticación.

### Tarea 15.2 [P2 · QA/DL] — A11y pass completo

- [ ] Dialog/focus restoration, live regions, labels, contraste, zoom y reduced motion.
- [ ] Reemplazar controles/glifos vacíos y alerts/confirms nativos.
- [ ] Congelar baseline visual de todos los S01–S59 alcanzables en harness/staging.

**Dependencias:** primitives y APIs de cuenta.  
**Evidencia:** auditoría AA, keyboard script y screenshot set por plataforma.  
**Gate de salida:** 0 defecto crítico de teclado/lectura/contraste en flujos de lanzamiento.

### Tarea 15.3 [P1 · FE/BE/QA] — Implementar YouTube Web sin Tauri

**Regla de producto:** YouTube debe existir en Desktop y Web. El `false` actual de `WEB_FOUNDATION_CAPABILITIES.youtubePublishing` es estado temporal, no una exclusión permanente. Esta tarea contiene el plan completo de implementación Web; no existe un documento/módulo separado.

#### A. Contrato compartido y capabilities

- [ ] Definir una interfaz compartida para channel status, connect, disconnect, upload, schedule, cancel, retry y progress.
- [ ] Retirar de la UI compartida cualquier dependencia directa de `src/lib/tauri.ts` para operaciones YouTube.
- [ ] Mantener `src/platform/capabilities.ts` como fuente de disponibilidad visible.
- [ ] No cambiar `WEB_FOUNDATION_CAPABILITIES.youtubePublishing` a `true` hasta que el flujo Web real de esta tarea pase su gate.

#### B. Desktop adapter — conservar lo que ya funciona

- [ ] Encapsular las funciones Tauri/Rust actuales detrás del contrato compartido sin reescribir comportamiento innecesariamente.
- [ ] Mantener Desktop Direct, Offline y YouTube verdes durante cada corte.
- [ ] Conservar los flujos actuales de channel status/connect/disconnect/upload/schedule/cancel/progress salvo cambio exigido por el contrato común.

#### C. Backend YouTube para Web

- [ ] Implementar OAuth server-side con `state` validado, callbacks/orígenes controlados y ningún client secret o refresh token expuesto al navegador.
- [ ] Guardar secretos/tokens de provider cifrados en la persistencia durable definida por Fase 1.
- [ ] Crear endpoints tenant-scoped para channel status, connect/disconnect, creación de job, schedule, progress, cancel y retry.
- [ ] Hacer idempotente la creación de jobs/uploads y reconciliar estado para evitar duplicados tras retry/refresh.
- [ ] Preparar el punto de enforcement de entitlement/quota; la política comercial final de límites YouTube se conecta obligatoriamente en Tarea 18.1 antes del release.

#### D. Web adapter puro

- [ ] Implementar el contrato usando únicamente HTTP/Web APIs seguras.
- [ ] Prohibido `invoke`, `@tauri-apps/*`, localhost helper o dependencia de que BeatGaler Desktop esté instalado.
- [ ] Manejar OAuth popup/redirect, popup bloqueado, cancelación, retry, expiración y reconexión.
- [ ] Mantener errores humanos y sin secretos/terminología interna de infraestructura.

#### E. Job/upload Web

- [ ] Implementar upload/job sin cargar archivos grandes completos en RAM cuando exista estrategia streaming/chunked segura.
- [ ] Progreso durable y recuperable después de refresh cuando el backend tenga un job activo.
- [ ] Cancel/retry bounded y estado final inequívoco.
- [ ] Schedule con timezone explícito y validación server-side.

#### F. UI compartida

- [ ] Reutilizar/adaptar el flujo existente: selección de beats → Visual/crop → Metadata/Presets → Visibilidad/Schedule → conexión/canal → Job/progreso/recovery.
- [ ] La diferencia Desktop/Web vive en adaptadores/capabilities, no en dos wizards independientes.
- [ ] Mantener estados empty/loading/error/retry/cancel accesibles y responsive.

#### G. Tests y evidencia de Fase 2

- [ ] Unit: contrato/capabilities y validaciones YouTube.
- [ ] DOM: cualquier intento de YouTube Web de invocar Tauri hace FAIL.
- [ ] Integration: UI → Web adapter → backend mock/controlado y Desktop adapter sin regresión.
- [ ] Backend: tenant isolation, OAuth state, token secrecy, idempotencia, schedule, cancel y retry.
- [ ] E2E staging/controlado: conectar canal → seleccionar beat → configurar metadata/visual/visibilidad → iniciar upload → observar progreso → resultado; incluir cancel/retry/disconnect.
- [ ] CI cross-platform: Desktop Direct/Offline/YouTube continúa verde en Windows + macOS arm64 + macOS x86_64.

**Dependencias de entrada:** Tarea 3.2 cerrada; Fase 1 debe haber dejado auth/session y persistencia durable aptas para OAuth/provider secrets.  
**Evidencia de salida de Fase 2:** tests Unit/DOM/Integration/Backend + E2E de staging/controlado + CI Desktop cross-platform verde.  
**Gate de salida de Tarea 15.3:** Web completa de principio a fin un upload YouTube controlado sin Tauri ni Desktop helper, con secretos server-side y job durable; Desktop conserva Direct/Offline/YouTube. Solo entonces `WEB_FOUNDATION_CAPABILITIES.youtubePublishing = true`.

#### Gates posteriores que NO bloquean la implementación de Fase 2 pero sí bloquean v1

- **Tarea 16.1:** callbacks, secretos y entorno YouTube deben existir correctamente en staging/producción separados.
- **Tarea 18.1:** quotas/entitlements YouTube se aplican server-side para Desktop y Web antes de reservar trabajo.
- **Tarea 25.1:** YouTube entra en la matriz cross-platform/browser por capability.
- **Gates de publicación:** el flujo YouTube Web real, limits por plan y pruebas de release deben seguir verdes; que 15.3 esté `[x]` no sustituye esos gates posteriores.
