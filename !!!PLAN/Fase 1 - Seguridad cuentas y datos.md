# Fase 1 — Seguridad, cuentas y datos durables

> Leer `Plan Maestro.md`. Esta fase conserva gates de aceptación pero no monopoliza agentes: trabajo independiente cross-phase avanza cuando una dependencia crítica bloquea a un rol.

**Estado:** `[ 🟡 ]` — CRITICAL PATH.  
**Critical gate:** **D7 — Data plane seguro**.  
**Integración estable:** `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`.  
**Release público:** 🔴 `NO-GO`.

## Semántica

`D6 → D7 → D8 → D9 → D10` define cierre/aceptación dentro de F1. Un slice independiente de otra fase puede avanzar antes. Nada se marca `[x]` sin evidencia literal. WOZ decide integración técnica; JOBS prioridades/owners/topología.

---

## D6 — `[x] PASS`

- 6.1 / PR #43 integrado `23bded948c4377b28fc48a72378816968d4cd413`.
- 6.2 / PR #44 integrado `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`.
- compile #128 `33194215442` SUCCESS; cross-process #4 `33194215463` SUCCESS; Required CI #363 `33194215450` SUCCESS.
- WOZ gate transaction Issue #41 `5455677550` PASS.

---

## D7 — ACTIVO

**Resultado:** cliente sin secretos de infraestructura y operaciones solo dentro de capability concedida.

### 7.1 [P0 · BE] — `[ 🟡 ]` WOZ / PR #46

**PR:** `woz/task-7.1-direct-capabilities` @ `bd62525a0b1701e00c2b4652b4a7a67699c8adab`, draft/open.

Implementado/candidato según PR:
- capability corta scope user/tenant/installation/session/vault/operation/object;
- deny-by-default allowlist + object IDs explícitos;
- lifecycle one-shot + revoke/expire;
- PostgreSQL store/migration `0005_direct_capabilities.sql`;
- tenant ceiling + bot ceiling;
- authorize-before-data-plane Web/Desktop;
- canonical scope compare.

**BBB review anterior `5456351308` sobre head `7e7bac...`:** materialmente acepta scope/deny-by-default/ceilings, pero halló 2 blockers revoke-wiring:
1. revoke target podía estrecharse por installation del body en eventos sensibles;
2. revoke podía fallar abierto ante error del store.

**PR #46 current head `bd62525...` declara delta específico para esos dos blockers:** canonical server-side revoke target + revoke completo por auth-session en account events + `503 DIRECT_CAPABILITY_REVOKE_FAILED` fail-closed + failure injection. **BBB debe re-review este exact head; aún no está aceptado por BBB.**

**Exact-head checks `bd62525...`:**
- D7 capability #16 / `33201030543` SUCCESS;
- D6 cross-process #26 / `33201030559` SUCCESS;
- temp-auth compile #148 / `33201030554` SUCCESS;
- Required CI #385 / `33201030567` = `IN_PROGRESS` al último preflight JOBS.

### 7.2 [P0 · QA/Security] — `[ 🟡 ]` AAA / PR #45

**PR:** `aaa/task-7.2-transport-isolation-adversarial` @ `e29368b4eeaf1641c4f3b9083b166f067bdd6182`.

Handoff AAA `5456406567` sobre WOZ head `7e7bac...`:
- D7 run #14 `33200605498` FAILURE únicamente en adversarial AAA;
- WOZ unit/PostgreSQL contracts SUCCESS;
- client secret-isolation SUCCESS;
- object substitution + replay PASS;
- explicit session revoke PASS;
- D6 cross-process #24 `33200605530` SUCCESS.

Findings reproducibles pendientes:
1. expiry/clock-skew inconsistente entre memory store y PostgreSQL;
2. response boundary no universalmente fail-closed en `ok:false` y no-refresh fallback;
3. ACTIVE capability no queda demostrablemente invalidada por lease expiry/bot quarantine.

AAA no modifica producción ni debilita assertions. Debe volver a retargetear el PR #45 existente cuando WOZ publique un head que responda a estos findings.

**Mientras espera ese delta WOZ:** AAA trabaja F2 / 11.1 Design foundations en un artefacto separado desde integración estable; no crea otro PR 7.2.

### BBB — NEXT inmediato

Re-review READ ONLY únicamente de los 2 revoke-wiring blockers sobre PR #46 @ `bd62525...`. Entregar PASS/FINDING con evidencia exacta. Si termina y no existe otro delta D7 listo, pasa a F4 / 21.1 readiness audit hasta que JOBS lo reactive.

### Gate D7 — `PENDING`

Cierre: **0 secretos de infraestructura en cliente y 0 operaciones fuera del scope**. No PASS mientras existan findings AAA/BBB materiales, CI exact-head pendiente o falta gate transaction WOZ.

---

## D8 — Sesión y ciclo de cuenta

### 8.1
- [ ] Cookie HttpOnly/Secure/SameSite o equivalente; CSRF explícito.
- [ ] Distinguir 401/expiry de offline/timeout.
- [ ] Session inventory, revoke-one/revoke-all, rotación sensible.

### 8.2
- [ ] Email verification/reset one-shot/expiry/anti-enumeration.
- [ ] MFA recovery + reauth + notifications.
- [ ] Export/delete + revocation/provider cleanup/retention/receipt.

JOBS puede adelantar slices que no dependan materialmente de D7. Falta proveedor/credencial/política → aislar `RO DECISION REQUIRED`, no inventar.

### Gate D8
Usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

---

## D9 — PostgreSQL/migración reversible — REUSE-FIRST

- [ ] migrations/constraints/indexes/transacciones;
- [ ] importer dry-run/checksums/idempotencia/quarantine/reporte;
- [ ] MFA/OAuth protegidos + hashes sesión no reversibles;
- [ ] staging/conteos/checks + rollback sin pérdida + corrupción fail-closed.

Evidencia reusable: PostgreSQL autoridad, PRs #29–#42, importer, rollback/current-PG, durability restart, fail-closed. JOBS puede preparar matriz `REQUISITO | EVIDENCIA | REUSE/GAP`; WOZ decide equivalencia técnica.

### Gate D9
Migración repetible/reversible; ningún JSON autoridad productiva.

---

## D10 — Restore y alpha — REUSE-FIRST

### 10.1
- [ ] backup cifrado/config/media strategy;
- [ ] restore aislado + RPO/RTO + core flows;
- [ ] access/retention/off-provider copy/backup alert.

Reusar literalmente: PITR restore, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call/rotation/rollback authority.

### 10.2
- [ ] revisar gates D2–D10/P0/evidencia independiente;
- [ ] si pasa: alpha interna 3–5 usuarios sintéticos, invite-only, sin pagos;
- [ ] si falla: demo local/deslizamiento sin scope creep.

RO decide alpha final. Cerrar F1 no autoriza release público.