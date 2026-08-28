# Registro de avances — BeatGaler

> Ledger compacto. Diffs/logs/handoffs extensos viven en GitHub, Actions e Issue #41.

## 2026-08-22 a 2026-08-24 — base

- 0.1 `[x]` Baseline/NO-GO y release ledger.
- 0.2 `[x]` checkpoint interno; no release público.
- 1.1 `[x]` negocio v1 comercial; no free-only.
- 1.2 `[ 🟡 ]` dependencias externas/release.
- 2.1 `[x]` contención auth/ownership/límites.
- 2.2 `[ 🟡 ]` incidente Git: HEAD sanitizado, tail externo/histórico pendiente.
- 3.1 `[x]` integración `integration-v0.8.0-alpha.1`, versión `0.8.0-alpha.1`.
- 3.2 `[x]` contrato plataforma PR #8 / merge `32a38c490a53650a0e9d6435c50cd009ef1b5123`.
- 4.1 `[x]` Required CI PR #9 / merge `c7894ad3c2b3e296e3d2939d73953b159e48852f`.
- 4.2 `[x]` supply chain PR #10 / merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; deuda GPL separada.

## 2026-08-24 a 2026-08-25 — 5.1

- PRs #13–#18: temporary auth + transferencia directa **1,992,294,400 bytes**, `galer_cloud_file_bytes=0`; permanent auth/token/API hash no llegan al cliente.
- PRs #23–#27: plataformas/pool/delete/expiry/recovery.
- 5.1 `[x]`: PR #28 / merge `d9ae76f42faee3a7207b9232b7421a0bec20b090` + CI + RO.

## 2026-08-25 a 2026-08-28 — 5.2

- PRs #29–#42: PostgreSQL/migrations, encryption/keyring, importer, durable ops/reconciliation/rollback/recovery, fail-closed cutover y AWS boundary.
- PostgreSQL autoridad productiva + restart durable + rollback dry-run CURRENT PG.
- PITR: RPO ~7 min; RTO `3643 s`.
- Key activa 2, versiones 1/2; lectura ciphertext v1.
- Alarmas RDS + on-call/rotation/rollback authority.
- 5.2 `[x]`: WOZ/RO Issue #41 `5448976400`. No repetir drills aceptados sin invalidación.
- Follow-up release: rotación OAuth client secret visible durante troubleshooting antes de release; no registrar valor.

## 2026-08-28 — D6

- PR #44 / 6.2 integrado `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`.
- PR #43 / 6.1 integrado `23bded948c4377b28fc48a72378816968d4cd413`.
- compile #128 `33194215442` SUCCESS; D6 cross-process #4 `33194215463` SUCCESS; Required CI #363 `33194215450` SUCCESS.
- D6 `[x] / PASS`: WOZ `5455677550`.

## 2026-08-28 — D7 / CLOSED

- WOZ PR #46 final tested head `6477fa6f6c4f04813acbbe5dbd43302347072adb`.
- PR #46 merge a integración: `e25c60429e453d7b8cb8ef294d89a01ef7511103`.
- D7 `33205320953` SUCCESS; D6 `33205320957` SUCCESS; temp-auth compile `33205321000` SUCCESS; Required CI #402 `33205320950` SUCCESS.
- D7 `[x] / PASS`: WOZ gate transaction `5457172823`.
- Architecture note: PASS aplica a capability mediation BeatGaler bajo Direct/shared-bot aceptado; no afirma primitive provider-native object-scoped.

## 2026-08-28 — DECISIÓN RO / ROMPECABEZAS + OWNER FIJO

- Trabajo cross-phase permitido por dependencia real.
- Cada owner conserva su área hasta cierre o reasignación explícita.
- Findings se consumen como input por el owner; no hopping automático.
- Owner hace self-test + exact-head CI.
- JOBS coordina/actualiza `!!!PLAN`; no código BeatGaler ni merges técnicos.

## 2026-08-28 — JOBS preflight anterior / WAVE #47 #50 #48 #49

Baseline entonces: `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.

- #49 / WOZ / 8.1 era candidate directamente encima del baseline con Required CI #406 verde; se secuenció primero.
- #47 / AAA / 11.1 y #50 / 12.2 estaban divergidos; dependencia obligatoria #47 → #50.
- #48 / BBB / 21.1 estaba técnico completo pero OPEN/DRAFT; BBB ya reasignado a 21.2 por `5458104890`.
- Ningún checkbox se adelantó en ese preflight.

## 2026-08-28 — WOZ 8.1 / PR #49 — CLOSED

- PR #49 `woz/task-8.1-session-security` exact tested head `f8ae2d1dedf0b4f977b4aedcaef5ac4ea83acdff`.
- Required CI #406 / `33208687131` SUCCESS; D6 `33208687050` SUCCESS; D7 `33208687027` SUCCESS; temp-auth compile #159 SUCCESS.
- Integrado como `14002b29c5101232c0ca8f8b85d808c8214975fb`.
- WOZ structured handoff Issue #41 `5458273984` = `STATUS: DONE`.
- 8.1 `[x]`. Gate D8 siguió `[ 🟡 ] / PENDING` porque 8.2 faltaba.

## 2026-08-28 — AAA 11.1 / PR #47 — CLOSED

- AAA reutilizó PR #47 después de #49; no artifact duplicado.
- Refreshed exact head `fdc6463e6b81efedc547c97595529d28e0ba2d83` sobre `14002b29...`.
- Resolución preservó la seguridad Web de #49 en `AccountGate`/tests y reaplicó únicamente foundations UI/a11y.
- Required CI #429 `33216364174` SUCCESS; D6 #68 `33216364104` SUCCESS; D7 #39 `33216364074` SUCCESS.
- PR #47 integrado como merge `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.
- 11.1 `[x] / DONE / INTEGRATED`.

## 2026-08-28 — WOZ 8.2 / PR #52 — TECHNICAL CANDIDATE, NO CIERRE GLOBAL

- PR #52 `woz/task-8.2-account-lifecycle` @ `ef0d6b142a92cdb88b2a3111e144ba6a9f15df9c` = OPEN / no mergeado / non-draft.
- Candidate implementa verification/reset hash-only one-shot/expiry/anti-enumeración; MFA recovery; reauth; notifications; export secret-free; delete/cleanup/receipt; revocación fail-closed.
- Required CI / Test Desktop Portability `33216990412` = SUCCESS sobre ese exact head.
- Candidate fue construido sobre `14002b29...`; integración ya avanzó a `489d81b...` por #47. Por tanto requiere refresh/revalidación exact-head antes de integración.
- Gate D8 además conserva tres dependencias explícitas: provider/templates de email, duración de retención y provider-only sensitive reauth.
- Estado: 8.2 `[ 🟡 ]`; D8 `[ 🟡 ] / PENDING`; WOZ conserva FULL OWNER y no salta D9.

## 2026-08-28 — AAA 12.2 / PR #50 — SLICE DONE, INTEGRACIÓN PENDIENTE

- PR #50 `aaa/f2-12.2-library` @ `258017fbd03e2a8edf0a93f7af2c7acb7ddf1a7c` = OPEN / no mergeado / non-draft.
- Handoff/PR declara slice técnico completo; Required CI #416 `33213031905` SUCCESS; D6 `33213031958` SUCCESS sobre el stack anterior.
- #47 ya no está pendiente: quedó integrado como `489d81b...`.
- Por evidence-before-claim, #50 debe actualizarse/revalidarse contra la integración canónica que ya contiene #47 y contra movimientos previos de la secuencia JOBS antes de `[x]`.
- AAA permanece FULL OWNER F2/12.2. No artifact duplicado.

## 2026-08-28 — BBB 21.1+21.2 / PR #51 — EN CURSO

- BBB consolidó manifest 21.1 + Upgrade Matrix 21.2 en PR #51 `bbb/task-21.2-upgrade-matrix`.
- PR #51 = OPEN / DRAFT; head observado `f70f17ea41cd26bd833bf7ee91949a3e4d752d4e`.
- El artifact cubre preservación 0.7.4 settings/SQLite/offline/cache, recovery, NSIS bridge y staging same-SHA.
- Required CI del head actual estaba QUEUED al último preflight; D6 del mismo head aparecía SUCCESS.
- Integración canónica se movió a `489d81b...`; el propio contrato de #51 exige fresh union + CI si baseline cambia.
- 21.1 y 21.2 permanecen `[ 🟡 ]`.

## 2026-08-28 — JOBS sync post-AAA/WOZ

**Baseline canónico:** `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

Decisión de secuencia para minimizar revalidación inútil:
1. WOZ continúa **#52 / 8.2**: refresh contra `489d81b...`, exact-head CI, integración técnica, handoff. D8 puede seguir PENDING por decisiones externas.
2. AAA continúa **#50 / 12.2** después del movimiento de integración #52: refresh final, exact-head CI, integración.
3. BBB continúa **#51 / 21.1+21.2** en paralelo, pero integración final requiere baseline vigente + exact-head evidence.

RO / provider / legal pendientes para cerrar D8:
- provider/templates de email verification/reset;
- retención/tombstone explícita para account deletion;
- provider-only/OAuth-only sensitive reauth.

No se marca 8.2, 12.2, 21.1 ni 21.2 `[x]` todavía. `Plan Maestro 2208 copy DONT TOUCH .md` permanece untouched. Release público sigue 🔴 `NO-GO`.

---

## Estado actual

- Integración estable: `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.
- WOZ: **F1/D8/8.2 FULL OWNER**; #49/8.1 `[x]`; #52 técnico verde histórico pero refresh/revalidación + decisiones externas pendientes; D8 `[ 🟡 ]`.
- AAA: **F2/12.2 FULL OWNER**; #47/11.1 `[x]`; #50 slice done pero integración/revalidación pendiente.
- BBB: **F4/21.2 FULL OWNER**; #51 combinado 21.1+21.2 OPEN/DRAFT/en CI; sin `[x]`.
- JOBS: coordinación/plan/handoffs; no código BeatGaler ni merges técnicos.
- D6: `[x] / PASS`.
- D7: `[x] / PASS`.
- D8: `[ 🟡 ] / PENDING`.
- 5.1/5.2: `[x]`.
- 2.2/1.2: tails externos `[ 🟡 ]`.
- Release público: 🔴 `NO-GO`.