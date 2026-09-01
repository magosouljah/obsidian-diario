# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE 115:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810` al preflight JOBS.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] #91 INTEGRATED / #92 EXACT-GREEN CANDIDATE PARKED / RUNTIME STILL OPEN`

Evidence ya cerrada:
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [x] silent Worker bootstrap seam acotado por #91: deadline de 30 s solo para `initialize`, `verify`, `get_index`, con fresh Worker on retry;
- [x] #91 exact-head Web/portability/Required CI aplicable PASS e integrado como `134a293985c314eb09c238115e3bcb71e79f1810`.

Live candidate actualizado por GitHub:
- [ 🟡 ] PR #92 `F2/12.1: repair Web startup and transport bootstrap` sigue OPEN/Ready/mergeable;
- exact base `134a293985c314eb09c238115e3bcb71e79f1810`;
- head vivo **`bb67f61135f5767b5d7a8220265ff82317020949`** (el snapshot `9947380...` quedó stale);
- changed files: 8; candidate incluye loader dismissal, Express 5 request containment, Web startup bridge/no-Tauri seams y regressions;
- exact-head workflows sobre `bb67f611...`: Web Production Build `33473295674` SUCCESS; D6 `33473295651` SUCCESS; D7 `33473295616` SUCCESS; Desktop Portability `33473295652` SUCCESS; Productive Temp Auth Compile `33473295563` SUCCESS; F0 secret scan `33473295638` SUCCESS; Upgrade staging skipped/no aplicable.

**CYCLE115: #92 PARKED / UNASSIGNED.** PR #93 conserva la única integration lane porque ya es evidencia directa del blocker Windows Auth alpha y está lista para expected-head review/merge. Si #93 cambia el baseline, #92 deberá refresh/revalidate antes de integración.

**12.1 permanece NOT_PASS.** Después de integrar #92 o equivalente todavía falta probar el resulting canonical deployment:
1. `/web-health` sano;
2. auth-health sano;
3. signed-out startup no queda tapado por loader;
4. authenticated startup completa temporary auth/worker/library o cae a estado recuperable explícito;
5. cold/warm startup real cuantificado;
6. cookie/marker/CSRF restore robustness y terminología pública pendiente según evidence viva.

### 13.1 — `[ 🟡 ] FROZEN`
#69 Web y #70 Server siguen candidates históricos stale/frozen. REUSE semantics solo bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP / OWNER AAA111`

Gate literal: ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa. Evidence reusable demuestra que Review Save/Save All pueden avanzar/cerrar antes de durable cloud completion/failure.

**Owner CYCLE115: `NIGHT-AAA-111`.** Minimum corrective: visible success/close/advance solo después de durable completion; failure/retry visible; Save All partial/failure semantics; focused Web/no-Tauri tests; bounded candidate; **NO MERGE**.

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
Playback candidate stale; no priorizar frente a startup/auth/durability.

### 14.2 — `[ ]`
Queue/seek/shuffle/repeat/error recoverable, responsive volume y Safari/Firefox/Chrome/iPhone/degraded-network evidence pendientes.

### 15.1 — `[ 🟡 ] OWNER BBB110 / RECENT-REAUTH + DURABLE PURGE GAP`

Purge lifecycle existe, pero faltan strong confirmation, recent-reauth seam y deterministic durable action boundary; UI puede limpiar optimistamente antes de purge completion.

**Owner CYCLE115: `NIGHT-BBB-110`.** Debe REUSE la decisión D8 de fresh same-provider authorization ligada a user/session, sin rediseñar auth. Minimum corrective solo si seam existente es suficiente: strong confirmation + recent reauth + visible success después de durable purge + failure/retry/no-false-success. **NO MERGE.** Si la seam productiva indispensable no existe, STOP `RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`.

### 15.2 / 15.3
A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; no falsear browser/runtime coverage.
