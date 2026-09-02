# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-153`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: Issue #97 — Pre-Beta 1 near-instant library reveal across Web/Desktop`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ c4e203cf5e44cf93c0c017c0120f097473fe91b2`
- `PREDECESSOR: NIGHT-WOZ-152 has no written worker RESULTADO/handoff, but GitHub independently proves its authorized PR #98 integration goal completed: #98 MERGED, exact head 00da0ab7716242bbd2c7cb8b8cfdea1ca8b3930c, Required CI 33575511576 SUCCESS, integration advanced to c4e203cf5e44cf93c0c017c0120f097473fe91b2.`
- `SERIALIZATION: WOZ153 exclusively owns Issue #97 mutation/integration. AAA150 is READ-ONLY F2/12.1 evidence. BBB149 owns recent-reauth. #89 has NO mutation owner and is fallback READ-ONLY only. #93 remains unassigned.`

### PRIMARY

Close the smallest real pre-Beta startup/reveal architecture gap from Issue #97 without Web-only presentation hacks.

1. Fresh preflight live integration, Issue #97, Issue #41, open PRs/branches, changed surfaces and CI; REUSE-FIRST + duplicate-check.
2. Measure/establish current causal path for time-to-first-usable-cards and time-to-full-visible-library on normal library startup. Preserve artwork-first presentation and playback readiness semantics.
3. Reuse #98's now-integrated authoritative INDEX / Web media platform behavior; do not regress temp-auth, Web playback/artwork, D6/D7, Desktop behavior or cloud correctness.
4. Implement the minimum shared/cross-platform architectural correction that materially removes sequential/progressive reveal latency. Do not solve it with a Web-only blank-card/hydrate-later hack.
5. Add focused deterministic tests/metrics where feasible; require Web + Desktop validation appropriate to the changed surface. Any unavailable real runtime evidence remains `UNVERIFIED`.
6. One candidate/PR only after duplicate-check; keep scope bounded to #97. Do not absorb #89, recent-reauth, Trash or Review.
7. Exact-head applicable CI required. Conditional expected-head merge is authorized **for the #97 candidate only** if scope is exact, tests/CI applicable are green, no required review blocker exists and live integration race-check is clean.
8. Maximum claim after merge: `ISSUE97_SOFTWARE_INTEGRATED`; Issue #97 may close only if its literal Web+Desktop acceptance evidence is satisfied. Do not infer Beta readiness from merge alone.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff, then STOP.

**Evidence required:** duplicate-check; causal measurement/baseline; exact files; branch/base/head/PR; tests; Web+Desktop evidence; exact-head CI; review state; race-check; merge SHA/parents if merged; explicit `UNVERIFIED`.  
**STOP:** scope drift, unavailable acceptance evidence misrepresented as PASS, overlap with AAA150/BBB149, any #89/#93 mutation, or merge without exact-green/race-free evidence.

### CI-FALLBACK

**PR #89 / F0 0.9 strictly READ-ONLY refresh-readiness inventory — only while PRIMARY #97 genuinely waits on external CI/review/build after a clean candidate exists.**

- **Independence:** #89 owns security workflow/DNS pinning/server/security docs; separate branch/PR from #97. If preflight discovers actual file/lock/dependency overlap, fallback becomes NONE immediately.
- **Scope:** inspect #89 exact base/head, failed F0/0.9 run `33454881387`, divergence versus live `c4e203cf...`, duplicate-check whether DNS-pinning corrective is already integrated elsewhere, and classify `REUSE_REFRESHABLE / SUPERSEDED / SCOPE_CHANGED`. No mutation/rerun/review/merge/new PR.
- **Evidence required:** live integration SHA; #89 start/end head/base; failed run/cause; changed-file inventory; divergence/duplicate evidence; classification.
- **STOP:** any mutation, rerun, review, merge, new PR, gate promotion, head movement, dependency overlap, or PRIMARY leaves external wait. Return to #97 and recheck before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-152`: no written worker final handoff; authorized integration outcome independently verified as `PR98_PRODUCTION_WEB_MTProto_CLEANUP_INTEGRATED`. This does **not** close F2/12.1 runtime-source proof.
