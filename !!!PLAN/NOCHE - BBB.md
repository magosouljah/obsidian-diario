# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-113`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1/D8 follow-up → minimal recent-reauth product seam for F2/15.1`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`
- `PREDECESSOR: NIGHT-BBB-112 no dejó matching RESULTADO DEL TURNO/handoff verificable antes de CYCLE118; SUPERSEDED / NOT_PASS. La pieza se reasigna porque el gap RECENT_REAUTH_PRODUCT_SEAM_REQUIRED sigue factual y bloquea F2/15.1.`
- `SERIALIZATION: BBB113 owns only the recent-reauth product seam. AAA114 owns Review. WOZ117 owns #89. No Trash UI/purge implementation this turn and no integration mutation.`

### PRIMARY

**Exponer la seam productiva mínima de recent reauth ya decidida en D8, sin rediseñar auth/session ni implementar todavía Empty Trash.**

1. Fresh preflight live integration `43fdf70e...` + Issue #41 + D8/#53 lineage; REUSE-FIRST + duplicate-check.
2. Confirmar que #95 no cambia la semántica D8 ni crea ya una seam equivalente. Si existe candidate suficiente, reutilizarlo y no duplicar.
3. Reutilizar literalmente la decisión D8: fresh same-provider authorization ligada a user/session. No password/MFA inventado y no nuevo proveedor.
4. Encontrar el punto productivo mínimo donde auth/session puede emitir/verificar un estado `recently reauthenticated` consumible por un caller destructivo.
5. Si existe una primitive interna suficiente, exponer un contrato bounded para Settings/Trash; no tocar SettingsPanel/Trash purge UI en este assignment.
6. La seam debe quedar ligada a la sesión/usuario correctos, expirar/requerir fresh authorization según la semántica existente y fallar cerrado.
7. Añadir focused tests para fresh authorization success, wrong user/session, expired/not-fresh y failure/no-grant; preservar Web/Desktop y D6/D7.
8. Un solo candidate/PR bounded si duplicate-check limpio; exact-head applicable CI. **NO MERGE CYCLE118**.
9. Si exige rediseñar account lifecycle, provider auth o storage/session architecture, STOP `RECENT_REAUTH_SEAM_REDESIGN_REQUIRED` con evidencia exacta.
10. Claim máximo: `RECENT_REAUTH_PRODUCT_SEAM_CANDIDATE_READY`; no cerrar F2/15.1 todavía. Escribir resultado aquí + Issue #41 y STOP.

**Required evidence:** exact existing D8 primitive reused; exact files/functions; contract semantics; tests; branch/base/head/PR; exact-head applicable CI; UNVERIFIED.  
**STOP:** Trash UI/purge behavior, Review, F2/12.1 runtime/deploy, #89/#93, provider mutation, integration mutation, duplicate candidate o architectural redesign.

### CI-FALLBACK

Solo si PRIMARY entra genuinamente en `WAITING_CI`:
- **Scope:** F1/1.7 blocker classification READ-ONLY sobre live state.
- **Evidence required:** cada blocker enlazado a PR/Issue/runtime evidence y clasificado `MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL` sin promover gate.
- **STOP:** cualquier code/branch/PR/plan/provider mutation, decisión RO o fin de WAITING_CI; después recheck PRIMARY.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-112`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE118.
- `NIGHT-BBB-111`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE117.
- `NIGHT-BBB-110`: `BLOCKED_STOP / RECENT_REAUTH_PRODUCT_SEAM_REQUIRED`; evidencia causal sigue reusable.
