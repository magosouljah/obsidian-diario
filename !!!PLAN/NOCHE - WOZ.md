# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F1 — seguridad / datos durables.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Cerrar F1 factual y REUSE-FIRST, sin repetir drills aceptados. Un turno = una asignación JOBS. WOZ no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-006`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F1 / D10.1 — integrar artifact verificado y reducir gate a blocker externo`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 672e133bc9cb8a47a29d4b34e13fc535290e5681`
- `CANDIDATE: PR #56 @ 0abe39e096d10d992764a2d24874e46529109a70`
- `CI_FACTUAL: Test - Desktop Portability 33250824435 SUCCESS; D7 33250824401 SUCCESS; D6 33250824418 SUCCESS; Productive Temp Auth Compile 33250824441 SUCCESS; Upgrade 21.2 Staging skipped/no aplica.`
- `CONTEXT: NIGHT-WOZ-005 redujo D10.1 a un único requisito no demostrable localmente: copia real fuera del primary provider/account failure domain.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F1 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. Revalida PR #56 exact head/base, Ready/non-draft, mergeable y CI exact-head. No rerun ceremonial.
3. Si la combinación sigue compatible con integración `672e133...`, integra PR #56 usando exact-head protection y verifica el SHA resultante.
4. Después publica gate transaction D10.1 actualizado:
   - config+índice/media strategy = PASS integrado;
   - restore/RPO/RTO/core flows = PASS REUSED;
   - access/retention = PASS REUSED;
   - backup-failure condition+routing contract = PASS integrado;
   - off-provider copy = PENDING_EXTERNAL_PROOF.
5. No reclames delivery productivo de backup.failure si no existe; no reclames off-provider copy con dry-run local.
6. Reduce el blocker externo a una acción literal: RO selecciona/autoriza destino fuera del primary provider/account failure domain y se ejecuta una copia mínima + read/checksum verification.
7. No repetir PITR/cutover/restart/migrations/rotation. No iniciar D10.2 ni F3 bajo este Assignment ID.
8. Actualiza solo este markdown y Issue #41 con evidencia; luego STOP.

### Fuera de scope

D10.2 alpha; F2/F3/F4; release público; nueva infraestructura/costo; cualquier `!!!PLAN` salvo este markdown.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-005`  
`TURN_STATUS: PENDING`  
`GATE: D10.1 / PENDING`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ 672e133bc9cb8a47a29d4b34e13fc535290e5681`  
`HEAD_AFTER: woz/d10.1-backup-readiness-contract @ 0abe39e096d10d992764a2d24874e46529109a70`  
`PR: #56 OPEN / ready-for-review / mergeable`  
`CHANGES: executable D10.1 contract cubre control-config+index+media, dry-run manifest+SHA256 y backup.failure routing fail-closed; no falsea off-provider proof.`  
`TESTS: self-test local PASS_LOCAL_CONTRACT.`  
`CI: exact-head posterior verificado por JOBS: Required CI/Test Desktop Portability 33250824435 SUCCESS; D7 33250824401 SUCCESS; D6 33250824418 SUCCESS; compile 33250824441 SUCCESS.`  
`D10.1_MATRIX: config+index/media PASS candidate; restore/RPO/RTO/core PASS REUSED; access/retention PASS REUSED; backup-failure contract PASS candidate; off-provider PENDING_EXTERNAL_PROOF.`  
`BLOCKERS: único EXTERNAL_BLOCKER — evidencia de copia real fuera del primary provider/account failure domain.`  
`STOP: sí.`

## HISTORIAL

- `NIGHT-WOZ-006`: ASSIGNED — integrar PR #56 exact-head y dejar D10.1 external-only factual.
- `NIGHT-WOZ-005`: PENDING — PR #56 candidate; self-test PASS; único blocker off-provider; CI luego verificado SUCCESS por JOBS.
- `NIGHT-WOZ-004`: PENDING — tres gaps literales confirmados.
- `NIGHT-WOZ-003`: superseded unprocessed.
- `NIGHT-WOZ-002`: PENDING — D10.1 REUSE-FIRST audit.
- `NIGHT-WOZ-001`: superseded.
- D9: DONE/PASS — Issue #41 `5460959369`.
