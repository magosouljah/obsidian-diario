# Fase 0 — Contención e integración

> Leer primero `Plan Maestro.md`. Este archivo conserva **solo** requirements/gates/evidencia necesarios para cerrar Fase 0. El detalle de PRs, logs y handoffs vive en GitHub.

**Objetivo:** dejar una sola línea integrada, segura y recuperable para continuar a Fase 1.

**Estado:** `[ 🟡 ]` — falta cerrar **2.2 P0** y **1.2 P1**. 5.1 y 5.2 están `[x]`.

---

## Tablero

| Tarea | Estado | Gate resumido |
|---|---|---|
| 0.1 Congelar evidencia | [x] | baseline + NO-GO registrados |
| 0.2 Checkpoint interno | [x] | 4 Sep no es release público; RO puede parar |
| 1.1 Negocio | [x] | alcance comercial/distribución decidido |
| 1.2 Dependencias externas | [ 🟡 ] P1 | release governance + dominio/firma/reviews/test matrix |
| 2.1 Contención inmediata | [x] | auth/ownership/límites antes de carga |
| 2.2 Historial Git | [ 🟡 ] P0 | purga selectiva + cleanup + verificación |
| 3.1 Integración | [x] | `integration-v0.8.0-alpha.1` |
| 3.2 Contrato plataforma | [x] | Web sin Tauri; capacidades compartidas |
| 4.1 Required CI | [x] | merge bloqueado por CI requerido |
| 4.2 Supply chain | [x] | scans/SBOM/checksums/procedencia |
| 5.1 Trust boundary / Direct | [x] | temporary auth + media directa |
| 5.2 Datos/recovery/secrets | [x] | PG productivo + RPO/RTO + rotation + observabilidad |

---

## 1.2 `[ 🟡 ]` P1 — Dependencias externas de release

### Ya decidido
- BeatGaler v1 es comercial/pagada; no existe fallback free-only.
- Distribución v1: Web + Windows NSIS + macOS DMG.
- Mercados iniciales: MX / US / CA / EU / UK; edad 18+.
- Apple Developer: **`PENDING — DEFERRED`**. No se compra todavía, pero sigue siendo gate antes de anunciar macOS público soportado.

### Falta para `[x]`
- [ ] Modelo canónico de release/provenance corregido y protegido.
- [ ] Alphas/betas separadas del canal stable/latest; future prereleases correctamente marcadas.
- [ ] Dominio/DNS/TLS/support/security-abuse/status con owners/evidencia.
- [ ] Windows Authenticode + RFC3161 timestamp plan/owner listo para release.
- [ ] Revisión legal independiente reservada.
- [ ] Revisión de seguridad independiente reservada.
- [ ] Matriz anónima de 12–20 testers + hardware/plataformas/DAWs y fechas.

**Finding vigente:** `magosouljah/galer` ya tiene releases alpha públicas, pero la auditoría BBB encontró governance insuficiente: alphas observadas no prerelease/immutable, `galer:main` sin protección y tag público no ligado directamente al SHA fuente BeatGaler. Preservar evidencia; no borrar releases casualmente.

**Gate 1.2:** ninguna dependencia launch-critical queda sin owner/plan/evidencia o deferral explícito aceptado. **NO SATISFECHO.**

---

## 2.2 `[ 🟡 ]` P0 — Resolver exposición histórica

### Confirmado
- HEAD actual está sanitizado.
- Configuración real/local queda fuera de Git.
- AAA WAVE 2 confirmó **metadatos operacionales** todavía alcanzables en historia pública.
- No se confirmó plaintext credential; esta evidencia **no autoriza revoke/rotation por sí sola**.
- WOZ/RO dio **GO** a purga histórica **selectiva y coordinada** en Issue #41 comment `5448976400`.

### Procedimiento obligatorio antes/durante el rewrite
- [ ] Freeze de escrituras al repo.
- [ ] Inventario completo `public ref → SHA` y revisión de refs task/tmp obsoletas.
- [ ] Fresh mirror + `git-filter-repo` selectivo sobre los tres paths históricos privados ya identificados y los identificadores históricos exactos del example antiguo.
- [ ] Verificación pre-push de paths/valores/historia completa + equivalencia del árbol actual.
- [ ] Excepción temporal de force-push solo donde sea imprescindible; restaurar protecciones inmediatamente.
- [ ] Cleanup GitHub-side de cache/PR refs / Support cuando aplique.
- [ ] Fresh clone post-purge + búsqueda histórica negativa + `Required CI` verde.

**No hacer:** rewrite genérico, borrar evidencia innecesariamente, rotar/revocar credenciales sin evidencia adicional.

**Gate 2.2:** exposición histórica identificada resuelta y verificada post-purge. **NO SATISFECHO.**

---

## 5.1 `[x]` — Trust boundary / Direct

**Cierre compacto:** PRs #11–#28.
- permanent auth/control secrets permanecen control-side;
- Web/Desktop productivos usan temporary auth;
- media directa probada con **1,992,294,400 bytes** y `galer_cloud_file_bytes=0`;
- Windows + macOS + Chrome/Web Worker probados;
- exclusividad por vault preferida; shared-bot solo fallback cuando no hay bots libres, max 4 + waitlist;
- riesgos residuales cross-vault fallback y cleanup >48h aceptados/documentados.

No reabrir sin evidencia nueva o decisión RO.

---

## 5.2 `[x]` — PostgreSQL / recovery / secret management

**Cierre autoritativo:** WOZ/RO Issue #41 comment `5448976400`.

### Evidencia 4/4 WAVE 3
1. **Durabilidad + rollback:** PostgreSQL autoridad productiva; restart/barrier fail-closed y rollback dry-run desde CURRENT PG; AAA aceptó independientemente.
2. **Restore:** PITR aislado representativo; **RPO ~7 min <=15 min**; **RTO 3643 s <=7200 s**; AAA verificó independientemente.
3. **Rotación multiversión:** key activa `2`, versiones `1,2`, ciphertext v1 legible bajo keyring v2; WOZ aceptó.
4. **Observabilidad/ownership:** alarmas RDS críticas enrutadas + on-call/rotation/rollback authority; WOZ aceptó.

PRs #29–#42 contienen la implementación/evidencia software.

**Regla:** no repetir restore, cutover, migrations, restart de durabilidad ni key rotation para 5.2 salvo nueva evidencia que invalide el cierre.

**Follow-up separado:** un OAuth client secret fue visible al operador durante troubleshooting; rotarlo antes de release sin publicar su valor. No reabre 5.2.

---

## Tareas cerradas — referencias mínimas

- **0.1 / 0.2:** release ledger + NO-GO + checkpoint interno.
- **1.1:** negocio/mercados/distribución cerrados.
- **2.1:** `PASS regression-http-containment`; límite técnico 1.99 GB decimal.
- **3.1:** rama integrada/versionada/protegida.
- **3.2:** `src/platform/capabilities.ts`; Web-no-Tauri.
- **4.1:** `Required CI` Web/shared + PostgreSQL + supply chain + Windows + macOS.
- **4.2:** scans/SBOM/checksums/procedencia; deuda GPL conocida sigue como gate global separado.

El detalle completo histórico puede recuperarse del Git history de este archivo, PRs/Actions e Issue #41.

---

## Gate de salida de Fase 0

Fase 0 cambia a `[x]` únicamente cuando:
- [ ] **2.2 `[x]`**;
- [ ] **1.2 `[x]`**;
- [ ] no aparece un nuevo P0/P1 de Fase 0 que invalide el avance.

Hasta entonces: **NO iniciar Fase 1 como frente principal.**