# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE 108:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] PUBLIC STARTUP BLOCKER + RUNTIME EVIDENCE`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [ ] public Web startup termina normalmente;
- [ 🟡 ] cold/warm startup Web real cuantificado.

Owner runtime Issue #41 `5485984669` prueba infraestructura pública (`/web-health`, auth-health, www→apex, TLS), pero `https://beatgaler.com` queda en `Loading Galer`; no reabrir deploy/DNS/TLS por ese síntoma.

`NIGHT-AAA-103` no dejó final result/handoff verificable al preflight CYCLE 108. **Owner nuevo: `NIGHT-AAA-104`.** Debe reproducir el stall desde baseline `38517c...`, identificar el primer bootstrap phase irresuelto y aplicar solo corrective Web mínimo con termination semantics, focused tests, Web/no-Tauri proof y exact-head CI; **NO MERGE**. Shared auth/session/backend/provider/deploy => STOP.

### 13.1 — `[ 🟡 ] FROZEN`
#69 Web y #70 Server siguen candidates históricos stale/frozen. Reuse semantics solo bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP`
Gate literal: ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa. Issue #41 `5478129410` revalidó que Review Save/Save All pueden avanzar/cerrar antes de durable cloud completion/failure. Sigue OPEN y sin owner material CYCLE 108 mientras AAA104 ataca startup.

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
Playback candidate stale; no priorizar frente a P1 startup/auth/durability.

### 14.2 — `[ ]`
Queue/seek/shuffle/repeat/error recoverable, responsive volume y Safari/Firefox/Chrome/iPhone/degraded-network evidence pendientes.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH SEAM`
Evidence reusable `NIGHT-WOZ-094`: purge lifecycle existe, pero faltan strong confirmation, recent-reauth seam y deterministic durable action boundary; UI actualmente puede limpiar optimistamente antes de purge completion. Sigue sin owner CYCLE 108 y entra también en blockers D10.2 salvo decisión RO explícita de exclusión para alpha.

### 15.2 / 15.3
A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; no falsear browser/runtime coverage.
