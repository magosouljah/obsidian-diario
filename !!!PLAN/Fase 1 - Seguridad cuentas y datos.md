# Fase 1 — Seguridad, cuentas y datos durables

> Leer `Plan Maestro.md`. D8 y D9 están cerrados. D10.1 está asignado a WOZ por el turno nocturno.

**Estado:** D8 `[x] / PASS`; D9 `[x] / PASS`; D10.1 `ASSIGNED / IN PROGRESS`.  
**Integración estable:** `integration-v0.8.0-alpha.1` @ `6c4499d124a64d138e791ea4abf0091766dde7e9`.  
**Release público:** 🔴 `NO-GO`.

## D6 — `[x] PASS`

- 6.1 / PR #43 integrado `23bded948c4377b28fc48a72378816968d4cd413`.
- 6.2 / PR #44 integrado `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`.
- compile #128 `33194215442` SUCCESS; cross-process #4 `33194215463` SUCCESS; Required CI #363 `33194215450` SUCCESS.
- WOZ gate transaction Issue #41 `5455677550` PASS.

## D7 — `[x] PASS`

- PR #46 exact tested head `6477fa6f6c4f04813acbbe5dbd43302347072adb`; merge `e25c60429e453d7b8cb8ef294d89a01ef7511103`.
- D7 `33205320953`, D6 `33205320957`, Productive Temp Auth Compile `33205321000`, Required CI #402 `33205320950`: SUCCESS.
- WOZ gate Issue #41 `5457172823`: PASS.

## D8 — `[x] PASS / CLOSED`

Baseline de cierre `6c4499d124a64d138e791ea4abf0091766dde7e9`.

- 8.1 / PR #49 exact head `f8ae2d1dedf0b4f977b4aedcaef5ac4ea83acdff`; merge `14002b29c5101232c0ca8f8b85d808c8214975fb`; handoff `5458273984` DONE.
- 8.2 / PR #52 exact head `f5ae901fb48444b6ea845048fb86f4dd482d75ec`; Required CI #443 `33219253446`, D6 #81, D7 #53, compile #171 SUCCESS; merge `c25ec6a824bc0ae60fbf65858d53be26d453f205`.
- Resoluciones RO / PR #53 exact head `ab952c464f351aac736405c8559f5b85f421bc0c`; Amazon SES; deletion retention 0 días; provider-only recent reauth; Required CI #455, D6 #91, D7 #65, compile #175 SUCCESS; merge `6c4499d124a64d138e791ea4abf0091766dde7e9`.
- Gate D8 PASS por Issue #41 `5460381842`.

Follow-up fuera de D8: F2/15.1 debe incluir “Vaciar Trash” con borrado permanente, confirmación fuerte y recent reauth.

## D9 — PostgreSQL/migración reversible — `[x] PASS / CLOSED`

WOZ cerró D9 por REUSE-FIRST en Issue #41 handoff `5460959369` (`STATUS: DONE`, `RESULT: PASS`) sin crear rama/PR ceremonial.

Requisitos aceptados mediante evidencia existente verificada:
- [x] migrations/constraints/indexes/transacciones;
- [x] importer dry-run/checksums/idempotencia/quarantine/reporte;
- [x] MFA/OAuth protegidos + hashes sesión no reversibles;
- [x] staging/conteos/checks + rollback sin pérdida + corrupción fail-closed;
- [x] PostgreSQL permanece autoridad productiva; ningún JSON es autoridad productiva.

Evidencia reusable incluye PRs #29–#42, importer/rollback CURRENT PG, durabilidad/restart fail-closed, dump/backup cifrado + restore aislado en CI, PITR/RPO representativo y controles ya aceptados en 5.2. No reabrir D9 sin evidencia material nueva.

## D10 — Restore y alpha

### 10.1 — `ASSIGNED / IN PROGRESS` — WOZ `NIGHT-WOZ-002`
- [ ] backup cifrado/config/media strategy;
- [ ] restore aislado + RPO/RTO + core flows;
- [ ] access/retention/off-provider copy/backup alert.

REUSE-FIRST obligatorio: PITR restore, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call/rotation/rollback authority y evidencia de backup/restore ya existente. No repetir drills solo para recrear evidencia.

### 10.2 — `NOT STARTED`
- [ ] revisar gates D2–D10/P0/evidencia requerida;
- [ ] si pasa: alpha interna 3–5 usuarios sintéticos, invite-only, sin pagos;
- [ ] si falla: demo local/deslizamiento sin scope creep.

RO decide alpha final. Cerrar F1 no autoriza release público.