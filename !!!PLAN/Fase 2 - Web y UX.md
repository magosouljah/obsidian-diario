# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE154:** `integration-v0.8.0-alpha.1 @ c4e203cf5e44cf93c0c017c0120f097473fe91b2`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] #92/#94/#95/#96/#98 INTEGRATED / EXACT RUNTIME-SOURCE CLOSE REVIEW OPEN`

- #98 `fix(web): finalize production MTProto transport` está **MERGED**. Exact candidate head `00da0ab7716242bbd2c7cb8b8cfdea1ca8b3930c`; base anterior `aa445095...`; merge avanzó integration a `c4e203cf...`.
- Exact-head Required CI `33575511576` / check `100081022125` = SUCCESS. Supporting D6/D7/Web build/temp-auth compile/secret scan fueron SUCCESS.
- PR #98 reporta clean production deployment, public/local health PASS, library materialization, artwork y playback success.
- Evidence-before-claim: esos runtime reports no prueban por sí solos una identidad inmutable de deployment/source. **12.1 sigue NOT_PASS** hasta close review literal.
- `NIGHT-AAA-150`: READ-ONLY close review; clasificar cada required runtime item y exact deployment binding. No mutation.

### Issue #97 — `[ 🟡 ] PRE-BETA BLOCKER / ACTIVE OWNER WOZ153`

Issue #97 sigue OPEN y dice `Must be addressed before Beta 1`. Requiere medir first usable cards/full visible library, near-instant normal startup, preservar artwork/playback readiness y validar Desktop + Web.

#98 ya está integrado, por lo que la superficie dejó de estar bloqueada por ownership. `NIGHT-WOZ-153` es owner exclusivo: mínimo correction arquitectónico cross-platform, no Web-only blank-card/hydrate-later hack, exact-head CI y conditional merge del candidate #97 only si exact/green/race-free.

### 13.1 — `[ 🟡 ] FROZEN`

#69 Web y #70 Server siguen candidates históricos stale/frozen; solo REUSE bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP / BLOCKED_WRITE_SURFACE`

AAA114 probó que Review puede avanzar/cerrar antes de durable cloud completion. `platform.cloudData.commitImportedBeat()` aporta boundary awaitable/retry-safe y #69 conserva semantics reutilizables. CYCLE154 sigue `UNASSIGNED`; no abrir concurrentemente si #97 requiere App/startup surface.

### 14.1 / 14.2

#98 prueba funcionalidad Web reportada de playback/artwork; performance/queue/browser evidence no se promueve más allá de lo literal. #97 concentra startup/reveal pre-Beta.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH PRODUCT SEAM`

D8 decidió fresh same-provider authorization ligada a user/session; falta boundary productiva consumible por destructive callers. `NIGHT-BBB-149` posee únicamente esa seam mínima, candidate-only, **NO MERGE / no Trash**. Después se reasigna 15.1 para strong confirmation + durable deterministic purge/no-false-success.

### 15.2 / 15.3

A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; CI software/PR body/source-unbound behavior no sustituyen runtime exacto probado.
