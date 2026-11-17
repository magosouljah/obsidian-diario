# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-156`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: Issue #97 — REUSE PR #100, measure then close near-instant library reveal across Web/Desktop`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`
- `PREDECESSOR: NIGHT-WOZ-155 = ACTIVE_PROGRESS_SUPERSEDED_BY_FRESH_ASSIGNMENT; no terminal RESULTADO DEL TURNO/handoff exists yet, but GitHub live produced PR #100 during CYCLE157.`
- `LIVE_FACT: PR #100 OPEN/Ready on exact base c2766fb... @ head 5f0a0727edacbcb404eb4e31571468262744ec95. It is observational instrumentation only; it records startup surfaces/card counts and explicitly does not change startup/performance behavior. CI is running. This is progress, not Issue #97 closure.`
- `SERIALIZATION: WOZ156 exclusively owns Issue #97 and PR #100 mutation/integration. AAA153 owns #89. BBB152 owns recent-reauth. #93 remains unassigned.`

### PRIMARY

REUSE PR #100; do not open a duplicate #97 candidate.

1. Fresh preflight: live integration, #97, #100 base/head/files/checks/reviews, Issue #41 and duplicate-check.
2. Let the current exact-head instrumentation CI finish; do not treat green instrumentation as #97 PASS.
3. Use the tracer to obtain factual Web + Desktop startup sequences and measure time-to-first-usable-cards / full-visible-library, including whether `Empty Gallery` appears while truth is unresolved.
4. From those measurements isolate the causal bottleneck. Amend/reconstruct the same #100 lineage with the minimum shared/cross-platform correction; no Web-only blank-card/hydrate-later presentation hack and no false empty-state masking.
5. Preserve artwork-first presentation, playback readiness, #98 Web media/index behavior, #99 provenance, temp-auth and D6/D7 semantics.
6. Add focused deterministic tests around the corrected startup truth/reveal behavior. Real unavailable runtime evidence stays `UNVERIFIED`.
7. Exact-head applicable CI after the actual correction. Conditional expected-head merge is authorized for #100 only when the candidate contains the bounded correction (not instrumentation-only), Web+Desktop evidence is sufficient for the literal changed behavior, required CI is green, no review blocker exists and integration race-check is clean. If AAA153 moves integration first, refresh/revalidate before merge.
8. Maximum claim after merge: `ISSUE97_SOFTWARE_INTEGRATED`; close Issue #97 only if literal Web+Desktop acceptance evidence supports it. Do not infer Beta readiness from merge alone.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Evidence required:** #100 start/end base+head; exact changed files; CI/check IDs; Web/Desktop traces and measurements; causal finding; exact correction; tests; review/race state; merge SHA/parents if merged; explicit `UNVERIFIED`.  
**STOP:** duplicate #97 PR, merging instrumentation-only as if it closed #97, scope drift, unavailable acceptance evidence represented as PASS, overlap with AAA153/BBB152, any #89/#93 mutation, or merge without exact-green/race-free evidence.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

Reason: while #100 waits on CI, its next safe action is the same PRIMARY lane (collecting/using #97 measurements once executable). F2/12.1 source proof is canonical-SHA dependent; #93 and recent-reauth carry separate ownership/dependency constraints.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-155`: no terminal RESULTADO DEL TURNO/handoff before CYCLE157, but PR #100 appeared live during JOBS preflight; classified `ACTIVE_PROGRESS / SUPERSEDED_BY_NIGHT-WOZ-156`, not PASS.
- `NIGHT-WOZ-152`: previous authorized #98 integration remains historical evidence only.
