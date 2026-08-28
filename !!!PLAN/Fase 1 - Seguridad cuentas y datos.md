# Fase 1 — Seguridad, cuentas y datos durables

> Leer `Plan Maestro.md`. Fase 1 mantiene sus gates y ownership fijo: **WOZ es dueño completo de D8** hasta cerrarlo.

**Estado:** `[ 🟡 ]` — D8 activo.  
**Integración estable:** `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.  
**Release público:** 🔴 `NO-GO`.

## D6 — `[x] PASS`

- 6.1 / PR #43 integrado `23bded948c4377b28fc48a72378816968d4cd413`.
- 6.2 / PR #44 integrado `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`.
- compile #128 `33194215442` SUCCESS; cross-process #4 `33194215463` SUCCESS; Required CI #363 `33194215450` SUCCESS.
- WOZ gate transaction Issue #41 `5455677550` PASS.

---

## D7 — `[x] PASS`

**Resultado:** cliente sin secretos de infraestructura y operaciones solo dentro de capability concedida.

### 7.1 / 7.2 — cerrado por WOZ

- PR #46 `woz/task-7.1-direct-capabilities` exact tested head `6477fa6f6c4f04813acbbe5dbd43302347072adb`.
- Merge a integración: `e25c60429e453d7b8cb8ef294d89a01ef7511103`.
- D7 capability run `33205320953` SUCCESS.
- D6 cross-process run `33205320957` SUCCESS.
- Productive Temp Auth Compile `33205321000` SUCCESS.
- Required CI #402 `33205320950` SUCCESS: Web/shared, PostgreSQL recovery, Supply Chain/HEAD secret scan, Windows, macOS arm64 y macOS x86_64 verdes.
- Findings AAA `5456406567` cerrados dentro de PR #46: expiry/skew parity, fail-closed response redaction y live lease/quarantine coupling.
- Findings BBB `5456351308` + revoke-order posterior cerrados: canonical revoke targeting, durable fail-closed y revoke pre-mutation.
- WOZ gate transaction Issue #41 `5457172823`: `GATE D7 / PASS`.

Gate D7 cerrado: **0 secretos de infraestructura en cliente y 0 operaciones fuera del scope concedido** dentro del contrato aceptado.

No reabrir D7 sin nueva evidencia material.

---

## D8 — ACTIVO — WOZ FULL OWNER

**Gate D8:** usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

Baseline de entrada: `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.

### 8.1 — sesión y seguridad de sesión — PRIMARY WOZ NEXT
- [ ] Cookie HttpOnly/Secure/SameSite o equivalente; CSRF explícito.
- [ ] Distinguir 401/expiry de offline/timeout.
- [ ] Session inventory, revoke-one/revoke-all, rotación sensible.
- [ ] Preflight REUSE/GAP + duplicate-check antes de crear artefacto.
- [ ] Tests/CI exact-head aplicables y regresiones de la propia área verdes.

### 8.2 — ciclo de cuenta — WOZ SAME OWNER
- [ ] Email verification/reset one-shot/expiry/anti-enumeración.
- [ ] MFA recovery + reauth + notifications.
- [ ] Export/delete + revocation/provider cleanup/retention/receipt.
- [ ] Tests/CI exact-head aplicables.

Si provider/legal/credenciales o una decisión RO bloquean un subitem de 8.2, marcar solo ese subitem `RO DECISION REQUIRED` / `BLOCKED` y continuar el resto independiente de D8. WOZ no salta automáticamente a D9.

### Gate D8 — `PENDING`

No PASS hasta evidencia exact-head suficiente y transacción estructurada de WOZ.

---

## D9 — PostgreSQL/migración reversible — REUSE-FIRST

- [ ] migrations/constraints/indexes/transacciones;
- [ ] importer dry-run/checksums/idempotencia/quarantine/reporte;
- [ ] MFA/OAuth protegidos + hashes sesión no reversibles;
- [ ] staging/conteos/checks + rollback sin pérdida + corrupción fail-closed.

Evidencia reusable: PostgreSQL autoridad, PRs #29–#42, importer, rollback/current-PG, durability restart, fail-closed.

**Gate D9:** migración repetible/reversible; ningún JSON como autoridad productiva.

---

## D10 — Restore y alpha — REUSE-FIRST

### 10.1
- [ ] backup cifrado/config/media strategy;
- [ ] restore aislado + RPO/RTO + core flows;
- [ ] access/retention/off-provider copy/backup alert.

Reusar literalmente: PITR restore, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call/rotation/rollback authority.

### 10.2
- [ ] revisar gates D2–D10/P0/evidencia requerida;
- [ ] si pasa: alpha interna 3–5 usuarios sintéticos, invite-only, sin pagos;
- [ ] si falla: demo local/deslizamiento sin scope creep.

RO decide alpha final. Cerrar F1 no autoriza release público.