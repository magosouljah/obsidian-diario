# Fase 1 — Seguridad, cuentas y datos durables

> Leer `Plan Maestro.md`. D8 y D9 están cerrados. D10.1 sigue abierto únicamente por gaps literales de backup readiness y continúa con WOZ por el turno nocturno.

**Estado:** D8 `[x] / PASS`; D9 `[x] / PASS`; D10.1 `[ 🟡 ] / PENDING`.  
**Integración estable:** `integration-v0.8.0-alpha.1` @ `5b05ca8450bc3fe6bb8e9baaaca0c4a2d836d858`.  
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
- 8.2 / PR #52 exact head `f5ae901fb48444b6ea845048fb86f4dd482d75ec`; Required CI #443, D6 #81, D7 #53, compile #171 SUCCESS; merge `c25ec6a824bc0ae60fbf65858d53be26d453f205`.
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

## D10 — Restore y alpha

### 10.1 — `[ 🟡 ] PENDING` — WOZ `NIGHT-WOZ-004`

Gate transaction WOZ Issue #41 `5461379758`:
- [ 🟡 ] backup cifrado/config/media strategy: falta evidencia literal suficiente de estrategia completa para config + índice/media;
- [x] restore aislado + RPO/RTO + core flows: PASS — PITR aislado real, RPO ~7 min <=15 min, RTO `3643 s` <=7200 s;
- [ 🟡 ] access/retention/off-provider copy/backup alert: access/retention cubiertos; falta evidencia literal de copia off-provider y backup-failure alert específica o equivalencia literal.

`NIGHT-WOZ-003` quedó sin procesar y fue superseded explícitamente por `NIGHT-WOZ-004` para evitar doble ejecución; el scope no cambió. REUSE-FIRST estricto: no repetir restore/cutover/restart/rotation. Si un gap requiere credencial, proveedor, costo nuevo o decisión RO, registrar acción externa mínima y mantener PENDING.

### 10.2 — `NOT STARTED`
- [ ] revisar gates D2–D10/P0/evidencia requerida;
- [ ] si pasa: alpha interna 3–5 usuarios sintéticos, invite-only, sin pagos;
- [ ] si falla: demo local/deslizamiento sin scope creep.

RO decide alpha final. Cerrar F1 no autoriza release público.
