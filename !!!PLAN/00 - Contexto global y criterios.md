# Contexto global y criterios del Plan Maestro

> Archivo de referencia. **No sustituye** a [`Plan Maestro.md`](./Plan%20Maestro.md). Se lee cuando una decisión necesita contexto de auditoría, diseño, prioridad, calendario o roles.

## Veredicto ejecutivo

BeatGaler tiene una base de producto real y valiosa: biblioteca, importación y Review, edición, reproducción, Trash, sincronización cloud, modo offline desktop, YouTube, actualizador firmado por Tauri y un conjunto de pruebas que ya detecta varias regresiones. El estado de lanzamiento permanece **NO-GO** hasta satisfacer todos los gates P0/P1 aplicables.

La razón no es falta de pulido. Los bloqueos históricos identificados incluyen seguridad y operación: credenciales de infraestructura llegando al cliente, rutas legacy antes de autenticar, sesión Web reutilizable en `localStorage`, persistencia JSON, ausencia de deploy/restore reproducibles, promesas legales adelantadas a funciones, firma/notarización incompleta y divergencias Web/Desktop. Parte de esta base ya se ha corregido en Fase 0; el resto conserva sus tareas/gates.

Decisiones de calendario:

- **4 de septiembre:** checkpoint interno de seguridad, datos e integración; no fecha pública.
- **9 de octubre:** primera ventana pública recomendada si todos los gates pasan y existe suficiente paralelismo.
- **30 de octubre:** ruta conservadora si una sola persona concentra la ejecución o dependencias externas llegan tarde.
- El calendario nunca justifica recortar seguridad, datos, pagos, firma o evidencia.

## Evidencia y alcance base

La auditoría base utilizó:

| Fuente remota | SHA auditado | Versión observada | Papel |
|---|---|---:|---|
| `web-foundation-v0.1.0` | `e79728642839493326df706aba993a4cde2bdc02` | `0.7.0` | arquitectura Web, adaptadores browser, import/playback/edit/Trash Web |
| `galer-cloud-v0.7.4` | `131df88753c812c0fdf440a5558fff46b2a83f57` | `0.7.4` | baseline desktop, runtimes Windows, portabilidad macOS, Direct Cloud |

### Clasificación de afirmaciones

- **CURRENT:** estado observado directamente.
- **MEASURED:** resultado de inventario/build/tests/análisis reproducible.
- **TARGET:** objetivo propuesto; no describe estado actual.
- **DECISION:** elección arquitectónica/producto sujeta a aprobación.
- **GATE:** condición que debe demostrarse antes de avanzar/publicar.

Mediciones base registradas el 22 de agosto de 2026:

- Web: 317 archivos rastreados; 234 de texto y 83 binarios inventariados.
- Cloud: 281 archivos rastreados; 59 superficies/estados canónicos y 48 rutas HTTP inventariadas; el inventario posterior expande superficies hasta S63.
- Divergencia base: 11 commits exclusivos Web, 8 Cloud, con 12 rutas solapadas.
- Conflictos detectados en `src/App.tsx`, `src/components/Drawer.tsx`, `src/lib/libraryStateManager.ts` y `tests/integration/coreIntegration.test.tsx`; fueron resueltos conscientemente en Tarea 3.1.
- Build Web base: 118 módulos; bundle principal 623.24 kB minificado y Worker 1,205.98 kB, con warning de tamaño.
- Build Cloud base: 101 módulos; bundle principal 600.98 kB minificado.
- Web base: typecheck, 8 suites TS, 55 DOM, 9 integración, 14 backend y regresiones aprobaron.
- Cloud base: typecheck, 7 suites TS, 7 DOM, 8 integración, 11 backend y regresiones aprobaron.
- Producción npm: cero vulnerabilidades conocidas en grafos de producción auditados; tooling tenía 24 vulnerabilidades (1 crítica, 18 altas, 4 moderadas, 1 baja) y sigue sujeto a 4.2.
- La evidencia Rust/native local original quedó inconclusa por espacio; CI cross-platform posterior sí aporta evidencia para la línea integrada.

## Viabilidad de fechas

### 4 de septiembre de 2026

**NO-GO como lanzamiento público.** Solo alpha interna si todos los P0 de seguridad/datos del checkpoint están cerrados. Si falta uno, es demo local con datos sintéticos.

### 9 de octubre de 2026

Ventana pública recomendada bajo paralelismo suficiente, dependencias externas disponibles y cero P0/P1.

### 30 de octubre de 2026

Ruta conservadora con el mismo alcance/gates cuando una sola persona concentra la ejecución o certificados/cuentas externas llegan tarde.

## Estrategia de integración y versión

1. Rama protegida de integración desde la base desktop más nueva.
2. Portar Web por capacidades, no merge ciego.
3. Resolver conflictos centrales con tests Web/Desktop.
4. Convergencia `0.8.0-alpha.1`; beta `0.9.0-beta.1`; RC `1.0.0-rc.1`; pública `1.0.0`.
5. Web, backend, Windows, macOS y updater deben salir del mismo tag/SHA protegido.
6. Artefactos finales inmutables; checksums, SBOM, procedencia y promoción registradas.

La compatibilidad se demuestra con contratos comunes y E2E por plataforma; similitud de nombres entre ramas no cuenta como paridad.

## Inventario de pantallas/superficies

Leyenda: **I** implementado/alcanzable, **P** parcial, **H** placeholder, **U** huérfano/no alcanzable, **A** ausente, **D** solo desktop. “Acción” describe tratamiento de lanzamiento.

| ID | Superficie/estado | Cloud 0.7.4 | Web foundation | Acción de lanzamiento |
|---|---|---:|---:|---|
| S01 | Ventana principal desktop | I | D | conservar tamaño/mínimo y probar lifecycle por OS |
| S02 | Loader HTML previo a React | I | I | unificar marca y estado accesible |
| S03 | Restauración de sesión | I | P | distinguir offline/timeout de 401; retry sin logout |
| S04 | Crash boundary | P | P | marca BeatGaler, ID seguro, diagnóstico/retry |
| S05 | Login/registro/MFA | P | P | verify/reset/recovery/rate limit/responsive |
| S06 | Callback OAuth éxito/error | I | I | popup/redirect, cancel/retry |
| S07 | Overlay desbloqueo X | I | I | simplificar etapas, foco/reduced motion |
| S08 | Shell/galería principal | I | I | jerarquía compartida y responsive |
| S09 | Skeleton galería | I | I | geometría igual al contenido |
| S10 | Refresh/progreso | I | I | estado único no bloqueante |
| S11 | Biblioteca vacía/cloud unavailable | I | P | bootstrap Web atómico/estados separados |
| S12 | Sin resultados | I | I | limpiar filtros/copy consistente |
| S13 | Conexión pobre/offline | I | I | banner persistente y alcance degradado |
| S14 | Error descarga | I | I | retry/detalle seguro |
| S15 | Aviso proyecto | I | D | conservar/normalizar |
| S16 | Progreso descarga cloud | I | I | sistema de jobs/toasts |
| S17 | Upload interrumpido/rollback | I | D | recovery guiado |
| S18 | Búsqueda expandible | P | P | clear/Escape/mobile |
| S19 | Orden Name/BPM/Rating/Manual | P | P | ocultar Manual donde no aplica |
| S20 | Selección masiva | I | P | commit Web seguro o explicar bloqueo |
| S21 | Color tags | I | I | tokens/contraste/teclado |
| S22 | Rename tag global | I | D | journal/rollback/progreso |
| S23 | Drag overlay/HUD | I | P | Web solo acciones soportadas |
| S24 | Beat card normal | I | I | jerarquía estable |
| S25 | Card busy/success | I | I | estado único, sin layout jump |
| S26 | Warnings card | P | P | icono/texto/acción |
| S27 | Menú card/bulk | I | P | filtrar por capabilities |
| S28 | Galer Cloud Files modal | I | I | Dialog/progreso accesible |
| S29 | “What are you adding?” | H | H/D | retirar Loop/Stems falsos del camino principal |
| S30 | Drawer detail/edit/bulk/review | I | P | modos explícitos/Save/cierre |
| S31 | Estados Drawer | I | P | pending/error/empty/retry uniforme |
| S32 | Review skeleton | I | I | estructura final/cancelación |
| S33 | Crop imagen | I | I | teclado/zoom/confirmación |
| S34 | Add Beat fuente | P | I simplificado | adaptar por plataforma |
| S35 | Add Beat scanning | I | D | progreso/cancel |
| S36 | Add Beat conflicto múltiple | I | D | decisiones/roles claros |
| S37 | Add Beat resultados | I | D | resumen/error/retry |
| S38 | Decisiones fuzzy | I | D | preview/teclado |
| S39 | Conflictos audio | I | D | comparar/skip reversible |
| S40 | Player fijo | I | I | controles/foco/shortcuts/responsive |
| S41 | Queue/volumen | P | I | índice activo/popover/sheet |
| S42 | Menú player | I | I | capabilities/a11y |
| S43 | YouTube paso 1 | P | D actual | llevar a Web mediante Tarea 15.3 |
| S44 | YouTube Visual | I | D actual | llevar a Web mediante Tarea 15.3 |
| S45 | YouTube Metadata/Presets | I | D actual | llevar a Web mediante Tarea 15.3 |
| S46 | YouTube Visibilidad/Schedule | I | D actual | llevar a Web mediante Tarea 15.3 |
| S47 | Scheduler | I | D actual | accesible + Web mediante Tarea 15.3 |
| S48 | YouTube Conexión/Job | I | D actual | Web backend/adaptador mediante Tarea 15.3 |
| S49 | Job tray | P | D actual | estados/acciones; Web en Tarea 15.3 |
| S50 | Settings Account | I | I | secciones cortas |
| S51 | Settings Plan | H | H | billing real o retirar CTA |
| S52 | Settings Preferences | I | P | capability/guardado/feedback |
| S53 | Settings Trash | I | I | restore/purge/error por item |
| S54 | Settings Tools/Updater | I dev | D | separar diagnóstico/updater |
| S55 | Privacy | H/P | H/P | documento verdadero/versionado |
| S56 | Terms | H/P | H/P | aceptación/refund |
| S57 | Alert/confirm | P | P | Dialog semántico |
| S58 | SetupModal huérfano | U | U | eliminar/reconstruir onboarding |
| S59a | 404/deep link | A | A | ruta segura |
| S59b | Ventanas secundarias | A | A | mantener ventana única |
| S59c | Mobile nativo | A | A | fuera de scope; Web responsive sí |
| S59d | Delete account | A | A | reauth/consecuencias/recibo |
| S59e | Forgot/reset | A | A | one-shot/success/error |
| S59f | Email verification | A | A | pending/resend/verified/error |
| S59g | MFA recovery | A | A | generar/usar/regenerar |
| S59h | Checkout/payment/cancel | A/H | A/H | Stripe real o retirar simulación |
| S59i | Soporte/status visible | A | A | diagnóstico/contacto/status |
| S60 | Pickers navegador/SO | I | I | filtros/cancel/foco/prueba real |
| S61 | Sesiones/dispositivos | P | P | inventario/revoke/límites |
| S62 | Providers OAuth | P | P | connect/disconnect/linking/retry |
| S63 | Quotas/entitlement reached | P | P | uso/límite/acción, incluido YouTube |

Rutas Web antes de publicar: landing, app autenticada, callback OAuth, Privacy, Terms, soporte/status y 404 seguro. Android/iOS nativo queda fuera del lanzamiento; “mobile” significa Web responsive.

## Sistema de diseño y experiencia

Objetivo: que el usuario entienda qué existe, qué ocurre, qué puede hacer y si su cambio ya es durable.

Principios:

- jerarquía estable: orientación → contenido → acción primaria → secundarias → estado del sistema;
- tokens/primitives compartidos antes que estilos inline;
- foco visible, Dialog semántico, live regions, labels y color nunca como única señal;
- objetivo WCAG 2.2 AA para Web y equivalencia teclado/lector en desktop;
- responsive diseñado para 390–430, 768, 1024 y ≥1280 px, no “desktop encogido”;
- motion breve e interrumpible; reduced-motion elimina/reduce animación;
- capability contract filtra/adapta acciones antes de renderizar;
- feedback: banner persistente, inline local, toast transitorio según duración/gravedad.

Componentes obligatorios compartidos: `Button`, `IconButton`, `LinkButton`, `TextField`, `PasswordField`, `Select`, `Checkbox`, `Switch`, `SegmentedControl`, `Menu`, `Popover`, `Tooltip`, `Dialog`, `Drawer`, `Sheet`, `Toast`, `Banner`, `InlineAlert`, `Skeleton`, `EmptyState`, `ErrorState`, `Progress`, `JobItem`, `StatusBadge`, `BeatCard`, `Tag`, `Rating`, `LibraryToolbar`, `PlayerBar`, `Queue`, `ReviewShell`, `SettingsShell`, `Stepper`.

## Rediseño por plataforma

### Compartido

1. Fundamentos/tokens/iconos/feedback/dialogs/focus.
2. AccountGate completo.
3. Biblioteca/search/sort/tags/cards/selección.
4. Review/Drawer con Save durable/conflictos/progreso.
5. Player/queue.
6. Settings/Plan/Trash/legal/Tools por capability.
7. YouTube: UI compartida; adaptador Desktop actual + adaptador Web posterior.

### Web

- URLs estables, responsive real desde 390 px.
- Bootstrap vacío, Save All y bulk edit con transacciones Web, nunca Tauri.
- Download/playback con estrategia Safari/Firefox/iPhone y límites de memoria.
- Sesión segura/CSP/headers; ningún secreto infraestructura en JS.
- Acciones nativas ocultas/adaptadas por capability.
- YouTube se implementa como Web pura mediante Tarea 15.3; no Desktop helper.

### Windows

- Densidad desktop/teclado; runtimes empaquetados; app identity/rutas consistentes.
- NSIS con Authenticode/timestamp.
- UAC, usuario estándar, paths, antivirus/SmartScreen, sleep/wake y DAWs declarados.

### macOS

- Safe areas/menú/shortcuts/Dock/close coherentes.
- Developer ID + hardened runtime + notarización + stapling.
- Intel + Apple Silicon solo si ambos artefactos/equipos pasan.
- Gatekeeper/Finder/sleep/wake/permisos/iCloud/external/DAWs declarados.

## Priorización del trabajo

Baseline: **12 P0, 11 P1, 7 P2 y 4 P3** como grupos de gate.

### P0 — no se publica

1. Delivery reproducible Web/backend con staging/producción.
2. Persistencia transaccional, backup cifrado y restore.
3. Tag/SHA único, artefactos inmutables y rollback.
4. Tenant derivado de sesión; auth antes de cargas.
5. Ninguna credencial Telegram compartida en cliente.
6. Sesión/CSP/CDN/localhost/XSS endurecidos.
7. Export/delete real de cuenta/datos.
8. Incidente de estado operacional resuelto.
9. Billing completo; sin fallback free-only.
10. Privacy/Terms/refund/consentimiento verdaderos.
11. Developer ID/notarización/stapling macOS.
12. Authenticode/timestamp Windows.

### P1 — no se promete plataforma/flujo

- observabilidad/on-call/incidente;
- separación de entornos/secretos;
- rama/versión única y compatibilidad;
- verify/reset/revoke-all/MFA recovery/abuso;
- quotas/entitlements server-side;
- soporte/escalación;
- marca/dominio/IDs/ownership distribución;
- runtimes Windows/matriz física;
- updater rings/kill switch/minimum version/rollback;
- capacidad bots/recovery dependencias;
- Web: bootstrap, Save All, bulk edit, OAuth, sesión;
- YouTube Web como parte de la paridad funcional del producto mediante Tarea 15.3.

### P2 — antes de crecimiento amplio

CI requerido/pins/scans/SBOM, retención/logs/acceso, licencias/EULA/notices, rendimiento Web, a11y/browser E2E/responsive, limpieza repo y onboarding/errores.

### P3 — post-lanzamiento salvo regresión

Microinteracciones/delight, preferencias visuales extra, reordenamiento/manual no soportado Web y limpieza documental/copy no crítica.

## Modelo de ejecución

- **RO:** release/product owner; alcance/go-no-go.
- **FE:** React/Web/diseño.
- **BE:** backend/datos/seguridad.
- **DE:** desktop/Tauri/packaging/updater.
- **DL:** diseño/a11y/copy.
- **QA:** automatización/E2E/compatibilidad/beta.
- **OP:** infraestructura/observabilidad/backups/incidentes.
- **LF:** legal/finanzas/soporte/dominio.

Una persona puede cubrir varios roles. Que el repo tenga un solo maintainer y `Required approvals = 0` **no elimina** la necesidad de revisión independiente en los gates que explícitamente la exigen (security, legal, firma/release). La fecha del 9 de octubre asume paralelismo; sin él se usa la ruta del 30 de octubre.

Cada evidencia se guarda con: gate, versión/SHA, entorno, fecha/hora, ejecutor, resultado, enlace al log/artefacto y aprobador cuando el gate lo requiera.
