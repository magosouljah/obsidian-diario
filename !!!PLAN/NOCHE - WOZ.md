# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-117`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F0 / 0.9 — REUSE PR #89 DNS-rebinding SSRF P1; refresh/revalidate + conditional integration`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`
- `PREDECESSOR: NIGHT-WOZ-116 no dejó matching RESULTADO DEL TURNO/handoff verificable antes de CYCLE118; SUPERSEDED / NOT_PASS.`
- `LIVE_PR_FACT: #89 sigue OPEN @ daf87da6ffd604ccac991311036919ae2de9bd7a, base registrada 816f946c... y GitHub ahora reporta mergeable=false contra integración 43fdf70e...; exact refresh/revalidation es obligatoria.`
- `SERIALIZATION: WOZ117 exclusively owns #89 refresh/revalidation/integration. AAA114 owns Review; BBB113 owns recent-reauth product seam. #93 remains parked/unassigned.`

### PRIMARY

**F0 / 0.9 — REUSE #89; preservar solo el bounded SSRF P1/audit slice, refrescar sobre integración viva y mergear únicamente bajo evidencia exacta.**

1. Fresh preflight integration HEAD, #89 base/head/mergeability/changed files, Issue #41 y owner collision.
2. Duplicate-check por cualquier SSRF/DNS-pinning corrective posterior ya integrado, incluyendo el nuevo PR #95 baseline. Si duplicate/resolved, STOP con evidencia en vez de refrescar.
3. Reconcile #89 history-preserving sobre `43fdf70e...` o el live baseline más reciente; preservar F2/12.1 #92/#94/#95, auth/session y release changes.
4. Scope debe seguir exactamente AI-assisted audit docs + DNS-rebinding SSRF hardening/regression/workflow. No unrelated security cleanup.
5. Run exact-head F0/0.9 security gate + all applicable required CI después del refresh. Old-head green no es autoritativo.
6. Inmediatamente antes de integrar: recheck integration HEAD, #89 exact refreshed head/base, changed files, mergeability, CI y owner collisions.
7. Si exact/green/race-free, WOZ117 está autorizado a expected-head merge **PR #89 solamente** y verificar merge SHA + parents.
8. Maximum claim: `F0/0.9 DNS_REBINDING_SSRF_P1_CORRECTIVE_INTEGRATED`; AI-assisted audit no es independent pentest y F0 global permanece abierto.
9. No tocar #93, Review, recent-reauth/Trash ni production deploy/runtime.
10. Escribir RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** duplicate-check; pre/post integration SHA; exact refreshed #89 base/head; changed-file inventory; exact-head security/required CI conclusions; merge SHA/parents si merged; residual P0/P1/P2/P3 y independent-review UNVERIFIED.  
**STOP:** unsafe refresh, scope drift, failed/cancelled required CI, mergeability/race change, newer duplicate, auth/F2 collision o cualquier integration mutation distinta de expected-head #89.

### CI-FALLBACK

Solo si PRIMARY entra genuinamente en `WAITING_CI`:
- **Scope:** F4/25.1 / PR #93 blocker classification **READ-ONLY** against live baseline only; no branch refresh and no mutation.
- **Evidence required:** current #93 base/head/mergeability, historical exact-green evidence that remains reusable, and exact reasons why canonical refresh is still required.
- **STOP:** cualquier code/branch/PR/provider/plan mutation, RO decision, o PRIMARY CI leaves WAITING_CI; then recheck #89 before closing.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-WOZ-116`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE118.
- `NIGHT-WOZ-115`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE117.
