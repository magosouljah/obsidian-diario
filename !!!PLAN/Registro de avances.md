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

- **WOZ PR #46** `woz/task-7.1-direct-capabilities` current candidate `bd62525a0b1701e00c2b4652b4a7a67699c8adab`, draft/open.
- Candidate incluye scoped capability, deny-by-default, one-shot lifecycle, PostgreSQL store, ceilings y authorize-before-data-plane.
- **BBB handoff `5456351308`** sobre head anterior `7e7bac...`: acepta materialmente scope/deny/ceilings pero encontró 2 revoke-wiring blockers: canonical revoke targeting y fail-closed durable revoke.
- PR #46 current head declara delta específico para ambos blockers; BBB exact-head re-review pendiente.
- PR #46 exact-head: D7 #16 `33201030543` SUCCESS; D6 #26 `33201030559` SUCCESS; compile #148 `33201030554` SUCCESS; Required CI #385 `33201030567` IN_PROGRESS al último preflight.
- **AAA PR #45** current head `e29368b4eeaf1641c4f3b9083b166f067bdd6182`; handoff `5456406567`.
- AAA D7 #14 `33200605498` falla solo en adversarial AAA; unit/PostgreSQL capability contracts, client isolation, object substitution/replay y explicit session revoke pasan.
- Findings AAA pendientes: memory/PostgreSQL expiry-skew inconsistente; fail-closed response redaction incompleta; ACTIVE capability no invalidada demostrablemente por lease expiry/bot quarantine.
- D7 sigue `[ 🟡 ] / PENDING`.

## 2026-08-28 — DECISIÓN RO / MODELO ROMPECABEZAS

RO elimina la restricción artificial “todos avanzan Día por Día”. Desde ahora:
- trabajo por dependencia real, incluso cross-phase;
- JOBS puede reordenar fases/tareas/owners/slices/paralelismo;
- gates controlan cierre/promoción de lo dependiente, no todo inicio futuro;
- agentes construyen piezas distintas; revisión independiente sigue separada;
- rol bloqueado → JOBS lo mueve a slice independiente útil si existe;
- WOZ conserva decisión técnica/integración; RO conserva producto/riesgo/go-no-go.

Commits de transición:
- Plan Maestro inicial: `7aa798884bb7d8e6eb6105985884e1578a107250`; sync live posterior `4fb0c61f83bcfae4047ab2ce1e7392e7df8bc732`.
- Equipo multi-IA: `5418cdf1c6858d6056a0d0c938d161c012b9bdaf`.
- Fase 1: inicial `3e89f8a9ea91e2db3bbc18e2001427b728ff9b59`; sync live `17e3c93eb58e94bf411df7ac87b2fa8a2d5934d0`.
- Fase 2: `7bcdacea9d304bdbbb1e15b2a894304c32891a0e`.
- Fase 4: `3f757f6c66cdf8348e8c75467cb604bd4e31779f`.

### Lanes actuales

- **WOZ:** F1/7.1 PR #46 → responder findings AAA y cerrar CI/reviews exact-head.
- **AAA:** bloqueado para repetir 7.2 hasta nuevo delta WOZ → trabaja F2/11.1 Design foundations en paralelo; al nuevo head vuelve al PR #45 existente.
- **BBB:** primero re-review D7 exact-head `bd62525...`; si termina y no hay otro delta crítico, salta F4/21.1 readiness audit READ ONLY.
- **JOBS:** grafo/handoffs/REUSE D9-D10.

---

## Estado actual

- F1: `[ 🟡 ]` CRITICAL PATH D7.
- F2: parallel build activo por bloqueo AAA.
- F4: audit standby tras re-review BBB.
- D6: `[x] / PASS`.
- D7: `PENDING`.
- 5.1/5.2: `[x]`.
- 2.2/1.2: tails externos `[ 🟡 ]`.
- Release público: 🔴 `NO-GO`.
- WOZ NEXT: PR #46 responder AAA F1–F3; no merge/gate hasta CI + re-reviews/evidencia.