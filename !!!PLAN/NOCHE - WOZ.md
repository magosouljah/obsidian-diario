# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-009`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 16.1 candidate closure → 16.2 software-only promotion contract`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`
- `REUSE_PR: #59 / woz/night-16.1-runtime-operability`
- `KNOWN_CANDIDATE_HEAD: 0e0bf188ceb298c5c6846e56576665b50a69e922`
- `JOBS_PRECHECK: PR #59 OPEN / Ready / mergeable=true; exact base f73c9ee...; Test - Desktop Portability 33258609802 SUCCESS; D6 33258609811 SUCCESS; D7 33258609799 SUCCESS; temp-auth compile 33258609793 SUCCESS.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F3 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. REUSE-FIRST: continúa exclusivamente #59 para 16.1; no abras candidate duplicado.
3. Revalida head/base `0e0bf188...` → `f73c9ee...`, mergeability y checks. CI ya terminó verde después de tu turno anterior, pero debes confirmar que no apareció cambio/failure posterior.
4. Si la combinación sigue vigente, realiza race-check final y merge protegido con expected-head. Verifica merge SHA. Si cambió integration HEAD materialmente, refresca la MISMA PR y exige nuevo exact-head CI.
5. Tras merge, 16.1 NO se marca completo: el contrato software dependency-safe puede quedar DONE/INTEGRATED, pero separación física staging/prod permanece PENDING_EXTERNAL.
6. Después de integrar #59, inicia 16.2 únicamente software-only/dependency-safe y REUSE-FIRST: audita workflows/deploy assets; contrato PR→preview, candidate tag→staging, approval→production; API origin/TLS/headers inyectables y release fail-closed sin Tailscale/local fallback; smoke/rollback scripts/fixtures sin deploy real.
7. Un único candidate para 16.2 solo si existe delta real. Si ya existe todo, reporta REUSED con evidencia.
8. No crear RDS/provider projects/buckets/bots/OAuth projects/secret stores ni costo nuevo. No deploy productivo/staging real. No Stripe/DNS/legal/F2/F4.
9. Actualiza solo este markdown + Issue #41 con evidencia y STOP.

### Fuera de scope

F1/D10.1; D10.2; F2; F4; Stripe 17.x; legal/DNS 19.x; capacidad 20.x; recursos/costo nuevos; release público; cualquier `!!!PLAN` salvo este markdown.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-008`  
`TURN_STATUS: PENDING_CI`  
`BASELINE_AT_PREFLIGHT: f73c9ee8d058df3c780170c8c2a3fabef975c54d`  
`BRANCH_HEAD: 0e0bf188ceb298c5c6846e56576665b50a69e922`  
`PR: #59 OPEN / mergeable=true`  
`TURN_END_BLOCKER: macOS x86_64 / Required CI todavía en curso.`  
`JOBS_POSTCHECK: Test - Desktop Portability 33258609802 terminó SUCCESS; D6/D7/temp-auth compile también SUCCESS; el blocker de CI transitorio desapareció.`

## HISTORIAL

- `NIGHT-WOZ-009`: ASSIGNED.
- `NIGHT-WOZ-008`: PENDING_CI — #59 refreshed a `0e0bf188...`; CI terminó verde después.
- `NIGHT-WOZ-007`: PENDING_EXTERNAL — PR #59 + self-test 7/7; physical separation external.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrado `f0d65aa...`; D10.1 external-only.
- D9: DONE/PASS — Issue #41 `5460959369`.
