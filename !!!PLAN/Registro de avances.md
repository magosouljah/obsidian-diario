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

## 2026-08-28 — WOZ 8.2 / PR #52 — snapshot pre-refresh

- PR #52 `woz/task-8.2-account-lifecycle` @ `ef0d6b142a92cdb88b2a3111e144ba6a9f15df9c` era OPEN/no mergeado en este snapshot.
- Candidate implementaba verification/reset hash-only one-shot/expiry/anti-enumeración; MFA recovery; reauth; notifications; export secret-free; delete/cleanup/receipt; revocación fail-closed.
- Required CI / Test Desktop Portability `33216990412` = SUCCESS sobre ese exact head.
- Como el baseline había avanzado por #47, este snapshot exigía refresh/revalidación antes de integración.

## 2026-08-28 — AAA 12.2 / PR #50 — snapshot pre-refresh

- PR #50 `aaa/f2-12.2-library` @ `258017fbd03e2a8edf0a93f7af2c7acb7ddf1a7c` era OPEN/no mergeado en este snapshot.
- Required CI #416 `33213031905` SUCCESS; D6 `33213031958` SUCCESS sobre el stack anterior.
- Evidence-before-claim exigía actualización/revalidación después de #47/#52 antes de `[x]`.

## 2026-08-28 — BBB 21.1+21.2 / PR #51 — snapshot temprano

- BBB consolidó manifest 21.1 + Upgrade Matrix 21.2 en PR #51 `bbb/task-21.2-upgrade-matrix`.
- En este snapshot: OPEN/DRAFT, head `f70f17ea41cd26bd833bf7ee91949a3e4d752d4e`; CI todavía en curso.
- 21.1 y 21.2 permanecieron `[ 🟡 ]`.

## 2026-08-28 — JOBS sync intermedio post-#47

**Baseline entonces:** `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

Secuencia fijada entonces:
1. #52 / 8.2 refresh + integración;
2. #50 / 12.2 después de #52;
3. #51 / 21.1+21.2 en paralelo con baseline vigente.

Ese estado queda como ledger histórico y fue superado por los cierres siguientes.

## 2026-08-28 — WOZ 8.2 / PR #52 — CLOSED

- WOZ reutilizó PR #52 y lo refrescó contra integración que ya contenía #47.
- Exact tested head final: `f5ae901fb48444b6ea845048fb86f4dd482d75ec`.
- Required CI #443 / `33219253446` SUCCESS.
- D6 #81 / `33219253348` SUCCESS.
- D7 #53 / `33219253320` SUCCESS.
- Productive Temp Auth Compile #171 / `33219253332` SUCCESS.
- PR #52 integrado como `c25ec6a824bc0ae60fbf65858d53be26d453f205`.
- 8.2 técnico `[x] / DONE / INTEGRATED`.
- Gate D8 siguió PENDING en ese momento únicamente por las tres decisiones RO/provider/legal todavía abiertas.

## 2026-08-28 — BBB #51 — EXACT-HEAD VERDE, PROCESS BLOCKER

- PR #51 exact head `e9fc4e68fc555357ee470996c51544b879cbae93`, base `c25ec6a824bc0ae60fbf65858d53be26d453f205`.
- Required CI #451 / `33220523143` SUCCESS.
- Upgrade 21.2 Staging #8 / `33220523159` SUCCESS.
- D6 #88 / `33220523127` SUCCESS; D7 #61 / `33220523155` SUCCESS.
- Windows literal 0.7.4 → Galer PASS; macOS arm64/x86_64 identity/migration PASS.
- DRAFT → ready falló antes de mutar por error del connector GraphQL `Repository.fullDatabaseId`; merge rechazado correctamente con HTTP 405 mientras seguía draft.
- Handoff BBB Issue #41 `5460283021`: `STOP / PENDING_PROCESS_BLOCKER`; no bypass usado.
- Resultado: evidencia técnica integration-ready para ese baseline, pero 21.1/21.2 siguieron `[ 🟡 ]` porque #51 no se integró.

## 2026-08-28 — AAA 12.2 / PR #50 — CLOSED

- AAA reutilizó PR #50; no artifact duplicado.
- Rebuilt exact tested head `b7a31d686a361f559783b5dc7cb8bebc5aa04e8e` directamente sobre post-#52 baseline `c25ec6a824bc0ae60fbf65858d53be26d453f205`.
- Delta final: 1 commit / 4 files; sin auth/session/backend/data-plane/infra.
- Required CI #452 / `33233250213` SUCCESS.
- D6 #89 / `33233250229` SUCCESS; D7 #62 / `33233250210` SUCCESS; compile #173 / `33233250206` SUCCESS.
- PR #50 integrado como `39e894c0fcefffa5d3222e3c135a086937a10a8e`.
- AAA handoff Issue #41 `5460303449` = `STATUS: DONE`, `NEXT_WITHIN_AREA: none`.
- 12.2 `[x] / DONE / INTEGRATED`.

## 2026-08-28 — WOZ D8 RO resolutions / PR #53 — CLOSED + GATE PASS

- PR #53 `woz/d8-ro-resolutions` exact tested head `ab952c464f351aac736405c8559f5b85f421bc0c` sobre baseline `39e894c...`.
- Resoluciones RO integradas:
  - Amazon SES para delivery de verification/reset con templates `VERIFY_EMAIL` y `RESET_PASSWORD`;
  - account deletion retention = `0` días, cleanup inmediato, sin tombstone recuperable;
  - provider-only/OAuth-only recent reauth mediante fresh same-provider authorization ligada a user/session.
- Required CI #455 / `33234071878` SUCCESS.
- D6 #91 / `33234071860` SUCCESS; D7 #65 / `33234071863` SUCCESS; compile #175 / `33234071871` SUCCESS.
- PR #53 integrado como `6c4499d124a64d138e791ea4abf0091766dde7e9`.
- WOZ gate transaction Issue #41 `5460381842`: **GATE D8 = PASS**.
- D8 `[x] / PASS`; D9 queda dependency-ready, pero WOZ no lo inicia sin asignación separada.
- Follow-up fuera de D8 registrado para F2/15.1: acción visible **“Vaciar Trash”** con borrado permanente, confirmación fuerte y recent reauth.

## 2026-08-28 — JOBS sync factual post-D8 / post-12.2

**Baseline canónico:** `integration-v0.8.0-alpha.1` @ `6c4499d124a64d138e791ea4abf0091766dde7e9`.

- D8/8.2 y resoluciones RO cerradas con evidencia verificable; Gate D8 `[x] / PASS`.
- F2/12.2 cerrado/integrado; AAA terminó su owner actual y espera asignación explícita.
- WOZ terminó D8 y espera asignación explícita; D9 está dependency-ready, no auto-asignado.
- F2/11.2 y 12.1 están dependency-ready, pero no auto-asignados.
- F2/15.1 “Vaciar Trash” queda `QUEUED / UNASSIGNED`; registrar no equivale a implementar.
- BBB conserva FULL OWNER F4/21.2. PR #51 sigue OPEN/DRAFT.
- Como el baseline se movió desde `c25ec6a...` a `6c4499d...`, la evidencia verde de #51 `e9fc4e68...` ya no autoriza integración final: requiere fresh union/refresh + exact-head Required CI + Upgrade Staging + D6/D7 aplicables.
- PR #48 no se considera superseded/cerrado hasta que #51 aterrice verificablemente.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece untouched.
- Release público sigue 🔴 `NO-GO`.

---

## Estado actual

- Integración estable: `integration-v0.8.0-alpha.1` @ `6c4499d124a64d138e791ea4abf0091766dde7e9`.
- WOZ: **sin asignación activa**; D8 `[x] / PASS`; D9 dependency-ready/unassigned.
- AAA: **sin asignación activa**; 11.1 y 12.2 `[x]`; 11.2/12.1 dependency-ready; 15.1 Trash follow-up queued.
- BBB: **F4/21.2 FULL OWNER**; #51 combinado 21.1+21.2 OPEN/DRAFT; requiere refresh contra baseline vivo + exact-head evidence; 21.1/21.2 `[ 🟡 ]`.
- JOBS: coordinación/plan/handoffs; no código BeatGaler ni merges técnicos.
- D6: `[x] / PASS`.
- D7: `[x] / PASS`.
- D8: `[x] / PASS`.
- 5.1/5.2: `[x]`.
- 2.2/1.2: tails externos `[ 🟡 ]`.
- Release público: 🔴 `NO-GO`.