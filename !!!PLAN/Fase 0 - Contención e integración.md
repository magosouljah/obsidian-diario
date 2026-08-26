# Fase 0 — Contener, decidir y crear una sola línea de release

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 22–28 de agosto  
**Objetivo:** eliminar ambigüedad, contener exposición y producir `0.8.0-alpha.1` desde una rama protegida.

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
- Backlog operativo: [BeatGaler Issue #3 — P0/P1 Launch Backlog](https://github.com/magosouljah/BeatGaler/issues/3).

**Dependencias:** ninguna.  
**Evidencia:** SHAs, auditorías, release ledger y backlog P0/P1.  
**Gate de salida:** alcance y regla “0 P0/P1” aceptados; nadie presenta el 4 de septiembre como fecha pública.

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
- **Monedas iniciales:** MXN, USD, CAD, EUR y GBP. La arquitectura podrá ampliar monedas después sin multiplicar lógica de producto.
- **Refund comercial base:** solicitud dentro de los primeros 14 días de la compra inicial, con controles antiabuso razonables y sin dificultar artificialmente el ejercicio de derechos; prevalecen los derechos obligatorios superiores de la jurisdicción aplicable.
- **Estructura inicial:** operar inicialmente desde México bajo la estructura fiscal/legal individual más simple que resulte válida (objetivo actual: persona física con actividad empresarial), sujeto a validación con contador/asesor antes de aceptar cobros reales. Crear una sociedad queda como decisión futura si aporta valor operativo, patrimonial, de inversión o contratación.
- **Impuestos:** todavía no se consideran implementados; cálculo, registro y obligaciones por mercado son gate de billing/legal antes de v1.
- **Distribución v1:** Web pública + instalador Windows `.exe` generado con NSIS + macOS DMG, distribuidos directamente por BeatGaler. Microsoft Store y Mac App Store quedan fuera de v1 salvo decisión posterior.

### Tarea 1.2 [P1 · RO/LF] — Reservar dependencias con lead time

- [ 🟡 ] Confirmar dominio y ownership de DNS, GitHub Releases, email de soporte y status page. **Estado:** no hay dominio todavía; GitHub Releases queda como canal previsto; email de soporte y status page se configuran después de adquirir el dominio.
- [ 🟡 ] Iniciar/confirmar Apple Developer ID, notarización y servicio/certificado Authenticode con timestamp. **Estado:** Apple Developer aún no está contratado y Authenticode sigue pendiente.
- [ 🟡 ] Reservar revisión legal, seguridad independiente, hardware físico y 12–20 testers. **Estado:** hay disponibilidad de testers; revisión legal/seguridad y la matriz física final siguen pendientes de reserva.

**Decisiones/estado de reservas de 1.2:**
- **Dominio/DNS:** pendiente. Prioridad externa inmediata junto con Apple Developer.
- **GitHub Releases:** se conserva como canal previsto de artefactos/release.
- **Email de soporte + status page:** pendientes del dominio definitivo.
- **Apple Developer:** pendiente de alta; necesario para Developer ID, notarización y stapling de macOS.
- **macOS soportado:** objetivo de v1 = **Apple Silicon + Intel**. Ambas arquitecturas deben pasar pruebas físicas antes de anunciar soporte.
- **Windows Authenticode:** pendiente de seleccionar/contratar servicio o certificado con timestamp.
- **Testers:** disponibilidad humana confirmada; la selección formal de 12–20 y su cobertura por plataforma/dispositivo se hará antes de beta.
- **Legal y seguridad independiente:** pendientes de reservar; no se consideran completadas por revisión interna.

**Dependencias:** Día 0.  
**Evidencia:** decision log y comprobantes de disponibilidad, nunca secretos.  
**Gate de salida:** ninguna decisión de alcance crítica queda sin owner/fecha; si falta firma de OS, se activa fecha conservadora.

## Día 2 — 25 de agosto — Contención de seguridad e incidente

**Resultado:** superficies de mayor riesgo cerradas a tráfico público.

### Tarea 2.1 [P0 · BE/OP] — Retirar exposición inmediata

- [x] Deshabilitar o autenticar antes de Multer todas las rutas legacy de media/metadata.
- [x] Limitar cuerpo, archivo, concurrencia y frecuencia en edge y aplicación.
- [x] Desactivar registro público hasta tener abuse controls y verificación.

**Estado técnico de 2.1:**
- Se añadió `cloud-server/http-containment.js` y `cloud-server/server.js` quedó como bootstrap de seguridad; la lógica previa completa se preserva sin modificación en `cloud-server/server-core.js`.
- `/metadata/artwork`, `/beats/upload`, `/projects/upload` y `/cloud-files/upload` exigen una sesión válida **antes** de ejecutar Multer. Después del multipart se verifica ownership server-side de la instalación y se rechaza un `beatgalerUserId` contradictorio.
- `/metadata/upsert` y `/library/artwork` reciben el mismo gate; `/library/upsert` responde `410` antes de Multer.
- Máximo técnico por archivo: **1.99 GB decimal = 1,990,000,000 bytes**, validado anticipadamente cuando sea posible y por tamaño real tras multipart.
- Rate limit/concurrencia antes de recibir archivos; defaults: 30 intentos de upload/minuto por sesión y 2 uploads concurrentes, configurables.
- En `NODE_ENV=production`, `/auth/register` queda cerrado salvo `BEATGALER_PUBLIC_REGISTRATION=1`.
- Evidencia runtime: `npm run test:containment` produjo **`PASS regression-http-containment`**.

### Tarea 2.2 [P0 · BE/RO] — Tratar el estado rastreado como incidente potencial

- [x] Determinar en privado si IDs/bots/vaults son reales, sintéticos o revocados. **Resultado:** se encontró información operacional concreta; se trata como potencialmente real.
- [ 🟡 ] Retirar del HEAD la información operacional y mantener configuración real fuera de Git. **Hecho:** se eliminaron `transport-pool-state.backup.json`, `transport-bots.json` y `transport-bots.local.json`; el backend usa configuración privada o `TRANSPORT_BOTS_FILE`; `transport-bots.example.json` quedó sanitizado.
- [ 🟡 ] Revisar de nuevo la exposición del historial Git en unos días y decidir si amerita purga. No se añade scanner permanente por ahora; la historia antigua no se declara limpia hasta esa revisión.

**Decisiones de seguridad de 2.2:**
- No se rota ni revoca ningún token por esta limpieza del HEAD porque no se confirmó un token en claro comprometido.
- La **revocación sí será una capacidad de seguridad obligatoria**, pero su implementación/operación completa se incorpora antes de escalar la flota hacia ~80 bots; puede adelantarse si aparece evidencia de credencial comprometida.
- El HEAD actual debe contener únicamente plantillas sanitizadas; configuraciones reales/locales quedan ignoradas por Git.

**Dependencias:** acceso de owners a infraestructura.  
**Evidencia:** `PASS regression-http-containment`; diff Cloud hasta `626efe933cb61130d5f7d20bcdd398f53b61d434`; revisión futura del historial sin reproducir identificadores.  
**Gate de salida:** ninguna ruta mutante/carga opera sin identidad autenticada y el incidente tiene resolución explícita, incluida decisión sobre el historial antiguo.

## Día 3 — 26 de agosto — Integración de ramas

**Resultado:** una rama protegida compila y conserva capacidades Web/Desktop.

### Tarea 3.1 [P1 · RO/DE/FE] — Construir la base integrada

- [x] Crear la rama protegida y fijar versión `0.8.0-alpha.1`. La base real usada fue Cloud `626efe933cb61130d5f7d20bcdd398f53b61d434`.
- [x] Portar Web por capacidades; resolver App, Drawer, library state y test de integración conscientemente.
- [x] Eliminar backups/dumps/binlogs y contenido impropio del árbol público sin borrar evidencia necesaria del incidente.

**Evidencia 3.1:** rama `integration-v0.8.0-alpha.1`, HEAD previo `4662a109bcc769774e33fe53182088c605846002`, versión `0.8.0-alpha.1`, GitHub `protected: true`, PR #4 y CI `Test - Desktop Portability` run #63 PASS en Windows, macOS arm64 y macOS x86_64.

### Tarea 3.2 [P1 · QA] — Probar contrato de plataforma

- [x] Ejecutar typecheck, TS/DOM/integration/backend/regresiones en la convergencia.
- [x] Añadir test que asegura que Web no invoca comandos Tauri y Desktop conserva Direct/offline/YouTube.
- [x] Generar matriz de capacidades compartida como fuente única.

**Evidencia 3.2:**
- `src/platform/capabilities.ts` es la matriz compartida y ahora incluye `youtubePublishing`.
- `tests/unit/platformCapabilities.test.ts` queda realmente ejecutado por `scripts/run-unit-tests.mjs`.
- Nuevo guard DOM: si un flujo del adaptador Web intenta invocar Tauri, la prueba falla.
- Desktop queda protegido explícitamente para Direct, Offline y YouTube.
- Web mantiene Direct/Offline/YouTube en `false` **como estado actual**, no como regla permanente de producto. YouTube Web es objetivo obligatorio y está planificado en Tarea 15.3.
- PR BeatGaler #8 `test(platform): enforce 3.2 Web/Desktop contract`.
- Commit de trabajo `818214889ef3c6f97a262a91046f7df0e4f723fe`.
- CI PR `Test - Desktop Portability` run #64 PASS en Windows, macOS arm64 y macOS x86_64.
- PR #8 mergeado en `integration-v0.8.0-alpha.1`; merge commit `32a38c490a53650a0e9d6435c50cd009ef1b5123`.
- CI post-merge run #65 PASS en Windows, macOS arm64 y macOS x86_64 antes de marcar esta tarea `[x]`.
- Ruleset: `Required approvals = 0` porque existe un solo maintainer; se mantienen PR + CI/checks. Esto no sustituye reviewers externos requeridos por gates posteriores de seguridad/legal/firma.

**Dependencias:** Días 1–2 y working tree limpio.  
**Gate de salida:** `0.8.0-alpha.1` reproduce ambos conjuntos de funciones sin conflicto silenciado. **SATISFECHO.**

## Día 4 — 27 de agosto — Supply chain y CI requerido

**Resultado:** cada cambio relevante recibe un veredicto automático antes de merge.

### Tarea 4.1 [P2 · QA/OP] — Crear pipeline obligatorio

- [x] Web build + browser smoke; frontend/shared; backend; Rust; regresiones; portabilidad y packaging estático.
- [x] Fijar Node/Rust/actions; usar lockfiles; cachear sin ocultar checks.
- [x] Bloquear merge si falla una suite o si versiones/manifiestos divergen.

**Evidencia 4.1:**
- `Test - Desktop Portability` incorpora `Web + shared gate`, Windows, macOS arm64, macOS x86_64 y un agregador estable `Required CI`.
- Web ejecuta build real (`tsc + vite build --mode web`) y smoke de la app compilada en Chrome headless; el target Web se alinea a ES2020 por el uso real de `BigInt`, sin alterar los targets Desktop.
- El gate shared ejecuta `version:check`, typecheck, unit TS, DOM, integration, backend, regresiones y packaging/portabilidad estático.
- Node queda fijado en `22.23.2`; Rust en `1.98.0`; Actions relevantes quedan fijadas por SHA completo; npm usa `npm ci` y Cargo usa `--locked`.
- Windows falla cerrado si `Cargo.lock` se regenera y conserva el artefacto de diagnóstico; macOS conserva sus guards/placeholder ordering y compila el grafo locked en ambas arquitecturas.
- El workflow corre en PR y también en push a `integration-v0.8.0-alpha.1`.
- PR BeatGaler #9 `ci: enforce Task 4.1 required pipeline`.
- Commits de trabajo: `e86ab19a7f3eef3a7036a50f8cb083add94c2292`, `a4f58943f222ef8f6a5c85a3e72142353fdf0a72` y `71a559dc4cdcb8e16159c709a7c2d0f64e61e5a0`.
- CI PR run #68 PASS 5/5: Web/shared, Windows, macOS arm64, macOS x86_64 y `Required CI`.
- PR #9 mergeado en `integration-v0.8.0-alpha.1`; merge commit `c7894ad3c2b3e296e3d2939d73953b159e48852f`.
- CI post-merge run #70 PASS 5/5, incluido `Required CI`.
- Ruleset confirmado: PR obligatorio, `Required CI` como único status check requerido, rama actualizada antes de merge y `Required approvals = 0` por existir un solo maintainer.

**Gate de salida 4.1:** cualquier fallo de Web/shared, Windows o cualquiera de los dos Mac hace fallar `Required CI`, y GitHub bloquea el merge. **SATISFECHO.**

### Tarea 4.2 [P2 · BE/DE] — Cerrar supply chain conocida

- [x] Actualizar Vitest/Vite/WebdriverIO/transitivas hasta cero critical/high o excepción temporal aprobada y fechada.
- [x] Añadir npm/Cargo advisories, license scan, secret scan, SBOM y checksums.
- [x] Verificar binarios Node/FFmpeg/Bot API por digest y registrar procedencia.

**Evidencia 4.2:**
- PR BeatGaler #10 `security: enforce Task 4.2 supply chain gate`; head final `902e4edf6f6f5d28f0f98922d5f22cc623c92f3d`.
- Dependencias frontend/test actualizadas y `npm audit --audit-level=high` pasa sin critical/high; RustSec `cargo audit` pasa; licencias npm/Cargo se verifican por scripts dedicados.
- Gitleaks `8.30.1` se ejecuta HEAD-only con binario descargado y checksum fijado; no quedan hallazgos en el gate final.
- `cargo-cyclonedx 0.5.9` y `npm sbom` generan SBOM CycloneDX; el artefacto `supply-chain-evidence` incluye reportes, SBOMs, checksums de lockfiles y `runtime-sources.json`.
- Actions externas de CI/build/release quedan verificadas por SHA completo; Node, FFmpeg y Bot API registran fuente/pin y verificaciones de digest en los workflows correspondientes.
- CI PR run #100 (`32702389575`) PASS 6/6: Web/shared, Supply chain, Windows, macOS arm64, macOS x86_64 y `Required CI`.
- Artefacto `supply-chain-evidence` id `9511091432`, digest `sha256:d3b38c3be14ec01f0c283522049732a4e300588d8f0a9c588ec30221e0222419`.
- PR #10 mergeado en `integration-v0.8.0-alpha.1`; merge commit `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`.
- El merge sintético aprobado por CI (`2eb539e40d1f076ae8f9c6dcec1a6762ae8ca5e1`) y el merge real comparten exactamente el árbol `9a7000f3f3a1840ebae0310ac3df6b827561f2c5`, por lo que el contenido integrado es el mismo que pasó los gates.

**Dependencias:** rama integrada.  
**Evidencia:** required checks en PR de prueba, reportes fechados y SBOM.  
**Gate de salida:** no existe bypass informal; cualquier excepción tiene owner, compensación y expiración. **SATISFECHO; no se usó excepción temporal.**

## Día 5 — 28 de agosto — ADR de confianza y checkpoint de arquitectura

**Resultado:** diseño técnico aprobado para Web, Desktop, sesión y datos.

### Tarea 5.1 [P0 · BE/Security reviewer] — Aprobar límites de confianza

- [x] Sustituir credenciales Telegram en cliente por acceso temporal seguro sin romper el data plane directo.
- [x] Eliminar discovery inseguro de `127.0.0.1:4000`; fijar origen remoto o autenticar criptográficamente el servicio local.
- [x] Vendorizar/localizar parser ID3; definir CSP, headers, CORS, cookie/CSRF y scopes Tauri mínimos.

**Estado/evidencia 5.1 — APROBADO / SATISFECHO:**
- Frontera inmutable conservada: **MP3/WAV/artwork/samples/PROJECT ZIP viajan dispositivo ↔ Telegram directamente; Galer Cloud controla autorización/asignación pero nunca transporta esos bytes como relay.**
- M0-A..H probaron incrementalmente la frontera criptográfica, bind split, identidad bot, renovación/recovery, transferencia directa de **1,992,294,400 bytes** con `galer_cloud_file_bytes=0`, Windows x86_64, macOS arm64/x86_64, Chrome + Web Worker real, delete reciente/cross-bot, pool/admission max-4 y expiración natural/server-side. El historial detallado queda preservado en `Registro de avances.md` y en PRs #11–#27.
- Decisión RO preservada: temporary auth representa la identidad completa del transport bot y no se asume scope criptográfico por vault. Se prefiere exclusividad mientras haya bots libres; shared-bot solo cuando no haya bots libres, con reparto justo, máximo 4 vaults activos/bot, waitlist y observabilidad. El RO acepta el riesgo residual cross-vault de ese fallback.
- Delete físico cross-bot >48 h puede devolver `MESSAGE_DELETE_FORBIDDEN`; queda aceptado como deuda futura de GC. INDEX es autoridad y el cleanup físico es post-commit/oportunista; la reconciliación durable/garbage journal corresponde a Tarea 5.2.
- PR #28 `feat(security): migrate productive Direct Web auth to temporary keys`, rama `task-5.1-productive-temp-auth-migration`, head probado `5119b3c6616b1a9c725bca1edad8e39036c4b463`: Web/Desktop productivos dejan de recibir `bot_token`, `telegram_api_id`, `telegram_api_hash` o permanent auth del transport bot; permanent auth queda control-side; Web/Worker y Desktop helper usan temporary auth; renovación/refresh es fail-closed y la inicialización de permanent bot auth se serializa.
- Hardening productivo de #28: no queda discovery productivo de `127.0.0.1:4000` ni origen recordado arbitrario; ID3 de navegador es local y el guard inspecciona `dist` para impedir regreso de jsDelivr; CSP/headers de seguridad quedan activos; CORS usa allowlist explícita y bearer sin cookies/`Access-Control-Allow-Credentials`; scopes FS Tauri se reducen a los flujos usados.
- Evidencia de rama: compile probe #32 (`32909324459`) PASS; CI PR #226 (`32909324476`) **PASS 6/6**, incluido `Required CI`.
- **Aprobación RO 2026-08-25:** el Release Owner aprobó explícitamente Tarea 5.1 y aceptó los riesgos residuales documentados.
- PR #28 fue mergeado en `integration-v0.8.0-alpha.1` como `d9ae76f42faee3a7207b9232b7421a0bec20b090`.
- Evidencia integrada final: CI #228 (`32912362077`) sobre el SHA integrado terminó **PASS 6/6**: Web/shared, Supply chain, Windows, macOS arm64, macOS x86_64 y `Required CI`.
- La revisión independiente externa **no** se declara satisfecha por esta aprobación interna. Permanece pendiente como gate global de seguridad/release según `Gates - Publicación y contingencias.md` y Tarea 1.2.

**Dependencias:** contención terminada.  
**Evidencia:** ADR/threat model/rollback + PRs/probes M0 + implementación productiva #28 + aprobación RO + CI integrado.  
**Gate de salida 5.1:** límites de confianza implementados, evidencia adversarial registrada, riesgos residuales aceptados por RO y código integrado con `Required CI` verde. **SATISFECHO.**

### Tarea 5.2 [P0 · BE/OP] — Aprobar arquitectura de datos

- [ 🟡 ] Aprobar una persistencia transaccional durable con migrations, constraints, backup/restore y rollback como requisito de producción. **Arquitectura aprobada por RO el 25 de agosto de 2026; cutover software controlado/default-off y worker durable ya integrados hasta PR #36; faltan cutover productivo y evidencia de infraestructura real.**
- [ 🟡 ] **DECISIÓN APROBADA:** PostgreSQL será la autoridad durable del control-plane para cuentas, sesiones, providers, MFA, entitlements, vault metadata, Direct leases/operations, jobs, auditoría, garbage journal e INDEX observations/reconciliation. El INDEX fijado conserva la autoridad lógica de beats, trash y tombstones; PostgreSQL nunca se convierte en manifest authority de la biblioteca.
- [ 🟡 ] Definir cifrado de secretos, migraciones, backup, RPO/RTO propuestos y rollback. **Definido e implementado en software/CI:** envelope encryption AES-256-GCM para secretos recuperables; KEK/master debe quedar fuera de PostgreSQL en KMS/Secret Manager real; objetivo RPO <=15 min y RTO <=2 h; importador idempotente, cutover marker y exporter rollback post-write existen. **Pendiente:** KMS real, PITR/WAL/retención y RPO/RTO productivos.
- [ 🟡 ] Definir reconciliación Telegram/index y garbage journal. **Definido e implementado en software/CI:** INDEX gana; PG stale se repara hacia INDEX; missing referenced object alerta sin reescribir verdad; unreferenced object pasa a orphan candidate tras safety window; cleanup físico es post-commit durable; `MESSAGE_DELETE_FORBIDDEN` nunca revierte INDEX ni resucita contenido; PR #36 añadió worker runtime durable con leases recuperables, `SKIP LOCKED`, retry/backoff y adversarial crash-after-external-effect sobre PostgreSQL real. **Pendiente solo evidencia/operación productiva correspondiente, no el worker software.**

**Estado/evidencia 5.2 — EN PROGRESO:**
- PR #29 integró ADR, threat model y plan de migration/rollback. PR #30 añadió schema PostgreSQL del control-plane, constraints y migration contract. PR #31 añadió migration runner, configuración PostgreSQL fail-closed y secret envelope AES-256-GCM. PR #32 añadió importador legacy idempotente, garbage journal repository y compatibilidad de auth. PR #33 añadió `pg@8.23.0`, bootstrap opt-in fail-closed y PostgreSQL 16 dentro de `Required CI`; durante #33 se detectó un race real de dos primeros arranques creando `schema_migrations` y se corrigió tomando el advisory lock antes de crear/verificar el ledger. PR #33 merge `1c5127b30ec7ee11e65d82100bae7fc33a2aeb52`; post-merge #254 PASS completo.
- PR #34 añadió durable Direct operation repository, idempotency + monotonic saga transitions, reconciliación pinned INDEX → PostgreSQL, orphan discovery conservador tras safety window, exporter PostgreSQL → legacy-compatible para rollback después de writes, crash-after-external-effect tests, conservación de writes post-migración y recovery real en CI con dos PostgreSQL 16 aislados. El drill hace dump → cifrado temporal → restore en segunda instancia y verifica constraints, secretos, INDEX observation, garbage debt y rollback. Pre-merge #255 PASS completo; artefacto `postgres-recovery-evidence` digest `sha256:09622af6bd0d663b328ce28cb2955245db9fd995d93428e9a2fdeeb3a8c07df1`. El restore verifier observó ~40 ms en el dataset pequeño de CI; **no representa RTO/RPO productivos**.
- PR #34 fue mergeado como `27ccdcbf41bbce0265730754cc2ff32fd32dc140`. CI post-merge #256 (`32946267360`) terminó PASS completo y el probe #55 (`32946271700`) PASS. La auditoría posterior detectó que PostgreSQL aún no era authority runtime: `server-core.js` seguía operando sobre `accounts-data.json`/`cloud-data.json`.
- **PR #35 cerró ese hueco de software:** `BEATGALER_CONTROL_PLANE_AUTHORITY=json|postgres` es explícito y default `json`; PG authority requiere PG enabled + snapshot SHA exacto; en producción falla cerrado mientras no exista KMS/Secret Manager real. El runtime PostgreSQL carga/persiste users, sessions, providers/OAuth, MFA, entitlements, vault metadata y compat state; los JSON legacy quedan virtualizados solo en modo PG, sin disk dual-write; una durability barrier impide acknowledgement antes de que la persistencia PG termine. Migration `0003_control_plane_cutover.sql` añade metadata de cutover/compatibilidad sin tablas de beats/trash/deleted authority.
- Cutover/rollback #35: parse/validate/dry-run antes de mutar; manifest SHA256 exacto de los JSON raw; import determinista e idempotente; round-trip validation; READY marker solo después de validación; rollback ciego a JSON rechazado mientras PG está READY; el rollback exporta el **estado PostgreSQL actual** y por tanto conserva writes post-cutover; JSON solo puede reactivarse si coincide exactamente con el digest comprometido del rollback export. OAuth/MFA hacen round-trip cifrado; stale sessions/providers/MFA/entitlements se eliminan autoritativamente.
- Durante CI de #35 se encontraron y corrigieron dos causas reales sin rebajar gates: (1) el test aislado hacía `DROP DATABASE ... WITH (FORCE)` y provocaba un `57P01` tardío después de que las assertions hubieran pasado; se retiró ese cleanup destructivo porque la DB vive solo en el servicio CI efímero; (2) el restore verifier heredado esperaba migrations `0001/0002` y se actualizó a `0001/0002/0003`, ya que el restore contenía correctamente la nueva migration.
- Head final pre-merge #35 `5a567ca57e677f023f5e2343436c9e2f42369314`. CI pre-merge #263 (`32998574256`) PASS completo: PostgreSQL live/recovery, Supply Chain, Web/shared, Windows, macOS arm64/x86_64 y `Required CI`; probe #61 (`32998574221`) PASS.
- PR #35 mergeado como `d98181582a37a7c7a15ca7c1c047faac7ded6d63`. CI push post-merge #264 (`32999292323`) PASS completo; CI PR de integración #265 (`32999298396`) PASS; probe post-merge #62 (`32999298425`) PASS sobre el mismo SHA. Artefacto `postgres-recovery-evidence` id `9617859760`, digest `sha256:63b1acc4dc9caaaf35a3f36f471102a5a57d3569d7e5ee54a004726a37f1c4a6`.
- **PR #36 cerró el hueco restante de garbage/reconciliation runtime:** worker durable con reclamación de leases usando `FOR UPDATE SKIP LOCKED`, retry/backoff persistente, errores sanitizados, reconciliación idempotente pinned INDEX→PG y cleanup físico mediante callback inyectable para no acoplar esta capa al transporte Direct. El test PostgreSQL adversarial prueba que, si el efecto externo ocurre y el proceso cae antes de marcar `done`, otro worker recupera al vencer el lease y tratar “objeto ya ausente” como éxito idempotente; INDEX/tombstones no se reescriben ni se resucitan.
- Evidencia #36: head pre-merge `97ff8a5ab85dd49905faf2dae32baa4ca41bc893`; CI PR #266 (`33001989737`) PASS completo incluido PostgreSQL live/recovery y `Required CI`; probe #63 (`33001989631`) PASS. Merge `97c120f7605c36d0862407d9d53c821262ce1a64`; CI push post-merge #267 (`33002946139`) PASS completo incluido `Required CI`; probe #64 (`33002953220`) PASS sobre el mismo SHA. Artefacto `postgres-recovery-evidence` id `9619336011`, digest `sha256:dc4587dfc4c634145594fddbaf01eba4e70fad2da37cbb81e8219ff210fc0cbc`.
- Deuda supply-chain preexistente permanece visible: `telegram@2.26.22` → `@cryptography/aes@0.1.1` → GPL-3.0-or-later. No se aprobó GPL globalmente y esta deuda no fue introducida por PostgreSQL.
- No se tocó la frontera 5.1: MP3/WAV/artwork/samples/PROJECT ZIP siguen dispositivo ↔ Telegram directo y cualquier regresión debe conservar `galer_cloud_file_bytes=0`. Tampoco se cambia token rotation/revoke sin necesidad explícita de seguridad.
- **Pendiente antes de cerrar 5.2:** proveedor PostgreSQL productivo y KMS/Secret Manager real; backups cifrados, WAL/PITR y retención; restore independiente que demuestre RPO <=15 min/RTO <=2 h; mecánica final de cutover productivo con snapshot externo inmutable, quarantine, write freeze/delta final/switch y rollback real; evidencia stolen-DB/backup-sin-KMS y key rotation. **5.2 permanece `[ 🟡 ]`; NO-GO.**

**Dependencias:** contención terminada.  
**Evidencia:** ADR/threat model/migration plan + PRs #29–#36 + CI PostgreSQL real/recovery + cutover/rollback software + worker durable/adversarial + post-merge integrado verde.  
**Gate de salida:** arquitectura aprobada, control-plane operando realmente sobre persistencia durable, migración/restore/rollback demostrados y evidencia productiva de backup/RPO/RTO conforme a `Gates - Publicación y contingencias.md`. **NO SATISFECHO todavía; no marcar `[x]`.**