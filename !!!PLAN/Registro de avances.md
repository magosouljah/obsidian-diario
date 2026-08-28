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

## 2026-08-28 — D7 / PR #46 + PR #45

- WOZ PR #46 `woz/task-7.1-direct-capabilities` @ `bd62525a0b1701e00c2b4652b4a7a67699c8adab`, draft/open.
- Candidate: scoped capability, deny-by-default, one-shot lifecycle, PostgreSQL store, ceilings, authorize-before-data-plane y revoke fail-closed.
- Exact-head PR #46: D7 #16 `33201030543` SUCCESS; D6 #26 `33201030559` SUCCESS; compile #148 `33201030554` SUCCESS; Required CI #385 `33201030567` SUCCESS.
- BBB `5456351308` dejó 2 findings revoke-wiring sobre head anterior; current PR #46 declara delta para ambos.
- AAA PR #45 `e29368b4eeaf1641c4f3b9083b166f067bdd6182`; handoff `5456406567` dejó findings expiry/skew, fail-closed response redaction y lease/quarantine lifecycle.
- D7 sigue `[ 🟡 ] / PENDING` hasta cierre técnico/gate WOZ.

## 2026-08-28 — DECISIÓN RO / ROMPECABEZAS

RO elimina la restricción “todos en el mismo Día”. Trabajo cross-phase permitido por dependencia real. JOBS puede organizar owners/fases/prioridades sin rebajar gates.

## 2026-08-28 — DECISIÓN RO / OWNER FIJO + SELF-TEST

RO precisa el modelo:
- **WOZ se queda en F1 / D7** y hace todo el ciclo técnico de esa área: implementación, fixes, pruebas, CI, integración y gate.
- **AAA se queda en F2 / 11.1** hasta cerrarla; implementa y prueba su propia pieza. No vuelve automáticamente a 7.2.
- **BBB se queda en F4 / 21.1** hasta cerrarla; implementa/audita y prueba su propia pieza. No vuelve automáticamente a D7.
- Findings AAA/BBB previos de D7 pasan a ser input/casos de prueba que WOZ debe reproducir y cerrar dentro de su propia área.
- No hopping automático al aparecer/desaparecer dependencias.
- Si un owner queda bloqueado, conserva ownership y reporta blocker; JOBS solo reasigna mediante decisión explícita.
- Revisión independiente adicional se conserva únicamente cuando JOBS/RO o un gate posterior la exige literalmente.

Commits de sincronización:
- Plan Maestro `747ff3a57162a3b5212331ef6eaa42cd4136789f`.
- Equipo multi-IA `1f2b6a480eea40024b5fc9bf386e4f9c28780daf`.
- Fase 1 `72303b5c80ab8d62104f9417a156bf374468ef85`.
- Fase 2 `ddb633b79c603f82dbc69fee3fdb10aebb447a59`.
- Fase 4 `1cb4a7b62c99fae6deb13c85817a4e03070d8a46`.

---

## Estado actual

- WOZ: F1/D7 full owner.
- AAA: F2/11.1 full owner.
- BBB: F4/21.1 full owner.
- JOBS: coordinación; no hopping automático.
- D6: `[x] / PASS`.
- D7: `PENDING`.
- 5.1/5.2: `[x]`.
- 2.2/1.2: tails externos `[ 🟡 ]`.
- Release público: 🔴 `NO-GO`.
- WOZ NEXT: cerrar D7 dentro de PR #46 absorbiendo findings pendientes y dejando tests/CI propios + gate estructurado.