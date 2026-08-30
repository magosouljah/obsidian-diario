# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Área:** F3 / 19.2 — legal surfaces de producto.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-045`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 19.2 — SAME PR #76 canonical legal copy in existing Settings surfaces`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `REUSE_PR: #76 / legal/privacy-terms-v1 @ 36d218609cf2488997755312fa2dafd0a019d070`
- `PREDECESSOR: NIGHT-AAA-044 had no RESULTADO DEL TURNO / Issue #41 handoff observable by JOBS CYCLE 049; it is SUPERSEDED and MUST NOT execute late.`
- `HOLD_PR: #69 @ b2ab75ae1dbde4e3aba389da844f466920a5d6eb — STOP_WRITE_SURFACE / DO NOT TOUCH under this assignment.`

### PRIMARY

1. Preflight live integration + SAME #76 exact head/base + duplicate-check. Confirm no other owner has modified #76 after this assignment.
2. REUSE-FIRST: do not create a second legal UI. Reuse the existing Privacy/Terms surfaces in `src/components/SettingsPanel.tsx` and the canonical documents already present on #76 (`docs/legal/PRIVACY.md`, `docs/legal/TERMS.md`).
3. Replace only the temporary August 11 legal copy/placeholders/old contact in the existing in-app Privacy/Terms surfaces with the canonical v1 content/metadata already approved in #76. Use `Bruno Garcia` and `support@beatgaler.com` exactly as the canonical source says.
4. Preserve the existing public `/privacy` and `/terms` routes and unauthenticated links from #76. Do not invent new policy, billing rule, provider, legal promise or UX surface.
5. Add/update only focused tests needed to prove the in-app legal surfaces use the canonical content and no stale Gmail/placeholders remain.
6. Run focused tests plus fresh exact-head applicable CI. Do not merge #76 unless the full PR is race-clean, exact-head green and the authorized owner flow permits it; otherwise leave a structured handoff for JOBS/next owner.
7. Do not touch F2 #69/#70, F4, billing implementation, infrastructure/DNS/deploy, or legal policy text beyond exact canonical reuse.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** live base/head; exact changed files; proof old placeholders/contact removed from Settings legal surfaces; focused tests; fresh exact-head CI; merge SHA only if actually merged.  
**STOP:** canonical docs conflict/ambiguity, another owner mutates #76, required broad product redesign, legal-policy invention, infrastructure/DNS work, or non-attributable CI failure.

### CI-FALLBACK

**F2 / 13.2 READ-ONLY gap map**, only if PRIMARY becomes genuinely `WAITING_CI`/waiting review/merge after its code delta is complete.

**Alcance:** inspect current integration only for ReviewShell Import/Edit/Bulk, fixed CTA/progress N/N, per-item error/retry/skip/cancel/confirmation and existing E2E/component coverage. No branch/PR/commit/write; do not touch #69/#70 or #76 files.  
**Evidencia requerida:** exact baseline + `EXISTS/PARTIAL/GAP/PENDING_DEPENDENCY` matrix, literal paths/symbols/tests and minimum future slices.  
**STOP:** any write, dependency on unmerged #76, overlap with #69/#70, attempt to close 13.2 from audit only, or insufficient source evidence. Recheck PRIMARY before closing.

## RESULTADO PROCESADO — NIGHT-AAA-044

- `STATUS: NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No RESULTADO DEL TURNO or Issue #41 handoff for AAA044 was observable by CYCLE 049.
- No audit/PASS claim is accepted from AAA044.

## RESULTADO PROCESADO — NIGHT-AAA-043

- `STATUS: PENDING / STOP_WRITE_SURFACE`.
- Baseline `a9d35a3d...`; #69 remains OPEN/Ready/mergeable @ `b2ab75ae...`, stale from `3ad8f55a...`.
- #69 remains frozen/unowned; no refresh/product wiring/tests/fresh CI/merge occurred.
- Issue #41 handoff: `5470672560`.

## HOLDING / FROZEN

- F2/13.1 Web #69: frozen/unowned pending patch-capable surface.
- F2/13.1 server #70: frozen by safe-write + stale baseline.
- F4 #74/#71 remain outside AAA045.

## HISTORIAL COMPACTO

- `NIGHT-AAA-045`: ASSIGNED — SAME #76 canonical legal Settings reuse; F2/13.2 read-only CI fallback.
- `NIGHT-AAA-044`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-AAA-043`: PENDING / STOP_WRITE_SURFACE — #69 preserved.
