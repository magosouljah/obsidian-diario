# Gates — Publicación y contingencias

> Antes de usar este archivo: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md). Este documento se abre cuando una tarea afecta release, go/no-go, riesgo, contingencia o una condición obligatoria de publicación.

## Condiciones obligatorias para publicar

### Fuente y automatización

- [ ] Un solo tag/SHA genera Web, backend, Windows, macOS, updater, SBOM y checksums.
- [ ] Branch protection, reviews/aprobaciones aplicables, environments y required checks activos.
- [ ] Frontend, backend, Rust, integración, regresiones, browser E2E, packaging y security scans verdes.
- [ ] Cero vulnerabilidad critical/high conocida en producción o build/release; excepciones solo con owner, compensación y expiración aprobada.
- [ ] Artefactos no se sobrescriben y la procedencia es verificable.

**Nota de gobernanza GitHub:** BeatGaler tiene un solo maintainer. El ruleset de integración usa `Required approvals = 0` para no crear un bloqueo imposible de auto-review, pero mantiene PR + CI/checks. Esto no elimina revisiones independientes donde security/firma/release las exigen como gate. **Legal se rige por la excepción RO-approved documentada en el RACI: el review F0/0.8 puede cerrarse mediante auditoría AI-assisted y aceptación explícita de riesgo, sin afirmar independent counsel review.**

### Seguridad

- [ ] Ninguna credencial Telegram compartida llega a cliente/bundle/worker/log.
- [ ] Identidad tenant deriva de sesión; autorización y límites preceden a upload/Telegram.
- [ ] Sesión Web, CSP, headers, CORS/CSRF y origen API aprobados; parser ID3 local/pinned.
- [ ] Local API desktop no puede ser suplantada por otro proceso.
- [ ] Cross-tenant de control-plane/session substitution, replay, expiry, SSRF, rate limit y abuso tienen pruebas negativas. **Excepción arquitectónica explícita:** cuando no existe ningún bot libre, el RO permite shared-bot como fallback de capacidad; una temporary auth de esa identidad no se considera criptográficamente scoped a un único vault y el riesgo residual cross-vault queda aceptado/documentado. No se puede presentar este fallback como aislamiento demostrado.
- [ ] Incidente de estado rastreado cerrado y secrets/data scan limpio.

### Web

- [ ] Cuenta nueva → índice vacío → Add Beat → Review → Save → refresh.
- [ ] Save All y bulk edit son transacciones Web o la acción no se presenta como disponible.
- [ ] Playback/download tienen límites y fallbacks probados en navegadores soportados.
- [ ] **YouTube Web funciona de principio a fin sin Tauri ni Desktop helper** y conserva el contrato compartido con Desktop.
- [ ] Chrome, Safari, Firefox e iPhone pasan la matriz acordada.
- [ ] 390–430 px, 200% zoom, teclado, lector, contraste y reduced motion pasan.
- [ ] Landing/app/callback/legal/support/404 y API pública usan dominio/TLS finales.

### Datos y cuentas

- [ ] PostgreSQL/migraciones/constraints activos; JSON no es autoridad productiva.
- [ ] Importador dry-run/idempotente y rollback demostrados.
- [ ] Backup cifrado, alerta y restore independiente con RPO/RTO aprobados.
- [ ] Verify/reset/MFA recovery/session inventory/revoke/export/delete pasan E2E.
- [ ] Retención, tombstones, provider cleanup y audit record coinciden con Privacy.

### Pagos y planes

- [ ] Checkout, firma webhook, duplicados/desorden/retry/idempotencia probados.
- [ ] Customer/subscription/invoice/entitlement y portal/cancelación son server-side.
- [ ] Quotas se aplican atómicamente en endpoints, no solo UI.
- [ ] Límites YouTube por plan se aplican server-side tanto para Desktop como Web.
- [ ] 3DS, rechazo, renewal failure, cancel, upgrade/downgrade y refund pasan.
- [ ] Compra real controlada y refund quedan reconciliados a cero.
- [ ] Si cualquier punto falla, v1 se retrasa; BeatGaler v1 no tiene fallback free-only.

### Windows

- [ ] NSIS y binarios con Authenticode/timestamp; publisher verificado.
- [ ] Runtimes cloud incluidos y verificados después de instalar.
- [ ] Clean install, upgrade, uninstall, usuario estándar/UAC, path, network, sleep/wake y DAWs soportados pasan.
- [ ] Updater válido/alterado/rollback probado.

### macOS

- [ ] Developer ID, hardened runtime, notarización, stapling y Gatekeeper pasan.
- [ ] Intel y Apple Silicon pasan físicamente si ambos se anuncian.
- [ ] Clean install, upgrade, Finder, permisos, network, sleep/wake y DAWs soportados pasan.
- [ ] Updater válido/alterado/rollback probado.

### Operación, capacidad y beta

- [ ] Staging y producción tienen datos, endpoints, secretos y aprobaciones aislados.
- [ ] Logs redactados, dashboards, alertas, on-call, status, soporte y runbooks activos.
- [ ] Deploy rollback, data restore, bot/master/API/DB/Stripe/Telegram failure drills pasan.
- [ ] Capacity envelope al 2× del pico propuesto pasa; el pool demuestra que **exclusividad por vault es el camino normal** y que shared-bot solo aparece como fallback cuando no quedan bots libres, con reparto justo, observabilidad y admission/waitlist disponible.
- [ ] Dos betas; mínimo 12 testers en Beta 1 y testers nuevos en Beta 2.
- [ ] Soft launch 8 h + soak 24 h sin P0/P1 ni pago/dato pendiente.

### Identidad y legal

- [ ] Marca, entidad, bundle ID, dominio, DNS/TLS, release repo y emails tienen owner.
- [ ] Privacy, Terms, refund/cancelación y aceptación versionada aprobados.
- [ ] LICENSE/EULA/notices/codec y subprocesadores revisados.
- [ ] Soporte, seguridad/abuso, recovery y finanzas tienen escalación y cobertura.

**Estado del review F0/0.8:** `[x]` **AI-assisted review completed 2026-08-31; independent counsel deferred by explicit RO decision; residual legal risk accepted by RO.** Este `[x]` solo cierra la actividad de review. **No marca los checks legales anteriores como completados, no certifica compliance y no cierra los 12 P0/14 P1.** El backlog canónico está en [`Legal launch review - AI-assisted 2026-08-31.md`](./Legal%20launch%20review%20-%20AI-assisted%202026-08-31.md).

## Regla de publicación

> **NO PUBLICAR** mientras exista un P0 o P1; un owner confirmation launch-critical sin evidencia; un pago no reconciliado; una migración/restore/rollback no demostrado; o una plataforma/navegador anunciado sin prueba.

Un hotfix que toca auth, datos, pagos, transporte, firma o migración crea una nueva RC y repite todos los gates dependientes. La presión de fecha no cambia esta regla.

## Métricas y umbrales de éxito

Los siguientes valores son **targets propuestos** para aprobar por RO/owners; no describen el estado actual.

### Seguridad e integridad

- 0 P0/P1 conocidos y 0 acceso cross-tenant **no autorizado por las reglas del control-plane** en pruebas adversariales/carga. El shared-bot fallback aprobado por RO es una excepción de arquitectura explícita y no cuenta como aislamiento criptográfico por vault; cualquier acceso cruzado fuera de esa asignación explícita sigue siendo fallo.
- 0 secreto de infraestructura en cliente, artefactos, repo o logs.
- 100% de rutas mutantes con auth/tenant/ownership y negative tests.
- 100% de compras, refunds y cambios de entitlement reconciliados.
- 100% de restores de ensayo concluyen con core-flow verification.

### Producto

- ≥90% de testers nuevos completa signup→first beat→play→edit→restore sin asistencia.
- 0 pérdida silenciosa tras Save/Save All/bulk edit/refresh/restart.
- 100% de flujos críticos pasa en cada plataforma/navegador anunciado.
- YouTube debe pasar su flujo crítico en Desktop y Web antes de presentarse como paridad funcional v1.
- 0 defecto crítico de teclado, focus, contraste o lector en dichos flujos.

### Web y backend

- Core Web Vitals propuestos en p75: LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 en escenarios medidos.
- Error rate de requests core <1% y disponibilidad de soak ≥99.9%, excluyendo fallas deliberadas documentadas.
- RPO propuesto ≤24 h y RTO propuesto ≤2 h, sustituidos por targets más estrictos si legal/negocio lo exige.
- Load test al 2× del pico esperado durante 60 min, sin corrupción, fuga no autorizada o cola ilimitada.

### Release y soporte

- 100% de instaladores verifican firma de OS y updater antes de ejecutar.
- 8 h de soft launch + 24 h de soak sin P0/P1.
- Primer acuse de soporte crítico dentro de 30 min durante la ventana de lanzamiento propuesta.
- Rollback de app/deploy y restore de datos completan dentro del runbook aprobado.

## RACI de lanzamiento

`R` ejecuta, `A` responde por el resultado, `C` consulta/revisa, `I` informado.

| Frente | R | A | C | I |
|---|---|---|---|---|
| Alcance, fecha y go/no-go | RO | RO | Security, QA, DE, OP, LF | Todos |
| Integración/versiones | FE, DE | RO | BE, QA | DL, OP |
| Auth/data plane/tenant | BE | Security owner | FE, OP, QA | RO, LF |
| PostgreSQL/migración/backup | BE, OP | OP | QA, Security | RO, LF |
| Sistema de diseño/Web UX | FE, DL | DL | QA, BE | RO, Support |
| Billing/entitlements | BE, LF | Finance owner | QA, Security, FE | RO, Support |
| Web/backend deploy | OP, BE | OP | QA, Security | RO |
| Windows packaging | DE | DE | QA, OP, Security | RO, Support |
| macOS packaging | DE | DE | QA, OP, Security | RO, Support |
| QA/matriz/betas | QA | QA lead | FE, BE, DE, DL | RO, OP, LF |
| Observabilidad/incidente | OP | Incident owner | BE, QA, Support | Todos |
| Legal/privacidad/refund | LF | Legal owner | RO, BE, Security | Todos |
| Soporte/status | Support/LF | Support owner | OP, QA, Finance | RO |
| Lanzamiento/rollback | OP, DE | RO | Todos los approvers | Usuarios |

Si una sola persona cubre `R` y `A`, se requiere un reviewer externo para security y firma/release; la fecha usa la ruta conservadora. Para legal, aplica exclusivamente la excepción RO-approved siguiente; cerrar el review por esta excepción no cierra findings de compliance.

**LEGAL EXCEPTION — RO-APPROVED:** For the initial launch gate, independent external legal review may be deferred by explicit RO decision when an AI-assisted legal audit, legal-risk register, jurisdiction-specific findings and explicit residual-risk acceptance are recorded. This does not represent or certify independent counsel review.

Para F0/0.8, RO ejerció explícitamente esta excepción respecto de la auditoría AI-assisted del **2026-08-31**. Los findings sustantivos continúan sujetos a la regla `NO PUBLICAR` y a los gates de implementación aplicables.

## Registro de riesgos

| Riesgo | Prob. | Impacto | Señal temprana | Prevención/respuesta | Owner |
|---|---:|---:|---|---|---|
| Rediseño transporte Telegram excede estimación | Alta | Crítico | capability/proxy falla cross-tenant | mantener registro cerrado; cortar alpha | BE/Security |
| Certificados Apple/Windows llegan tarde | Media | Crítico | no disponibles a tiempo | mover a ruta conservadora; no unsigned | DE/RO |
| Migración JSON→Postgres pierde/duplica | Media | Crítico | dry-run difiere/rollback falla | snapshot/idempotencia/quarantine | BE/OP |
| Merge rompe Cloud/Web | Alta | Alto | contrato/capability falla | integrar por slices/bisectar | FE/DE/QA |
| Billing diverge Stripe | Media | Crítico | ledger ≠ Stripe | idempotencia/reconciliation/pause | BE/Finance |
| Bot/master se satura o shared-bot aparece con demasiada frecuencia | Media | Crítico | bots libres=0, shared leases/queue/error suben | sobredimensionar pool, exclusividad preferida, reparto justo, telemetría, admission/waitlist y capacidad de revoke de seguridad | BE/OP |
| Safari/iPhone consume RAM | Alta | Alto | memory/crash archivo grande | streaming/límites/copy soporte | FE/QA |
| Firma/notarización rompe runtimes | Media | Alto | codesign/notary/app falla | orden firma/entitlements/clean device | DE |
| Legal/copy no coincide | Media | Crítico | claim falso/placeholder | revisión post-implementación + backlog AI-assisted; no afirmar compliance | LF/RO |
| Solo developer es cuello de botella | Alta | Alto | gates sin reviewer/tareas atrasadas | ruta 30 Oct, reviewers externos donde gate los exige, excepciones RO explícitas, WIP limit | RO |
| Tooling vulnerable compromete build | Media | Alto | critical/high/action mutable | upgrade/pin/scan/SBOM | OP/QA |
| P0 durante beta/soft launch | Media | Crítico | anomalía datos/security/payment | stop/kill switch/rollback/nueva RC | Incident owner |
| Regresión carga inicial librería | Alta | Alto | espera mayor que optimización previa | medir cold/warm por fases y budget | FE/BE/QA |
| Estado sensible en historia Git | Media | Alto | reauditoría encuentra config real | HEAD sanitizado + decidir purga | BE/RO |
| YouTube Web se intenta resolver llamando Tauri | Media | Alto | browser requiere `invoke`/helper local | contrato/adaptador Web + guard Web-no-Tauri | FE/BE/QA |

## Caminos de contingencia

### Si el 4 de septiembre no pasa seguridad

- No alpha remota; demo local con datos sintéticos.
- Mantener registro, pagos y uploads públicos cerrados.
- Reestimar por blocker, no por días “perdidos”.

### Si Stripe no está listo

- Mover lanzamiento v1; nunca convertir v1 en free-only.
- Betas/promociones pueden usar entitlements reales regalados sin cobros no consentidos.
- No cobrar y conciliar manualmente.

### Si firma Windows/macOS no está lista

- Si el objetivo sigue simultáneo: mover todo el lanzamiento.
- Si RO cambia alcance explícitamente: Web preview y desktop “coming later”, nunca unsigned.
- Firma Tauri `.sig` no sustituye confianza OS.

### Si Safari/iPhone falla memoria/performance

- Corregir streaming y repetir beta; o reducir matriz soportada con copy/detección.
- No anunciar “Web móvil” solo porque el login cabe.

### Si capacidad Telegram es insuficiente

- Mantener **exclusividad por vault como preferencia**, añadir bots y usar admission/waitlist para que `bots libres = 0` sea excepcional.
- Si todos los bots están ocupados, el shared-bot fallback aprobado por RO puede asignar vaults adicionales siguiendo reparto justo por carga; debe quedar medido/observable y reducirse de nuevo cuando exista capacidad.
- No afirmar que temporary auth compartida queda aislada criptográficamente por vault. El riesgo residual cross-vault de ese fallback está aceptado explícitamente; cualquier cruce fuera de las asignaciones autorizadas sigue siendo incidente.

### Si YouTube Web no supera su gate antes del release

- v1 se considera incompleto respecto al objetivo de paridad definido; no marcar `youtubePublishing` Web como disponible.
- No usar Tauri/helper Desktop como atajo para Web.
- Reestimar el release o cambiar alcance solo mediante decisión explícita del RO actualizando `Plan Maestro.md` y todos los documentos afectados.

### Si aparece un P0 después del soft launch

- Congelar registro/pagos/uploads según blast radius.
- Rollback de artefacto/deploy y preservar datos/evidencia.
- Notificar status/afectados, reconciliar dinero/datos y crear nueva RC.

## Confirmaciones del propietario pendientes

Antes de GO, el owner aporta evidencia fechada sobre:

- protecciones GitHub, environments, secrets, retention y ownership del release repo;
- dominio/DNS/TLS/WAF/proxy, hosts/regiones/contratos providers;
- procedencia/remediación del estado operativo rastreado;
- Apple Developer ID y Authenticode: custodia/expiración/timestamp/clean-device;
- private key updater, match con public key, backup/rotation/kill switch;
- Stripe live, productos/precios/tax/refunds/disputes/webhooks/reconciliation;
- estructura fiscal/legal en México, jurisdicciones, edad 18+, Privacy/Terms/refund/DPA/subprocesadores/licencias;
- soporte/security-abuse contact/cobertura/autoridad recovery;
- ownership/políticas Telegram, storage/rate limits/concurrencia/drills;
- OS/arquitecturas/DAWs/navegadores soportados y hardware disponible.

Hasta entonces: **`needs owner confirmation`**, nunca “listo”.

## Fuentes externas de criterios

- [Tauri — Windows code signing](https://tauri.app/distribute/sign/windows/)
- [Tauri — macOS code signing](https://v2.tauri.app/distribute/sign/macos/)
- [Apple — notarizing macOS software](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution)
- [Stripe — Checkout subscriptions](https://docs.stripe.com/payments/checkout/build-subscriptions)
- [Stripe — webhooks](https://docs.stripe.com/webhooks?lang=node)
- [Stripe — subscription webhooks](https://docs.stripe.com/billing/subscriptions/webhooks?locale=en-GB)
- [Stripe — idempotency](https://docs.stripe.com/api/idempotent_requests)
- [OWASP — Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html)
- [OWASP — Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html)
- [OWASP — XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [OWASP — CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Request_Forgery_Prevention_Cheat_Sheet.html)
- [OWASP — HTTP Headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html)
- [Cloudflare Pages — Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/)
- [Cloudflare Pages — custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/)
- [Cloudflare Pages — rollbacks](https://developers.cloudflare.com/pages/configuration/rollbacks/)
- [Railway — PostgreSQL](https://docs.railway.com/databases/postgresql)
- [Railway — backups/restores](https://docs.railway.com/guides/postgres-backups-restores)

## Estado final esperado

- [ ] Rama `1.0.0` integrada y protegida.
- [ ] Web pública responsive, accesible y segura.
- [ ] YouTube funcional en Desktop y Web según capabilities reales.
- [ ] Windows firmado, instalado y actualizable.
- [ ] macOS Developer ID/notarizado/stapled y probado.
- [ ] Datos migrados, respaldados y restaurados.
- [ ] Cuentas recuperables, exportables y eliminables.
- [ ] Pagos, promociones y quotas reconciliados; v1 nunca usa fallback free-only.
- [ ] Dominio, legal, soporte, status y monitoreo activos.
- [ ] Capacidad demostrada; no una cantidad arbitraria de bots.
- [ ] Dos betas, soft launch y soak sin P0/P1.
- [ ] Go/no-go firmado y BeatGaler publicado con rollback listo.
