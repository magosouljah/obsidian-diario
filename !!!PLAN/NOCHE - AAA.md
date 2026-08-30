# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Área:** F3 / 19.2 — legal surfaces de producto.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-046`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 19.2 — SAME PR #76 refresh + canonical Settings reuse`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`
- `REUSE_PR: #76 / legal/privacy-terms-v1 @ 36d218609cf2488997755312fa2dafd0a019d070`
- `PREDECESSOR: NIGHT-AAA-045 produced no RESULTADO DEL TURNO / Issue #41 handoff observable before JOBS CYCLE 050; SUPERSEDED and MUST NOT execute late.`
- `FACTUAL_CHANGE: PR #73 merged and moved integration from a9d35a3d... to a306e3b3...; #76 is now diverged/behind and cannot reuse old exact-base evidence without refresh.`
- `HOLD_PR: #69 @ b2ab75ae1dbde4e3aba389da844f466920a5d6eb — STOP_WRITE_SURFACE / DO NOT TOUCH.`

### PRIMARY

1. Preflight live integration + SAME #76 exact head/base + duplicate-check. Confirm no other owner has modified #76.
2. REUSE-FIRST: keep SAME #76; do not create a replacement PR or second legal UI.
3. Reconcile #76 narrowly onto live integration `a306e3b3...`. If conflict requires broad product redesign, STOP/PENDING rather than expanding scope.
4. Reuse canonical `docs/legal/PRIVACY.md` + `docs/legal/TERMS.md` and the existing Privacy/Terms surfaces in `src/components/SettingsPanel.tsx`.
5. Replace only stale temporary August 11 copy/placeholders/old contact in Settings with canonical v1 content/metadata already approved in #76. Do not invent policy text.
6. Preserve public `/privacy` and `/terms` routes and unauthenticated entry links from #76.
7. Add/update only focused tests proving canonical in-app legal content and absence of stale placeholders/contact.
8. Run focused tests + fresh applicable exact-head CI on the refreshed head. Merge only if race-clean, mergeable and all required evidence applies; otherwise structured handoff.
9. Do not touch #69/#70, F4, billing implementation, provider resources, infra/DNS/deploy, or legal policy beyond canonical reuse.
10. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live base/head; refreshed head/base; changed files; proof stale Settings legal copy removed; focused tests; fresh exact-head CI; merge SHA only if actually merged.  
**STOP:** another owner changes #76, broad conflict, policy ambiguity/invention, infra/DNS/deploy requirement, non-attributable CI failure, or overlap with another owner.

### CI-FALLBACK

**F2 / 13.2 READ-ONLY gap map**, only if PRIMARY becomes genuinely `WAITING_CI`/waiting review/merge after the refreshed code delta is complete.

**Alcance:** inspect live integration only for ReviewShell Import/Edit/Bulk, fixed CTA/progress N/N, per-item error/retry/skip/cancel/confirmation and existing E2E/component coverage. No branch/PR/commit/write; do not touch #69/#70/#76 files.  
**Evidencia requerida:** exact baseline + `EXISTS/PARTIAL/GAP/PENDING_DEPENDENCY` matrix, literal paths/symbols/tests and minimum future slices.  
**STOP:** any write, dependency on unmerged #76, overlap with #69/#70, attempt to close 13.2 from audit only, or insufficient source evidence. Recheck PRIMARY before closing.

## RESULTADO PROCESADO — NIGHT-AAA-045

- `STATUS: NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No RESULTADO DEL TURNO or Issue #41 handoff was observable before CYCLE 050.
- GitHub live changed materially because #73 merged; AAA045's original exact-base assumption is stale.

## RESULTADO PROCESADO — NIGHT-AAA-043

- `STATUS: PENDING / STOP_WRITE_SURFACE`.
- #69 remains frozen/unowned; no refresh/product wiring accepted.
- Issue #41 handoff: `5470672560`.

## HOLDING / FROZEN

- F2/13.1 Web #69: frozen/unowned pending patch-capable surface.
- F2/13.1 server #70: frozen by safe-write + stale baseline.
- F4 remains outside AAA046.

## HISTORIAL COMPACTO

- `NIGHT-AAA-046`: ASSIGNED — SAME #76 refresh + canonical Settings reuse; F2/13.2 read-only CI fallback.
- `NIGHT-AAA-045`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-AAA-044`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-AAA-043`: PENDING / STOP_WRITE_SURFACE — #69 preserved.
