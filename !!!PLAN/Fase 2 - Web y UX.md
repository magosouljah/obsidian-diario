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

**Resultado:** configuración y recuperación tienen estados completos y lenguaje veraz; YouTube deja de ser una capacidad exclusiva de Desktop en el objetivo de producto.

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

### Tarea 15.3 [P1 · FE/BE/QA] — Portar YouTube a Web sin Tauri

**Regla de producto:** YouTube debe existir en Desktop y Web. El `false` actual de `WEB_FOUNDATION_CAPABILITIES.youtubePublishing` es estado temporal, no exclusión permanente.

**Módulo obligatorio al trabajar esta tarea:** [`Modulos/YouTube Web.md`](./Modulos/YouTube%20Web.md).

- [ ] Extraer un contrato compartido de YouTube; Desktop conserva Tauri/Rust detrás de su adaptador.
- [ ] Implementar backend Web para OAuth/estado/upload/schedule/progreso/retry/cancel/disconnect con secretos server-side.
- [ ] Implementar adaptador Web sin Tauri, sin helper local y sin dependencia de BeatGaler Desktop.
- [ ] Reutilizar UI compartida de selección, visual, metadata/presets, visibilidad/schedule, conexión y job/progreso.
- [ ] Añadir pruebas DOM/integration/backend/E2E que demuestren que YouTube Web funciona y nunca invoca Tauri.
- [ ] Mantener regresiones Desktop verdes para Direct, Offline y YouTube durante toda la migración.
- [ ] Cambiar `WEB_FOUNDATION_CAPABILITIES.youtubePublishing` a `true` solo después de que el flujo Web pase sus gates.

**Dependencias:** auth/OAuth Web seguro, backend durable, upload/job infrastructure y contrato de plataforma compartido.  
**Evidencia:** tests Web + backend + E2E, OAuth real de staging, upload real controlado, progreso/cancel/retry y CI cross-platform verde.  
**Gate de salida:** Web puede completar el flujo YouTube de principio a fin sin Tauri ni Desktop helper, mientras Desktop conserva Direct/Offline/YouTube sin regresiones.
