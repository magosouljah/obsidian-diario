# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F1 — seguridad / datos durables.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Cerrar F1 factual y REUSE-FIRST, sin repetir drills aceptados. Un turno = una asignación JOBS. WOZ no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-005`
- `ASSIGNMENT_STATUS: PENDING`
- `AREA: F1 / D10.1 — backup readiness / minimal verifiable artifact`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`
- `OBSERVED_BASE_AT_EXECUTION: integration-v0.8.0-alpha.1 @ 672e133bc9cb8a47a29d4b34e13fc535290e5681`
- `CONTEXT: NIGHT-WOZ-005 produjo el artifact mínimo verificable; quedan cerrados localmente coverage config+index/media y backup-failure condition/routing. La copia off-provider literal sigue requiriendo prueba externa real.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F1 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub/runtime actual.
2. REUSE-FIRST estricto. No repetir restore, cutover, restart, migrations ni rotation ya aceptados.
3. Construye/reutiliza **un solo artifact mínimo** que convierta los tres gaps restantes en evidencia verificable sin aprovisionar costo/credenciales por inferencia:
   - matriz/contrato ejecutable de cobertura de backup para config + índice/media como conjunto;
   - mecanismo/contrato de copia off-provider con dry-run o verificación local segura si puede demostrarse sin proveedor nuevo; si el requisito literal exige un destino externo real, deja exactamente ese punto como EXTERNAL_BLOCKER;
   - backup-failure alert específica: config/test/validator que pruebe la condición y el routing esperado sin inventar delivery productivo si no existe.
4. Duplicate-check antes de crear rama/PR. Si ya existe artifact que satisface literalmente, úsalo y no dupliques.
5. Si hay cambio técnico/documental versionado necesario, artifact mínimo + tests/CI aplicables. Si requiere credencial, proveedor o costo real, no lo ejecutes por inferencia: reduce a una sola acción externa concreta.
6. Emite matriz D10.1 `PASS | PENDING | FAIL` requirement por requirement y handoff Issue #41.
7. No iniciar D10.2 ni F3 bajo este Assignment ID.
8. Actualiza solo este markdown y STOP.

### Fuera de scope

D10.2 alpha; F2/F3/F4; release público; nueva infraestructura de costo; repetir drills 5.2; cualquier `!!!PLAN` salvo este markdown nocturno.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-005`  
`TURN_STATUS: PENDING`  
`GATE: D10.1 / PENDING`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 672e133bc9cb8a47a29d4b34e13fc535290e5681`  
`HEAD_AFTER: woz/d10.1-backup-readiness-contract @ 0abe39e096d10d992764a2d24874e46529109a70`  
`PR: #56 OPEN / ready-for-review`  
`CHANGES: cloud-server/d10-backup-readiness-contract.mjs — único artifact autocontenido con contrato de coverage control-config+index+media, dry-run manifest+SHA256 que explícitamente no reclama prueba externa y validador/simulación backup.failure con routing fail-closed.`  
`TESTS: node cloud-server/d10-backup-readiness-contract.mjs --self-test => PASS_LOCAL_CONTRACT; coverage [control-config,index,media]; backupFailureAlert PASS_CONDITION_AND_ROUTE_VALIDATION; offProvider PENDING_EXTERNAL_PROOF; manifest SHA256 b44e2b863ef905acd5e0a671ca3bb8d936263369928c5290be7e2ff43be3a8ae.`  
`CI: exact-head workflows disparados para 0abe39e096d10d992764a2d24874e46529109a70; Test - Desktop Portability run 33250824435 estaba QUEUED al cierre; Upgrade 21.2 Staging skipped por no aplicar. No se reejecutó ningún drill productivo.`  
`EVIDENCE_REUSED: isolated PITR restore; RPO ~7 min <=15 min; RTO 3643 s <=7200 s; core flows; encryption; retention; least privilege; 5.2 aceptado.`  
`EVIDENCE_NEW: PR #56; commit 0abe39e096d10d992764a2d24874e46529109a70; self-test local PASS; dry-run manifest/checksum; Issue #41 handoff del turno.`  
`D10.1_MATRIX: backup config+index/media strategy = PASS via executable contract; isolated restore/RPO/RTO/core flows = PASS REUSED; access/retention = PASS REUSED; backup-failure condition+routing contract = PASS; off-provider copy = PENDING_EXTERNAL_PROOF.`  
`UNVERIFIED: delivery productivo real de backup.failure; existencia/lectura de una copia real fuera del primary provider/account failure domain; CI final del exact head al momento de STOP.`  
`BLOCKERS: EXTERNAL_BLOCKER único — producir evidencia de una copia real off-provider/off-account verificable (destino externo ya aprobado o decisión/credencial RO); no puede satisfacerse con local dry-run sin falsear el requisito.`  
`RECOMMENDATION_TO_JOBS: mantener D10.1 PENDING solo por off-provider proof; consumir CI final de PR #56 y, si verde, integrar el artifact sin repetir restore. Reducir la acción externa a: seleccionar/autorizar destino fuera del primary provider/account failure domain y ejecutar una copia mínima + read/checksum verification; luego WOZ puede cerrar D10.1 sin nuevo drill de PITR.`  
`TURN_FINISHED_AT: 2026-08-29T05:45-06:00`

## HISTORIAL

- `NIGHT-WOZ-005`: PENDING — PR #56 / executable D10.1 contract; coverage + backup-failure routing PASS local; único blocker real = off-provider proof; CI exact-head en curso al STOP.
- `NIGHT-WOZ-004`: PENDING — tres gaps literales seguían abiertos; Issue #41 `5461893650`.
- `NIGHT-WOZ-003`: SUPERSEDED_UNPROCESSED.
- `NIGHT-WOZ-002`: PENDING — D10.1 audit REUSE-FIRST; Issue #41 `5461379758`.
- `NIGHT-WOZ-001`: superseded before execution.
- D9: DONE/PASS — Issue #41 `5460959369`.
