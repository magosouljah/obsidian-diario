# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Reducir el mayor bloque técnico restante de F0–F4 con REUSE-FIRST y evidencia real, sin inventar infraestructura/costo ni invadir F2/F4. Un turno = una asignación JOBS. WOZ no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-008`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 16.1 candidate closure → 16.2 software-only promotion contract`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`
- `REUSE_PR: #59 / woz/night-16.1-runtime-operability`
- `KNOWN_CANDIDATE_HEAD: 292a7706bc4f6c21eccc60f2838cda0cd8ed4adc`
- `JOBS_PRECHECK: #59 OPEN / Ready / mergeable=true; D6 33256145573 SUCCESS; D7 33256145614 SUCCESS; productive temp-auth compile 33256145521 SUCCESS; Test - Desktop Portability 33256145531 estaba IN_PROGRESS en el último preflight.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F3 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. REUSE-FIRST: continúa exclusivamente #59 para 16.1; no abras candidate duplicado.
3. Revalida head/base y el workflow Test - Desktop Portability `33256145531`. D6/D7/compile ya fueron verificados verdes por JOBS sobre exact head.
4. Si Desktop Portability/Required CI aplicable termina SUCCESS, #59 sigue Ready/mergeable y no cambió la combinación, realiza race-check final y merge protegido con expected-head. Verifica merge SHA. Si falla, corrige la MISMA PR y vuelve a exigir exact-head.
5. Tras merge, 16.1 **no** se marca completo: el contrato software dependency-safe puede quedar DONE/INTEGRATED, pero la separación física staging/prod (projects, DB, storage, bots, OAuth callbacks, secrets/ownership) permanece PENDING_EXTERNAL hasta evidencia real.
6. Después de integrar #59, inicia 16.2 únicamente en el carril **software-only/dependency-safe** y REUSE-FIRST: audita workflows/deploy assets existentes; define/ajusta el contrato reproducible PR→preview, candidate tag→staging, approval→production; API origin/TLS/headers inyectables y release fail-closed sin Tailscale/local fallback; smoke/rollback scripts o fixtures que no requieran desplegar infraestructura real.
7. No crear RDS/provider projects/buckets/bots/OAuth projects/secret stores ni costo nuevo. No ejecutar deploy productivo ni staging real sin credenciales/RO.
8. Si 16.2 requiere infraestructura para probar el último tramo, separa DONE software-only de blocker externo literal. Un único candidate si hay delta real; si ya existe todo, entrega REUSED con evidencia.
9. No volver a D10.1; no tocar Stripe/DNS/legal/F2/F4. Actualiza solo este markdown + Issue #41 con evidencia y STOP.

### Fuera de scope

F1/D10.1; D10.2; F2; F4; Stripe 17.x; legal/DNS 19.x; capacidad 20.x; recursos/costo nuevos; release público; cualquier `!!!PLAN` salvo este markdown.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-007`  
`TURN_STATUS: PENDING_EXTERNAL`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`  
`BRANCH_HEAD: woz/night-16.1-runtime-operability @ 292a7706bc4f6c21eccc60f2838cda0cd8ed4adc`  
`PR: #59 OPEN / Ready / mergeable=true; exact base f0d65aa...`  
`CHANGES: runtime-operability contract /healthz, /readyz fail-closed, drain, proxy trust, bounded timeouts, graceful shutdown, deployment-env contract; no provider resources.`  
`TESTS: local node:test 7/7 PASS.`  
`POST_TURN_JOBS_CI: D6 33256145573 SUCCESS; D7 33256145614 SUCCESS; compile 33256145521 SUCCESS; Test - Desktop Portability 33256145531 todavía IN_PROGRESS en el último fetch.`  
`BLOCKER_16_1: separación física staging/prod real permanece externa aun si #59 integra.`  
`STOP: sí.`

## HISTORIAL

- `NIGHT-WOZ-008`: ASSIGNED — cerrar #59 si exact-head termina verde; después 16.2 software-only/dependency-safe.
- `NIGHT-WOZ-007`: PENDING_EXTERNAL — PR #59 + self-test 7/7; external physical separation.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrado como `f0d65aa...`; D10.1 external-only.
- `NIGHT-WOZ-005`: PENDING — PR #56 candidate.
- `NIGHT-WOZ-004`: PENDING — D10.1 gaps confirmados.
- `NIGHT-WOZ-003`: superseded unprocessed.
- `NIGHT-WOZ-002`: PENDING — D10.1 audit.
- `NIGHT-WOZ-001`: superseded.
- D9: DONE/PASS — Issue #41 `5460959369`.
