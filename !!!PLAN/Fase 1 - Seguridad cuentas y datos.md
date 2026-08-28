# Fase 1 — Seguridad, cuentas y datos durables

> Leer `Plan Maestro.md`. Fase 1 mantiene sus gates y ownership fijo: **WOZ es dueño completo de D8** hasta cerrarlo.

**Estado:** `[ 🟡 ]` — D8 activo.  
**Integración estable:** `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.  
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
- Required CI #402 `33205320950` SUCCESS.
- WOZ gate transaction Issue #41 `5457172823`: `GATE D7 / PASS`.

Gate D7 cerrado. No reabrir sin nueva evidencia material.

---

## D8 — ACTIVO — WOZ FULL OWNER

**Gate D8:** usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

Baseline canónico vivo: `integration-v0.8.0-alpha.1` @ `489d81b05d5bde338cb7f5b8408b20c1c78d4404`.

### 8.1 — sesión y seguridad de sesión — `[x] DONE / INTEGRATED`
- [x] Cookie HttpOnly/Secure/SameSite o equivalente; CSRF explícito.
- [x] Distinguir 401/expiry de offline/timeout.
- [x] Session inventory, revoke-one/revoke-all, rotación sensible.
- [x] Preflight REUSE/GAP + duplicate-check antes de crear artefacto.
- [x] Tests/CI exact-head aplicables y regresiones de la propia área verdes.

**Artifact canónico:** PR #49 `woz/task-8.1-session-security` exact tested head `f8ae2d1dedf0b4f977b4aedcaef5ac4ea83acdff`.

**Evidencia de cierre:**
- Required CI / Test Desktop Portability #406 `33208687131` SUCCESS;
- D6 `33208687050` SUCCESS;
- D7 `33208687027` SUCCESS;
- Productive Temp Auth Compile #159 SUCCESS;
- PR #49 merged;
- merge a integración `14002b29c5101232c0ca8f8b85d808c8214975fb`;
- WOZ structured handoff Issue #41 `5458273984` = `STATUS: DONE`.

8.1 queda cerrado. Esto **no** convierte por sí solo D8 en PASS.

### 8.2 — ciclo de cuenta — `[ 🟡 ] TECHNICAL CANDIDATE / REVALIDACIÓN + DECISIONES PENDIENTES`

**Artifact canónico:** PR #52 `woz/task-8.2-account-lifecycle` @ `ef0d6b142a92cdb88b2a3111e144ba6a9f15df9c` — OPEN / no mergeado / non-draft.

Cobertura técnica verificada del candidate:
- [x] Motor hash-only de email verification/reset, one-shot, expiry y anti-enumeración.
- [x] MFA recovery codes hash-only/one-shot, reauth session-bound y security notifications.
- [x] Export con reauth y exclusión de secretos.
- [x] Delete con reauth, revocación de sesiones/capabilities, cleanup provider/local metadata y deletion receipt.
- [x] Fail-closed si falta política explícita de retención.
- [x] Tests unitarios de lifecycle incluidos en Required CI del candidate.

**CI del candidate `ef0d6b...`:** Required CI / Test Desktop Portability run `33216990412` = SUCCESS; checks aplicables observados verdes sobre ese exact head.

**Pero NO cerrar 8.2 todavía:** PR #52 fue construido sobre integración `14002b29...`; mientras corría/terminaba su evidencia, PR #47 fue integrado y la rama canónica avanzó a `489d81b...`. Por tanto el candidate debe incorporar el baseline vivo, resolver cualquier interacción dentro del ownership WOZ y repetir exact-head CI antes de integración.

**Dependencias explícitas todavía no resueltas para el Gate D8:**
- **Email delivery/provider/templates:** `BLOCKED / PROVIDER DECISION REQUIRED`. El engine/notifier boundary existe, pero no hay provider/template productivo aprobado en repo/plan.
- **Retention duration:** `RO / LEGAL DECISION REQUIRED`. El delete falla cerrado si no se configura `BEATGALER_ACCOUNT_TOMBSTONE_RETENTION_DAYS`; no inventar duración.
- **Provider-only sensitive reauth:** `PROVIDER DECISION REQUIRED`. Password-backed está implementado; OAuth/provider-only permanece fail-closed con `PROVIDER_REAUTH_REQUIRED` hasta contrato aprobado.

**WOZ NEXT:** continuar en el mismo PR #52, refresh/revalidar contra `489d81b...`, CI exact-head, integrar el cierre técnico 8.2 y publicar handoff. Mantener Gate D8 `PENDING` mientras las decisiones anteriores no estén resueltas/aceptadas.

### Gate D8 — `[ 🟡 ] PENDING`

No PASS hasta:
1. 8.1 + 8.2 integrados y demostrados sobre baseline canónico;
2. provider/templates de verification/reset resueltos/aceptados;
3. retención definida por autoridad aplicable;
4. provider-only reauth resuelto/aceptado;
5. transacción estructurada WOZ `GATE D8`.

No saltar a D9 mientras D8 permanezca así.

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