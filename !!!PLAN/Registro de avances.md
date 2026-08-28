# Registro de avances — BeatGaler

> **Ledger compacto.** Este archivo conserva hitos, cambios de estado y evidencia mínima. Los logs, diffs, experimentos y handoffs completos viven en PRs, Actions e Issue #41.
>
> **Lectura normal:** leer solo entradas recientes/relevantes para la tarea actual. El detalle anterior sigue en Git history.

## 2026-08-22

- **0.1 `[x]` — Baseline/NO-GO.** Release ledger congeló SHAs, pruebas, warnings y límites; sin tag público.
- **0.2 `[x]` — Checkpoint interno.** 4 Sep queda como checkpoint, no release público; RO mantiene stop authority; 0 P0/P1 para publicar.
- **1.1 `[x]` — Negocio.** v1 comercial, nunca free-only; MX/US/CA/EU/UK, 18+, MXN/USD/CAD/EUR/GBP, Web + Windows NSIS + macOS DMG.
- **1.2 `[ 🟡 ]` — Dependencias externas.** Dominio/DNS/support/status, firma, reviews independientes y testers quedan pendientes.
- **2.1 `[x]` — Contención.** Auth/ownership/límites antes de multipart; registro público cerrado por defecto.
- **2.2 `[ 🟡 ]` — Incidente Git.** HEAD sanitizado; deuda histórica aún pendiente.

## 2026-08-23 a 2026-08-24

- **3.1 `[x]` — Integración.** `integration-v0.8.0-alpha.1`, versión `0.8.0-alpha.1`, CI multiplataforma verde.
- **3.2 `[x]` — Contrato plataforma.** PR #8 / merge `32a38c490a53650a0e9d6435c50cd009ef1b5123`.
- **4.1 `[x]` — Required CI.** PR #9 / merge `c7894ad3c2b3e296e3d2939d73953b159e48852f`.
- **4.2 `[x]` — Supply chain.** PR #10 / merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; deuda GPL queda como gate global separado.

## 2026-08-24 a 2026-08-25 — Tarea 5.1

- **M0 / Direct.** PRs #13–#18 probaron temporary auth y transferencia directa de **1,992,294,400 bytes** con `galer_cloud_file_bytes=0`; permanent auth/token/API hash no llegan al cliente.
- **Plataformas/pool/delete/expiry.** PRs #23–#27: Windows/macOS/Chrome-WebWorker, delete reciente, límite >48 h documentado, fair pool, exclusividad preferida, shared fallback solo sin bots libres, max 4 + waitlist, expiry/recovery.
- **5.1 `[x]`.** PR #28; merge `d9ae76f42faee3a7207b9232b7421a0bec20b090`; Required CI verde y aprobación RO.

## 2026-08-25 a 2026-08-27 — Tarea 5.2 software

- **PRs #29–#36.** PostgreSQL schema/migrations, envelope encryption, importer idempotente, garbage journal, durable Direct ops, reconciliation, rollback/recovery, runtime authority y worker durable.
- **PR #37.** Cutover fail-closed/staging sealed/READY atómico; merge `edad9e324132fa086ef729ef4faec574661578a9`.
- **PR #39.** Keyring versionado + rotación transaccional; merge `1a5cc387aef431cd5f5115ad537f55e80856fb08`.
- **PR #40.** AWS Secrets Manager software boundary; merge `f997415c794c74ee1b86ef593476dba3587eeca1`.
- **PR #42.** Base64 canónico estricto; merge histórico previo al rewrite `a968122127c584b5557b25e70a21eb64f75b3c0e`.

## 2026-08-27 / UTC 2026-08-28 — WAVE 2/3

- **2.2 reauditoría.** HEAD limpio; metadatos operacionales históricos aún alcanzables. GO técnico para purga selectiva/coordinada; no plaintext credential confirmado.
- **1.2 reauditoría.** Releases públicas con governance insuficiente; dominio/DNS/support/status, Authenticode, reviews y matriz física pendientes. Apple Developer = `PENDING — DEFERRED`.
- **5.2 criterio 1 PASS.** PostgreSQL autoridad productiva + restart durable + rollback dry-run desde CURRENT PG.
- **5.2 criterio 2 PASS.** PITR aislado representativo: RPO ~7 min; **RTO 3643 s = 1h00m43s**.
- **5.2 criterio 3 PASS.** Key activa `2`, versiones `1,2`; ciphertext v1 leído bajo keyring v2.
- **5.2 criterio 4 PASS.** Alarmas RDS críticas + on-call/rotation/rollback authority.
- **Security follow-up.** OAuth client secret visible al operador durante troubleshooting; rotar antes de release. No registrar valor.

## 2026-08-28 — cierre y simplificación operativa

- **5.2 `[x]` — CERRADA.** Síntesis WOZ/RO Issue #41 comment `5448976400`: 4/4 aceptados. No repetir restore/cutover/migrations/durability restart/key rotation sin evidencia nueva.
- **2.2 GO técnico.** Purga histórica selectiva/coordinada autorizada; 2.2 sigue `[ 🟡 ]` hasta cierre externo.
- **`!!!PLAN` compactado por JOBS.** Camino operativo corto: Plan Maestro → fase activa → avances relevantes → Issue #41.

## 2026-08-28 — post-rewrite y activación Fase 1

- **Baseline post-rewrite inicial:** `b9c2317297ff3c0f7a6246ac97517fa978f6caea`.
- **Required CI post-rewrite PASS:** run #314 (`33148873459`).
- **2.2 `[ 🟡 ]` tail externo no bloqueante.** Falta GitHub Support + fresh verification final.
- **Fase 1 `[ 🟡 ]` ACTIVA.** Orden: `6.1 ∥ 6.2 → D6 → 7.1 ∥ 7.2 → D7 → 8.1 ∥ 8.2 → D8 → 9.1 ∥ 9.2 → D9 → 10.1 → 10.2`.

## 2026-08-28 — D6 integración y fast lane JOBS

- **PR #44 / 6.2 integrado.** Merge de abuse controls + password KDF asíncrono en integración `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`; request path ya no depende de `scryptSync`.
- **PR #43 / 6.1 integrado.** Merge `23bded948c4377b28fc48a72378816968d4cd413`; session-bound authorization, ownership, PostgreSQL cross-process claim coordination y compatibilidad conjunta 6.1/6.2.
- **Head pre-merge final #43:** `5cfec64d756caf73ad3d57f4bb943e7adaabf6bd`; compile + D6 cross-process + Required CI = `SUCCESS`.
- **Head integrado actual:** `23bded948c4377b28fc48a72378816968d4cd413`.
- **Integración exact-head checks:** compile #128 (`33194215442`) `SUCCESS`; D6 cross-process #4 (`33194215463`) `SUCCESS`; Required CI #363 (`33194215450`) sigue `IN_PROGRESS`, con Web/shared, PostgreSQL/recovery y supply-chain ya verdes.
- **D6:** `[ ⚠️ ]` implementación integrada, **Gate todavía `PENDING`** hasta cierre de #363 + decisión estructurada WOZ. JOBS no autoacepta.
- **AAA/BBB NOW:** `LIBRE / BLOQUEADO POR D6`; no reabrir trabajo aceptado sin delta nuevo.
- **Fast lane preasignado:** D6 PASS → WOZ 7.1 / AAA 7.2 / BBB review 7.1; D7 PASS → WOZ 8.1 / AAA 8.2 / BBB review; D8 PASS → D9 REUSE-FIRST; D9 PASS → 10.1 REUSE-FIRST; después 10.2 decisión alpha.
- **REUSE-FIRST reforzado 9/10.** JOBS prepara matrices, WOZ decide equivalencia técnica/GAP, AAA prueba gaps, BBB revisa independencia. Prohibido repetir drills ya aceptados solo para recrear evidencia.

---

## Estado al cierre de esta entrada

- Fase 0: `[ 🟡 ]` residual/administrativa; trabajo técnico de avance concluido.
- 5.1: `[x]`.
- 5.2: `[x]`.
- 2.2: `[ 🟡 ]` tail externo no bloqueante.
- 1.2: `[ 🟡 ]` P1 externo de release.
- Fase 1: `[ 🟡 ]` **ACTIVA — Día 6 CLOSEOUT**.
- D6: `PENDING` por Required CI #363 + gate transaction WOZ.
- Release público: 🔴 `NO-GO`.
- WOZ NEXT: cerrar D6 transaction; si PASS, iniciar 7.1 inmediatamente.