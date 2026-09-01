# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-108`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 15.1 — Empty Trash recent-reauth + strong confirmation + durable purge boundary`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`
- `PREDECESSOR: NIGHT-BBB-107 produjo PR #93 exact-head green; JOBS CYCLE 113 procesó el resultado y transfirió #93 a WOZ112 para integration review. BBB108 ya no posee #93.`
- `SERIALIZATION: BBB108 owns only F2/15.1 Trash/recent-reauth. AAA109 owns F2/13.2. WOZ112 owns PR #93. #92/#89 parked/unassigned. No integration mutation.`

### PRIMARY

**F2 / 15.1 — cerrar o reducir el gap de “Vaciar Trash” con el mínimo corrective, reutilizando la recent-reauth seam canónica.**

1. Fresh preflight sobre live integration, Issue #41, D8 recent-reauth decision y paths Trash/Settings/delete lifecycle; REUSE-FIRST + duplicate-check.
2. Verificar qué existe hoy para purge durable y dónde la UI puede limpiar optimistamente antes de completion.
3. Reutilizar la decisión D8: recent reauth = fresh same-provider authorization ligada a user/session; no inventar password/MFA nuevo ni rediseñar auth.
4. Implementar únicamente si el gap y los paths son claros: strong confirmation + recent-reauth gate + visible success solo después de durable deterministic purge; failure debe quedar visible/reintentable, sin pérdida silenciosa.
5. Preservar delete-retention 0 días / no recoverable tombstone y tenant isolation existentes.
6. Añadir tests focales de confirmation, recent-reauth required/expired, durable success, failure/no-false-success y Web/no-Tauri cuando aplique.
7. Un solo candidate/PR bounded si duplicate-check limpio; **NO MERGE CYCLE 113**.
8. Si falta una seam productiva indispensable o tocar auth/session core sería necesario, STOP `RECENT_REAUTH_PRODUCT_SEAM_REQUIRED` en vez de ampliar scope.
9. Escribir RESULTADO DEL TURNO aquí + Issue #41 y STOP.

**Required evidence:** exact files/functions; existing purge semantics; exact recent-reauth seam reused; before/after UI durability; tests; branch/base/head/PR; exact-head CI; UNVERIFIED.  
**STOP:** auth/session core redesign, Review, #89/#92/#93, provider/deploy, integration mutation, ambiguous destructive semantics o duplicate candidate.

### CI-FALLBACK

Solo si PRIMARY entra en `WAITING_CI` por CI/build remoto real:
- **Scope:** F1/1.7 blocker classification **READ-ONLY** usando GitHub/plan vivo; preparar matriz `PROVEN / MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL` para alpha interna 3–5 cuentas.
- **Evidence required:** cada fila debe citar evidencia ya existente; no cerrar gates, no tomar decisión RO, no editar Plan Maestro/fases, no tocar provider/infra/código.
- **STOP:** cualquier necesidad de implementación, decisión RO, plan mutation, provider call, o si PRIMARY deja de estar WAITING_CI. Después recheck PRIMARY antes de cerrar turno.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

- `NIGHT-BBB-107`: `CANDIDATE_EXACT_GREEN / NO_MERGE`. PR #93 `bbb/night-25.1-auth-live-rebuild @ b2c4eb441280343c4b9c39d57851c6d3da33abaa`, exact base `134a293...`, changed files limitados a workflow/runner/auth E2E harness; no product files. Exact-head workflow runs: Windows Auth `33468863393` SUCCESS, job `99734302105` SUCCESS incluyendo `Run isolated Windows auth assertions`; D6/D7/Desktop Portability/Windows Import/secret scan SUCCESS; staging skipped/no aplicable. Product assertions permanecen token persistence + AccountGate exit. Claim máximo procesado: `F4/25.1 WINDOWS_AUTH_CANDIDATE_EXACT_GREEN`; global 25.1 aún no cerrado.
- `NIGHT-BBB-106`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 112.
- `NIGHT-BBB-105`: `BLOCKED_STOP / HARNESS_ONLY_PROVEN_REFRESH_UNSAFE`; causal evidence reusable.
