# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-010`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 16.2 — software-only reproducible promotion/deploy contract`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ be9e58c9edc0bb40742e0b91e3f2ebe771ace502`
- `JOBS_PRECHECK: PR #59 quedó MERGED como be9e58c9... con parents f73c9ee... + 0e0bf188...; 16.1 runtime/software contract puede procesarse DONE/INTEGRATED. La separación física staging/production continúa PENDING_EXTERNAL y no se reabre ni se falsea.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F3 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. Da por consumido el cierre verificable de #59; no reabras 16.1 runtime ni repitas CI/drills aceptados.
3. 16.1 completo permanece `[ 🟡 ] / PENDING_EXTERNAL` por separación física real de provider projects/DB/storage/bots/OAuth callbacks/secrets/ownership. No crear esos recursos ni costo.
4. Ejecuta **16.2 software-only/dependency-safe** con REUSE-FIRST: audita workflows/deploy assets existentes antes de crear nada.
5. Cierra o implementa únicamente contratos reproducibles que puedan probarse sin provider resources: PR→preview; candidate tag→staging; approval→production; mismo source SHA; API origin/TLS/headers inyectables; release fail-closed sin Tailscale/local fallback; smoke post-deploy y rollback al último artifact/DB compatible.
6. Un único candidate solo si existe delta real. Si los requisitos ya están cubiertos literalmente, reporta `REUSED` con paths/tests/evidence y no abras PR ceremonial.
7. Tests/CI exact-head aplicables. Si necesitas candidate, race-check e integración solo cuando la combinación vigente esté verde; si integration cambia materialmente, refresh + CI nuevo.
8. No Stripe 17.x, billing 18.x, DNS/legal 19.x, capacity 20.x, F2/F4, release público ni recursos/credenciales/costo nuevos.
9. Mantén explícitos como `PENDING_EXTERNAL` los deploys reales que requieran provider/RO; el contrato software no equivale a staging real.
10. Actualiza solo este markdown + Issue #41 con resultado de `NIGHT-WOZ-010` y STOP.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-009`  
`TURN_STATUS: PENDING_EXTERNAL`  
`BASELINE_BEFORE: integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`  
`PR: #59 / head 0e0bf188ceb298c5c6846e56576665b50a69e922`  
`MERGE: be9e58c9edc0bb40742e0b91e3f2ebe771ace502`  
`BASELINE_AFTER: integration-v0.8.0-alpha.1 @ be9e58c9edc0bb40742e0b91e3f2ebe771ace502`  
`RESULT: exact-head/race-check válido, #59 integrado; runtime software 16.1 DONE/INTEGRATED; physical staging/prod sigue external. 16.2 no iniciado.`

## HISTORIAL

- `NIGHT-WOZ-010`: ASSIGNED — F3/16.2 software-only.
- `NIGHT-WOZ-009`: PENDING_EXTERNAL — #59 merged `be9e58c...`; physical separation remains external.
- `NIGHT-WOZ-008`: PENDING_CI — #59 refreshed; CI terminó verde después.
- `NIGHT-WOZ-007`: PENDING_EXTERNAL — PR #59 + self-test 7/7; physical separation external.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrado `f0d65aa...`; D10.1 external-only.
- D9: DONE/PASS — Issue #41 `5460959369`.
