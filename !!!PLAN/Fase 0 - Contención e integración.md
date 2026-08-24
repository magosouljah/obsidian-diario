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

- [ 🟡 ] Sustituir credenciales Telegram en cliente por acceso temporal seguro sin romper el data plane directo. **Decisión de diseño en progreso:** Galer Cloud nunca será relay de archivos. M0-A demostró la frontera criptográfica sintética, M0-B0 confirmó el seam real de mtcute, M0-B1 probó el split network permanent-side/temp-side y M0-B2 ya probó identidad bot + RPC directo con permanent bot credentials exclusivamente del lado controlado. La arquitectura candidata supera ya el gate de identidad/protocolo, pero esta subparte sigue `[ 🟡 ]` porque faltan renovación/expiración/operación larga, data plane 1.9 GB y reemplazar de verdad las credenciales compartidas en el runtime Web/Desktop.
- [ ] Eliminar discovery inseguro de `127.0.0.1:4000`; fijar origen remoto o autenticar criptográficamente el servicio local.
- [ ] Vendorizar parser ID3; definir CSP, headers, CORS, cookie/CSRF y scopes Tauri mínimos.

**Estado/evidencia 5.1 — en progreso, NO aprobado:**
- Auditoría read-only confirmó que Desktop recibe actualmente `bot_token`, `telegram_api_id` y `telegram_api_hash`; el helper local consume el token. Web genera una clave RSA, recibe un credential envelope, lo descifra dentro del navegador y reconstruye `bot_token`, `telegram_api_id` y `telegram_api_hash`. El worker Web usa `@mtcute/web` para transferir directamente con Telegram; Galer no debe convertirse en relay para corregir la credencial.
- También siguen pendientes discovery de `127.0.0.1:4000`, parser ID3 cargado desde CDN y hardening Web/Tauri.
- Restricción arquitectónica inmutable: **MP3/WAV/artwork/samples/PROJECT ZIP viajan dispositivo ↔ Telegram directamente; Galer Cloud controla autorización/asignación pero nunca transporta los bytes como relay.**
- PR BeatGaler #11 `security: define Task 5.1 trust boundaries`, rama `task-5.1-trust-boundaries`. Head inicial `5cdcfcecccea63a31adc5eaf66416929c0fbb95a`; CI #103 PASS 6/6. La documentación corregida llega a `bb162c01c80e21a264c4022c9c682a90c14fbb98`; su descripción de PR también fue alineada para retirar privilege leases. CI #108 PASS 6/6 incluido `Required CI`.
- Evidencia de diseño: `docs/ADR-0051-TRUST-BOUNDARIES.md`, `docs/THREAT-MODEL-0051.md`, `docs/MIGRATION-0051-ROLLBACK.md`.
- La especificación oficial de Telegram confirma una separación protocolariamente plausible: el `encrypted_message` de binding se cifra con la permanent auth key, mientras `auth.bindTempAuthKey` se invoca usando la temporary auth key. M0-B1 convirtió esa plausibilidad en evidencia de red real para el bind y M0-B2 confirmó además herencia de identidad bot y RPC autorizada directa.
- PR #12 `test(security): probe Telegram admin-rights churn`, rama `task-5.1-permission-churn-probe`, head `2b8904880dfeaa57b970674a79abcb181161af0a`; CI #105 PASS 6/6.
- Resultado empírico #12: primera corrida = 80 cambios exitosos a 5 s, 2.5 s, 1 s y 500 ms, sin `FLOOD_WAIT`; segunda corrida poco después a 250 ms = Telegram devolvió `FLOOD_WAIT 533s` después de 20 cambios de esa corrida y la restauración automática inmediata también recibió `FLOOD`. La actividad acumulada puede haber contribuido, así que **no se afirma que “el límite es 20”**.
- Decisión derivada: permission churn frecuente queda **fuera de la arquitectura principal 5.1**. No habrá `operación -> grant delete -> borrar -> revoke delete`, promote/demote por chunk ni privilege leases dependientes de restore inmediato.
- Defensa adicional: temporary credentials, membership limitada, aislamiento entre tenants, sesiones cortas y permisos baseline mínimos/estables. `pin_messages` puede permanecer baseline si INDEX lo exige; `delete_messages` puede necesitar baseline si un transport bot debe borrar mensajes creados por **otro** transport bot. Delete propio y delete cross-bot se deben probar por separado.
- M0-A: PR #13 `test(security): prove M0 temp-auth binding boundary`, draft, rama `task-5.1-temp-auth-binding-probe`, head `96af35e85481ff85d856dc22949bfb314ebedc3e`. Parte del baseline integrado exacto `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; diff = 2 archivos (`scripts/telegram-temp-auth-binding-vector.mjs` y una línea de `package.json`). No usa red, bot token, API hash, auth keys reales ni vault. Valida un vector AES-IGE publicado y el envelope MTProto v1 con material sintético. El self-test aislado dio `PASS M0-A temp-auth binding vector: permanent-side envelope can be built without temp-key bytes or file relay`. Su API de binder no acepta bytes de temp auth key. Esto demuestra solamente una frontera de implementación local; `network_bind_proven=false` y `direct_mtproto_operation_proven=false`. CI #109 PASS 6/6 incluido `Required CI`.
- M0-B0: draft PR #14 `test(security): audit mtcute seam for M0-B`, rama `task-5.1-temp-auth-network-probe`, head `9bd8bee1eda87cbeab051a3937ef95f6c4884ec4`, apilado sobre #13 para que el diff sea solo el incremento B0. Cambia `scripts/telegram-temp-auth-mtcute-seam.mjs` y una línea de `package.json`; no usa red, secretos, bot ni vault. CI #110 falló únicamente porque una aserción del probe dependía de comillas concretas en el CJS publicado; se corrigió a una verificación semántica sin tocar producto. CI #111 terminó PASS 6/6 incluido `Required CI` en Web/shared, Supply chain, Windows, macOS arm64 y macOS x86_64.
- Evidencia ejecutada de B0: la copia instalada es `@mtcute/web 0.31.0` + `@mtcute/core 0.31.0`; existen generación de temp auth key (`p_q_inner_data_temp_dc`), `auth.bindTempAuthKey`, envío del bind bajo temp key y rolling refresh. A la vez, el stock PFS usa `this._session._authKey.key` para construir `encrypted_message`; por tanto `stock_use_pfs_satisfies_task_5_1=false`. El probe mantiene `network_bind_proven=false`, `direct_mtproto_operation_proven=false` y `galer_file_bytes=false`.
- M0-B1: draft PR #15 `test(security): prove M0-B1 split temp-auth bind`, rama `task-5.1-temp-auth-live-bind-probe`, head limpio `2b942deea108fc4818bbb1c088db2f144f3c42c0`, apilado sobre #14. El probe usa Telegram TEST DC y separa procesos: binder genera/conserva permanent auth; cliente genera/conserva temp auth; cliente envía al binder únicamente `msg_id`, `nonce`, `temp_auth_key_id`, `temp_session_id` y `expires_at`; binder devuelve permanent key id + `encrypted_message`; el cliente envía `auth.bindTempAuthKey` directamente a Telegram cifrado bajo la temp key. Telegram devolvió `boolTrue`. Resultado: `network_bind_proven=true`, `permanent_auth_reaches_client=false`, `temp_auth_key_reaches_binder=false`, `galer_file_bytes=false`, `bot_identity_proven=false` y `direct_mtproto_operation_proven=false`. Live probe run #16 PASS; CI del mismo head #117 PASS 6/6 incluido `Required CI`. Un experimento posterior de RPC post-bind produjo `mt_rpc_error` y fue retirado explícitamente del scope probado; no se registra como evidencia positiva.
- M0-B2: draft PR #16 `test(security): prove M0-B2 bot temp-auth identity`, rama `task-5.1-temp-auth-bot-probe`, head `5ff0d70edd6c4ac11ff54bbd52a68246342130ac`, apilado sobre #15. Cambia solo `scripts/telegram-temp-auth-bot-live.mjs` y `.github/workflows/probe-task-5.1-temp-auth-bot.yml`. El binder parent es el único que recibe los secretos dedicados; autoriza la permanent key como bot mediante `auth.importBotAuthorization`, sigue `USER_MIGRATE_N` solo del lado controlado y lanza el cliente con API id/hash/token eliminados de su environment. El cliente recibe únicamente el DC seleccionado como metadata de routing, genera/conserva la temp key, hace el bind directo y ejecuta `users.getUsers(inputUserSelf)` directamente con la temp key. El rerun limpio del workflow `32789070730`, job `97626995224`, terminó PASS en production DC 1 y confirmó que la identidad devuelta coincide exactamente con la autorizada por binder: `bot_identity_proven=true`, `network_bind_proven=true`, `direct_mtproto_operation_proven=true`, `permanent_auth_reaches_client=false`, `bot_token_reaches_client=false`, `api_hash_reaches_client=false`, `galer_file_bytes=false`, `vault_used=false` y `token_rotation_or_revoke=false`. Una primera tentativa del mismo head falló antes del bind durante creación fresca de temp key con `Step 4: invalid nonce hash from server`; el mismo head pasó al reintentarlo sin cambios, así que se clasifica como ruido transitorio del handshake. Un head previo ya había producido el mismo PASS pero quedó retenido por cleanup hasta timeout; el head final acota ese cleanup y el rerun termina verde. CI normal #130 del mismo head está en curso al registrar este avance: Web/shared, Supply chain, Windows y macOS arm64 ya PASS; macOS x86_64/`Required CI` siguen pendientes.
- Siguiente gate M0-C: demostrar renovación proactiva, recuperación ante expiración anticipada mediante un caso controlado/fault injection y continuidad de una operación lógica larga atravesando renovación, manteniendo permanent bot auth/credenciales exclusivamente del lado controlado y sin archivo/vault real. La auditoría de mtcute confirma que su PFS stock usa TTL 24 h, refresh 1 h antes con jitter y swap primary/secondary, pero ese mecanismo stock no puede reutilizarse tal cual porque construye el envelope con permanent-key bytes en el cliente.
- Después siguen **1.9 GB**, Windows/macOS/Web pura, delete cross-bot, cross-vault/shared-bot, escalabilidad/admission control y migración del runtime productivo sin credenciales compartidas.
- **No se cambió** transporte runtime, Bot API productivo, Offline, YouTube, Pinterest, UI, token rotation/revoke, vaults reales, datos, CSP, CORS, cookies, permisos Tauri ni parser ID3.

### Tarea 5.2 [P0 · BE/OP] — Aprobar arquitectura de datos

- [ ] Aprobar una persistencia transaccional durable con migrations, constraints, backup/restore y rollback como requisito de producción.
- [ ] **DECISION propuesta:** usar PostgreSQL para cuentas, sesiones, providers, MFA, entitlements, jobs y auditoría; confirmar esta elección en el ADR antes de implementar.
- [ ] Definir cifrado de secretos, migraciones, backup, RPO/RTO propuestos y rollback.
- [ ] Definir reconciliación Telegram/index y garbage journal.

**Dependencias:** contención terminada.  
**Evidencia:** ADRs revisados, threat model y plan de migración con rollback.  
**Gate de salida:** no empieza la implementación sensible sin una arquitectura aprobada y pruebas adversariales definidas.