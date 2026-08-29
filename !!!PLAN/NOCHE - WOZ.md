# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-013`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 16.2 — refresh + exact-head CI + integrate SAME PR #61`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`
- `REUSE_PR: #61 / woz/night-16.2-promotion-contract`
- `KNOWN_CANDIDATE_HEAD: aef1cd0b1a26be327e561f344d63dae5d8def7ef`
- `STALE_EVIDENCE: prior exact-head CI on aef1cd0... is historical only after #60 moved integration; repository rules already rejected using it for merge.`

### Orden JOBS

1. Preflight factual + race-check contra GitHub vivo, Plan Maestro, F3, Registro, roles, protocolo, este ledger e Issue #41. GitHub manda.
2. REUSE-FIRST exclusivamente SAME #61. No cerrar/reabrir duplicado, no nueva PR semánticamente equivalente.
3. Refrescar la branch existente sobre `7de7b57a...` preservando **solo** el delta F3/16.2. El compare previo ya demostró que el movimiento #60 fue solo tres paths F4 sin overlap semántico; vuelve a comprobarlo antes de mutar.
4. Si el connector no ofrece update-branch/rebase directo, puede usarse una reconstrucción Git-data mínima/merge-union de la **misma branch** únicamente si preserva exactamente el delta de #61 y los dos parents son verificables. No reconstruyas product code a mano ni abras otra PR.
5. Tras cualquier refresh material, exige CI aplicable **nuevo sobre el exact head nuevo**. El verde de `aef1cd0...` no autoriza la combinación post-#60.
6. Cuando CI aplicable esté verde, relee integration y PR; protected merge con expected-head solo si race-check sigue limpio. Después reread de integration + merge parents.
7. Tras merge, declarar únicamente `16.2 SOFTWARE DONE / EXTERNAL TAIL`. No afirmar staging/production físicos, provider resources, DNS/TLS productivo, deploy/rollback real.
8. No iniciar Stripe/D17, F2, F4, infraestructura real ni costo en esta asignación.
9. Si el refresh legítimo es imposible con herramientas disponibles, reporta `BLOCKED_TOOLING` con la operación exacta faltante; no rebajes Required CI ni uses el green viejo.
10. Handoff en este markdown + Issue #41 y STOP.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-012`  
`TURN_STATUS: PENDING_CI_REFRESH`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 7de7b57a508b3cf05cbded81501fbd3da63922a3`  
`HEAD_AFTER: woz/night-16.2-promotion-contract @ aef1cd0b1a26be327e561f344d63dae5d8def7ef (sin refresh post-#60)`  
`PR: #61 OPEN / Ready / mergeable`  
`CHANGES: ninguna a product code. WOZ detectó correctamente baseline movement por #60 y no usó CI viejo como autorización.`  
`TESTS/CI: prior Required CI verde es evidencia histórica; protected merge fue rechazado con Required status check expected después del cambio de base.`  
`EVIDENCE: live integration 7de7b57a...; #61 head aef1cd0...; compare sin overlap material F3/F4; Issue #41 comment 5464188400.`  
`UNVERIFIED: refreshed head sobre 7de7b57a..., exact-head CI nuevo, merge SHA, deploy real.`  
`BLOCKERS: refresh de misma branch + CI nuevo requerido; ningún gate puede rebajarse.`

## HISTORIAL

- `NIGHT-WOZ-013`: ASSIGNED — refresh SAME #61 sobre `7de7b57a...`, CI exact-head nuevo y merge protegido si procede.
- `NIGHT-WOZ-012`: PENDING_CI_REFRESH — merge rechazado correctamente tras movimiento #60; verde viejo no reutilizable para merge.
- `NIGHT-WOZ-011`: PENDING — #61 refreshed a `aef1cd0...`; CI luego verde para ese baseline.
- `NIGHT-WOZ-010`: PENDING — #61 candidate software 16.2.
- `NIGHT-WOZ-009`: PENDING_EXTERNAL — #59 merged `be9e58c...`; physical separation external.
- `NIGHT-WOZ-008`: PENDING_CI.
- `NIGHT-WOZ-007`: PENDING_EXTERNAL.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrado `f0d65aa...`; D10.1 external-only.
- D9: DONE/PASS — Issue #41 `5460959369`.
