# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-109`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F2 / 15.1 — Empty Trash recent-reauth + strong confirmation + durable purge boundary`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`
- `PREDECESSOR: NIGHT-BBB-108 no dejó RESULTADO DEL TURNO ni matching handoff verificable al preflight JOBS CYCLE 114; SUPERSEDED / NOT_PASS.`
- `SERIALIZATION: BBB109 owns only F2/15.1 Trash/recent-reauth. AAA110 owns F2/13.2. WOZ113 owns PR #93. #92/#89 parked/unassigned. No integration mutation.`

### PRIMARY

**F2 / 15.1 — cerrar o reducir el gap de “Vaciar Trash” con el mínimo corrective, reutilizando la recent-reauth seam canónica.**

1. Fresh preflight sobre live integration, Issue #41, D8 recent-reauth decision y paths Trash/Settings/delete lifecycle; REUSE-FIRST + duplicate-check.
2. Verificar qué existe hoy para purge durable y dónde la UI puede limpiar optimistamente antes de completion.
3. Reutilizar la decisión D8: recent reauth = fresh same-provider authorization ligada a user/session; no inventar password/MFA nuevo ni rediseñar auth.
4. Implementar únicamente si el gap y los paths son claros: strong confirmation + recent-reauth gate + visible success solo después de durable deterministic purge; failure debe quedar visible/reintentable, sin pérdida silenciosa.
5. Preservar delete-retention 0 días / no recoverable tombstone y tenant isolation existentes.
6. Añadir tests focales de confirmation, recent-reauth required/expired, durable success, failure/no-false-success y Web/no-Tauri cuando aplique.
7. Un solo candidate/PR bounded si duplicate-check limpio; **NO MERGE CYCLE 114**.
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

- `NIGHT-BBB-108`: `NO_RESULT / SUPERSEDED / NOT_PASS` en JOBS CYCLE 114.
- `NIGHT-BBB-107`: `CANDIDATE_EXACT_GREEN / NO_MERGE`; PR #93 sigue transferido a WOZ para integration review.
