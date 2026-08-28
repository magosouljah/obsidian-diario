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

## 2026-08-28 — D7 / CLOSED

- WOZ PR #46 `woz/task-7.1-direct-capabilities` final tested head `6477fa6f6c4f04813acbbe5dbd43302347072adb`.
- PR #46 merge a integración: `e25c60429e453d7b8cb8ef294d89a01ef7511103`.
- Branch `integration-v0.8.0-alpha.1` verificado en `e25c60429e453d7b8cb8ef294d89a01ef7511103`.
- D7 `33205320953` SUCCESS; D6 cross-process `33205320957` SUCCESS; temp-auth compile `33205321000` SUCCESS; Required CI #402 `33205320950` SUCCESS en Web/shared, PostgreSQL recovery, Supply Chain/HEAD secret scan, Windows, macOS arm64 y x86_64.
- AAA findings `5456406567` consumidos/cerrados por WOZ: expiry/skew parity, fail-closed response redaction, live lease/quarantine coupling.
- BBB findings `5456351308` + revoke-order posterior consumidos/cerrados por WOZ: canonical revoke target, durable fail-closed, pre-mutation revoke.
- D7 `[x] / PASS`: WOZ gate transaction `5457172823`.
- Architecture note: PASS aplica a capability mediation BeatGaler bajo Direct/shared-bot aceptado; no afirma primitive provider-native object-scoped.

## 2026-08-28 — F2 / 11.1 AAA

- PR #47 `aaa/f2-11.1-design-foundations` @ `ddad3124cc3d1577d76d9965b55189a2cfb88383` = OPEN / no mergeado.
- Handoff AAA `5456682762`: `DONE — INDEPENDENT SLICE ONLY`.
- Required CI #392 `33202493998` SUCCESS; D6 #33 `33202493855` SUCCESS.
- Candidate cubre tokens/primitives/focus/Dialog/reduced motion, AccountGate autofill/contrast/loading/390–430, docs y DOM/a11y tests en 7 files.
- 11.1 global permanece `[ 🟡 ]`: no `[x]` hasta integración/secuenciación verificable sobre el estado actual.

## 2026-08-28 — F4 / 21.1 BBB — audit inicial

- Handoff BBB `5456640788`: audit READ ONLY / FINDING sobre base `23bded948c4377b28fc48a72378816968d4cd413`.
- REUSE inicial: versión/name sources alineados, runtime pins/provenance, macOS universales, Windows Node/Bot API, common capabilities y release same-SHA checks.
- GAPS iniciales: bundle ID, updater endpoint, channel/feed, Windows FFmpeg y same-SHA manifest tooling. Este bloque queda como historia de entrada; fue superado por el candidate #48 descrito abajo.

## 2026-08-28 — DECISIÓN RO / ROMPECABEZAS

RO elimina la restricción “todos en el mismo Día”. Trabajo cross-phase permitido por dependencia real. JOBS puede organizar owners/fases/prioridades sin rebajar gates.

## 2026-08-28 — DECISIÓN RO / OWNER FIJO + SELF-TEST

RO precisa el modelo:
- **WOZ** terminó F1/D7 y, tras Gate D7 PASS, JOBS lo reasigna explícitamente a **F1 / D8 / 8.1+8.2** hasta cierre D8.
- Owners pueden cambiar solo por reasignación explícita JOBS/RO; GitHub/Issue más reciente prevalece sobre texto stale del plan.
- Findings de otros agentes se usan como input/casos de prueba por el owner actual.
- No hopping automático al aparecer/desaparecer dependencias.
- Si un owner queda bloqueado, conserva ownership y reporta blocker; JOBS solo reasigna mediante decisión explícita.
- Revisión independiente adicional se conserva únicamente cuando JOBS/RO o un gate posterior la exige literalmente.

## 2026-08-28 — JOBS preflight factual / WAVE #47 #50 #48 #49

Baseline canónico revalidado: `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.

### WOZ / PR #49 / F1 D8 8.1
- PR #49 `woz/task-8.1-session-security` @ `f8ae2d1dedf0b4f977b4aedcaef5ac4ea83acdff` = OPEN / no mergeado / no draft / mergeable al preflight.
- Compare desde baseline canónico: `ahead_by=7`, `behind_by=0`; es el único candidate de esta wave verificado directamente encima de `e25c604...`.
- Exact-head Required CI/Test Desktop Portability #406 `33208687131` SUCCESS; D6 #46 `33208687050` SUCCESS; D7 `33208687027` SUCCESS; Productive Temp Auth Compile #159 SUCCESS.
- El PR cubre sesión/CSRF/inventory/revocation/rotation y distingue 401/expiry de network loss; explícitamente **no reclama D8 PASS** porque 8.2 sigue pendiente.
- No se localizó handoff estructurado WOZ de #49 en Issue #41 durante el preflight. Estado documental de 8.1 = `[ 🟡 ] / READY_FOR_WOZ_INTEGRATION`, no `[x]`.
- WOZ NEXT: recheck final, integrar #49 por flujo autorizado, publicar handoff 8.1 y continuar 8.2 dentro del mismo ownership. D8 permanece `PENDING`.

### AAA / PR #47 → PR #50 / F2
- #47 @ `ddad3124...`: OPEN/no mergeado/no draft; handoff `5456682762` DONE independent slice; Required CI #392 SUCCESS. Contra `e25c604...`: `diverged`, `behind_by=49`.
- #49 y #47 comparten `src/components/AccountGate.tsx` y `tests/component-dom/accountGateWeb.test.tsx`; por evidence-before-claim, #47 debe revalidarse después de la integración #49.
- #50 @ `258017f...`: OPEN/no mergeado/no draft; handoff `5458081273` DONE; Required CI #416 SUCCESS; base PR = rama #47. Contra `e25c604...`: `diverged`, `behind_by=49`.
- Dependencia obligatoria: **#47 debe integrarse antes de #50**. Si cambia cualquiera de sus heads para incorporar integración vigente, se exige CI exact-head nuevo antes del cierre.
- Owner actual AAA = F2/12.2 por reasignación RO registrada en #50/handoff. 11.1 y 12.2 siguen `[ 🟡 ]` hasta integración verificable.
- AAA NEXT tras cerrar/integrar #47 y #50: 11.2 solo si D8/8.2 ya habilitó sus APIs; con el estado actual, la alternativa F2 independiente ya planificada es **12.1 Bootstrap y load**.

### BBB / PR #48 / F4 21.1 → 21.2
- PR #48 `bbb/f4-21.1-release-manifest` @ `a3ba448e9ded04f73ee77a3556809dcf72e707f5` = OPEN / DRAFT / no mergeado / mergeable al preflight.
- Handoff BBB `5457967950` = `READY_FOR_INTEGRATION / COMPLETE_TECHNICAL`; decisión RO usada por el candidate: nombre `Galer`, bundle ID `com.beatgaler.app`; Required CI #412 `33212138329` y matrices aplicables SUCCESS.
- Contra `e25c604...`: `diverged`, `behind_by=49`; #48 y #49 comparten `package.json`. El CI actual no prueba todavía la combinación post-#49.
- 21.1 permanece `[ 🟡 ]`: requiere incorporar baseline posterior a #49, estado apto para integración por flujo autorizado, CI exact-head y merge canónico antes de `[x]`.
- RO reasignó explícitamente BBB a **21.2 Upgrade Matrix** en Issue #41 `5458104890`, `STATUS: ASSIGNED / PRECHECK`, mientras #48 siga no integrado. BBB puede hacer trabajo dependency-safe, pero no falsear 21.1 cerrado.

### Decisión JOBS de secuencia
1. #49 primero por WOZ/integrador autorizado.
2. #47 después de incorporar/revalidar baseline post-#49.
3. #50 únicamente después de #47 integrado y con revalidación sobre la integración que ya lo contenga.
4. #48 incorporar/revalidar baseline post-#49 y luego integrar; su refresh puede correr en paralelo con la cadena F2 si no rompe mutex técnico.
5. JOBS **no ejecuta merges de código BeatGaler**; solo secuencia, exige evidencia, sincroniza `!!!PLAN` y publica handoffs.

No se marcó ningún checkbox nuevo por esta wave. Release público continúa 🔴 `NO-GO`.

---

## Estado actual

- Integración estable: `integration-v0.8.0-alpha.1` @ `e25c60429e453d7b8cb8ef294d89a01ef7511103`.
- WOZ: **F1/D8 full owner**; #49/8.1 ready para integración WOZ, después 8.2; D8 `[ 🟡 ] / PENDING`.
- AAA: **F2/12.2 owner actual**; #47→#50 pendientes de refresh/revalidación/integración; ambos sin `[x]`.
- BBB: **F4/21.2 FULL OWNER / PRECHECK** por `5458104890`; #48/21.1 técnico completo pero OPEN/DRAFT/no integrado; 21.1 sin `[x]`.
- JOBS: coordinación/plan/handoffs; no código BeatGaler ni merges técnicos.
- D6: `[x] / PASS`.
- D7: `[x] / PASS`.
- D8: `[ 🟡 ] / PENDING`.
- 5.1/5.2: `[x]`.
- 2.2/1.2: tails externos `[ 🟡 ]`.
- Release público: 🔴 `NO-GO`.