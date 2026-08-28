# Fase 1 — Seguridad, cuentas y datos durables

> Leer `Plan Maestro.md`. Fase 1 mantiene sus gates, pero el ownership actual es fijo: **WOZ es dueño completo de D7** hasta cerrarlo.

**Estado:** `[ 🟡 ]` — D7 activo.  
**Integración estable:** `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`.  
**Release público:** 🔴 `NO-GO`.

## D6 — `[x] PASS`

- 6.1 / PR #43 integrado `23bded948c4377b28fc48a72378816968d4cd413`.
- 6.2 / PR #44 integrado `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`.
- compile #128 `33194215442` SUCCESS; cross-process #4 `33194215463` SUCCESS; Required CI #363 `33194215450` SUCCESS.
- WOZ gate transaction Issue #41 `5455677550` PASS.

---

## D7 — ACTIVO — WOZ FULL OWNER

**Resultado:** cliente sin secretos de infraestructura y operaciones solo dentro de capability concedida.

### 7.1 / 7.2 — consolidado bajo WOZ para cierre D7

PR principal: **#46** `woz/task-7.1-direct-capabilities` @ `bd62525a0b1701e00c2b4652b4a7a67699c8adab`, draft/open.

Candidate actual incluye:
- capability corta scope user/tenant/installation/session/vault/operation/object;
- deny-by-default allowlist + object IDs explícitos;
- lifecycle one-shot + revoke/expire;
- PostgreSQL store/migration `0005_direct_capabilities.sql`;
- tenant ceiling + bot ceiling;
- authorize-before-data-plane Web/Desktop;
- canonical scope compare;
- canonical server-side revoke target;
- account/session revoke completo;
- fail-closed `503 DIRECT_CAPABILITY_REVOKE_FAILED` ante durable revoke failure.

Exact-head `bd62525...`:
- D7 capability #16 `33201030543` SUCCESS;
- D6 cross-process #26 `33201030559` SUCCESS;
- temp-auth compile #148 `33201030554` SUCCESS;
- Required CI #385 `33201030567` SUCCESS.

### Findings históricos que WOZ debe absorber como tests propios

**BBB `5456351308`:**
1. canonical server-side revoke targeting;
2. fail-closed/durable revoke cuando capability-store revoke falla.

El current head de PR #46 declara delta para ambos. **No se requiere que BBB vuelva a D7**; WOZ debe mantener pruebas que demuestren su cierre.

**AAA `5456406567` / PR #45 `e29368...`:**
1. expiry/clock-skew inconsistente memory vs PostgreSQL;
2. response redaction no universalmente fail-closed en `ok:false` y no-refresh fallback;
3. ACTIVE capability no invalidada demostrablemente por lease expiry/bot quarantine.

PR #45 queda como evidencia/adversarial input histórico. **AAA no vuelve automáticamente a 7.2.** WOZ reproduce esos casos dentro de PR #46 o artefacto técnico de su área, corrige lo aceptado y deja tests/CI propios verdes.

### Responsabilidad WOZ para cerrar D7

- reproducir/aceptar/rechazar cada finding material con evidencia;
- implementar solo el delta necesario;
- mantener tests de scope A→B, replay, expiry/skew, closed session/lease, quarantine, response redaction, revoke y ceilings;
- verificar que ningún client artifact recibe secretos de infraestructura;
- ejecutar CI exact-head aplicable;
- integrar técnicamente cuando proceda;
- publicar gate estructurado.

### Gate D7 — `PENDING`

Requisito: **0 secretos de infraestructura en cliente y 0 operaciones fuera del scope concedido**.

No PASS hasta que WOZ demuestre los requisitos con evidencia exact-head y publique la transacción del gate.

---

## D8 — Sesión y ciclo de cuenta

### 8.1
- [ ] Cookie HttpOnly/Secure/SameSite o equivalente; CSRF explícito.
- [ ] Distinguir 401/expiry de offline/timeout.
- [ ] Session inventory, revoke-one/revoke-all, rotación sensible.

### 8.2
- [ ] Email verification/reset one-shot/expiry/anti-enumeración.
- [ ] MFA recovery + reauth + notifications.
- [ ] Export/delete + revocation/provider cleanup/retention/receipt.

**Gate D8:** usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

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