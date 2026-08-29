# Fase 1 — Seguridad, cuentas y datos durables

> Leer `Plan Maestro.md`. D8 está cerrado. D9 queda dependency-ready, pero no se inicia sin asignación explícita JOBS/RO.

**Estado:** D8 `[x] / PASS`; D9 `READY_TO_WORK / UNASSIGNED`.  
**Integración estable:** `integration-v0.8.0-alpha.1` @ `6c4499d124a64d138e791ea4abf0091766dde7e9`.  
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

## D8 — `[x] PASS / CLOSED`

**Gate D8:** usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

Baseline canónico de cierre: `integration-v0.8.0-alpha.1` @ `6c4499d124a64d138e791ea4abf0091766dde7e9`.

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
- merge a integración `14002b29c5101232c0ca8f8b85d808c8214975fb`;
- WOZ structured handoff Issue #41 `5458273984` = `STATUS: DONE`.

### 8.2 — ciclo de cuenta — `[x] DONE / INTEGRATED`

**Artifact canónico:** PR #52 `woz/task-8.2-account-lifecycle` exact tested head `f5ae901fb48444b6ea845048fb86f4dd482d75ec`.

Cobertura integrada:
- [x] Motor hash-only de email verification/reset, one-shot, expiry y anti-enumeración.
- [x] MFA recovery codes hash-only/one-shot, reauth session-bound y security notifications.
- [x] Export con reauth y exclusión de secretos.
- [x] Delete con reauth, revocación de sesiones/capabilities, cleanup provider/local metadata y deletion receipt.
- [x] Fail-closed mientras las decisiones externas no estaban definidas.
- [x] Tests unitarios de lifecycle incluidos en Required CI.

**Evidencia exact-head final de #52:**
- Required CI #443 / `33219253446` SUCCESS;
- D6 #81 / `33219253348` SUCCESS;
- D7 #53 / `33219253320` SUCCESS;
- Productive Temp Auth Compile #171 / `33219253332` SUCCESS;
- merge a integración `c25ec6a824bc0ae60fbf65858d53be26d453f205`.

### Resoluciones RO de D8 — `[x] DONE / INTEGRATED`

PR #53 `woz/d8-ro-resolutions`, exact tested head `ab952c464f351aac736405c8559f5b85f421bc0c`, resolvió las tres decisiones que mantenían el gate pendiente:

- [x] **Email verification/reset:** Amazon SES; templates nominales `VERIFY_EMAIL` y `RESET_PASSWORD`; producción fail-closed si falta configuración SES requerida.
- [x] **Account deletion retention:** `0` días; cleanup inmediato; sin tombstone recuperable; receipt registra retención 0.
- [x] **Provider-only/OAuth-only sensitive reauth:** autorización reciente del mismo provider conectada al mismo usuario BeatGaler y a la sesión BeatGaler exacta; Google fresh login y X OAuth2 PKCE; sin inventar password local.

**Evidencia exact-head #53:**
- Required CI #455 / `33234071878` SUCCESS;
- D6 #91 / `33234071860` SUCCESS;
- D7 #65 / `33234071863` SUCCESS;
- Productive Temp Auth Compile #175 / `33234071871` SUCCESS;
- merge a integración `6c4499d124a64d138e791ea4abf0091766dde7e9`.

### Gate D8 — `[x] PASS`

WOZ publicó la transacción final en Issue #41 `5460381842`:
1. 8.1 integrado y demostrado — PASS;
2. 8.2 integrado y demostrado — PASS;
3. delivery verification/reset por Amazon SES — PASS;
4. retención account deletion = 0 días — PASS;
5. provider-only recent reauth — PASS;
6. usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura — PASS.

**D8 queda cerrado. No reabrir sin nueva evidencia material.**

Follow-up explícito fuera de D8: F2/15.1 debe incluir acción visible **“Vaciar Trash”** con borrado permanente, confirmación fuerte y recent reauth. Registrar en F2; no convertirlo en requisito retroactivo de D8.

---

## D9 — PostgreSQL/migración reversible — `READY_TO_WORK / UNASSIGNED` — REUSE-FIRST

D8 ya no bloquea D9 por dependencia. **Esto no asigna D9 a WOZ automáticamente.** JOBS/RO debe emitir una asignación separada antes de iniciar trabajo nuevo.

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