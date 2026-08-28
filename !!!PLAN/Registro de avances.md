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

- WOZ PR #46 `woz/task-7.1-direct-capabilities` final tested head `6477fa6f6c4f04813acbbe5dbd43302347072adb`.
- PR #46 merge a integración: `e25c60429e453d7b8cb8ef294d89a01ef7511103`.
- Branch `integration-v0.8.0-alpha.1` verificado en `e25c60429e453d7b8cb8ef294d89a01ef7511103`.
- D7 `33205320953` SUCCESS; D6 cross-process `33205320957` SUCCESS; temp-auth compile `33205321000` SUCCESS; Required CI #402 `33205320950` SUCCESS en Web/shared, PostgreSQL recovery, Supply Chain/HEAD secret scan, Windows, macOS arm64 y x86_64.
- AAA findings `5456406567` consumidos/cerrados por WOZ: expiry/skew parity, fail-closed response redaction, live lease/quarantine coupling.
- BBB findings `5456351308` + revoke-order posterior consumidos/cerrados por WOZ: canonical revoke target, durable fail-closed, pre-mutation revoke.
- D7 `[x] / PASS`: WOZ gate transaction `5457172823`.
- Architecture note: PASS aplica a capability mediation BeatGaler bajo Direct/shared-bot aceptado; no afirma primitive provider-native object-scoped.

## 2026-08-28 — F2 / 11.1 AAA

- PR #47 `aaa/f2-11.1-design-foundations` @ `ddad3124cc3d1577d76d9965b55189a2cfb88383` = OPEN / no mergeado.
- Handoff AAA `5456682762`: `DONE — INDEPENDENT SLICE ONLY`.
- Required CI #392 `33202493998` SUCCESS; D6 #33 `33202493855` SUCCESS.
- Candidate cubre tokens/primitives/focus/Dialog/reduced motion, AccountGate autofill/contrast/loading/390–430, docs y DOM/a11y tests en 7 files.
- 11.1 global permanece `[ 🟡 ]`: no `[x]` hasta integración/secuenciación verificable sobre el estado actual.

## 2026-08-28 — F4 / 21.1 BBB

- Handoff BBB `5456640788`: audit READ ONLY / FINDING sobre base `23bded948c4377b28fc48a72378816968d4cd413`.
- REUSE: versión/name sources alineados, runtime pins/provenance, macOS universales, Windows Node/Bot API, common capabilities y release same-SHA checks.
- GAPS: G1 bundle ID final = `RO DECISION REQUIRED`; G2 updater endpoint duplicado; G3 channel/feed sin fuente canónica; G4 Windows packaging omite FFmpeg; G5 manifest tooling no demostrado desde mismo SHA de artifacts.
- 21.1 permanece `[ 🟡 ]`; BBB conserva full ownership y debe implementar/probar los gaps autorizados sin entrar a 21.2/signing/notarization/release.

## 2026-08-28 — DECISIÓN RO / ROMPECABEZAS

RO elimina la restricción “todos en el mismo Día”. Trabajo cross-phase permitido por dependencia real. JOBS puede organizar owners/fases/prioridades sin rebajar gates.

## 2026-08-28 — DECISIÓN RO / OWNER FIJO + SELF-TEST

RO precisa el modelo:
- **WOZ** terminó F1/D7 y, tras Gate D7 PASS, JOBS lo reasigna explícitamente a **F1 / D8 / 8.1+8.2** hasta cierre D8.
- **AAA se queda en F2 / 11.1** hasta cerrarla; implementa y prueba su propia pieza. No vuelve automáticamente a 7.2.
- **BBB se queda en F4 / 21.1** hasta cerrarla; implementa/audita y prueba su propia pieza. No vuelve automáticamente a D7.
- Findings de otros agentes se usan como input/casos de prueba por el owner actual.
- No hopping automático al aparecer/desaparecer dependencias.
- Si un owner queda bloqueado, conserva ownership y reporta blocker; JOBS solo reasigna mediante decisión explícita.
- Revisión independiente adicional se conserva únicamente cuando JOBS/RO o un gate posterior la exige literalmente.

---

## Estado actual

- Integración estable: `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.
- WOZ: **F1/D8 full owner**; PRIMARY 8.1.
- AAA: F2/11.1 full owner; PR #47 OPEN, candidate DONE/CI verde, cierre global pendiente.
- BBB: F4/21.1 full owner; audit FINDING activo; bundle ID `RO DECISION REQUIRED`.
- JOBS: coordinación; no hopping automático.
- D6: `[x] / PASS`.
- D7: `[x] / PASS`.
- D8: `[ 🟡 ] / PENDING`.
- 5.1/5.2: `[x]`.
- 2.2/1.2: tails externos `[ 🟡 ]`.
- Release público: 🔴 `NO-GO`.
- WOZ NEXT: **8.1 — sesión y seguridad de sesión** sobre `e25c604...`; preflight REUSE/GAP + duplicate-check, requisitos literales, tests/CI exact-head, luego 8.2 dentro del mismo ownership.