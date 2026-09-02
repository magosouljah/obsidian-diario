# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-154`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: Issue #97 — Pre-Beta 1 near-instant library reveal across Web/Desktop`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`
- `PREDECESSOR: NIGHT-WOZ-153 = NO_RESULT / SUPERSEDED / NOT_PASS; no matching worker RESULTADO/handoff after CYCLE154.`
- `LIVE_FACT: Issue #97 remains OPEN with zero comments and literal Must be addressed before Beta 1 acceptance. PR #99 has since merged and moved integration to c2766fb..., but it is deployment-provenance plumbing, not a #97 closure.`
- `SERIALIZATION: WOZ154 exclusively owns Issue #97 mutation/integration. AAA151 owns PR #89. BBB150 owns recent-reauth. #93 remains unassigned.`

### PRIMARY

Close the smallest real pre-Beta startup/reveal architecture gap from Issue #97 without Web-only presentation hacks.

1. Fresh preflight live integration, Issue #97, Issue #41, open PRs/branches, changed surfaces and CI; REUSE-FIRST + duplicate-check.
2. Measure/establish current causal path for time-to-first-usable-cards and time-to-full-visible-library on normal library startup. Preserve artwork-first presentation and playback readiness semantics.
3. Reuse integrated #98 Web media/index behavior and #99 provenance plumbing; do not regress temp-auth, Web playback/artwork, D6/D7, Desktop behavior, deployment provenance, or cloud correctness.
4. Implement the minimum shared/cross-platform architectural correction that materially removes sequential/progressive reveal latency. Do not solve it with a Web-only blank-card/hydrate-later hack.
5. Add focused deterministic tests/metrics where feasible; require Web + Desktop validation appropriate to the changed surface. Any unavailable real runtime evidence remains `UNVERIFIED`.
6. One candidate/PR only after duplicate-check; keep scope bounded to #97. Do not absorb #89, recent-reauth, Trash or Review.
7. Exact-head applicable CI required. Conditional expected-head merge is authorized **for the #97 candidate only** if scope is exact, tests/CI applicable are green, no required review blocker exists and live integration race-check is clean.
8. Maximum claim after merge: `ISSUE97_SOFTWARE_INTEGRATED`; Issue #97 may close only if its literal Web+Desktop acceptance evidence is satisfied. Do not infer Beta readiness from merge alone.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Evidence required:** duplicate-check; causal measurement/baseline; exact files; branch/base/head/PR; tests; Web+Desktop evidence; exact-head CI; review state; race-check; merge SHA/parents if merged; explicit `UNVERIFIED`.  
**STOP:** scope drift, unavailable acceptance evidence misrepresented as PASS, overlap with AAA151/BBB150, any #89/#93 mutation, or merge without exact-green/race-free evidence.

### CI-FALLBACK

`CI-FALLBACK: NONE`.

Reason: #93 may overlap Desktop harness/auth surfaces and F2/12.1 production-source proof is materially dependent on the canonical integration SHA that a #97 merge would change. No independent fallback is safe enough to preauthorize this cycle.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-153`: no matching worker final result/handoff after CYCLE154 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-152`: previous authorized #98 integration outcome remains independently verified historical evidence only.
