# Módulo — YouTube Web

> Módulo especializado. Antes de usarlo: leer completo [`../Plan Maestro.md`](../Plan%20Maestro.md) y la [`Tarea 15.3 de Fase 2`](../Fase%202%20-%20Web%20y%20UX.md).

**Estado:** TARGET obligatorio para v1.  
**Regla de producto:** YouTube debe existir tanto en Desktop como en Web. Que `youtubePublishing` sea `false` hoy en Web describe únicamente el estado actual; **no es una exclusión permanente de la plataforma Web**.

## Estado actual

- Desktop: YouTube implementado mediante Tauri/Rust y debe conservarse sin regresiones.
- Web: YouTube todavía no está implementado.
- Web nunca debe depender de Tauri, helper local ni de que BeatGaler Desktop esté instalado.
- La UI/flujo de YouTube ya forma parte del producto; la implementación Web debe reutilizar lo compartible sin copiar la dependencia nativa.

## Contrato arquitectónico objetivo

1. Crear un contrato compartido de publicación YouTube para que UI/componentes compartidos no llamen directamente a `src/lib/tauri.ts`.
2. Mantener un adaptador Desktop que conserve la implementación Tauri/Rust actual.
3. Crear un adaptador Web puro respaldado por backend/control plane de BeatGaler.
4. OAuth refresh tokens, client secrets y demás secretos permanecen únicamente server-side; el navegador recibe estado/capabilities y credenciales efímeras solo cuando sea estrictamente necesario.
5. Implementar en Web el ciclo completo: conectar canal, leer estado, metadata, visual, visibilidad, schedule, iniciar upload, progreso, retry, cancelación, resultado y disconnect.
6. Reutilizar stepper/UI compartido y adaptar únicamente operaciones dependientes de plataforma.
7. No cambiar `WEB_FOUNDATION_CAPABILITIES.youtubePublishing` a `true` hasta que el flujo Web real esté implementado y probado.

## Plan de implementación — Tarea 15.3

La checklist oficial vive en `Fase 2 - Web y UX.md`; este módulo la detalla sin sustituirla.

### A. Contrato compartido

- Definir interfaz común para channel status/connect/disconnect/upload/schedule/cancel/progress.
- Remover dependencia directa de UI compartida hacia Tauri para operaciones YouTube.
- Hacer que la capability sea la fuente de disponibilidad visible.

### B. Desktop adapter

- Envolver las funciones Tauri/Rust existentes detrás del contrato.
- No reescribir el comportamiento Desktop si no es necesario.
- Mantener pruebas de regresión Direct + Offline + YouTube durante cada corte.

### C. Backend Web

- OAuth server-side con callbacks/orígenes exactos.
- Refresh tokens/client secrets cifrados y no expuestos al browser.
- Endpoints tenant-scoped para estado de canal, job creation, schedule, cancel, retry y disconnect.
- Idempotencia para creación de jobs/uploads y reconciliación de estados.
- Aplicar quotas/entitlements YouTube server-side antes de reservar trabajo.

### D. Web adapter

- Implementar el contrato usando únicamente HTTP/Web APIs seguras.
- Prohibido `invoke`, `@tauri-apps/*`, localhost helper o dependencia de BeatGaler Desktop.
- Manejar popup/redirect OAuth, blocked popup, cancel, retry, expiry y reconexión.

### E. Job/upload Web

- Evitar cargar archivos grandes enteros en memoria si el navegador/backend permite streaming/chunks seguros.
- Progreso durable y recuperable tras refresh cuando el backend tenga un job activo.
- Cancel/retry bounded; errores humanos y sin secretos.
- Schedule con timezone explícito y validación server-side.

### F. UI compartida

Reutilizar/adaptar las superficies actuales:
- selección de beats;
- Visual/crop;
- Metadata/Presets;
- Visibilidad/Schedule;
- conexión/canal;
- Job/progreso/recovery.

La diferencia Desktop/Web debe vivir en adaptadores/capabilities, no en duplicación masiva del wizard.

### G. Tests/gates

- Unit: contrato/capabilities y validaciones.
- DOM: Web YouTube no invoca Tauri.
- Integration: UI → Web adapter → mock backend y Desktop adapter sin regresión.
- Backend: tenant isolation, OAuth state, quota, idempotencia, cancel/retry/schedule.
- E2E staging: conectar canal real controlado → upload → progreso → resultado; cancel/retry; disconnect.
- Cross-platform CI: Desktop Direct/Offline/YouTube continúa verde en Windows + macOS arm64 + x86_64.
- Solo después de estos gates: `WEB_FOUNDATION_CAPABILITIES.youtubePublishing = true`.

## Relación con Tarea 3.2

Tarea 3.2 congela el contrato **actual** y evita regresiones durante la convergencia; no declara YouTube Desktop-only para v1.

Evidencia 3.2:
- PR BeatGaler #8: `test(platform): enforce 3.2 Web/Desktop contract`.
- Commit de trabajo: `818214889ef3c6f97a262a91046f7df0e4f723fe`.
- CI PR #64: PASS Windows + macOS arm64 + macOS x86_64.
- Merge `integration-v0.8.0-alpha.1`: `32a38c490a53650a0e9d6435c50cd009ef1b5123`.
- CI post-merge #65: PASS Windows + macOS arm64 + macOS x86_64 antes de cerrar 3.2.
- El test de capacidades ahora sí forma parte del runner TS.
- Guard DOM: cualquier invocación Tauri desde flujos Web cubiertos hace fallar la prueba.
- Desktop protegido explícitamente para Direct, Offline y YouTube.

## Gate final de este módulo

**Web puede completar YouTube de principio a fin sin Tauri ni Desktop helper, con secretos server-side y quotas reales, mientras Desktop conserva Direct/Offline/YouTube sin regresiones.**
