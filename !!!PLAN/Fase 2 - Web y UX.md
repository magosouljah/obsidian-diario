# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE 109:** `integration-v0.8.0-alpha.1 @ 1dbf60e58ca970c47d387b303e141e30e2b8eef5`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] PUBLIC STARTUP BLOCKER + RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ ] public Web startup termina normalmente;
- [ 🟡 ] cold/warm startup Web real cuantificado.

Owner runtime previo probó infraestructura pública, pero normal Web quedó observado en `Loading Galer`; no apareció evidencia posterior que cierre ese síntoma. El merge #88 no toca ni prueba este gate.

`NIGHT-AAA-104` no dejó final result/handoff verificable al preflight CYCLE 109. **Owner nuevo: `NIGHT-AAA-105`.** Reproducir desde baseline `1dbf60e...`, identificar primer bootstrap phase irresuelto y aplicar solo corrective Web mínimo con termination semantics, focused tests, Web/no-Tauri proof y exact-head CI; **NO MERGE**. Shared auth/session/backend/provider/deploy => STOP.

### 13.1 — `[ 🟡 ] FROZEN`
#69 Web y #70 Server siguen candidates históricos stale/frozen. REUSE semantics solo bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP`
Gate literal: ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa. Evidence reusable demuestra que Review Save/Save All pueden avanzar/cerrar antes de durable cloud completion/failure. Sigue OPEN y sin owner material CYCLE 109 mientras AAA105 ataca startup.

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
Playback candidate stale; no priorizar frente a startup/auth/durability.

### 14.2 — `[ ]`
Queue/seek/shuffle/repeat/error recoverable, responsive volume y Safari/Firefox/Chrome/iPhone/degraded-network evidence pendientes.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH SEAM`
Purge lifecycle existe, pero faltan strong confirmation, recent-reauth seam y deterministic durable action boundary; UI puede limpiar optimistamente antes de purge completion. Sigue sin owner CYCLE 109 y bloquea D10.2 salvo decisión RO explícita de exclusión para alpha.

### 15.2 / 15.3
A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; no falsear browser/runtime coverage.
