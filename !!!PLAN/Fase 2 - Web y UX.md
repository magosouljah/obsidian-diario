# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE153:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] #92 + #94 + #95 + #96 INTEGRATED / PR #98 ACTIVE / RUNTIME CLOSE REVIEW OPEN`

Evidence factual:
- PR #92 MERGED → `ada77811059a3319b271dcc98dd5d95efe807dec`.
- PR #94 MERGED → `08e5802d27ad81977b1c2f63ceb0fce398d41e42`.
- PR #95 MERGED → `43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.
- PR #96 MERGED → exact head `6247173ead703f831801fa103ca465fea04e5793`, merge `aa4450956579de381e82acf06c660b658c703cd1`, Required CI exact-head SUCCESS.
- **PR #98 NEW/OPEN:** `fix(web): finalize production MTProto transport`; exact base `aa445095...`, exact head `00da0ab7716242bbd2c7cb8b8cfdea1ca8b3930c`, 1 commit / 6 files. Root cause/fixes include Worker temp-auth key ownership, productive binder runtime, Web artwork/playback platform routing and authoritative INDEX startup behavior.
- At CYCLE153 assignment snapshot: D6 `33575511574` SUCCESS; D7 `33575511573` SUCCESS; Web Production Build `33575511615` SUCCESS; Productive Temp Auth Compile `33575511604` SUCCESS; F0 secret scan `33575511622` SUCCESS; Test - Desktop Portability / Required CI `33575511576` still IN_PROGRESS.
- PR #98 reports clean production deployment, public/local health PASS, library materialization, artwork and playback success. These claims are useful evidence but deployment-source identity must be bound literally before JOBS closes the runtime gate.

**12.1 remains NOT_PASS.**  
**AAA149:** exact runtime/deployment evidence READ-ONLY; no code/deploy/PR mutation.  
**WOZ152:** exclusive PR #98 mutation/integration owner; conditional expected-head merge only if exact/green/race-free.

### Issue #97 — `[ 🟡 ] PRE-BETA BLOCKER / DEFER IMPLEMENTATION UNTIL #98 CLEANUP`

`Pre-Beta 1: make library reveal near-instant across Web/Desktop` está OPEN y explícitamente requiere resolución antes de Beta 1. Acceptance direction: medir first usable cards/full visible library, near-instant normal startup, preservar artwork/playback semantics y validar Desktop + Web.

No mezclar #97 en #98: ambos tocan startup/presentation y #98 ya posee `src/App.tsx`/platform surfaces. CYCLE153 solo separa y registra el blocker. Implementation owner se emite después de que #98 deje de ocupar esa superficie.

### 13.1 — `[ 🟡 ] FROZEN`
#69 Web y #70 Server siguen candidates históricos stale/frozen. REUSE semantics solo bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP / BLOCKED_WRITE_SURFACE`

AAA114 revalidó que `handleReviewedBeatSaved` y `handleReviewedSaveAll` pueden advance/close antes de durable cloud completion. `platform.cloudData.commitImportedBeat()` aporta boundary awaitable/retry-safe y #69 conserva semantics reutilizables.

AAA114 no abrió candidate porque la superficie disponible exigía whole-file replacement de `src/App.tsx`, con riesgo de corrupción/scope widening. Resultado: `PENDING / STOP_WRITE_SURFACE / NOT_PASS`. **CYCLE153: UNASSIGNED.** Además #98 posee actualmente `src/App.tsx`, por lo que no se abre owner concurrente.

### 14.1 / 14.2
Playback funcional Web es evidencia de #98, pero performance/queue/browser evidence no se promueve más allá de lo literal. #97 pasa a ser el blocker startup-performance explícito pre-Beta.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH PRODUCT SEAM`

La decisión D8 existe, pero falta seam bounded de fresh same-provider authorization ligada a user/session y consumible por destructive callers.

**Owner CYCLE153: `NIGHT-BBB-148` únicamente para la seam D8 mínima.** No Trash UI/purge en ese assignment. Después se reasigna 15.1 para strong confirmation + durable deterministic completion/failure sin false success.

### 15.2 / 15.3
A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; no falsear browser/runtime coverage ni confundir CI software, PR description o behavior source-unbound con deployment exacto probado.
