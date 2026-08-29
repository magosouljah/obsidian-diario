# Fase 0 — Contención e integración

> Leer primero `Plan Maestro.md`. Este archivo conserva **solo** requirements/gates/evidencia necesarios para cerrar Fase 0. El detalle de PRs, logs y handoffs vive en GitHub.

**Objetivo:** dejar una sola línea integrada, segura y recuperable para continuar a Fase 1.

**Estado:** `[ 🟡 ]` residual/administrativo — **el trabajo técnico necesario para avanzar terminó y el RO autorizó Fase 1**. 5.1 y 5.2 están `[x]`. 2.2 conserva únicamente un **tail externo no bloqueante / pendiente de cierre administrativo**; 1.2 conserva dependencias externas de release. Fase 0 no se marca `[x]` mientras esos cierres sigan pendientes.

**Baseline técnico post-rewrite histórico de salida F0:** `integration-v0.8.0-alpha.1` @ `b9c2317297ff3c0f7a6246ac97517fa978f6caea`.  
**Required CI post-rewrite:** run **#314** (`33148873459`) = `SUCCESS` sobre ese SHA.  
**Baseline canónico vivo actual:** ver `Plan Maestro.md`; al último sync JOBS es `6c4499d124a64d138e791ea4abf0091766dde7e9`.

---

## Tablero

| Tarea | Estado | Gate resumido |
|---|---|---|
| 0.1 Congelar evidencia | [x] | baseline + NO-GO registrados |
| 0.2 Checkpoint interno | [x] | 4 Sep no es release público; RO puede parar |
| 1.1 Negocio | [x] | alcance comercial/distribución decidido |
| 1.2 Dependencias externas | [ 🟡 ] P1 / externo | release governance + dominio/firma/reviews/test matrix |
| 2.1 Contención inmediata | [x] | auth/ownership/límites antes de carga |
| 2.2 Historial Git | [ 🟡 ] tail externo no bloqueante | GitHub Support + verificación final de inaccesibilidad |
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

**Gate 1.2:** ninguna dependencia launch-critical queda sin owner/plan/evidencia o deferral explícito aceptado. **NO SATISFECHO.** Sigue bloqueando release cuando aplique, pero por decisión RO **no bloquea la ejecución interna posterior**.

---

## 2.2 `[ 🟡 ]` — Resolver exposición histórica

### Confirmado
- HEAD actual está sanitizado.
- Configuración real/local queda fuera de Git.
- AAA WAVE 2 confirmó metadatos operacionales alcanzables en la historia pública pre-rewrite; no confirmó plaintext credential y esa evidencia no autorizó revoke/rotation por sí sola.
- WOZ/RO autorizó la purga histórica selectiva/coordinada en Issue #41 comment `5448976400`.
- El trabajo técnico de rewrite necesario para avanzar ya fue ejecutado según la decisión RO vigente.
- Baseline post-rewrite: `b9c2317297ff3c0f7a6246ac97517fa978f6caea`.
- Required CI post-rewrite run #314 = `SUCCESS`.

### Trabajo técnico de la purga — completado para habilitar avance
- [x] Freeze/inventario y coordinación de refs necesarios para el rewrite.
- [x] Fresh mirror + rewrite selectivo del alcance aprobado.
- [x] Verificación técnica pre/post necesaria para fijar el nuevo baseline.
- [x] Excepción de force-push limitada al rewrite y retorno a línea post-rewrite.
- [x] Required CI post-rewrite verde: run #314 sobre `b9c2317297ff3c0f7a6246ac97517fa978f6caea`.

### Tail externo no bloqueante / pendiente de cierre administrativo
- [ ] **GitHub Support completa limpieza server-side** de caches/PR refs/referencias históricas aplicables.
- [ ] **Verificación final independiente/fresh** confirma inaccesibilidad de los refs/commits históricos afectados después de la limpieza server-side.

**Regla de cierre:** 2.2 **permanece `[ 🟡 ]`** hasta recibir evidencia de ambos puntos anteriores. No convertirla en `[x]` solo porque el rewrite y CI ya terminaron.

**Decisión RO vigente:** este tail externo **NO bloquea el trabajo interno posterior**. La excepción es únicamente de dependencia de avance interno; **no** equivale a cierre de 2.2 ni a GO de publicación.

**No hacer:** rewrite genérico adicional, borrar evidencia innecesariamente, rotar/revocar credenciales sin evidencia adicional, o repetir la purga solo para recrear evidencia.

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

## Estado de salida / handoff de Fase 0

Fase 0 **no se declara `[x]` administrativamente** mientras 2.2 y 1.2 sigan abiertos. Sin embargo, por decisión explícita del RO:
- el trabajo técnico necesario para avanzar terminó;
- 2.2 conserva exclusivamente un tail externo no bloqueante;
- 1.2 sigue como carril externo de release;
- el handoff de Fase 0 a Fase 1 ya fue consumido; F1 avanzó posteriormente hasta **D8 `[x] / PASS`**;
- el baseline `b9c231...` es evidencia histórica de salida F0, no el HEAD canónico actual;
- release público permanece 🔴 `NO-GO`.

**Estado activo actual:** consultar `Plan Maestro.md` y la fase vigente. No usar este archivo archivístico para retroceder el baseline ni reactivar D6–D8.