# Fase 0 — Contener, decidir y crear una sola línea de release

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 22–28 de agosto  
**Objetivo:** eliminar ambigüedad, contener exposición y producir `0.8.0-alpha.1` desde una rama protegida.

## Ejecución multi-cuenta durante Fase 0

Desde el 27 de agosto de 2026 el equipo operativo se divide en **cuatro roles** según `Equipo multi-IA - Roles y coordinación.md`: `JOBS` es dueño de `!!!PLAN` y coordinador normal de AAA/BBB; `WOZ` es jefe técnico e integrador; `AAA` y `BBB` son ayudantes ejecutores. JOBS mantiene el plan limpio, detecta desincronización, consulta Issue #41, asigna/reasigna automáticamente trabajo independiente a AAA/BBB y entrega a WOZ el siguiente frente técnico permitido. JOBS no modifica BeatGaler ni infraestructura; sus únicas escrituras de archivos de repositorio son dentro de `!!!PLAN`.

WOZ conserva la autoridad técnica: arquitectura, decisiones de implementación, código, infraestructura, aceptación/rechazo de findings e integración. AAA/BBB no cambian gates ni marcan `[x]`; entregan evidencia/handoff. BeatGaler Issue #41 es el `AI Coordination Inbox` para asignaciones, blockers y handoffs entre cuentas.

En la situación actual, la **Tarea 5.2 sigue siendo el frente técnico principal** y Tareas 1.2/2.2 continúan como trabajo paralelo autorizado. Dentro de 5.2 pueden separarse subtracks externos independientes sin fingir que auditorías o preparación software sustituyen la evidencia productiva real exigida por el gate. Las asignaciones transitorias de cada oleada viven en Issue #41, no se duplican aquí salvo que cambien estado, evidencia o un gate.

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
- [ 🟡 ] Iniciar/confirmar Apple Developer ID, notarización y servicio/certificado Authenticode con timestamp. **Estado:** **Apple Developer = `PENDING — DEFERRED`**; Authenticode sigue pendiente.
- [ 🟡 ] Reservar revisión legal, seguridad independiente, hardware físico y 12–20 testers. **Estado:** hay disponibilidad de testers; revisión legal/seguridad y la matriz física final siguen pendientes de reserva.

**Decisiones/estado de reservas de 1.2:**
- **Dominio/DNS:** pendiente. Prioridad externa inmediata.
- **GitHub Releases:** se conserva como canal previsto de artefactos/release.
- **Email de soporte + status page:** pendientes del dominio definitivo.
- **Apple Developer:** **`PENDING — DEFERRED`**. Sigue requerido para Developer ID, notarización y stapling de macOS, pero no es un frente activo de WAVE 3 y se retomará cuando corresponda a su gate de firma/notarización.
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
- Delete físico cross-bot >48 h puede devolver `MESSAGE_DELETE_FORBIDDEN`; queda aceptado como deuda futura de GC. INDEX es autoridad y el cleanup físico es post-commit/oportunista; un fallo no revierte INDEX ni revive assets viejos.
- PR #28 `feat(security): migrate productive Direct Web auth to temporary keys`, rama `task-5.1-productive-temp-auth-migration`, head probado `5119b3c6616b1a9c725bca1edad8e39036c4b463`: Web/Desktop productivos dejan de recibir `bot_token`, `telegram_api_id`, `telegram_api_hash` o permanent auth del transport bot al cliente. Permanent auth queda control-side; Web/Worker y Desktop helper usan temporary auth; renovación/refresh es fail-closed y la inicialización de permanent bot auth se serializa.
- Hardening productivo de #28: no queda discovery productivo de `127.0.0.1:4000` ni origins arbitrarios recordados; ID3 de navegador es local y el guard inspecciona `dist` para impedir regreso de jsDelivr; CSP/headers de seguridad quedan activos; CORS usa allowlist explícita y bearer sin cookies/`Access-Control-Allow-Credentials`; scopes FS Tauri se reducen a los flujos usados.
- Evidencia de rama: compile probe #32 (`32909324459`) PASS; CI PR #226 (`32909324476`) **PASS 6/6**, incluido `Required CI`.
- **Aprobación RO 2026-08-25:** el Release Owner aprobó explícitamente Tarea 5.1 y aceptó los riesgos residuales documentados.
- PR #28 fue mergeado en `integration-v0.8.0-alpha.1` como `d9ae76f42faee3a7207b9232b7421a0bec20b090`.
- Evidencia integrada final: CI #228 (`32912362077`) sobre el SHA integrado terminó **PASS 6/6**: Web/shared, Supply chain, Windows, macOS arm64, macOS x86_64 y `Required CI`.
- La revisión independiente externa **no** se declara satisfecha por esta aprobación interna. Permanece pendiente como gate global de seguridad/release según `Gates - Publicación y contingencias.md` y Tarea 1.2.

**Dependencias:** contención terminada.  
**Evidencia:** ADR/threat model/rollback + PRs/probes M0 + implementación productiva #28 + aprobación RO + CI integrado.  
**Gate de salida 5.1:** límites de confianza implementados, evidencia adversarial registrada, riesgos residuales aceptados por RO y código integrado con `Required CI` verde. **SATISFECHO.**

### Tarea 5.2 [P0 · BE/OP] — Aprobar arquitectura de datos

- [ 🟡 ] Aprobar una persistencia transaccional durable con migrations, constraints, backup/restore y rollback como requisito de producción. **Arquitectura aprobada; software integrado hasta PR #42; PostgreSQL ya es autoridad productiva. WAVE 3 congeló cuatro criterios de salida y el criterio 1 — aceptación independiente de durabilidad/rollback actual — ya fue satisfecho por AAA. 5.2 continúa `[ 🟡 ] / NO-GO` por los criterios 2–4.**
- [ 🟡 ] **DECISIÓN APROBADA:** PostgreSQL será la autoridad durable del control-plane para cuentas, sesiones, providers, MFA, entitlements, vault metadata, Direct leases/operations, jobs, auditoría, garbage journal e INDEX observations/reconciliation. El INDEX fijado conserva la autoridad lógica de beats, trash y tombstones; PostgreSQL nunca se convierte en manifest authority de la biblioteca. **Estado productivo WAVE 3: autoridad PostgreSQL activa y durabilidad tras restart verificada/aceptada.**
- [ 🟡 ] Definir cifrado de secretos, migraciones, backup, RPO/RTO propuestos y rollback. **Definido e implementado en software/CI.** AAA aceptó independientemente el rollback readiness/dry-run desde CURRENT PostgreSQL. **Pendiente:** restore independiente representativo con RPO/RTO medidos y rotación productiva multiversión; BBB confirma que esta última no requiere más código antes de ejecución productiva.
- [ 🟡 ] Definir reconciliación Telegram/index y garbage journal. **Definido e implementado en software/CI:** INDEX gana; PG stale se repara hacia INDEX; missing referenced object alerta sin reescribir verdad; unreferenced object pasa a orphan candidate tras safety window; cleanup físico es post-commit durable; `MESSAGE_DELETE_FORBIDDEN` nunca revierte INDEX ni resucita contenido; worker durable usa leases recuperables, `SKIP LOCKED`, retry/backoff y recovery crash-after-external-effect. **Pendiente solo la evidencia operativa incluida en criterios 2–4.**

**Estado/evidencia 5.2 — EN PROGRESO:**
- **WAVE 3 — estado productivo confirmado:** `integration-v0.8.0-alpha.1@a968122127c584b5557b25e70a21eb64f75b3c0e`; PostgreSQL ya es autoridad productiva; el estado del control-plane sobrevivió restart controlado y el proceso reiniciado pasó el barrier PostgreSQL fail-closed antes de servir.
- **Rollback actual:** WOZ ejecutó `READ_ONLY_ROLLBACK_DRY_RUN` desde CURRENT PostgreSQL sin escribir JSON, cambiar `control_plane_cutovers` ni imprimir secretos. **AAA revisó independientemente contrato + evidencia runtime y lo aceptó como rollback readiness/dry-run; criterio 1 WAVE 3 SATISFECHO.** No se exige repetir restart/cutover/import/migrations por esta revisión.
- **BBB WAVE 3 DONE:** confirmó que keyring multiversión, provider fail-closed y rotación transaccional están integrados/verde y que no existe un gap software que justifique nueva rama. Lo pendiente es evidencia productiva + ownership: alarm routing, `on-call owner`, `rotation operator`, `rollback authority`, pre/post aggregate key-version counts, smoke de provider, una rotación N→N+1 con N retenida, post-smoke/round-trip y aprobación posterior antes de retirar N.
- **Marco congelado de cuatro criterios:** **(1) SATISFECHO — aceptación independiente rollback/durabilidad.** **Abiertos:** **(2)** restore independiente representativo con RPO <=15 min/RTO <=2 h; **(3)** rotación productiva multiversión; **(4)** observabilidad + alertas + on-call + rollback authority. **No añadir criterios nuevos dentro de 5.2 sin nueva decisión explícita de WOZ/RO.**
- **No repetir:** cutover, import JSON, migrations ni restart de durabilidad ya demostrados. El reload/restart específico del lifecycle de claves que el runbook requiera después de una rotación no cuenta como repetición del test de durabilidad; debe justificarse exclusivamente por la rotación.
- PRs #29–#36 construyeron e integraron ADR/threat model/migration plan, schema PostgreSQL + constraints, migrations, envelope encryption, importador legacy idempotente, garbage journal, `pg@8.23.0`, bootstrap fail-closed, PostgreSQL 16 real en Required CI, durable Direct operations, reconciliación pinned INDEX→PG, orphan discovery, rollback exporter, recovery drill, autoridad runtime `json|postgres` default-off, durability barrier y worker durable de garbage/reconciliación. Merge #36 `97c120f7605c36d0862407d9d53c821262ce1a64`; post-merge #267 PASS y probe #64 PASS.
- **PR #37 cerró la mecánica final de cutover software:** migration `0004`, ledger durable `control_plane_cutover_stages`, bundles sellados, quarantine, final-delta stale rejection, binding a digest externo y READY atómico. Merge `edad9e324132fa086ef729ef4faec574661578a9`; CI post-merge #272 PASS; recovery artifact digest `sha256:8a7eb2ad2010da256a296ce66aa18f33e4d40153fda278a92da8d48fdc680e53`.
- **PR #38 se cerró sin merge por quedar supersedido por #37.**
- **PR #39 cerró adversariales software-only de secret-at-rest/key rotation:** keyring versionado + `rotateStoredControlPlaneSecrets`; restore aislado prueba ciphertext, wrong/missing key fail-closed, v7→v8 y rollback atómico. Merge `1a5cc387aef431cd5f5115ad537f55e80856fb08`; post-merge #274 PASS; recovery artifact digest `sha256:0053159a8e21be62e62e72a6996b5ca7baf97ee857db7655d4f827ecd99fc93c`.
- **PR #40 preparó frontera productiva AWS Secrets Manager:** `development|aws-secrets-manager`, `AWSCURRENT`, payload versionado, fail-closed, keyring multiversión. Merge `f997415c794c74ee1b86ef593476dba3587eeca1`; post-merge #285 PASS; probe #78 PASS.
- **PR #42 cerró base64 permisivo:** round-trip canónico, 32 bytes exactos y negativos de caracteres/padding/trailing data. Merge `a968122127c584b5557b25e70a21eb64f75b3c0e`; post-merge `33118368302` PASS completo incluido `Required CI`.
- La auditoría contra los adversariales software-testables del ADR permanece cubierta. Restore/RPO-RTO representativo y la evidencia productiva de rotación/observabilidad no pueden sustituirse por CI.
- Deuda supply-chain preexistente visible: `telegram@2.26.22` → `@cryptography/aes@0.1.1` → GPL-3.0-or-later. No fue introducida por PostgreSQL/AWS SDK y no amplía el gate de 5.2.
- No se tocó la frontera 5.1: media/proyectos siguen dispositivo ↔ Telegram directo y `galer_cloud_file_bytes=0` permanece obligatorio; no se cambia revoke/rotation de transport bots por esta tarea.
- **Pendiente antes de cerrar 5.2 — criterios ABIERTOS:** **(2)** restore independiente representativo con RPO <=15 min/RTO <=2 h medidos; **(3)** evidencia productiva de rotación multiversión; **(4)** observabilidad, alertas, on-call y rollback authority. **Criterio (1) satisfecho. 5.2 permanece `[ 🟡 ]`; NO-GO.**

**Dependencias:** contención terminada.  
**Evidencia:** ADR/threat model/migration plan + PRs #29–#42 + CI PostgreSQL/recovery + evidencia productiva WAVE 3 de autoridad/restart/rollback dry-run + aceptación independiente AAA + checklist/readiness BBB.  
**Gate de salida:** arquitectura aprobada, control-plane productivo durable y los **cuatro criterios WAVE 3** satisfechos; hoy **1/4 satisfecho, 3/4 abiertos**. **NO SATISFECHO todavía; no marcar `[x]`.**