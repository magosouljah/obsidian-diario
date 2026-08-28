# Registro de avances — BeatGaler

> **Ledger compacto.** Este archivo conserva hitos, cambios de estado y evidencia mínima. Los logs, diffs, experimentos y handoffs completos viven en PRs, Actions e Issue #41.
>
> **Lectura normal:** no releer todo el historial. Leer solo las entradas recientes/relevantes para la tarea actual. Las versiones detalladas anteriores siguen recuperables en Git history.

## 2026-08-22

- **0.1 `[x]` — Baseline/NO-GO.** Release ledger congeló SHAs, pruebas, warnings y límites; sin tag público.
- **0.2 `[x]` — Checkpoint interno.** 4 Sep queda como checkpoint, no release público; RO mantiene stop authority; 0 P0/P1 para publicar.
- **1.1 `[x]` — Negocio.** v1 comercial, nunca free-only; MX/US/CA/EU/UK, 18+, MXN/USD/CAD/EUR/GBP, Web + Windows NSIS + macOS DMG.
- **1.2 `[ 🟡 ]` — Dependencias externas.** Dominio/DNS/support/status, firma, reviews independientes y testers quedan pendientes.
- **2.1 `[x]` — Contención.** Auth/ownership/límites antes de multipart; registro público cerrado por defecto; `PASS regression-http-containment`.
- **2.2 `[ 🟡 ]` — Incidente Git.** HEAD sanitizado; deuda histórica aún pendiente.

## 2026-08-23 a 2026-08-24

- **3.1 `[x]` — Integración.** Creada `integration-v0.8.0-alpha.1`, versión `0.8.0-alpha.1`, CI multiplataforma verde.
- **3.2 `[x]` — Contrato plataforma.** Matriz compartida + guard Web-no-Tauri; PR #8 / merge `32a38c490a53650a0e9d6435c50cd009ef1b5123`.
- **4.1 `[x]` — Required CI.** PR #9 / merge `c7894ad3c2b3e296e3d2939d73953b159e48852f`; Web/shared + Windows + macOS requeridos.
- **4.2 `[x]` — Supply chain.** PR #10 / merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; scans, SBOM, checksums y procedencia. Deuda GPL conocida queda como gate global separado.

## 2026-08-24 a 2026-08-25 — Tarea 5.1

- **M0 / Direct.** PRs #13–#18 probaron temporary auth y transferencia directa de **1,992,294,400 bytes** con `galer_cloud_file_bytes=0`; permanent auth/token/API hash no llegan al cliente.
- **Plataformas/pool/delete/expiry.** PRs #23–#27: Windows/macOS/Chrome-WebWorker, delete reciente, límite >48 h documentado, fair pool, exclusividad preferida, shared fallback solo sin bots libres, max 4 + waitlist, expiry/recovery.
- **5.1 `[x]`.** PR #28 migró runtime productivo Web/Desktop; merge `d9ae76f42faee3a7207b9232b7421a0bec20b090`; Required CI verde y aprobación RO. Riesgos residuales aceptados/documentados.

## 2026-08-25 a 2026-08-27 — Tarea 5.2 software

- **PRs #29–#36.** PostgreSQL schema/migrations, envelope encryption, importer idempotente, garbage journal, durable Direct ops, reconciliation, rollback/recovery, runtime authority y worker durable.
- **PR #37.** Cutover fail-closed/staging sealed/READY atómico; merge `edad9e324132fa086ef729ef4faec574661578a9`.
- **PR #39.** Keyring versionado + rotación transaccional; merge `1a5cc387aef431cd5f5115ad537f55e80856fb08`.
- **PR #40.** AWS Secrets Manager software boundary; merge `f997415c794c74ee1b86ef593476dba3587eeca1`.
- **PR #42.** Base64 canónico estricto; merge histórico previo al rewrite `a968122127c584b5557b25e70a21eb64f75b3c0e`; post-merge Required CI verde.

## 2026-08-27 / UTC 2026-08-28 — WAVE 2/3

- **2.2 reauditoría.** AAA confirmó HEAD limpio pero metadatos operacionales aún alcanzables en historia pública. Recomendó `GO` para purga histórica selectiva/coordinada; no confirmó plaintext credential.
- **1.2 reauditoría.** BBB confirmó `magosouljah/galer` con alphas públicas pero governance insuficiente; dominio/DNS/support/status, Authenticode, reviews y matriz física pendientes. Apple Developer = `PENDING — DEFERRED`.
- **5.2 criterio 1 PASS.** PostgreSQL autoridad productiva + restart durable + rollback dry-run desde CURRENT PG; AAA aceptó independientemente.
- **5.2 criterio 2 PASS.** PITR aislado representativo: RPO ~7 min; segundo restore midió **RTO 3643 s = 1h00m43s**; AAA verificó independientemente.
- **5.2 criterio 3 PASS.** Key activa `2`, versiones `1,2`; ciphertext v1 leído correctamente bajo keyring v2; WOZ aceptó.
- **5.2 criterio 4 PASS.** Alarmas RDS críticas enrutadas + on-call/rotation/rollback authority; WOZ aceptó.
- **Security follow-up.** Un OAuth client secret fue visible al operador durante troubleshooting; debe rotarse antes de release. Su valor no se registra.

## 2026-08-28 — cierre y simplificación operativa

- **5.2 `[x]` — CERRADA.** WOZ/RO publicó síntesis global en Issue #41 comment `5448976400`: 4/4 aceptados, sin blocker real nuevo. No repetir restore/cutover/migrations/durability restart/key rotation para 5.2 sin evidencia nueva.
- **2.2 GO técnico.** El mismo veredicto WOZ/RO autorizó purga histórica selectiva/coordinada con write freeze, inventario refs, fresh mirror + filter-repo selectivo, verificación pre/post, cleanup GitHub-side y Required CI. 2.2 siguió `[ 🟡 ]` hasta terminar su cierre.
- **`!!!PLAN` compactado por JOBS.** Se reemplazó la lectura enciclopédica por camino operativo corto: `Plan Maestro` → fase activa → avances relevantes → Issue #41; Gates/Contexto/fases futuras solo bajo demanda. Se compactaron `Plan Maestro`, `Fase 0`, `Equipo multi-IA` y este Registro sin rebajar gates ni tocar el archivo histórico protegido.

## 2026-08-28 — post-rewrite y activación de Fase 1

- **Baseline post-rewrite verificado.** `integration-v0.8.0-alpha.1` apunta a `b9c2317297ff3c0f7a6246ac97517fa978f6caea`.
- **Required CI post-rewrite PASS.** `Test - Desktop Portability` run **#314** (`33148873459`) terminó `SUCCESS` sobre `b9c2317297ff3c0f7a6246ac97517fa978f6caea`.
- **2.2 `[ 🟡 ]` — tail externo no bloqueante / pendiente de cierre administrativo.** Decisión RO vigente: el trabajo técnico necesario para avanzar terminó. Quedan únicamente (1) limpieza server-side por GitHub Support y (2) verificación final de inaccesibilidad de refs/commits históricos. **No marcar 2.2 `[x]`** hasta recibir ambas evidencias.
- **Excepción de dependencia aprobada por RO.** El tail externo de 2.2 no bloquea Fase 1. 1.2 permanece como carril externo de release. Esta decisión no reduce ningún gate de publicación.
- **Fase 1 `[ 🟡 ]` — ACTIVA.** Día 6 queda activado inmediatamente; release público sigue 🔴 `NO-GO`.
- **Orden obligatorio Fase 1.** `6.1 ∥ 6.2 → D6 → 7.1 ∥ 7.2 → D7 → 8.1 ∥ 8.2 → D8 → 9.1 ∥ 9.2 → D9 → 10.1 → 10.2`. No iniciar un Día posterior antes de aprobar el gate anterior.
- **Día 6 / F1-A.** WOZ PRIMARY = 6.1 + integración/cierre técnico del Día 6; AAA = 6.2 abuse controls + suite adversarial; BBB = review independiente READ ONLY de 6.1; JOBS = coordinación/plan/`WOZ NEXT`.
- **Gate D6.** Requiere identidad user/installation/tenant derivada de sesión validada, auth+authz+límites antes de trabajo costoso, ownership por objeto, matriz 401/403/413/429, pruebas cross-tenant y cero acceso/mutación cross-tenant en suite adversarial.
- **Después de D6 PASS.** AAA → 7.2; BBB → review independiente de 7.1; WOZ → 7.1 + integración. Hasta entonces 7.x permanece bloqueado.
- **REUSE-FIRST 9.x/10.x.** Cada requirement se mapeará primero contra evidencia aceptada de Fase 0/5.2: PostgreSQL autoridad productiva, migrations/versionado, importer/rollback, durabilidad, PITR restore, RPO ~7 min, RTO 3643 s, keyring multiversión y observabilidad/ownership. No repetir restore/cutover/migrations/durability restart/key rotation solo para recrear evidencia.

---

## Estado al cierre de esta entrada

- Fase 0: `[ 🟡 ]` residual/administrativa; trabajo técnico de avance concluido.
- 5.1: `[x]`.
- 5.2: `[x]`.
- 2.2: `[ 🟡 ]` — **tail externo no bloqueante / pendiente de cierre administrativo**.
- 1.2: `[ 🟡 ]` P1 externo de release.
- Fase 1: `[ 🟡 ]` **ACTIVA — Día 6**.
- D6: `PENDING`.
- Release público: 🔴 `NO-GO`.
- WOZ NEXT: 6.1 + integración con 6.2 en paralelo.