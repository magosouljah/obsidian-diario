# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo CYCLE 103:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[ 🟡 ] RO / ALPHA DECISION`.  
**Release público:** 🔴 `NO-GO`.

## D6 — `[x] PASS`
PR #43 integrado `23bded948c4377b28fc48a72378816968d4cd413`; PR #44 integrado `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`; D6 cross-process + compile + Required CI aceptados. WOZ gate Issue #41 `5455677550`.

## D7 — `[x] PASS`
PR #46 exact tested head `6477fa6f6c4f04813acbbe5dbd43302347072adb`; merge `e25c60429e453d7b8cb8ef294d89a01ef7511103`; D7/D6/temp-auth/Required CI SUCCESS. WOZ gate `5457172823`.

## D8 — `[x] PASS / CLOSED`
8.1 PR #49 integrado `14002b29c5101232c0ca8f8b85d808c8214975fb`; 8.2 PR #52 integrado `c25ec6a824bc0ae60fbf65858d53be26d453f205`; RO resolutions PR #53 integrado `6c4499d124a64d138e791ea4abf0091766dde7e9`. Gate D8 PASS Issue #41 `5460381842`.

Follow-up fuera de D8: F2/15.1 Vaciar Trash sigue requiriendo confirmación fuerte + recent reauth + action boundary determinista.

## D9 — `[x] PASS / CLOSED`
WOZ cerró D9 REUSE-FIRST en Issue #41 `5460959369`. PostgreSQL sigue autoridad durable; migraciones/checksums/idempotencia/quarantine/rollback y protección de secretos/sesiones fueron aceptados. No reabrir por ceremonia.

## D10 — Restore y alpha

### 10.1 — `[x] PASS / CLOSED`

Evidencia técnica reusable ya aceptada:
- restore aislado real + RPO ~7 min <=15 min + RTO `3643 s` <=7200 s;
- access/retention aceptados;
- PR #56 exact tested head `0abe39e096d10d992764a2d24874e46529109a70`, integrado como `f0d65aa66988e3e1a026e237b65c65a56b098aa9`;
- strategy control-config + index + media y backup-failure condition/routing contract = PASS;
- Issue #41 `5470149521`: encrypted off-provider Google Drive copy privado/owner-only con download/readback y exact SHA-256 match.

**No repetir PITR/restore/cutover/restart/migrations/rotation.** D10.1 PASS no autoriza alpha ni release público.

### 10.2 — `[ 🟡 ] RO / ALPHA DECISION`

Owner aprobó como intención una alpha interna 3–5 cuentas invite-only, sin release público ni tester charges, condicionada a gates D2–D10/P0 y evidencia aplicable. La autorización final sigue siendo decisión RO independiente.

Estado factual nuevo a incluir en readiness:
- infraestructura Web pública está probada por owner Issue #41 `5485984669`, pero `https://beatgaler.com` queda detenido en `Loading Galer`; es bloqueo funcional F2, no fallo de deploy;
- F4 Windows Auth sigue rojo en exact #84 `f53d46f...`, run `33449587244` / job `99676242317`.

- [ ] reconciliar gates D2–D10/P0 actuales contra evidencia viva;
- [ ] clasificar blockers externos/RO restantes;
- [ ] ejecutar alpha solo tras autorización RO explícita y prerequisitos satisfechos;
- [ ] si no pasa, mantener demo/local sin scope creep.

**Owner CYCLE 103: `NIGHT-WOZ-102` READ-ONLY.** Debe producir mapa fila-por-fila `PROVEN / BLOCKED_EXTERNAL / RO_DECISION_REQUIRED / BLOCKED_BY_F2/F3/F4`, con evidencia exacta y distinguiendo alpha interna de release público. No puede lanzar alpha, mutar provider/infra, usar credenciales, crear usuarios ni cobrar testers. Maximum claim: `D10.2 READY_FOR_RO_DECISION` solo si los prerequisitos no-RO pasan factual.

**Principio:** cierre de F1 no equivale a release público; F5 permanece cerrado hasta que F0–F4 cumplan sus gates reales.
