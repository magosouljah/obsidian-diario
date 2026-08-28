# Fase 0 — Contener, decidir y crear una sola línea de release

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 22–28 de agosto  
**Objetivo:** eliminar ambigüedad, contener exposición y producir `0.8.0-alpha.1` desde una rama protegida.

## Ejecución multi-cuenta durante Fase 0

Desde el 27 de agosto de 2026 el equipo operativo se divide en **cuatro roles** según `Equipo multi-IA - Roles y coordinación.md`: `JOBS` es dueño de `!!!PLAN` y coordinador normal de AAA/BBB; `WOZ` es jefe técnico e integrador; `AAA` y `BBB` son ayudantes ejecutores. JOBS mantiene el plan limpio, detecta desincronización, consulta Issue #41, asigna/reasigna trabajo independiente a AAA/BBB y entrega a WOZ el siguiente frente técnico permitido. JOBS no modifica BeatGaler ni infraestructura; sus únicas escrituras de archivos de repositorio son dentro de `!!!PLAN`.

WOZ conserva la autoridad técnica: arquitectura, decisiones de implementación, código, infraestructura, aceptación/rechazo de findings e integración. AAA/BBB no cambian gates ni marcan `[x]`; entregan evidencia/handoff. BeatGaler Issue #41 es el `AI Coordination Inbox` para asignaciones, blockers y handoffs entre cuentas.

**Estado actual de Fase 0:** Tarea 5.2 alcanzó **4/4 criterios WAVE 3 satisfechos individualmente** y queda `[ ⚠️ ]` a la espera de síntesis global WOZ/RO antes de `[x]`. Fase 0 continúa abierta por **Tarea 2.2 `[ 🟡 ]` (P0)** y **Tarea 1.2 `[ 🟡 ]` (P1)**. No avanzar a Fase 1 hasta resolver los gates pendientes de Fase 0.

## Día 0 — 22–23 de agosto — Baseline y NO-GO

**Resultado:** alcance auditado, inventario y reglas de publicación congelados.

### Tarea 0.1 [P0 · RO/QA] — Congelar evidencia

- [x] Registrar las dos ramas y SHAs auditados en el release ledger.
- [x] Guardar conteos de pruebas, warnings, vulnerabilidades y límites no verificados.
- [x] Etiquetar el estado actual `NO-GO`; no crear un tag de release público.

### Tarea 0.2 [P0 · RO] — Convertir el 4 de septiembre en checkpoint interno

- [x] Comunicar que no habrá cobros ni usuarios reales en ese hito.
- [x] Definir quién tiene autoridad de parar el release.
- [x] Abrir backlog P0/P1 con un owner y evidencia de salida por item.

**Decisión de gobernanza de 0.2:**
- El **4 de septiembre de 2026** es checkpoint interno; no es fecha de lanzamiento público.
- En ese hito no se aceptan cobros ni usuarios reales de producción.
- El **Release Owner (RO)** tiene autoridad final para detener el release.
- Cualquier P0/P1 abierto o fallido bloquea el release aunque exista presión de calendario.
- Backlog operativo: BeatGaler Issue #3 — P0/P1 Launch Backlog.

**Dependencias:** ninguna.  
**Evidencia:** SHAs, auditorías, release ledger y backlog P0/P1.  
**Gate de salida:** alcance y regla “0 P0/P1” aceptados; nadie presenta el 4 de septiembre como fecha pública. **SATISFECHO.**

## Día 1 — 24 de agosto — Charter de producto y decisiones externas

**Resultado:** producto público, monetización y distribución definidos sin placeholders.

### Tarea 1.1 [P0 · RO/LF] — Cerrar decisiones de negocio

- [x] Elegir lanzamiento pagado completo o preview free-only: **v1 siempre será comercial/pagada y nunca free-only**. Si Stripe/billing no supera todos los gates, v1 se retrasa. La Official Beta puede entregar planes reales gratuitamente mediante códigos/promociones/grants temporales.
- [x] Confirmar entidad legal, países iniciales, edad mínima, currency, impuestos y política de refund.
- [x] Confirmar distribución directa Web/NSIS/DMG; stores quedan post-lanzamiento salvo decisión explícita.

**Decisiones de negocio de 1.1:**
- **Modelo comercial:** los planes existen desde el inicio. No se crea un modo free-only para v1. Los accesos regalados son entitlements completos del plan otorgado durante un periodo definido.
- **Promociones/autocobro:** un plan regalado conserva exactamente las capacidades del plan. Si el usuario inicia una suscripción con renovación automática, el cobro al terminar el periodo gratis solo puede activarse si antes aceptó claramente el precio, la fecha del primer cobro y la renovación automática.
- **Mercados iniciales:** México, Estados Unidos, Canadá, Unión Europea y Reino Unido.
- **Edad mínima:** 18 años.
- **Monedas iniciales:** MXN, USD, CAD, EUR y GBP.
- **Refund comercial base:** solicitud dentro de los primeros 14 días de la compra inicial, con controles antiabuso razonables y sin dificultar artificialmente derechos obligatorios superiores.
- **Estructura inicial:** operar inicialmente desde México bajo la estructura fiscal/legal individual más simple que resulte válida, sujeto a validación con contador/asesor antes de aceptar cobros reales.
- **Impuestos:** todavía no se consideran implementados; cálculo, registro y obligaciones por mercado son gate de billing/legal antes de v1.
- **Distribución v1:** Web pública + instalador Windows `.exe` NSIS + macOS DMG, distribuidos directamente por BeatGaler. Stores quedan fuera de v1 salvo decisión posterior.

### Tarea 1.2 [P1 · RO/LF] — Reservar dependencias con lead time

- [ 🟡 ] Confirmar dominio y ownership de DNS, GitHub Releases, email de soporte y status page. **Estado actualizado:** dominio/DNS/support/status siguen pendientes. GitHub Releases **ya existe y está activo públicamente** en `magosouljah/galer`, con alphas publicadas, pero su governance **NO satisface todavía el gate de release**.
- [ 🟡 ] Iniciar/confirmar Apple Developer ID, notarización y servicio/certificado Authenticode con timestamp. **Estado:** **Apple Developer = `PENDING — DEFERRED`**; Authenticode sigue pendiente.
- [ 🟡 ] Reservar revisión legal, seguridad independiente, hardware físico y 12–20 testers. **Estado:** hay disponibilidad humana de testers, pero revisión legal/seguridad, roster/matriz física y evidencia fechada siguen pendientes.

**Decisiones/estado de reservas de 1.2:**
- **Dominio/DNS:** pendiente. Deben definirse owner legal, registrar/DNS provider, recovery/MFA, renovación, apex/www/app/api/OAuth callbacks, TLS/WAF/proxy y rollback DNS.
- **GitHub Releases:** canal operativo pero **no release-gate-ready**. Auditoría BBB WAVE 2 verificó releases alpha públicas hasta `v0.8.0-alpha.5`; las observadas aparecían `draft=false`, `prerelease=false`, `immutable=false`; `magosouljah/galer:main` estaba sin protección/rulesets y el tag público no quedaba directamente ligado al SHA fuente BeatGaler. No usar esto como evidencia de release final.
- **Release containment pendiente:** antes de nuevas publicaciones públicas, WOZ/RO debe decidir el modelo canónico de release/provenance, proteger el canal, marcar alphas/betas como prerelease, separar test ring de `/releases/latest`, exigir artefactos completos del mismo SHA y preservar evidencia existente sin borrado casual.
- **Email de soporte + status page:** pendientes del dominio definitivo; requieren SPF/DKIM/DMARC, escalación y ownership.
- **Apple Developer:** **`PENDING — DEFERRED`**. Sigue requerido para Developer ID, notarización, stapling y Gatekeeper de macOS, pero no se compra/activa todavía.
- **macOS soportado:** objetivo v1 = **Apple Silicon + Intel**, ambos con prueba física antes de anunciar soporte.
- **Windows Authenticode:** pendiente de seleccionar/contratar servicio/certificado, integrar SHA-256 + RFC3161 timestamp y verificar installer/binarios.
- **Testers:** disponibilidad humana no equivale a gate; falta roster anónimo 12–20, cobertura por plataforma/navegador/DAW y evidencia fechada.
- **Legal y seguridad independiente:** pendientes de reservar; revisión interna no los sustituye.

**Dependencias:** Día 0.  
**Evidencia:** auditoría BBB WAVE 2 en Issue #41 + comprobantes externos seguros cuando existan.  
**Gate de salida:** ninguna decisión de alcance crítica queda sin owner/fecha y las dependencias de firma/release/review/test están realmente reservadas o justificadamente diferidas. **NO SATISFECHO; `[ 🟡 ]`.**

## Día 2 — 25 de agosto — Contención de seguridad e incidente

**Resultado:** superficies de mayor riesgo cerradas a tráfico público.

### Tarea 2.1 [P0 · BE/OP] — Retirar exposición inmediata

- [x] Deshabilitar o autenticar antes de Multer todas las rutas legacy de media/metadata.
- [x] Limitar cuerpo, archivo, concurrencia y frecuencia en edge y aplicación.
- [x] Desactivar registro público hasta tener abuse controls y verificación.

**Estado técnico de 2.1:**
- `cloud-server/http-containment.js` y bootstrap seguro en `server.js`; auth antes de Multer, ownership server-side, límites de tamaño/rate/concurrencia y registro público cerrado por defecto en producción.
- Máximo técnico por archivo: **1.99 GB decimal = 1,990,000,000 bytes**.
- Evidencia runtime: `npm run test:containment` → **`PASS regression-http-containment`**.

### Tarea 2.2 [P0 · BE/RO] — Tratar el estado rastreado como incidente potencial

- [x] Determinar en privado si IDs/bots/vaults son reales, sintéticos o revocados. **Resultado:** se encontró información operacional concreta; se trata como potencialmente real.
- [x] Retirar del HEAD la información operacional y mantener configuración real fuera de Git. **Hecho/verificado:** se eliminaron `transport-pool-state.backup.json`, `transport-bots.json` y `transport-bots.local.json`; configuración real/local queda privada/ignorada y `transport-bots.example.json` sanitizado.
- [ 🟡 ] Reauditar historial Git y resolver exposición antigua. **Reauditoría WAVE 2 completada por AAA:** confirmó metadatos operacionales todavía alcanzables en historia pública y recomienda **GO para una purga histórica selectiva y coordinada**. No encontró evidencia de plaintext credential que justifique rotación/revoke por sí sola. La purga todavía no se ejecutó ni verificó post-rewrite.

**Decisiones de seguridad de 2.2:**
- La limpieza de HEAD está cerrada; la deuda restante está en historia alcanzable.
- **Recomendación vigente:** ejecutar una purga histórica **selectiva**, no una reescritura indiscriminada. Requiere decisión WOZ/RO, write freeze, coordinación completa de refs/protecciones, ventana controlada y cleanup GitHub-side/Support cuando aplique.
- No se rota ni revoca ningún token por la evidencia histórica actual porque no se confirmó un token en claro comprometido. La revocación operativa sigue siendo capacidad obligatoria antes de escalar la flota hacia ~80 bots o ante compromiso confirmado.
- El HEAD actual debe contener únicamente plantillas sanitizadas; configuraciones reales/locales quedan fuera de Git.

**Dependencias:** decisión WOZ/RO + coordinación destructiva de historial.  
**Evidencia:** `PASS regression-http-containment`; HEAD sanitizado; handoff AAA WAVE 2 `GO targeted coordinated history purge` en Issue #41.  
**Gate de salida:** ninguna ruta mutante/carga opera sin identidad autenticada y el incidente tiene resolución explícita, incluida purga/decisión histórica y verificación posterior. **NO SATISFECHO; `[ 🟡 ]`.**

## Día 3 — 26 de agosto — Integración de ramas

**Resultado:** una rama protegida compila y conserva capacidades Web/Desktop.

### Tarea 3.1 [P1 · RO/DE/FE] — Construir la base integrada

- [x] Crear la rama protegida y fijar versión `0.8.0-alpha.1` desde Cloud `626efe933cb61130d5f7d20bcdd398f53b61d434`.
- [x] Portar Web por capacidades y resolver conflictos centrales conscientemente.
- [x] Eliminar backups/dumps/binlogs y contenido impropio del árbol público sin borrar evidencia necesaria del incidente.

**Evidencia 3.1:** rama `integration-v0.8.0-alpha.1`, versión `0.8.0-alpha.1`, rama protegida; CI #63 PASS Windows + macOS arm64/x86_64.

### Tarea 3.2 [P1 · QA] — Probar contrato de plataforma

- [x] Ejecutar typecheck, TS/DOM/integration/backend/regresiones en la convergencia.
- [x] Añadir test que asegura que Web no invoca comandos Tauri y Desktop conserva Direct/offline/YouTube.
- [x] Generar matriz de capacidades compartida como fuente única.

**Evidencia 3.2:** PR #8, commit `818214889ef3c6f97a262a91046f7df0e4f723fe`, merge `32a38c490a53650a0e9d6435c50cd009ef1b5123`; CI post-merge #65 PASS. `src/platform/capabilities.ts` es la matriz compartida y el guard DOM impide Tauri desde Web.

**Gate de salida:** `0.8.0-alpha.1` reproduce ambos conjuntos de funciones sin conflicto silenciado. **SATISFECHO.**

## Día 4 — 27 de agosto — Supply chain y CI requerido

**Resultado:** cada cambio relevante recibe un veredicto automático antes de merge.

### Tarea 4.1 [P2 · QA/OP] — Crear pipeline obligatorio

- [x] Web build + browser smoke; frontend/shared; backend; Rust; regresiones; portabilidad y packaging estático.
- [x] Fijar Node/Rust/actions; usar lockfiles; cachear sin ocultar checks.
- [x] Bloquear merge si falla una suite o si versiones/manifiestos divergen.

**Evidencia 4.1:** PR #9; `Required CI` agrega Web/shared, Windows, macOS arm64/x86_64; Node `22.23.2`, Rust `1.98.0`, Actions por SHA, npm/Cargo locked. Merge `c7894ad3c2b3e296e3d2939d73953b159e48852f`; post-merge #70 PASS 5/5.

**Gate de salida 4.1:** cualquier fallo requerido bloquea merge. **SATISFECHO.**

### Tarea 4.2 [P2 · BE/DE] — Cerrar supply chain conocida

- [x] Actualizar transitivas hasta cero critical/high o excepción temporal aprobada.
- [x] Añadir npm/Cargo advisories, license scan, secret scan, SBOM y checksums.
- [x] Verificar binarios Node/FFmpeg/Bot API por digest y registrar procedencia.

**Evidencia 4.2:** PR #10, head `902e4edf6f6f5d28f0f98922d5f22cc623c92f3d`; CI #100 PASS 6/6; artefacto `supply-chain-evidence` digest `sha256:d3b38c3be14ec01f0c283522049732a4e300588d8f0a9c588ec30221e0222419`; merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`.

**Gate de salida:** no existe bypass informal; cualquier excepción tiene owner, compensación y expiración. **SATISFECHO.**

## Día 5 — 28 de agosto — ADR de confianza y checkpoint de arquitectura

**Resultado:** diseño técnico aprobado para Web, Desktop, sesión y datos.

### Tarea 5.1 [P0 · BE/Security reviewer] — Aprobar límites de confianza

- [x] Sustituir credenciales Telegram en cliente por acceso temporal seguro sin romper el data plane directo.
- [x] Eliminar discovery inseguro de `127.0.0.1:4000`.
- [x] Vendorizar/localizar parser ID3; definir CSP, headers, CORS y scopes Tauri mínimos.

**Estado/evidencia 5.1 — APROBADO / SATISFECHO:**
- Frontera inmutable: media/proyectos viajan **dispositivo ↔ Telegram directamente**; Galer Cloud controla autorización/asignación pero no relaya bytes.
- M0-A..H probó bind split, identidad bot, renovación/recovery, **1,992,294,400 bytes** directos con `galer_cloud_file_bytes=0`, Windows, ambos macOS, Chrome/Web Worker, delete reciente/cross-bot, pool max-4/waitlist y expiración natural.
- Riesgos residuales aceptados por RO: shared-bot fallback cross-vault cuando no haya bots libres y cleanup físico cross-bot >48 h como deuda GC con INDEX como autoridad.
- PR #28 migró Web/Desktop productivos a temporary auth sin entregar permanent auth/token/API hash al cliente y cerró discovery/ID3/CSP/headers/CORS/scopes. Head `5119b3c6616b1a9c725bca1edad8e39036c4b463`; CI PR #226 PASS 6/6; merge `d9ae76f42faee3a7207b9232b7421a0bec20b090`; CI integrado #228 PASS 6/6.
- Aprobación RO explícita 2026-08-25; revisión independiente externa permanece como gate global de release.

**Gate de salida 5.1:** límites de confianza implementados, evidencia adversarial registrada, riesgos residuales aceptados por RO y código integrado verde. **SATISFECHO.**

### Tarea 5.2 [P0 · BE/OP] — Aprobar arquitectura de datos

- [ ⚠️ ] Aprobar persistencia transaccional durable con migrations, constraints, backup/restore y rollback. **Arquitectura aprobada; software integrado hasta PR #42; PostgreSQL es autoridad productiva; evidencia WAVE 3 4/4 reunida. Falta solo síntesis global WOZ/RO antes de `[x]`.**
- [ ⚠️ ] **DECISIÓN APROBADA:** PostgreSQL es autoridad durable del control-plane; el pinned Galer T-Library Schema v2 INDEX conserva la autoridad lógica de beats/trash/tombstones. **Autoridad PostgreSQL productiva + durabilidad tras restart verificadas.**
- [ ⚠️ ] Cifrado de secretos, migraciones, backup, RPO/RTO y rollback definidos/implementados. **Rollback readiness desde CURRENT PostgreSQL aceptado; restore PITR representativo real demuestra RPO ~7 min y RTO 3643 s, verificado independientemente por AAA.**
- [ ⚠️ ] Reconciliación INDEX/PG y garbage journal definidos/implementados; worker durable usa leases recuperables, `SKIP LOCKED`, retry/backoff y recovery adversarial. **No queda evidencia operativa pendiente dentro de los cuatro criterios WAVE 3.**

**Estado/evidencia 5.2 — LISTA PARA SÍNTESIS GLOBAL `[ ⚠️ ]`:**
- **Base integrada:** `integration-v0.8.0-alpha.1@a968122127c584b5557b25e70a21eb64f75b3c0e`. PRs #29–#42 integraron schema/migrations/envelope encryption/importer, garbage/reconciliation, runtime authority/cutover/rollback fail-closed, keyring multiversión, AWS Secrets Manager y base64 canónico con Required CI verde.
- **Criterio 1 — SATISFECHO:** PostgreSQL productivo sobrevivió terminación/restart controlado preservando marker READY, snapshot SHA, counts/fingerprints y volvió a servir solo tras el barrier fail-closed. `READ_ONLY_ROLLBACK_DRY_RUN` reconstruyó/validó rollback desde CURRENT PG sin escribir JSON, cambiar marker ni imprimir secretos. AAA lo aceptó independientemente.
- **Criterio 2 — SATISFECHO:** primer restore PITR aislado real desde production RDS probó funcionalidad representativa y RPO ~7 min <=15 min. Como el primer drill no capturó un `drill_start` confiable, WOZ ejecutó un segundo restore **solo para RTO**: `drill_start=2026-08-28 04:21:11 UTC`, `core_smoke_pass=2026-08-28 05:21:54 UTC`, **RTO=3643s = 1h00m43s <=7200s**. AAA re-revisó y marcó criterio 2 `SATISFIED`.
- **Criterio 3 — PASS / ACEPTADO POR WOZ:** rotación productiva multiversión N→N+1: key activa `2`, versiones `1,2` disponibles; servicio arrancó con v2; 3 filas productivas de provider permanecían cifradas con v1 y `loadAuthSnapshot` las descifró correctamente usando el keyring real con v2 activa. El primer intento con JSON secreto malformado falló cerrado y se recuperó antes del PASS. **No repetir rotación.**
- **Criterio 4 — PASS / ACEPTADO POR WOZ:** alarmas críticas RDS configuradas y enrutadas al path SNS confirmado; `on-call owner`, `rotation operator` y `rollback/abort authority` quedaron asignados durante la ventana. BBB había dejado su package review en `PENDING`, pero WOZ reconcilió explícitamente que ese estado no obliga a repetir mutaciones productivas y aceptó la evidencia directa para WAVE 3.
- **Backup retention observado:** 1 día por restricción/costo actual. Se registra como limitación operativa; no invalida el RPO/RTO medido de WAVE 3 ni debe presentarse como política final de producción si otro gate exige más retención.
- **Security follow-up:** durante troubleshooting de la rotación productiva se expuso un OAuth client secret en terminal visible al operador. No aparece en Issue #41; **debe rotarse separadamente antes de release**. No se convierte artificialmente en un quinto criterio WAVE 3.
- **No repetir:** cutover, import JSON, migrations, restart de durabilidad, restores o rotación ya demostrados, salvo nueva evidencia que invalide el resultado.
- **Deuda separada:** `legacy-exporter.js` usa consultas concurrentes sobre un único pg client y genera warning de compatibilidad futura con pg@9; registrar antes de upgrade mayor. Deuda GPL preexistente `telegram@2.26.22` → `@cryptography/aes@0.1.1` permanece fuera del gate técnico de 5.2 pero bloquea release hasta resolución/revisión.

**Dependencias:** contención terminada.  
**Evidencia:** ADR/threat model/migration plan + PRs #29–#42 + Required CI/recovery + Issue #41 WAVE 3: autoridad/restart/rollback dry-run, PITR/RPO, RTO final, rotación productiva, observabilidad/ownership y revisiones AAA/WOZ.  
**Gate de salida:** arquitectura aprobada, control-plane productivo durable y los cuatro criterios WAVE 3 satisfechos. **EVIDENCIA 4/4 DISPONIBLE; pendiente únicamente la síntesis global WOZ/RO. Estado `[ ⚠️ ]`; no marcar `[x]` hasta ese veredicto.**