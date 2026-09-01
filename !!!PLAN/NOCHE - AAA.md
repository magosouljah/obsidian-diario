# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-107`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 13.2 — durable Review Save/Save All completion / no silent loss`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`
- `PREDECESSOR: NIGHT-AAA-106 dejó NO_RESULT verificable al preflight JOBS CYCLE 111; SUPERSEDED / NOT_PASS.`
- `NEW_CONCURRENT_FACT: PR #92 existe sobre F2/12.1 y NO pertenece a este scope; WOZ110 es owner exclusivo de #92/integration lane.`
- `SERIALIZATION: AAA107 owns only F2/13.2. BBB106 owns #84. WOZ110 owns #92. No #92/#84/#89/Trash/deploy/provider/integration mutation.`

### PRIMARY

**F2 / 13.2 — cerrar el gap probado de durable completion/no-silent-loss con el mínimo corrective Web-safe.**

1. Preflight sobre live integration `134a293...` o posterior, Issue #41 y paths/tests Review; REUSE-FIRST y duplicate-check incluyendo evidencia #72/AAA074.
2. Aislar el punto exacto donde Save o Save All puede avanzar/cerrar antes de conocer durable cloud completion/failure.
3. Reutilizar semantics durables existentes; no rediseñar backend, auth/session ni data plane.
4. Aplicar el corrective mínimo para que success/close/advance visible ocurra solo después de durable completion; failure queda visible, recuperable y sin pérdida silenciosa.
5. Save All debe conservar semántica explícita de parcial/fallo; no declarar éxito global si alguna operación no terminó durablemente.
6. Preservar Web pure/no-Tauri y compatibilidad Desktop.
7. Añadir tests focales: success completion, failure/no-close, Save All partial/failure y touched-path Web/no-Tauri call-spies.
8. Un solo candidate/PR bounded si duplicate-check limpio; exact base/head + CI aplicable. **NO MERGE CYCLE 111.**
9. Claim máximo: `F2/13.2 DURABLE_REVIEW_CANDIDATE_READY`; PASS solo con evidencia literal exact-head.
10. Escribir RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** files/functions exactos; before/after semantics; tests; Web/no-Tauri proof; branch/base/head/PR; exact-head CI; UNVERIFIED explícito.  
**STOP:** duplicate candidate, auth/session/backend redesign, Trash, #84/#89/#92, deploy/provider, integration mutation o race que requiera refresh inseguro.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-AAA-106`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 111.
- `NIGHT-AAA-105`: #91 quedó integrado como `134a293...`; F2/12.1 todavía no es PASS y ahora además existe #92 para el loader signed-out observado en runtime.
