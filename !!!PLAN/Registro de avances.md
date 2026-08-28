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
- 4.2 `[x]` supply chain PR #10 / merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; deuda GPL queda separada.

## 2026-08-24 a 2026-08-25 — 5.1

- PRs #13–#18: temporary auth + transferencia directa **1,992,294,400 bytes**, `galer_cloud_file_bytes=0`; permanent auth/token/API hash no llegan al cliente.
- PRs #23–#27: Windows/macOS/Chrome Worker, delete, límite >48h documentado, fair pool, exclusividad preferida, shared fallback solo sin bots libres, max 4 + waitlist, expiry/recovery.
- 5.1 `[x]`: PR #28 / merge `d9ae76f42faee3a7207b9232b7421a0bec20b090` + CI + aceptación RO.

## 2026-08-25 a 2026-08-28 — 5.2

- PRs #29–#42: PostgreSQL/migrations, encryption/keyring, importer idempotente, durable ops/reconciliation/rollback/recovery, fail-closed cutover, AWS boundary/base64 strict.
- PostgreSQL autoridad productiva + restart durable + rollback dry-run desde CURRENT PG.
- PITR aislado representativo: RPO ~7 min; RTO `3643 s`.
- Key activa 2, versiones 1/2; lectura ciphertext v1 bajo keyring v2.
- Alarmas RDS críticas + on-call/rotation/rollback authority.
- 5.2 `[x]`: cierre WOZ/RO Issue #41 `5448976400`. No repetir drills aceptados sin invalidación nueva.
- Follow-up release: rotar OAuth client secret expuesto al operador durante troubleshooting antes de release; no registrar valor.

## 2026-08-28 — Fase 1 / D6

- PR #44 / 6.2 integrado `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`: abuse controls + KDF asíncrono.
- PR #43 / 6.1 integrado `23bded948c4377b28fc48a72378816968d4cd413`: session-bound authz + ownership + PostgreSQL cross-process.
- Exact integrated head: compile #128 `33194215442` SUCCESS; D6 cross-process #4 `33194215463` SUCCESS; Required CI #363 `33194215450` SUCCESS.
- D6 `[x] / PASS`: WOZ Issue #41 `5455677550`.

## 2026-08-28 — D7 primeros handoffs

- BBB 7.1 READ ONLY `5455758175`: gaps reproducibles en scoped capability/deny-by-default, lifecycle revoke, bot/tenant ceilings y revocación inmediata control-side.
- AAA 7.2 parcial: PR #45 @ `1d923c467922231df157bdc42f9aad62405d34ea`; Required CI #364 `33195699165` SUCCESS.
- AAA boundary finding `5455777574`: early-return/fallback no universalmente redactado; no fuga observada actual; PR #45 añade guards/tests pero no fix productivo.
- D7 `[ 🟡 ] / PENDING`; WOZ 7.1 permanece critical path.

## 2026-08-28 — DECISIÓN RO / MODELO ROMPECABEZAS

RO elimina la restricción artificial “todos avanzan Día por Día”. Desde ahora:
- trabajo desbloqueado por dependencia real, incluso cross-phase;
- JOBS puede reordenar fases/tareas, owners, slices y paralelismo para acelerar;
- gate controla cierre/promoción de lo dependiente, no prohíbe trabajo futuro independiente;
- agentes construyen piezas distintas y no duplican implementación;
- si un agente queda bloqueado, JOBS lo mueve a un slice independiente útil cuando exista;
- WOZ conserva decisiones técnicas/integración; RO conserva alcance/riesgo/go-no-go.

**Plan sync:**
- Plan Maestro commit `7aa798884bb7d8e6eb6105985884e1578a107250`.
- Equipo multi-IA commit `5418cdf1c6858d6056a0d0c938d161c012b9bdaf`.
- Fase 1 commit `3e89f8a9ea91e2db3bbc18e2001427b728ff9b59`.

**Lanes activadas:**
- WOZ → F1 / 7.1 critical.
- AAA → F2 / 11.1 Design foundations slice independiente mientras 7.2 espera contrato 7.1; PR #45 se preserva.
- BBB → F4 / 21.1 Release manifest readiness audit READ ONLY mientras espera nuevo delta D7.
- JOBS → grafo, handoffs y matrices REUSE D9/D10.

---

## Estado actual

- F0: residual/administrativa.
- F1: `[ 🟡 ]` CRITICAL PATH D7.
- F2: parallel build habilitado por slices independientes.
- F4: parallel audit/prep habilitado.
- D6: `[x] / PASS`.
- D7: `PENDING`.
- 5.1/5.2: `[x]`.
- 2.2/1.2: tails externos `[ 🟡 ]`.
- Release público: 🔴 `NO-GO`.
- WOZ NEXT: 7.1; AAA y BBB ya no deben permanecer ociosos por ese blocker.