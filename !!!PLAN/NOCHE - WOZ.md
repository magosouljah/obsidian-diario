# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Reducir el mayor bloque técnico restante de F0–F4 con REUSE-FIRST y evidencia real, sin inventar infraestructura/costo ni invadir F2/F4. Un turno = una asignación JOBS. WOZ no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-007`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 16.1 — entornos / runtime-operability dependency-safe slice`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`
- `CONTEXT: NIGHT-WOZ-006 integró PR #56. D10.1 quedó exclusivamente PENDING_EXTERNAL_PROOF por copia real fuera del primary provider/account failure domain; no queda trabajo técnico interno útil en ese lane hasta acción externa RO. JOBS reasigna WOZ explícitamente a F3/16.1.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F3 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. REUSE-FIRST: audita primero los assets/runtime/deploy/config existentes para prod/staging, health/readiness/dependency checks, graceful shutdown, timeouts y proxy trust. No asumas que F3 parte de cero.
3. Ejecuta únicamente el slice dependency-safe de 16.1 que pueda demostrarse sin nuevas credenciales/costo:
   - separar/validar contractualmente staging vs producción donde ya exista soporte;
   - health/readiness/dependency checks fail-closed;
   - graceful shutdown, timeouts y proxy trust seguros/reproducibles;
   - documentar el gap exacto de recursos/secretos/callbacks separados si requiere acción externa.
4. No crees una segunda RDS, nueva infraestructura pagada, cuentas/provider projects, buckets o recursos con costo sin autorización RO explícita. No cambies DNS/Stripe/legal.
5. Duplicate-check antes de rama/PR. Si código/config necesita cambio, usa un único candidate mínimo y CI exact-head. Si todo lo dependency-safe ya existe, entrega evidencia REUSED en vez de reimplementarlo.
6. Si staging real separado requiere credenciales/decisión externa, reduce el blocker a una acción literal y no lo declares PASS. La ausencia de staging productivo no impide cerrar subrequisitos puramente software si están demostrados.
7. No volver a D10.1 ni repetir restore/cutover/restart/migrations/rotation. No tocar F2/F4.
8. Actualiza solo este markdown + Issue #41 con evidencia y STOP.

### Fuera de scope

F1/D10.1 off-provider copy; D10.2; F2; F4; Stripe 17.x; legal/DNS 19.x; capacidad 20.2 salvo inspección de dependencias; nueva infraestructura/costo; release público; cualquier `!!!PLAN` salvo este markdown.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-006`  
`TURN_STATUS: PENDING`  
`GATE: D10.1 / PENDING_EXTERNAL_PROOF`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 672e133bc9cb8a47a29d4b34e13fc535290e5681`  
`HEAD_AFTER: integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`  
`PR: #56 MERGED; exact candidate head 0abe39e096d10d992764a2d24874e46529109a70; merge SHA f0d65aa66988e3e1a026e237b65c65a56b098aa9.`  
`CHANGES: integrado el artifact D10.1 que cubre estrategia control-config+index+media y contrato backup.failure condition+routing fail-closed; no se añadió provider/costo ni se falseó off-provider proof.`  
`TESTS: self-test local previo PASS_LOCAL_CONTRACT; no se repitió drill.`  
`CI: REUSED exact-head — Test - Desktop Portability 33250824435 SUCCESS; D7 33250824401 SUCCESS; D6 33250824418 SUCCESS; Productive Temp Auth Compile 33250824441 SUCCESS; Upgrade 21.2 Staging 33250824399 SKIPPED/no aplica.`  
`EVIDENCE_REUSED: restore aislado real; RPO ~7 min <=15 min; RTO 3643 s <=7200 s; core flows PASS; access/retention PASS; exact-head CI verde.`  
`EVIDENCE_NEW: PR #56 merge protegido por expected_head_sha; integración verificada en f0d65aa66988e3e1a026e237b65c65a56b098aa9 con parents 672e133bc9cb8a47a29d4b34e13fc535290e5681 + 0abe39e096d10d992764a2d24874e46529109a70.`  
`D10.1_MATRIX: config+index/media PASS INTEGRATED; restore/RPO/RTO/core PASS REUSED; access/retention PASS REUSED; backup-failure condition+routing contract PASS INTEGRATED; off-provider copy PENDING_EXTERNAL_PROOF.`  
`UNVERIFIED: delivery productivo real de backup.failure; copia real fuera del primary provider/account failure domain.`  
`BLOCKERS: único EXTERNAL_BLOCKER — RO debe seleccionar/autorizar destino fuera del primary provider/account failure domain y ejecutar copia mínima + read/checksum verification.`  
`RECOMMENDATION_TO_JOBS: mantener D10.1 PENDING exclusivamente por off-provider proof; no repetir restore/CI/drills. WOZ queda disponible para reasignación independiente.`  
`TURN_FINISHED_AT: 2026-08-29T06:48:00-06:00`  
`STOP: sí.`

## HISTORIAL

- `NIGHT-WOZ-007`: ASSIGNED — reasignación explícita a F3/16.1 dependency-safe, sin costo/infra nueva no autorizada.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrado como f0d65aa66988e3e1a026e237b65c65a56b098aa9; D10.1 external-only por off-provider proof.
- `NIGHT-WOZ-005`: PENDING — PR #56 candidate; self-test PASS; único blocker off-provider; CI luego verificado SUCCESS por JOBS.
- `NIGHT-WOZ-004`: PENDING — tres gaps literales confirmados.
- `NIGHT-WOZ-003`: superseded unprocessed.
- `NIGHT-WOZ-002`: PENDING — D10.1 REUSE-FIRST audit.
- `NIGHT-WOZ-001`: superseded.
- D9: DONE/PASS — Issue #41 `5460959369`.
