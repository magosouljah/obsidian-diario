
asegurate q mi plan esta perfecto basado en mi repostorio de github
https://github.com/magosouljah/BeatGaler
1. galer-cloud-v0.7.4
2. web-foundation-v0.1.0
3. ignora el branch local

haz una lectura adversarial independiente: busca contradicciones, cifras que parezcan estado real cuando solo son objetivos y cualquier función/pantalla omitida.

si vas a hacer cambios dime antes de hacerlo


# BeatGaler — Plan maestro para terminar y publicar Web, Windows y macOS

**Versión del plan:** 1.0  
**Fecha de auditoría:** 22 de agosto de 2026, `America/Mexico_City`  
**Hito original:** 4 de septiembre de 2026  
**Fecha pública recomendada:** 9 de octubre de 2026, condicionada a todos los gates  
**Ruta conservadora si una persona concentra la ejecución:** 30 de octubre de 2026  
**Alcance:** lanzamiento público directo desde la web, con aplicación Web y descargas firmadas para Windows y macOS.

## Veredicto ejecutivo

BeatGaler tiene una base de producto real y valiosa: biblioteca, importación y Review, edición, reproducción, Trash, sincronización cloud, modo offline desktop, YouTube, actualizador firmado por Tauri y un conjunto de pruebas que ya detecta varias regresiones. Sin embargo, las dos ramas auditadas no forman todavía una versión publicable y el estado actual es **NO-GO** para un lanzamiento público, pagado o simultáneo en Web, Windows y macOS.

La razón no es falta de pulido. Hay bloqueos de seguridad y operación: credenciales de infraestructura Telegram llegan al cliente; existen rutas legacy que aceptan cargas antes de autenticar; el Web guarda una sesión reutilizable en `localStorage`; la persistencia del backend sigue en JSON; no hay deploy reproducible Web/backend ni restore probado; los textos legales prometen funciones ausentes; macOS usa firma ad-hoc sin notarización y Windows carece de Authenticode. Además, Web y Desktop divergen y presentan cuatro conflictos de integración justo en archivos centrales.

Por ello:

- El **4 de septiembre** deja de ser una fecha pública y se convierte en un **checkpoint interno de seguridad, datos e integración**. Solo podría abrirse una alpha privada, gratuita, con invitación y datos no sensibles si sus gates P0 específicos están cerrados.
- El **9 de octubre** es la primera ventana razonable para una publicación pública de las tres plataformas si hay al menos cuatro frentes trabajando en paralelo, las cuentas/certificados externos están disponibles antes del 27 de agosto y no aparece un hallazgo P0 nuevo.
- Si el mismo desarrollador debe ejecutar, probar y aprobar casi todo, la fecha recomendada pasa al **30 de octubre** y aun así conserva los mismos gates; no se recorta seguridad para recuperar calendario.
- El rediseño se implementará **por cortes verticales desde el inicio**. Primero fundamentos, accesibilidad y flujos de mayor impacto; el deleite opcional queda después del lanzamiento. Dejar todo el rediseño para el final multiplicaría regresiones y obligaría a repetir la beta.

Reglas inmutables del plan:

1. Ningún P0 ni P1 abierto al publicar.
2. Ninguna plataforma se declara soportada sin instalación y flujo crítico en equipo limpio.
3. Ningún pago se acepta sin reconciliación, reembolso y entitlement server-side demostrados.
4. Ninguna evidencia externa se marca como lista sin propietario, fecha y enlace verificable.

## Evidencia y alcance

La auditoría ignoró cualquier checkout anterior y utilizó clones nuevos del repositorio remoto solicitado:

| Fuente remota | SHA auditado | Versión observada | Papel en la integración |
|---|---|---:|---|
| [`web-foundation-v0.1.0`](https://github.com/magosouljah/BeatGaler/tree/web-foundation-v0.1.0) | `e79728642839493326df706aba993a4cde2bdc02` | aplicación `0.7.0` | arquitectura Web, adaptadores de navegador, import/playback/edit/Trash Web |
| [`galer-cloud-v0.7.4`](https://github.com/magosouljah/BeatGaler/tree/galer-cloud-v0.7.4) | `131df88753c812c0fdf440a5558fff46b2a83f57` | aplicación `0.7.4` | baseline desktop más nuevo, runtimes Windows, portabilidad macOS, Direct Cloud |

Evidencia medida:

- Web: 317 archivos rastreados; 234 archivos de texto leídos completamente y 83 binarios inventariados.
- Cloud: 281 archivos rastreados; 59 superficies/estados canónicos y 48 rutas HTTP inventariadas. La reconciliación de diseño expande las nueve ausencias agrupadas en S59 y añade los pickers S60: **68 grupos explícitos**.
- Divergencia desde `d289f8c1649286376b194565710adb60e125e0f0`: 11 commits exclusivos de Web, 8 de Cloud, 69 y 28 rutas cambiadas respectivamente, con 12 rutas solapadas.
- Una simulación de merge solo lectura encontró conflicto textual en `src/App.tsx`, `src/components/Drawer.tsx`, `src/lib/libraryStateManager.ts` y `tests/integration/coreIntegration.test.tsx`.
- Build Web: aprobado; 118 módulos. Bundle principal 623.24 kB minificado y Worker 1,205.98 kB, ambos con warning de tamaño.
- Build frontend Cloud: aprobado; 101 módulos. Bundle principal 600.98 kB minificado, también con warning.
- Web: typecheck, 8 suites TS, 55 pruebas DOM, 9 de integración, 14 backend y regresiones aprobaron.
- Cloud: typecheck, 7 suites TS, 7 pruebas DOM, 8 de integración, 11 backend y regresiones aprobaron.
- Producción npm: cero vulnerabilidades conocidas en los cuatro grafos de producción auditados el 22 de agosto. El grafo completo de herramientas de cada rama tiene 24 paquetes vulnerables —1 crítico, 18 altos, 4 moderados y 1 bajo— y debe cerrarse como riesgo de supply chain.
- Rust/native no obtuvo veredicto local: la compilación limpia agotó el disco disponible. No se interpreta ni como pass ni como fallo del producto; CI y equipos limpios deben producir la evidencia.
- Se renderizaron y revisaron login y registro de ambas ramas, incluido Web a 390 × 844. Las superficies autenticadas/nativas se verificaron por código y pruebas, pero todavía requieren inspección visual con cuenta de staging y equipos reales.

Exclusiones deliberadas:

- No se cambió, publicó, desplegó ni empujó código al repositorio.
- No se usaron ni inspeccionaron credenciales del usuario.
- No se asumió la existencia de dominio, hosting, certificados, cuenta Stripe, backups, monitoreo, testers o acuerdos legales.
- Los estados de CI remoto, Telegram real, OAuth, YouTube, GitHub Releases y hardware físico permanecen **`needs owner confirmation`** hasta aportar evidencia fechada.

## Viabilidad de la fecha

### 4 de septiembre de 2026

**NO-GO como lanzamiento público.** En trece días calendario no cabe responsablemente integrar dos ramas divergentes, sustituir dos límites de confianza críticos, migrar datos, construir staging/producción, completar ciclo de cuentas y pagos, firmar dos sistemas operativos, probar restore/rollback y ejecutar dos betas.

Puede conservarse como alpha interna solo si para el 2 de septiembre se cumplen todos estos mínimos:

- rutas legacy retiradas o autenticadas antes de Multer;
- ninguna credencial compartida Telegram entregada a navegador/desktop;
- incidente de estado operativo rastreado resuelto;
- sesión Web/CSP/CDN/localhost endurecidos;
- una rama integrada y reproducible;
- datos sintéticos, sin pagos y con registro por invitación;
- kill switch, logs y propietario de incidente activos.

Si falta uno, el 4 de septiembre es únicamente una demo local.

### 9 de octubre de 2026

Es la **ventana pública recomendada** bajo estas suposiciones de capacidad:

- cuatro frentes paralelos como mínimo: cliente/diseño, backend/seguridad, desktop/release y QA/operaciones;
- decisión de alcance, dominio, entidad legal, planes y distribución directa tomada el 24 de agosto;
- Apple Developer ID y mecanismo de firma Windows disponibles como máximo el 27 de agosto;
- revisión independiente de seguridad y legal accesible durante septiembre;
- testers y hardware Intel/Apple Silicon/Windows reservados antes del 7 de septiembre.

La fecha se mueve automáticamente si una dependencia externa incumple su gate. No se recupera recortando pruebas.

### 30 de octubre de 2026

Es la ruta conservadora si una sola persona lleva la mayor parte del trabajo o si los certificados/cuentas externas no están listos en agosto. Mantiene el mismo alcance y los mismos gates; solo elimina paralelismo y añade tiempo de corrección entre betas.

## Estrategia de integración y versión

No se debe desarrollar el release directamente sobre ninguna de las dos ramas auditadas.

1. Crear una rama protegida de integración desde `galer-cloud-v0.7.4` porque contiene la versión desktop 0.7.4 y el empaquetado Windows más completo.
2. Portar los 11 commits/cortes Web por capacidad, no mediante un merge ciego: plataforma/capabilities, transporte, biblioteca, importación, reproducción, edición, Trash y pruebas.
3. Resolver explícitamente los cuatro archivos en conflicto con tests de contrato Web/Desktop antes de continuar.
4. Nombrar la primera convergencia `0.8.0-alpha.1`; beta externa `0.9.0-beta.1`; release candidate `1.0.0-rc.1`; versión pública `1.0.0`.
5. Generar Web, backend, Windows, macOS y updater desde el mismo tag/SHA protegido.
6. Prohibir `--clobber` para artefactos finales y registrar checksums, SBOM, procedencia y promoción de canal.

La compatibilidad se prueba mediante contratos comunes y E2E por plataforma; similitud de nombres entre ramas no cuenta como paridad.

## Inventario de pantallas

Leyenda: **I** implementado, **P** parcial, **H** placeholder, **A** ausente, **D** solo desktop. “Acción” identifica el tratamiento de lanzamiento, no elimina funciones actuales.

| ID | Superficie/estado | Cloud 0.7.4 | Web foundation | Acción de lanzamiento |
|---|---|---:|---:|---|
| S01 | Ventana principal desktop | I | D | conservar tamaño/mínimo y probar lifecycle por OS |
| S02 | Loader HTML previo a React | I | I | unificar marca y estado accesible |
| S03 | Restauración de sesión | I | P | distinguir offline/timeout de 401; retry sin logout |
| S04 | Crash boundary | P | P | marca BeatGaler, ID seguro, copiar diagnóstico/retry |
| S05 | Login/registro/MFA | P | P | añadir verify/reset/recovery/rate limit y responsive |
| S06 | Callback OAuth éxito/error | I | I | popup reservado o redirect, cancel/retry |
| S07 | Overlay de desbloqueo X | I | I | simplificar etapas, foco y reduced motion |
| S08 | Shell y galería principal | I | I | nueva jerarquía compartida y responsive Web |
| S09 | Skeleton de galería | I | I | geometría igual al contenido; sin animación excesiva |
| S10 | Refresh/progreso | I | I | estado único no bloqueante y anuncio accesible |
| S11 | Biblioteca vacía/cloud unavailable | I | P | bootstrap Web atómico y estados diagnósticos separados |
| S12 | Sin resultados de búsqueda | I | I | CTA para limpiar filtros y copy consistente |
| S13 | Conexión pobre/offline | I | I | banner persistente con acción y alcance de modo degradado |
| S14 | Error de descarga | I | I | toast accionable, retry y detalle seguro |
| S15 | Aviso de proyecto | I | D | conservar, normalizar severidad y copy |
| S16 | Progreso/completado de descarga cloud | I | I | consolidar en sistema de jobs/toasts |
| S17 | Upload interrumpido/rollback | I | D | preservar y convertir en recovery guiado |
| S18 | Búsqueda expandible | P | P | botón clear visible, label, Escape y móvil |
| S19 | Orden Name/BPM/Rating/Manual | P | P | chevron real; ocultar Manual donde no aplica |
| S20 | Selección masiva | I | P | commit Web seguro o deshabilitar con explicación |
| S21 | Paleta de color de tags | I | I | tokens, contraste y navegación teclado |
| S22 | Rename tag global | I | D | preservar journal/rollback y feedback por progreso |
| S23 | Drag overlay/HUD | I | P | mantener desktop; Web solo acciones soportadas |
| S24 | Beat card normal | I | I | jerarquía estable, targets claros y metadata escaneable |
| S25 | Card busy/success | I | I | estado único por acción; evitar saltos de layout |
| S26 | Warnings de card | P | P | icono/texto/acción y prioridad semántica |
| S27 | Menú card y bulk | I | P | filtrar por capabilities y validar cada comando |
| S28 | Galer Cloud Files modal | I | I | shared Dialog, disponibilidad y progreso accesible |
| S29 | “What are you adding?” | H | H/D | sacar Loop/Stems deshabilitados del camino principal |
| S30 | Drawer detail/edit/bulk/review | I | P | dividir por modos, Save persistente y cierre visible |
| S31 | Estados de Drawer | I | P | patrón uniforme pending/error/empty/retry |
| S32 | Review skeleton | I | I | igualar estructura final y preservar cancelación |
| S33 | Crop de imagen | I | I | teclado, zoom etiquetado y confirmación visible |
| S34 | Add Beat — elegir fuente | P | I simplificado | iconos/cierre reales; adaptar acciones por plataforma |
| S35 | Add Beat — scanning | I | D | progreso determinado/indeterminado y cancel seguro |
| S36 | Add Beat — conflicto de múltiples archivos | I | D | conservar decisiones y explicación de roles |
| S37 | Add Beat — resultados | I | D | resumen de importación, errores por item y retry |
| S38 | Decisiones fuzzy | I | D | lenguaje claro, preview y navegación teclado |
| S39 | Conflictos de audio | I | D | comparación explícita y opción skip reversible |
| S40 | Player fijo | I | I | controles estables, foco, shortcuts y responsive |
| S41 | Queue y volumen | P | I | corregir índice activo; drawer móvil y popover desktop |
| S42 | Menú contextual player | I | I | capabilities y accesibilidad iguales a card |
| S43 | YouTube paso 1 | P | D | stepper, cierre visible y selección resumida |
| S44 | YouTube paso 2 Visual | I | D | preview/crop con estados vacíos claros |
| S45 | YouTube paso 3 Metadata/Presets | I | D | reducir densidad y mostrar requisitos antes de avanzar |
| S46 | YouTube paso 4 Visibilidad/Schedule | I | D | timezone explícito, errores inline y resumen |
| S47 | Scheduler | I | D | reemplazar wheels frágiles por control accesible |
| S48 | YouTube paso 5 Conexión/Job | I | D | estado OAuth, progreso y recovery coherentes |
| S49 | Job tray | P | D | restaurar iconos/botones y una taxonomía de estados |
| S50 | Settings — Account | I | I | secciones cortas, acciones peligrosas separadas |
| S51 | Settings — Plan | H | H | conectar billing real o retirar CTA de compra |
| S52 | Settings — Preferences | I | P | controles por capability, guardado y feedback uniformes |
| S53 | Settings — Trash | I | I | restore/purge con undo donde sea seguro y error por item |
| S54 | Settings — Tools/Updater | I dev | D | separar diagnóstico de opciones públicas; updater con rings |
| S55 | Privacy | H/P | H/P | documento versionado, verdadero y con contacto real |
| S56 | Terms | H/P | H/P | documento versionado, aceptación y política de refund |
| S57 | Alert/confirm compartido | P | P | Dialog semántico; retirar alerts nativos |
| S58 | SetupModal huérfano | A | A | eliminarlo o reconstruir onboarding; nunca dejar ruta personal |
| S59a | 404/not-found y recuperación de deep link | A | A/no aplica | ruta segura, explicación y vuelta a la aplicación |
| S59b | Ventanas secundarias internas | A | A | conservar ventana única; no fingir superficies inexistentes |
| S59c | Pantallas mobile nativas | A | A | fuera de scope; mobile significa Web responsive, no app nativa |
| S59d | Delete account/self-service | A | A | reauth, consecuencias, confirmación, progreso y recibo |
| S59e | Forgot/reset password | A | A | request, token one-shot, nueva clave, éxito/error |
| S59f | Email verification | A | A | pending/resend/verified/error y retorno a sesión |
| S59g | MFA recovery codes | A | A | generar, guardar/copiar, usar y regenerar de forma segura |
| S59h | Checkout/payment/cancelación | A/H | A/H | flujo Stripe real o retirar simulación/CTA |
| S59i | Soporte/status/observabilidad visible | A | A | diagnóstico seguro, contacto y status accesibles |
| S60 | Pickers archivo/carpeta/save del navegador/SO | I | I | filtros correctos, cancelación/foco y prueba real por plataforma |

Rutas Web adicionales que deben existir antes de publicar: landing pública, aplicación autenticada, callback OAuth, privacidad, términos, soporte/status y un 404 seguro. No se necesita un router complejo, pero sí URLs estables y comprobables. Android/iOS quedan fuera del lanzamiento; sus iconos no constituyen soporte móvil nativo.

## Auditoría visual

La inspección renderizada confirmó un shell oscuro consistente entre ramas, pero también labels y texto secundario con contraste bajo, estilos de autofill del navegador que rompen los inputs oscuros, una tarjeta de registro que ocupa casi todo el viewport de 390 px y dependencia intensa de estilos inline. La revisión completa del árbol mostró problemas adicionales: controles sin glifo, copy inglés/español mezclado, marca BeatVault residual, ausencia de media queries, dialogs sin semántica/focus trap, Settings de ancho rígido, estados loading/error indistinguibles y acciones desktop que aparecen en Web.

El rediseño no busca “hacerlo más bonito” de forma aislada. Busca que un usuario pueda entender qué existe, qué está ocurriendo, qué puede hacer y si su cambio ya es durable.

| Before | After | Why |
|---|---|---|
| “Beat Galer”, “BeatGaler” y “BeatVault” conviven | Una marca `BeatGaler`, una guía de naming y copy por locale | Confianza y reconocimiento consistentes |
| Inputs oscuros cambian a autofill claro del navegador | Estilos autofill explícitos, contraste AA y tokens de campo | Evita una ruptura visible desde el primer contacto |
| Labels y texto de ayuda demasiado tenues | Roles de texto `primary/secondary/muted` con contraste medido | Legibilidad sin convertir todo en blanco puro |
| Botones de cerrar, clear, sort e iconos aparecen vacíos | SVG compartidos, `aria-label`, tooltip y hit area estable | Recupera descubribilidad, teclado y accesibilidad |
| Cada componente inventa tamaños, radios y colores inline | Tokens semánticos y primitives compartidos | Reduce deriva visual y acelera cambios seguros |
| Settings fija sidebar de 220 px y grids rígidos | Navegación adaptable: sidebar desktop, tabs/lista móvil | Hace viable Web a 390–430 px sin apretar contenido |
| Todos los estados compiten en cards, banners y toasts | Jerarquía: banner persistente, inline local, toast transitorio | La duración y gravedad determinan el componente |
| `Loading plans…` también representa un error | State machine `idle/loading/success/empty/error` con retry | El usuario nunca queda esperando indefinidamente |
| Acciones incompatibles llegan a Web y fallan | Capability contract filtra, deshabilita o adapta antes de render | Mantiene promesas por plataforma y evita callejones |
| Review combina importar, editar, bulk y recovery en un Drawer enorme | Shell estable con modos explícitos, step/status y CTA primaria fija | Baja carga cognitiva sin perder funciones |
| Add Beat muestra Loop/Stems “Coming soon” como opciones | Solo capacidades disponibles en el flujo; roadmap fuera del CTA | Reduce frustración y decisiones falsas |
| Estados cloud usan spans/glifos vacíos y copy variable | Icono + texto + tono semántico con misma taxonomía | Estado comprensible sin depender del color |
| Player/queue no marca siempre el elemento actual | Modelo único de reproducción y fila activa visible | Evita desorientación durante sesiones largas |
| Confirm nativo y diálogo DOM conviven | Un `Dialog` accesible con foco, Escape y retorno de foco | Consistencia y seguridad para acciones destructivas |
| Animación/feedback se decide por componente | Política de motion: repetido instantáneo; overlays breves y cancelables | La interfaz se siente rápida y predecible |
| Privacy/Terms viven como texto largo dentro de Settings | URLs versionadas, resumen legible y documentos enlazables | Consentimiento auditable y navegación pública |
| Errores muestran texto técnico o solo “Cloud unavailable” | Mensaje humano + acción + código de soporte + detalle local | Recuperación sin filtrar secretos |
| Responsive se prueba como reducción del desktop | Layout por prioridad: contenido, acción primaria, contexto | El móvil Web se diseña, no solo “cabe” |

### Jerarquía de experiencia

1. **Orientación:** ubicación, estado de conexión, cuenta y plataforma.
2. **Contenido:** biblioteca y beat activo dominan la pantalla.
3. **Acción primaria:** Add Beat, Save o Play según contexto; una sola primaria por superficie.
4. **Acciones secundarias:** menús y shortcuts, nunca compiten visualmente con la primaria.
5. **Estado del sistema:** feedback local inmediato; progreso durable en job tray; incidentes globales en banner.

### Principios Emil aplicados

- Reducir elementos que no ayudan a la decisión actual; no eliminar capacidades.
- Mantener estable la geometría de cards, player y drawers durante loading.
- Hacer instantáneas las acciones repetidas y de teclado.
- Reservar motion para explicar entrada/salida, causalidad o cambio espacial.
- Tratar hover, focus, pressed, disabled, loading, error y offline como parte del componente, no como parches.
- Preferir una composición clara y una transición bien afinada sobre muchos adornos.

## Sistema de diseño compartido

El sistema vive en una capa React compartida y expone tokens semánticos; cada plataforma adapta densidad, ventanas y convenciones sin duplicar el lenguaje visual.

### Tokens

- **Color:** baseline oscuro propuesto: `canvas #0B0C0F`, `surface-1 #121419`, `surface-2 #191C22`, `sunken #08090B`, `border-subtle #262A31`, `border-strong #3A404B`, `text-primary #F5F7FA`, `text-secondary #BEC5D0`, `text-muted #98A2B2`, `accent #8E7CFF`, `success #4FD39B`, `warning #F3B95F`, `danger #FF6B7A`, `info #67B7FF`, `focus-ring #86B7FF`. Son punto de partida sujeto a medición AA; ningún componente usa accent como éxito/error.
- **Tipografía:** stack de sistema; escala propuesta 12/14/16/20/24/32 px; metadata y labels a 12–14, cuerpo a 14–16, títulos por jerarquía; números de tiempo/BPM con cifras tabulares.
- **Espacio:** unidad 4 px; escala 4/8/12/16/24/32/48. El ritmo se define por relación, no por márgenes únicos.
- **Radios:** 6 px para controles, 10 px para superficies y 14 px para modales; pills solo para filtros, estados compactos y selección.
- **Borde/elevación:** bordes antes que sombras; elevación solo para overlays, menús, player flotante y drag preview.
- **Tamaño:** glyph 18–20 px; hit target mínimo 40 × 40 px en desktop y 44 × 44 px en compact/touch.
- **Layout:** ancho de lectura para Settings/legal; grid de biblioteca por minmax; player con zonas fijas; drawer con ancho adaptable y modo full-screen en viewport estrecho.
- **Z-index:** contenido, sticky, popover, drawer, modal, toast; registro único para evitar que un toast quede detrás de un modal.

### Componentes obligatorios

- `Button`, `IconButton`, `LinkButton`, `TextField`, `PasswordField`, `Select`, `Checkbox`, `Switch`, `SegmentedControl`.
- `Menu`, `Popover`, `Tooltip`, `Dialog`, `Drawer`, `Sheet`, `Toast`, `Banner`, `InlineAlert`.
- `Skeleton`, `EmptyState`, `ErrorState`, `Progress`, `JobItem`, `StatusBadge`.
- `BeatCard`, `Tag`, `Rating`, `LibraryToolbar`, `PlayerBar`, `Queue`, `ReviewShell`, `SettingsShell`, `Stepper`.

Cada componente documenta variantes, estados, teclado, lectores de pantalla, reduced motion, responsive y capabilities. Ninguna pantalla crea otro botón/modal/toast con estilos inline si existe un primitive.

### Accesibilidad

- Objetivo WCAG 2.2 AA para la aplicación Web y equivalencia de teclado/lector en desktop.
- Todos los dialogs tienen `role`, nombre, descripción cuando aplique, trap de foco, Escape, retorno de foco y orden predecible.
- Focus ring visible; nunca se elimina sin reemplazo.
- Estado, error y progreso usan live regions con anuncios no repetitivos.
- Iconos decorativos se ocultan; controles de solo icono siempre tienen nombre accesible.
- Color nunca es la única señal. Texto/error se asocia al campo correspondiente.
- Zoom 200%, high contrast y reduced motion forman parte del gate de aceptación.

### Responsive

- Viewports de diseño propuestos: 390–430 px, 768 px, 1024 px y ≥1280 px; se validan también alturas cortas.
- Web móvil: Settings apila navegación, Drawer se vuelve Sheet full-height, queue usa Sheet y player conserva play/seek/track sin desbordar.
- Desktop: se respeta mínimo 900 × 600 actual; por debajo no se promete soporte nativo.
- Pointer fino obtiene hover/tooltips; touch no depende de hover; teclado conserva shortcuts y focus.

### Motion

- Repetición, búsqueda, filtros, selección y teclado: respuesta instantánea.
- Menú/popover: 100–160 ms; drawer/sheet: 180–240 ms; modal ocasional: hasta 260 ms.
- Solo `transform` y `opacity` en animación normal; no animar layout costoso durante audio/importación.
- Toda animación es interrumpible y tiene salida; `prefers-reduced-motion` la elimina o reduce a fade corto.
- Skeleton usa shimmer sobrio o pulso lento; no se mueve contenido ya cargado.

### Gobernanza

- Una página de referencia o Storybook-equivalente con todos los estados.
- Screenshot tests por primitive y cuatro flujos clave.
- Cambios de tokens requieren revisión Design + Frontend; excepciones inline deben incluir motivo y fecha de retiro.
- Una checklist visual/a11y acompaña cada PR, junto a tests funcionales.

## Rediseño por plataforma

### Cambios compartidos

1. Fundamentos: tokens, iconos, campos, buttons, feedback, dialogs y focus.
2. AccountGate: login/registro/MFA/recovery, autofill, error y estado de red.
3. Biblioteca: header, search/sort/tags, cards, selección y empty/error/loading.
4. Review/Drawer: modos explícitos, Save durable, conflictos y progreso.
5. Player/queue: estado activo, responsive, teclado y fallos de streaming.
6. Settings: Account, Plan, Preferences, Trash, legal y Tools por capability.
7. YouTube desktop: stepper, scheduler, job tray y recovery.

### Web

- Navegación URL estable para landing/app/callback/legal/support/404.
- Biblioteca realmente responsive desde 390 px; Drawer y queue como sheets en móvil.
- Bootstrap de cuenta vacía, Save All y bulk edit implementados con transacciones Web, no llamadas Tauri.
- Download/playback con estrategia explícita para Safari/Firefox/iPhone y límites de memoria.
- Sesión HttpOnly/Secure/SameSite o diseño equivalente revisado; CSP y headers estrictos; ningún secreto de infraestructura en JS.
- Acciones nativas ocultas por capability con explicación cuando una alternativa Web exista.

### Windows

- Conservar densidad de escritorio y menús/contextos; targets coherentes con mouse/teclado.
- Unificar el empaquetado de runtimes Node/Bot API de Cloud, app identity final y rutas app-data.
- Instalador NSIS firmado con Authenticode y timestamp; estado updater comprensible y reinicio seguro.
- Probar UAC, usuario estándar, paths no ASCII/largos, antivirus/SmartScreen, sleep/wake y DAWs declarados.
- Evitar translucencia intensa; priorizar contraste y respuesta inmediata.

### macOS

- Respetar safe areas, tráfico de ventana, menú de aplicación, shortcuts y comportamiento Dock/close existente.
- Developer ID, hardened runtime, notarización y stapling integrados al workflow.
- Mantener universal Intel/Apple Silicon solo si ambos artefactos y equipos físicos pasan.
- Usar material/translucencia con moderación en chrome, nunca detrás de texto denso.
- Probar Gatekeeper, Finder, sleep/wake, permisos, paths iCloud/external y DAWs declarados.

### Orden de implementación del rediseño

El rediseño se ejecuta por partes y acompaña las correcciones funcionales:

- Antes de seguridad/integración: solo tokens mínimos y primitives que eviten trabajo desechable.
- Durante cada flujo P0/P1: se rediseña esa superficie y se añaden sus pruebas en la misma entrega.
- Siete días antes de la RC: freeze de estructura, tokens y navegación.
- Después del freeze: solo accesibilidad, copy, errores y correcciones; ningún cambio ornamental amplio.
- Post-lanzamiento: microinteracciones opcionales, personalización y nuevos efectos.

Así se valida el diseño dos veces en beta y se evita una capa cosmética tardía que rompa funciones.

## Priorización del trabajo

El baseline de release agrupa **12 P0, 13 P1, 5 P2 y 2 P3**. Son grupos de gate, no conteo de todos los defectos. Las auditorías por rama contienen hallazgos solapados y más detalle visual; no deben sumarse entre sí.

### P0 — no se publica

1. Delivery reproducible Web/backend con staging y producción.
2. Persistencia transaccional, backup cifrado y restore demostrado.
3. Release ligado a tag/SHA aprobado, artefactos inmutables y rollback.
4. Tenant derivado de sesión en cada ruta; auth antes de cargas.
5. Ninguna credencial Telegram compartida en cliente.
6. Sesión/CSP/CDN/localhost y límite XSS endurecidos.
7. Exportación y eliminación de cuenta/datos reales.
8. Investigación y remediación del estado operativo rastreado.
9. Billing completo si se acepta dinero; de lo contrario alcance free-only explícito.
10. Privacy, Terms, refund y consentimiento verdaderos/versionados.
11. Developer ID + notarización + stapling macOS.
12. Authenticode + timestamp Windows.

### P1 — no se promete la plataforma/flujo

- Observabilidad, alertas, on-call e incidente.
- Separación de entornos y secretos.
- Rama/versión única y compatibilidad cruzada.
- Verify/reset/revoke-all/MFA recovery y abuso.
- Quotas/entitlements server-side.
- Soporte y escalación operables.
- Marca, dominio, IDs y ownership de distribución.
- Paridad de runtimes Windows y matriz de compatibilidad física.
- Updater con rings, kill switch, versión mínima y rollback.
- Capacidad de bots medida y recovery de dependencias.
- Web: bootstrap de biblioteca vacía, Save All, bulk edit, OAuth y restauración de sesión.

### P2 — antes de crecimiento amplio

- CI requerido, dependencias/actions fijadas, advisories, licencias, SBOM y secret scan.
- Redacción/log retention y controles de acceso.
- LICENSE/EULA/third-party notices/codec review.
- Rendimiento Web: chunks, thumbnails, lazy artwork, memoria de playback/download.
- Accesibilidad AA, real-browser E2E y responsive.
- Limpieza del repositorio: backups/dumps/binlogs/rutas personales y plantillas impropias.
- First-run/onboarding y estados fallidos claros.

### P3 — después del lanzamiento salvo que sea una regresión funcional

- Microinteracciones y motion de deleite.
- Preferencias visuales adicionales.
- Reordenamiento/manual features no soportados en Web.
- Limpieza documental y de copy que no afecte consentimiento o soporte.

## Modelo de ejecución

Roles usados en el calendario:

- **RO:** release owner/product owner; decide alcance y acepta gates.
- **FE:** cliente React/Web y sistema de diseño.
- **BE:** backend, datos y seguridad.
- **DE:** desktop, Tauri, packaging y updater.
- **DL:** design lead/accesibilidad/copy.
- **QA:** automatización, E2E, compatibilidad y beta.
- **OP:** infraestructura, observabilidad, backups e incidentes.
- **LF:** legal, finanzas, soporte y dominio.

Una persona puede cubrir varios roles, pero quien implementa un gate P0 no debe ser su único aprobador. La fecha del 9 de octubre supone trabajo paralelo; sin él se usa la ruta del 30 de octubre.

Cada evidencia se guarda con: gate, versión/SHA, entorno, fecha/hora, ejecutor, resultado, enlace al log/artefacto y aprobador.

## Fase 0 — Contener, decidir y crear una sola línea de release

**Fechas:** 22–28 de agosto  
**Objetivo:** eliminar ambigüedad, contener exposición y producir `0.8.0-alpha.1` desde una rama protegida.

### Día 0 — 22–23 de agosto — Baseline y NO-GO

**Resultado:** alcance auditado, inventario y reglas de publicación congelados.

**Tarea 0.1 [P0 · RO/QA] — Congelar evidencia.**

- [ ] Registrar las dos ramas y SHAs auditados en el release ledger.
- [ ] Guardar conteos de pruebas, warnings, vulnerabilidades y límites no verificados.
- [ ] Etiquetar el estado actual `NO-GO`; no crear un tag de release público.

**Tarea 0.2 [P0 · RO] — Convertir el 4 de septiembre en checkpoint interno.**

- [ ] Comunicar que no habrá cobros ni usuarios reales en ese hito.
- [ ] Definir quién tiene autoridad de parar el release.
- [ ] Abrir backlog P0/P1 con un owner y evidencia de salida por item.

**Dependencias:** ninguna.  
**Evidencia:** SHAs, auditorías y ledger firmados por RO.  
**Gate de salida:** alcance y regla “0 P0/P1” aceptados; nadie presenta el 4 de septiembre como fecha pública.

### Día 1 — 24 de agosto — Charter de producto y decisiones externas

**Resultado:** producto público, monetización y distribución definidos sin placeholders.

**Tarea 1.1 [P0 · RO/LF] — Cerrar decisiones de negocio.**

- [ ] Elegir lanzamiento pagado completo o preview free-only; este plan recomienda pagado solo si Stripe pasa todos los gates.
- [ ] Confirmar entidad legal, países iniciales, edad mínima, currency, impuestos y política de refund.
- [ ] Confirmar distribución directa Web/NSIS/DMG; stores quedan post-lanzamiento salvo decisión explícita.

**Tarea 1.2 [P1 · RO/LF] — Reservar dependencias con lead time.**

- [ ] Confirmar dominio y ownership de DNS, GitHub Releases, email de soporte y status page.
- [ ] Iniciar/confirmar Apple Developer ID, notarización y servicio/certificado Authenticode con timestamp.
- [ ] Reservar revisión legal, seguridad independiente, hardware físico y 12–20 testers.

**Dependencias:** Día 0.  
**Evidencia:** decision log y comprobantes de disponibilidad, nunca secretos.  
**Gate de salida:** ninguna decisión de alcance crítica queda sin owner/fecha; si falta firma de OS, se activa fecha conservadora.

### Día 2 — 25 de agosto — Contención de seguridad e incidente

**Resultado:** superficies de mayor riesgo cerradas a tráfico público.

**Tarea 2.1 [P0 · BE/OP] — Retirar exposición inmediata.**

- [ ] Deshabilitar o autenticar antes de Multer todas las rutas legacy de media/metadata.
- [ ] Limitar cuerpo, archivo, concurrencia y frecuencia en edge y aplicación.
- [ ] Desactivar registro público hasta tener abuse controls y verificación.

**Tarea 2.2 [P0 · BE/RO] — Tratar el estado rastreado como incidente potencial.**

- [ ] Determinar en privado si IDs/bots/vaults son reales, sintéticos o revocados.
- [ ] Rotar/reaprovisionar lo afectado si es real; conservar evidencia de cadena de custodia.
- [ ] Purgar historia bajo procedimiento aprobado y añadir secret/data scan.

**Dependencias:** acceso de owners a infraestructura.  
**Evidencia:** pruebas negativas 401/403/413/429 y acta de incidente sin reproducir identificadores.  
**Gate de salida:** ninguna ruta mutante/carga opera sin identidad autenticada y el incidente tiene resolución explícita.

### Día 3 — 26 de agosto — Integración de ramas

**Resultado:** una rama protegida compila y conserva capacidades Web/Desktop.

**Tarea 3.1 [P1 · RO/DE/FE] — Construir la base integrada.**

- [ ] Crear la rama protegida desde Cloud `131df887...` y fijar versión `0.8.0-alpha.1`.
- [ ] Portar Web por capacidades; resolver App, Drawer, library state y test de integración conscientemente.
- [ ] Eliminar backups/dumps/binlogs y contenido impropio del árbol público sin borrar evidencia necesaria del incidente.

**Tarea 3.2 [P1 · QA] — Probar contrato de plataforma.**

- [ ] Ejecutar typecheck, TS/DOM/integration/backend/regresiones en la convergencia.
- [ ] Añadir test que asegura que Web no invoca comandos Tauri y Desktop conserva Direct/offline/YouTube.
- [ ] Generar matriz de capacidades compartida como fuente única.

**Dependencias:** Días 1–2 y working tree limpio.  
**Evidencia:** PR revisado, diff de resolución y suites verdes.  
**Gate de salida:** `0.8.0-alpha.1` reproduce ambos conjuntos de funciones sin conflicto silenciado.

### Día 4 — 27 de agosto — Supply chain y CI requerido

**Resultado:** cada cambio relevante recibe un veredicto automático antes de merge.

**Tarea 4.1 [P2 · QA/OP] — Crear pipeline obligatorio.**

- [ ] Web build + browser smoke; frontend/shared; backend; Rust; regresiones; portabilidad y packaging estático.
- [ ] Fijar Node/Rust/actions; usar lockfiles; cachear sin ocultar checks.
- [ ] Bloquear merge si falla una suite o si versiones/manifiestos divergen.

**Tarea 4.2 [P2 · BE/DE] — Cerrar supply chain conocida.**

- [ ] Actualizar Vitest/Vite/WebdriverIO/transitivas hasta cero critical/high o excepción temporal aprobada y fechada.
- [ ] Añadir npm/Cargo advisories, license scan, secret scan, SBOM y checksums.
- [ ] Verificar binarios Node/FFmpeg/Bot API por digest y registrar procedencia.

**Dependencias:** rama integrada.  
**Evidencia:** required checks en PR de prueba, reportes fechados y SBOM.  
**Gate de salida:** no existe bypass informal; cualquier excepción tiene owner, compensación y expiración.

### Día 5 — 28 de agosto — ADR de confianza y checkpoint de arquitectura

**Resultado:** diseño técnico aprobado para Web, Desktop, sesión y datos.

**Tarea 5.1 [P0 · BE/Security reviewer] — Aprobar límites de confianza.**

- [ ] Sustituir credenciales Telegram en cliente por proxy/capability short-lived, tenant-scoped y revocable.
- [ ] Eliminar discovery inseguro de `127.0.0.1:4000`; fijar origen remoto o autenticar criptográficamente el servicio local.
- [ ] Vendorizar parser ID3; definir CSP, headers, CORS, cookie/CSRF y scopes Tauri mínimos.

**Tarea 5.2 [P0 · BE/OP] — Aprobar arquitectura de datos.**

- [ ] Elegir PostgreSQL y esquema para cuentas, sesiones, providers, MFA, entitlements, jobs y auditoría.
- [ ] Definir cifrado de secretos, migraciones, backup, RPO/RTO propuestos y rollback.
- [ ] Definir reconciliación Telegram/index y garbage journal.

**Dependencias:** contención terminada.  
**Evidencia:** ADRs revisados, threat model y plan de migración con rollback.  
**Gate de salida:** no empieza la implementación sensible sin una arquitectura aprobada y pruebas adversariales definidas.

## Fase 1 — Seguridad, cuentas y datos durables

**Fechas:** 31 de agosto–4 de septiembre  
**Objetivo:** cerrar los P0 de confianza y alcanzar un alpha interno restaurable.

### Día 6 — 31 de agosto — Autorización tenant y abuso

**Resultado:** cada operación usa identidad derivada del servidor y límites previos al trabajo costoso.

**Tarea 6.1 [P0 · BE] — Unificar middleware de autorización.**

- [ ] Derivar user/installation/tenant solo de sesión validada; ignorar IDs de cuerpo para autorización.
- [ ] Autenticar y autorizar antes de Multer, Telegram, lookup de artwork o creación de topic.
- [ ] Añadir ownership por objeto y borrar endpoints legacy no usados.

**Tarea 6.2 [P0 · BE/QA] — Abuse controls.**

- [ ] Rate limit por IP/cuenta/tenant, delays progresivos y límites de upload/concurrencia.
- [ ] Mover scrypt síncrono fuera del event loop o usar implementación asíncrona controlada.
- [ ] Probar credential stuffing, IDs ajenos, bodies inválidos, 2 GB y race conditions sin ejecutar cargas destructivas.

**Dependencias:** ADR de Día 5.  
**Evidencia:** matriz 401/403/413/429 y pruebas cross-tenant.  
**Gate de salida:** cero acceso o mutación cross-tenant en suite adversarial.

### Día 7 — 1 de septiembre — Data plane seguro

**Resultado:** navegador y desktop ya no reciben una identidad Telegram compartida.

**Tarea 7.1 [P0 · BE] — Implementar mediación/capabilities.**

- [ ] Emitir capacidades cortas limitadas por usuario, vault, operación y objeto.
- [ ] Rotar/revocar al terminar lease, logout, password change, delete o incidente.
- [ ] Añadir ceilings por bot/tenant y deny-by-default.

**Tarea 7.2 [P0 · QA/Security reviewer] — Validar aislamiento.**

- [ ] Intentar usar capability de A contra vault/objeto de B.
- [ ] Probar replay, expiración, clock skew, sesión cerrada y bot quarantined.
- [ ] Verificar que bundles, workers, logs y memoria serializada no contienen bot token/API hash.

**Dependencias:** Día 6.  
**Evidencia:** threat tests y escaneo de artefactos.  
**Gate de salida:** 0 secretos de infraestructura en cliente y 0 operaciones fuera del scope.

### Día 8 — 2 de septiembre — Sesión y ciclo de cuenta

**Resultado:** sesiones Web endurecidas y cuentas recuperables/controlables.

**Tarea 8.1 [P0/P1 · BE/FE] — Sesión Web.**

- [ ] Migrar a cookie HttpOnly/Secure/SameSite o mecanismo equivalente revisado; CSRF explícito.
- [ ] Distinguir 401/expiry de offline/timeout; no borrar una sesión válida por error transitorio.
- [ ] Session inventory, revoke-one/revoke-all y rotación tras eventos sensibles.

**Tarea 8.2 [P1 · BE/FE/LF] — Lifecycle completo.**

- [ ] Email verification, forgot/reset con tokens one-shot/expiry y respuesta anti-enumeración.
- [ ] MFA recovery codes, reautenticación para email/password/delete y notificaciones.
- [ ] Export y delete con revocación, provider cleanup, retención/tombstone y recibo.

**Dependencias:** email provider/plantillas y decisiones legales.  
**Evidencia:** E2E de happy/abuse/replay y auditoría de sesión.  
**Gate de salida:** usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

### Día 9 — 3 de septiembre — PostgreSQL y migración reversible

**Resultado:** el backend deja de depender de JSON monolítico.

**Tarea 9.1 [P0 · BE/OP] — Esquema y migrador.**

- [ ] Crear migrations versionadas, constraints, índices y transacciones.
- [ ] Importador JSON con dry-run, checksums, idempotencia, quarantine y reporte por registro.
- [ ] Cifrar/proteger MFA/OAuth; hashes de sesión siguen no reversibles.

**Tarea 9.2 [P0 · QA/OP] — Cutover ensayado.**

- [ ] Snapshot antes, migración staging, comparación de conteos y checks funcionales.
- [ ] Simular fallo a mitad y ejecutar rollback sin perder datos.
- [ ] Desactivar fallback que convierte corrupción en servicio vacío.

**Dependencias:** PostgreSQL staging y ADR de datos.  
**Evidencia:** reporte de migración, diff lógico y rollback exitoso.  
**Gate de salida:** migración repetible y reversible; ningún JSON actúa como autoridad de producción.

### Día 10 — 4 de septiembre — Restore y alpha interna

**Resultado:** checkpoint original convertido en evidencia, no marketing.

**Tarea 10.1 [P0 · OP/QA] — Backup y restore.**

- [ ] Backup cifrado de Postgres/configuración y estrategia para índice/media Telegram.
- [ ] Restaurar en entorno aislado, medir RPO/RTO y ejecutar core flows.
- [ ] Verificar acceso, retention, off-provider copy y alerta por backup fallido.

**Tarea 10.2 [P0 · RO/Security reviewer] — Decidir alpha.**

- [ ] Revisar gates D2–D10, P0 nuevos y evidencia independiente.
- [ ] Si pasa: 3–5 usuarios internos, datos sintéticos, invitación, sin pagos.
- [ ] Si falla: demo local; comunicar deslizamiento sin ampliar alcance.

**Dependencias:** Días 2–9.  
**Evidencia:** video/log de restore, checklist P0 y decisión firmada.  
**Gate de salida:** servicio restaurable y alpha contenida; esto no autoriza lanzamiento público.

## Fase 2 — Flujos Web completos y rediseño de alto impacto

**Fechas:** 7–11 de septiembre  
**Objetivo:** paridad funcional honesta, responsive y accesible para los flujos principales.

### Día 11 — 7 de septiembre — Foundations y AccountGate

**Resultado:** primitives compartidos y adquisición de cuenta coherente.

**Tarea 11.1 [P1 · FE/DL] — Design foundations.**

- [ ] Tokens, tipografía, iconos, focus, buttons, fields, feedback, Dialog y reduced motion.
- [ ] Documentar todos los estados; retirar duplicación inline empezando por AccountGate.
- [ ] Corregir autofill, contraste, loading y layout 390–430 px.

**Tarea 11.2 [P1 · FE/QA] — Auth UI completa.**

- [ ] Login/register/MFA/verify/reset/recovery/error/offline.
- [ ] OAuth con popup reservado o redirect, blocked/cancel/retry.
- [ ] Tests teclado, lector, zoom, móvil y errores de red.

**Dependencias:** APIs de Día 8.  
**Evidencia:** catálogo visual, axe/manual keyboard y E2E auth.  
**Gate de salida:** todas las variantes de cuenta son alcanzables, legibles y recuperables.

### Día 12 — 8 de septiembre — Library, cards y primera cuenta Web

**Resultado:** una cuenta Web nueva entra a una biblioteca autoritativa y puede orientarse.

**Tarea 12.1 [P1 · BE/FE] — Bootstrap y load.**

- [ ] Aprovisionar índice vacío atómicamente en control plane.
- [ ] Separar empty, no-results, offline, auth y cloud failure.
- [ ] Añadir thumbnails/lazy artwork, paginación o ventana y presupuesto de memoria.

**Tarea 12.2 [P1/P2 · FE/DL] — Rediseñar biblioteca.**

- [ ] Header/search/sort/tags/selection con iconos y nombres accesibles.
- [ ] Card con jerarquía fija y estados cloud/playback/download sin salto.
- [ ] Grid para 390, 768, 1024 y desktop; touch no depende de hover.

**Dependencias:** data plane y foundations.  
**Evidencia:** E2E cuenta limpia + screenshots baseline + performance trace.  
**Gate de salida:** registro → empty gallery → Add Beat es posible sin Desktop previo.

### Día 13 — 9 de septiembre — Import, Review y bulk edit

**Resultado:** importar y editar en Web nunca cae en Tauri ni produce éxito falso.

**Tarea 13.1 [P1 · FE/BE] — Persistencia Web correcta.**

- [ ] `Save All` comitea cada candidato con expectativas de índice y resume parciales.
- [ ] Bulk edit usa una transacción Web conflict-safe o queda deshabilitado con explicación hasta completarla.
- [ ] Garbage journal limpia uploads huérfanos tras fallo/cancel.

**Tarea 13.2 [P1 · FE/DL/QA] — ReviewShell.**

- [ ] Modos Import/Edit/Bulk explícitos, CTA fija, close visible y progreso N/N.
- [ ] Errores por item, retry/skip/cancel y confirmación durable.
- [ ] E2E multi-file, conflicto, refresh simultáneo y rollback.

**Dependencias:** biblioteca y data plane.  
**Evidencia:** tests de Save All/bulk y reconciliación posterior al refresh.  
**Gate de salida:** ninguna acción visible Web llama Tauri; 0 pérdida silenciosa.

### Día 14 — 10 de septiembre — Playback, queue y descargas

**Resultado:** reproducción y archivos funcionan dentro de límites conocidos por navegador.

**Tarea 14.1 [P1/P2 · FE/BE] — Streaming/memoria.**

- [ ] Definir soporte MediaSource/Range y fallback seguro por navegador.
- [ ] Evitar ensamblar archivos gigantes en RAM; imponer límites y comunicar alternativa.
- [ ] Cancelar/reanudar donde sea seguro y liberar object URLs/buffers.

**Tarea 14.2 [P2 · FE/DL/QA] — Player/queue.**

- [ ] Corregir índice activo, shortcuts, seek, shuffle/repeat y error recoverable.
- [ ] Queue/volumen como popover desktop y sheet Web móvil.
- [ ] Probar Safari/Firefox/Chrome/iPhone con archivo pequeño/grande y red degradada.

**Dependencias:** biblioteca estable.  
**Evidencia:** matriz browser, perfiles de memoria y E2E playback/download.  
**Gate de salida:** no hay crash por fallback soportado y la pista activa siempre es inequívoca.

### Día 15 — 11 de septiembre — Settings, Trash y accesibilidad transversal

**Resultado:** configuración y recuperación tienen estados completos y lenguaje veraz.

**Tarea 15.1 [P1 · FE/DL] — SettingsShell.**

- [ ] Sidebar desktop y navegación apilada móvil; Account/Plan/Preferences/Trash/legal por secciones.
- [ ] State machines reales para catálogo, cache, Trash y updater; error + retry.
- [ ] Acciones peligrosas separadas, confirmadas y con reautenticación.

**Tarea 15.2 [P2 · QA/DL] — A11y pass completo.**

- [ ] Dialog/focus restoration, live regions, labels, contraste, zoom y reduced motion.
- [ ] Reemplazar controles/glifos vacíos y alerts/confirms nativos.
- [ ] Congelar baseline visual de todos los S01–S59 alcanzables en harness/staging.

**Dependencias:** primitives y APIs de cuenta.  
**Evidencia:** auditoría AA, keyboard script y screenshot set por plataforma.  
**Gate de salida:** 0 defecto crítico de teclado/lectura/contraste en flujos de lanzamiento.

## Fase 3 — Producción, pagos, legal y operación

**Fechas:** 14–18 de septiembre  
**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

### Día 16 — 14 de septiembre — Staging y producción reproducibles

**Resultado:** el mismo SHA se despliega de forma aislada y reversible.

**Tarea 16.1 [P0 · OP/BE] — Entornos.**

- [ ] Crear proyectos separados, base de datos, buckets/volúmenes, bots, OAuth callbacks y secretos para staging/producción.
- [ ] Si se mantiene la propuesta del usuario: Cloudflare Pages para Web y Railway para API/PostgreSQL; documentar alternativa y ownership.
- [ ] Health, readiness y dependency checks; graceful shutdown, timeouts y proxy trust.

**Tarea 16.2 [P0 · OP/QA] — Pipeline de promoción.**

- [ ] PR → preview; tag candidato → staging; aprobación → producción.
- [ ] Inyectar API origin público, TLS y headers; eliminar Tailscale/local fallbacks de release.
- [ ] Smoke post-deploy y rollback al último artefacto/DB compatible.

**Dependencias:** rama integrada y migraciones.  
**Evidencia:** deploy desde cero, smoke y rollback con mismo SHA.  
**Gate de salida:** no existe paso manual irrepetible ni secreto compartido entre entornos.

### Día 17 — 15 de septiembre — Stripe Checkout y webhooks

**Resultado:** compra sandbox crea estado comercial verificable, no un cambio DEV.

**Tarea 17.1 [P0 si pagado · BE/LF] — Catálogo y checkout.**

- [ ] Definir productos/precios/trial/currency/tax y mapearlos a IDs internos estables.
- [ ] Checkout Session server-side; customer linkage y success/cancel URLs sin confiar en query params.
- [ ] Idempotency keys en mutaciones Stripe y sin precios decididos por cliente.

**Tarea 17.2 [P0 si pagado · BE/QA] — Webhook seguro.**

- [ ] Verificar firma sobre raw body, guardar event ID y procesar asíncrono/reintentable.
- [ ] Manejar duplicados, desorden, timeout y eventos desconocidos.
- [ ] Cubrir checkout complete, invoice paid/failed, subscription updated/deleted y dispute/refund relevantes.

**Dependencias:** cuenta/productos Stripe confirmados y entorno staging.  
**Evidencia:** matriz sandbox, replay/duplicate test y ledger consistente.  
**Gate de salida:** la UI nunca concede plan por redirect; solo estado server-side reconciliado.

### Día 18 — 16 de septiembre — Entitlements, portal y reconciliación

**Resultado:** planes se aplican atómicamente y el usuario puede gestionar/cancelar.

**Tarea 18.1 [P1 · BE/FE] — Enforcement.**

- [ ] Aplicar beats/storage/project/device/session/YouTube limits antes de reservar recursos.
- [ ] Transacción o reserva evita carreras; errores incluyen uso, límite y acción posible.
- [ ] Billing Portal/cancelación y estado `active/trialing/past_due/canceled` en Settings.

**Tarea 18.2 [P0 si pagado · LF/BE/QA] — Dinero y ledger.**

- [ ] Job de reconciliación Stripe↔BeatGaler y cola de excepciones con owner.
- [ ] Probar 3DS, rechazo, pago tardío, renewal failed, cancel, upgrade/downgrade y refund.
- [ ] Separar accesos inmediatamente peligrosos de grace periods aprobados.

**Dependencias:** Día 17.  
**Evidencia:** 100% de escenarios de billing esperados reconciliados en sandbox.  
**Gate de salida:** no existe pago sin plan correcto ni plan pagado sin evento/ledger justificable.

### Día 19 — 17 de septiembre — Dominio, identidad, legal y soporte

**Resultado:** una persona real sabe quién opera BeatGaler, qué acepta y dónde pedir ayuda.

**Tarea 19.1 [P0/P1 · LF/RO] — Identidad pública.**

- [ ] Fijar nombre, bundle ID, dominio, API/status/support URLs y sender domains.
- [ ] Configurar DNS/TLS, redirects canónicos y callbacks OAuth exactos.
- [ ] Registrar versión/fecha de Terms/Privacy aceptada en signup.

**Tarea 19.2 [P0/P1 · LF/FE] — Legal y soporte operable.**

- [ ] Privacy describe Telegram, pagos, providers, retención, export/delete y transferencias reales.
- [ ] Terms/refund/cancelación/renewal y contacto sin placeholders, aprobados por owner legal.
- [ ] Soporte con intake, severidad, SLA propuesto, recuperación, abuso/seguridad, refund y escalación.

**Dependencias:** flujos reales de cuenta/datos/pago ya definidos.  
**Evidencia:** URLs versionadas, aceptación E2E y prueba de ticket/escalación.  
**Gate de salida:** copy y comportamiento coinciden; ningún placeholder o promesa ausente.

### Día 20 — 18 de septiembre — Observabilidad, capacidad y recovery

**Resultado:** fallos se detectan, limitan y recuperan antes de afectar a todos.

**Tarea 20.1 [P1 · OP/BE] — Operación.**

- [ ] Logs estructurados/redactados, métricas, tracing/error reporting y retention.
- [ ] Dashboards/alerts para auth, API, DB, Stripe, Telegram, lease pool, queue, backup y release.
- [ ] On-call, runbook, status page, severidad y kill switches de registro/pagos/uploads.

**Tarea 20.2 [P1 · OP/QA] — Capacity envelope.**

- [ ] Definir pico esperado y probar al doble durante 60 minutos como target propuesto.
- [ ] Medir lease/upload/index latency, errores Telegram, queue depth y recuperación.
- [ ] Añadir admission control, per-bot ceiling, 30% de margen propuesto y waitlist; no exigir “80 bots” sin necesidad medida.

**Dependencias:** staging production-shaped.  
**Evidencia:** dashboard, alert delivery, load report y dependency-loss drill.  
**Gate de salida:** alertas accionables y capacidad medida; 0 fuga cross-tenant bajo carga.

## Fase 4 — Artefactos desktop confiables y release chain

**Fechas:** 21–25 de septiembre  
**Objetivo:** instaladores reconocidos por Windows/macOS y updater reversible desde un SHA único.

### Día 21 — 21 de septiembre — Manifest e identidad únicos

**Resultado:** Web, backend y desktop comparten versión, endpoints y matriz de capabilities.

**Tarea 21.1 [P1 · DE/RO] — Release manifest.**

- [ ] Fijar bundle ID final antes de migrar app-data/updater.
- [ ] Unificar VERSION/npm/Cargo/Tauri/Settings, endpoint y channel.
- [ ] Incluir runtimes Windows presentes en Cloud y recursos universales macOS con digests.

**Tarea 21.2 [P1 · DE/QA] — Migración y compatibilidad.**

- [ ] Probar upgrade desde 0.7.4 y preservar settings/SQLite/offline/cache.
- [ ] Probar instalación limpia y datos corruptos/incompletos con recovery seguro.
- [ ] Generar artefactos de staging desde el mismo SHA.

**Dependencias:** release branch y app identity del Día 19.  
**Evidencia:** manifest diff, version check y upgrade test.  
**Gate de salida:** no hay versión/endpoints divergentes ni runtime omitido.

### Día 22 — 22 de septiembre — Windows firmado

**Resultado:** instalador y binarios Windows tienen publisher verificable.

**Tarea 22.1 [P0 · DE/OP] — Authenticode.**

- [ ] Integrar certificado/servicio de firma sin exponer private key.
- [ ] Firmar binarios e instalador NSIS con timestamp; verificar cadena tras descarga.
- [ ] Conservar firma Tauri de updater como capa separada.

**Tarea 22.2 [P1 · QA/DE] — Matriz limpia.**

- [ ] Instalación/upgrade/uninstall como usuario estándar y UAC esperado.
- [ ] SmartScreen/antivirus, paths no ASCII/largos, offline/poor network y sleep/wake.
- [ ] DAWs y versiones Windows declaradas por product owner; updater válido e inválido.

**Dependencias:** certificado disponible y manifest Día 21.  
**Evidencia:** `signtool verify`, timestamp, screenshots/logs clean-machine.  
**Gate de salida:** Windows no muestra publisher desconocido y core flows pasan tras instalar.

### Día 23 — 23 de septiembre — macOS firmado y notarizado

**Resultado:** DMG/app aceptados por Gatekeeper en Intel y Apple Silicon soportados.

**Tarea 23.1 [P0 · DE/OP] — Developer ID.**

- [ ] Revisar entitlements/hardened runtime y firmar nested binaries en orden correcto.
- [ ] Enviar con `notarytool`, esperar Accepted, staple ticket a app/DMG y verificar offline.
- [ ] Custodiar/rotar certificado y credenciales mediante secretos de entorno protegido.

**Tarea 23.2 [P1 · QA/DE] — Matriz física.**

- [ ] Instalar desde descarga en cuenta limpia, verificar Gatekeeper/Finder y first run.
- [ ] Intel + Apple Silicon, macOS mínimo 12 y versiones declaradas; sleep/wake/firewall/disk pressure.
- [ ] DAWs declarados, updater válido/inválido y preservación de app-data.

**Dependencias:** membership/certificado y binarios universales.  
**Evidencia:** codesign/notary/stapler/spctl y logs físicos.  
**Gate de salida:** artefacto notarizado/stapled y core flows pasan en ambas arquitecturas prometidas.

### Día 24 — 24 de septiembre — Updater, procedencia y rollback

**Resultado:** una mala versión puede detenerse o revertirse sin sobrescribir evidencia.

**Tarea 24.1 [P0/P1 · DE/OP] — Cadena inmutable.**

- [ ] Tag protegido debe resolver exactamente al SHA de los runs consumidos.
- [ ] Checksums, SBOM y provenance por artefacto; eliminar selección arbitraria y `--clobber` final.
- [ ] Canales internal/beta/stable, porcentaje/rings, minimum version y kill switch.

**Tarea 24.2 [P1 · QA/DE] — Lifecycle updater.**

- [ ] Update desde N-1, cancelación, red cortada, disco lleno, firma inválida y manifest alterado.
- [ ] Reinicio/recovery y rollback a la versión compatible anterior.
- [ ] Ensayar retiro de `latest.json`/artefacto malo y comunicación de incidente.

**Dependencias:** artefactos firmados.  
**Evidencia:** release ledger, attestation y rollback rehearsal.  
**Gate de salida:** tag→SHA→artefacto es demostrable y rollback cumple runbook.

### Día 25 — 25 de septiembre — Matriz cross-platform y freeze estructural

**Resultado:** candidato beta conserva funciones y el rediseño deja de cambiar estructura.

**Tarea 25.1 [P1 · QA/FE/DE] — Suite completa.**

- [ ] Web Chrome/Safari/Firefox/iPhone; Windows y macOS físicos; cuenta limpia y upgrade.
- [ ] Auth/import/Review/playback/edit/Trash/offline/YouTube/updater/billing por capability.
- [ ] Comparar datos al refresh/restart y confirmar cero llamadas de plataforma inválida.

**Tarea 25.2 [P1/P2 · DL/RO] — Design freeze.**

- [ ] Aprobar tokens, navegación, library, drawer, player, settings y wizard.
- [ ] Registrar P2/P3 restantes; solo a11y/copy/error/regresión entra antes de RC.
- [ ] Preparar guion beta, formulario y criterios P0/P1/P2.

**Dependencias:** Fases 2–4.  
**Evidencia:** matriz firmada, snapshots y backlog triage.  
**Gate de salida:** beta candidate `0.9.0-beta.1`, 0 P0 conocido y ningún P1 core conocido.

## Fase 5 — Dos betas, carga y release candidate

**Fechas:** 28 de septiembre–2 de octubre  
**Objetivo:** validar usuarios reales controlados, fallos y operación antes de congelar RC.

### Día 26 — 28 de septiembre — Beta 1 guiada

**Resultado:** al menos 12 testers representativos completan el guion en las tres plataformas.

**Tarea 26.1 [P1 · QA/Support] — Distribuir con seguridad.**

- [ ] Cohortes por Web/Windows/macOS/arquitectura/navegador; consentimiento y canal de soporte.
- [ ] Instalación, onboarding, importación, Review, player, edit, Trash y updater.
- [ ] Billing sandbox o compra real de owner únicamente; no cobrar testers por accidente.

**Tarea 26.2 [P1 · OP/RO] — Observar.**

- [ ] Correlacionar IDs de soporte sin exponer archivos/nombres/tokens.
- [ ] Revisar API/DB/Stripe/Telegram/bots y alertas durante la sesión.
- [ ] Clasificar P0 seguridad/datos, P1 core, P2 crecimiento y P3 polish.

**Dependencias:** beta candidate y soporte/on-call.  
**Evidencia:** tasa de finalización por flujo, tickets y dashboard.  
**Gate de salida:** 12 guiones completos o causa documentada; cualquier P0 detiene la beta.

### Día 27 — 29 de septiembre — Corrección y regresión Beta 1

**Resultado:** todos los P0/P1 de Beta 1 cerrados con test.

**Tarea 27.1 [P0/P1 · Owners] — Triage estricto.**

- [ ] Repro mínimo, causa raíz, fix, test y reviewer por hallazgo.
- [ ] No combinar refactors o delight no relacionados.
- [ ] Data repair script solo con dry-run, backup y aprobación.

**Tarea 27.2 [P1 · QA] — Revalidar.**

- [ ] Suites afectadas y regresión completa del candidato.
- [ ] Repro en el dispositivo/navegador original.
- [ ] Confirmar que fix no cambia legal, billing o formato sin migración.

**Dependencias:** evidencia Beta 1.  
**Evidencia:** issue→PR→test→retest enlazado.  
**Gate de salida:** 0 P0/P1 abierto; P2 tiene owner o aceptación explícita antes de crecimiento.

### Día 28 — 30 de septiembre — Carga y game day

**Resultado:** BeatGaler degrada de forma controlada y se recupera.

**Tarea 28.1 [P1 · OP/BE/QA] — Carga.**

- [ ] Cuenta limpia, refresh, lease, import/upload, playback Range, index commits y webhooks al 2× del pico propuesto.
- [ ] Archivos grandes dentro de límites; queues/admission y saturación controlada.
- [ ] Comparar pool actual vs capacidad requerida; agregar bots solo si la métrica lo exige.

**Tarea 28.2 [P0/P1 · OP] — Fallas deliberadas.**

- [ ] API/DB/Stripe/Telegram/bot/master/SSE caídos o lentos; estado pool corrupto.
- [ ] Kill switches, fail closed, retry bounded, alert, status y recovery.
- [ ] Restore de backup y rollback de app/deploy durante el ejercicio.

**Dependencias:** monitoring y runbooks.  
**Evidencia:** load/game-day report con timeline y acciones.  
**Gate de salida:** sin pérdida/cross-tenant; RPO/RTO y alert delivery dentro de targets aprobados.

### Día 29 — 1 de octubre — Beta 2 no guiada

**Resultado:** testers nuevos completan sin ayuda los flujos de lanzamiento.

**Tarea 29.1 [P1 · QA/DL] — Usabilidad real.**

- [ ] Al menos 8 testers nuevos, distribuidos por plataformas; primero observación, luego entrevista.
- [ ] Medir tiempo/abandono/error de signup→first beat→play→edit→restore.
- [ ] Probar recuperación, delete/export, billing/portal y soporte.

**Tarea 29.2 [P1 · RO/Owners] — Cierre.**

- [ ] P0/P1 tienen fix o el release se mueve; no se “aceptan” por fecha.
- [ ] P2 que afecta crecimiento tiene compensación/limitación y owner.
- [ ] Validar copy final, download page, changelog y known limitations.

**Dependencias:** Día 28 exitoso.  
**Evidencia:** guiones, métricas, tickets y aceptación por plataforma.  
**Gate de salida:** 0 P0/P1; core-flow completion objetivo ≥90% sin asistencia para cohorte propuesta.

### Día 30 — 2 de octubre — RC inmutable

**Resultado:** `1.0.0-rc.1` queda congelado y reproducible.

**Tarea 30.1 [P0 · RO/OP/DE] — Cortar RC.**

- [ ] Tag protegido y firmado; generar todos los artefactos desde el mismo SHA.
- [ ] SBOM, checksums, signatures, notarization ticket, migrations y release notes.
- [ ] Promover a staging; no reconstruir manualmente para producción.

**Tarea 30.2 [P0/P1 · QA/Security/LF] — Gate formal.**

- [ ] Suite completa, advisory/secret/license scan y revisión de diferencias desde beta.
- [ ] Security, legal, payments, support, recovery y platform sign-offs.
- [ ] Abrir change freeze: solo hotfix P0/P1 con nueva RC y repetición de gates afectados.

**Dependencias:** dos betas y game day.  
**Evidencia:** release dossier firmado.  
**Gate de salida:** RC inmutable, 0 P0/P1 y 100% de confirmaciones launch-critical con evidencia.

## Fase 6 — Ensayo, soft launch y publicación

**Fechas:** 5–9 de octubre  
**Objetivo:** promover el RC sin cambiarlo, observar y abrir gradualmente.

### Día 31 — 5 de octubre — Ensayo final de producción

**Resultado:** cada operación irreversible se ejecuta una vez de forma controlada.

**Tarea 31.1 [P0 · QA/LF/OP] — Transacción real controlada.**

- [ ] Owner crea cuenta limpia, verifica, compra, recibe entitlement, cancela y obtiene refund.
- [ ] Reconciliar Stripe/BeatGaler/banco según disponibilidad y borrar/exportar cuenta de prueba.
- [ ] Confirmar emails, Terms version, support ticket y status link.

**Tarea 31.2 [P0 · QA/DE/OP] — Disaster rehearsal.**

- [ ] Instalar descargas públicas candidatas en equipos limpios.
- [ ] Backup→restore, app rollback, updater rollback y cierre de registro/pagos/uploads.
- [ ] Verificar que todas las alertas llegan al owner de guardia.

**Dependencias:** RC.  
**Evidencia:** conciliación a cero, install logs y runbook timestamps.  
**Gate de salida:** ensayo completo sin intervención improvisada.

### Día 32 — 6 de octubre — Soft launch a 25 usuarios

**Resultado:** producción atiende una cohorte limitada con soporte activo.

**Tarea 32.1 [P0/P1 · RO/OP] — Apertura gradual.**

- [ ] 25 invitaciones propuestas, límite de registros y capacidad reservada.
- [ ] Web y descargas desde URLs definitivas; stable updater solo para cohorte.
- [ ] Staff de incidente, soporte y pagos disponible.

**Tarea 32.2 [P1 · QA/OP] — Observación.**

- [ ] Revisar a 15 min, 1 h, 4 h y 8 h: auth, errors, latency, DB, Stripe, bots, queues.
- [ ] Contactar usuarios afectados y pausar con kill switch si cruza threshold.
- [ ] Hotfix solo P0/P1 mediante nueva RC y smoke.

**Dependencias:** Día 31.  
**Evidencia:** dashboard anotado y ledger de cohortes/incidentes.  
**Gate de salida:** 8 horas sin P0/P1 y 100% de pagos reconciliados.

### Día 33 — 7 de octubre — Soak de 24 horas

**Resultado:** operación estable durante un ciclo completo.

**Tarea 33.1 [P1 · OP/LF] — Continuidad.**

- [ ] Monitorear jobs nocturnos, backups, session expiry, webhooks y bot maintenance.
- [ ] Responder tickets bajo SLA propuesto y probar handoff de guardia.
- [ ] Revisar logs por secretos/datos y alertas ruidosas/silenciosas.

**Tarea 33.2 [P1 · RO/QA] — Cohort review.**

- [ ] Core-flow completion, crashes, errores, conversion y soporte por plataforma.
- [ ] Reconciliar pagos/planes y storage/index.
- [ ] Decidir continuar, mantener cohorte o rollback.

**Dependencias:** soft launch activo.  
**Evidencia:** informe 24 h y reconciliación.  
**Gate de salida:** 24 h sin incidente crítico y sin deuda de datos/dinero.

### Día 34 — 8 de octubre — Decisión pública

**Resultado:** una decisión binaria, auditable y comunicable.

**Tarea 34.1 [P0 · RO + approvers] — Go/no-go.**

- [ ] Revisar cada gate obligatorio y owner confirmation.
- [ ] Security, QA, Desktop, Ops, Legal/Finance y Support firman o bloquean.
- [ ] Cualquier P0/P1, pago no reconciliado o plataforma no probada produce NO-GO.

**Tarea 34.2 [P1 · RO/LF] — Preparar comunicación.**

- [ ] Landing, downloads, checksum/signature help, pricing, FAQ, status y support.
- [ ] Anuncio y rollback/delay message preparados antes de abrir.
- [ ] Snapshot final de datos/config y staffing de 8 horas.

**Dependencias:** soak aprobado.  
**Evidencia:** acta go/no-go y checklist firmada.  
**Gate de salida:** solo un GO unánime de gates permite el Día 35.

### Día 35 — 9 de octubre — Lanzamiento público

**Resultado:** BeatGaler disponible públicamente con rollout controlado.

**Tarea 35.1 [P0 · OP/RO] — Rollout.**

- [ ] Abrir 10%, luego 50% y 100% de capacidad propuesta solo tras checkpoints.
- [ ] Abrir registro, Web, Windows, macOS y planes desde el mismo release dossier.
- [ ] Congelar cambios no críticos; rollback/kill switches listos.

**Tarea 35.2 [P1 · Todos] — Operar ocho horas.**

- [ ] Seguimiento continuo de seguridad, errores, pagos, datos, bots, tickets y downloads.
- [ ] Reconciliar cada compra y muestrear export/delete/updater.
- [ ] Publicar status transparente; incident command ante cualquier threshold.

**Dependencias:** GO del Día 34.  
**Evidencia:** snapshots pre/post, dashboard, ledger de release y reporte de 8 h.  
**Gate de salida:** 100% abierto o rollback controlado; nunca estado ambiguo.

## Fase 7 — Buffer y estabilización

**Fechas:** 10–16 de octubre  
**Objetivo:** proteger datos/dinero, estabilizar y convertir feedback en roadmap.

### Día 36 — 10–11 de octubre — Guardia de fin de semana

**Resultado:** cobertura continua sin introducir cambios de alcance.

**Tarea 36.1 [P0/P1 · OP/Support] — Triage.**

- [ ] Vigilar cuentas, pagos, corrupción, cross-tenant, updater y firma.
- [ ] Hotfix solo con repro, test, approval, canary y rollback.
- [ ] Mantener status y comunicación a usuarios afectados.

**Dependencias:** lanzamiento.  
**Evidencia:** handoff y timeline de incidentes.  
**Gate de salida:** ningún P0/P1 sin owner/respuesta.

### Día 37 — 12 de octubre — Conciliación y restore de rutina

**Resultado:** dinero y datos cierran sin excepciones ocultas.

**Tarea 37.1 [P0 · LF/BE/OP] — Cierre operativo.**

- [ ] Stripe↔BeatGaler, refunds/disputes, entitlements y cuentas huérfanas.
- [ ] Verificar backup diario y restaurar una muestra aislada.
- [ ] Revisar garbage journal, Trash physical deletes y bot memberships.

**Dependencias:** datos del lanzamiento.  
**Evidencia:** conciliación a cero o cola con owner/SLA.  
**Gate de salida:** sin deuda financiera o de integridad no explicada.

### Día 38 — 13 de octubre — Rendimiento y capacidad real

**Resultado:** configuración se ajusta a tráfico observado, no a intuición.

**Tarea 38.1 [P2 · OP/FE/BE] — Analizar.**

- [ ] p50/p95/p99, Web vitals, memory, chunk/cache, uploads, lease y queue por plataforma.
- [ ] Comparar pico real con envelope y margen; ajustar admission/alerts.
- [ ] Priorizar thumbnails/lazy load/query/indexes donde la evidencia lo muestre.

**Dependencias:** telemetría suficiente.  
**Evidencia:** reporte antes/después y budgets.  
**Gate de salida:** capacity plan actualizado sin ampliar innecesariamente la flota.

### Día 39 — 14 de octubre — Experiencia y soporte

**Resultado:** feedback se convierte en problemas reproducibles y prioridades.

**Tarea 39.1 [P2/P3 · DL/QA/Support] — Síntesis.**

- [ ] Agrupar fricción por flujo/plataforma; separar bug, copy, educación y feature.
- [ ] Revisar abandono de onboarding/import/checkout y top tickets.
- [ ] Mantener P0/P1 en carril inmediato; P2/P3 al roadmap.

**Dependencias:** métricas/tickets.  
**Evidencia:** insight→evidencia→owner→fecha.  
**Gate de salida:** backlog priorizado sin duplicados ni peticiones vagas.

### Día 40 — 15 de octubre — Patch candidate

**Resultado:** primera actualización pequeña y segura, solo si hace falta.

**Tarea 40.1 [P1/P2 · Owners/QA] — Preparar `1.0.1`.**

- [ ] Elegir fixes de alto impacto/bajo riesgo; no rediseño amplio.
- [ ] Suite completa afectada, firmas, notarización y beta ring.
- [ ] Update/rollback y release notes verificadas.

**Dependencias:** backlog y necesidad real.  
**Evidencia:** release dossier de patch.  
**Gate de salida:** publicar solo si mejora riesgo neto; si no, no forzar versión.

### Día 41 — 16 de octubre — Postmortem y roadmap

**Resultado:** lanzamiento cerrado como aprendizaje operacional.

**Tarea 41.1 [P2 · RO/Todos] — Revisión.**

- [ ] Qué funcionó, qué falló, detección, respuesta y costos.
- [ ] Actualizar runbooks, gates, SLOs y ownership.
- [ ] Priorizar i18n, motion de deleite, stores, mobile nativo y funciones aplazadas.

**Dependencias:** una semana de datos.  
**Evidencia:** postmortem sin culpa y roadmap aprobado.  
**Gate de salida:** operación normal, owners permanentes y deuda de lanzamiento visible.

## Condiciones obligatorias para publicar

### Fuente y automatización

- [ ] Un solo tag/SHA genera Web, backend, Windows, macOS, updater, SBOM y checksums.
- [ ] Branch protection, reviews, environments y required checks activos.
- [ ] Frontend, backend, Rust, integración, regresiones, browser E2E, packaging y security scans verdes.
- [ ] Cero vulnerabilidad critical/high conocida en producción o build/release; excepciones solo con owner, compensación y expiración aprobada.
- [ ] Artefactos no se sobrescriben y la procedencia es verificable.

### Seguridad

- [ ] Ninguna credencial Telegram compartida llega a cliente/bundle/worker/log.
- [ ] Identidad tenant deriva de sesión; autorización y límites preceden a upload/Telegram.
- [ ] Sesión Web, CSP, headers, CORS/CSRF y origen API aprobados; parser ID3 local/pinned.
- [ ] Local API desktop no puede ser suplantada por otro proceso.
- [ ] Cross-tenant, replay, expiry, SSRF, rate limit y abuso tienen pruebas negativas.
- [ ] Incidente de estado rastreado cerrado y secrets/data scan limpio.

### Web

- [ ] Cuenta nueva → índice vacío → Add Beat → Review → Save → refresh.
- [ ] Save All y bulk edit son transacciones Web o la acción no se presenta como disponible.
- [ ] Playback/download tienen límites y fallbacks probados en navegadores soportados.
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
- [ ] 3DS, rechazo, renewal failure, cancel, upgrade/downgrade y refund pasan.
- [ ] Compra real controlada y refund quedan reconciliados a cero.
- [ ] Si cualquier punto falla, el release no cobra; “free-only” requiere copy y scope propios.

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
- [ ] Capacity envelope al 2× del pico propuesto pasa sin fuga tenant; admission/waitlist disponible.
- [ ] Dos betas; mínimo 12 testers en Beta 1 y testers nuevos en Beta 2.
- [ ] Soft launch 8 h + soak 24 h sin P0/P1 ni pago/dato pendiente.

### Identidad y legal

- [ ] Marca, entidad, bundle ID, dominio, DNS/TLS, release repo y emails tienen owner.
- [ ] Privacy, Terms, refund/cancelación y aceptación versionada aprobados.
- [ ] LICENSE/EULA/notices/codec y subprocesadores revisados.
- [ ] Soporte, seguridad/abuso, recovery y finanzas tienen escalación y cobertura.

## Regla de publicación

> **NO PUBLICAR** mientras exista un P0 o P1; un owner confirmation launch-critical sin evidencia; un pago no reconciliado; una migración/restore/rollback no demostrado; o una plataforma/navegador anunciado sin prueba.

Un hotfix que toca auth, datos, pagos, transporte, firma o migración crea una nueva RC y repite todos los gates dependientes. La presión de fecha no cambia esta regla.

## Métricas y umbrales de éxito

Los valores siguientes son **targets propuestos** para aprobar por RO/owners; no describen el estado actual.

### Seguridad e integridad

- 0 P0/P1 conocidos y 0 fuga cross-tenant en pruebas adversariales/carga.
- 0 secreto de infraestructura en cliente, artefactos, repo o logs.
- 100% de rutas mutantes con auth/tenant/ownership y negative tests.
- 100% de compras, refunds y cambios de entitlement reconciliados.
- 100% de restores de ensayo concluyen con core-flow verification.

### Producto

- ≥90% de testers nuevos completa signup→first beat→play→edit→restore sin asistencia.
- 0 pérdida silenciosa tras Save/Save All/bulk edit/refresh/restart.
- 100% de los flujos críticos pasa en cada plataforma/navegador anunciado.
- 0 defecto crítico de teclado, focus, contraste o lector en dichos flujos.

### Web y backend

- Core Web Vitals propuestos en p75: LCP ≤2.5 s, INP ≤200 ms, CLS ≤0.1 en páginas Web públicas/app dentro de escenarios medidos.
- Error rate de requests core <1% y disponibilidad de soak ≥99.9%, excluyendo fallas deliberadas documentadas.
- RPO propuesto ≤24 h y RTO propuesto ≤2 h, sustituidos por targets más estrictos si legal/negocio lo exige.
- Load test al 2× del pico esperado durante 60 min, sin corrupción, fuga o cola ilimitada.

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

Si una sola persona cubre `R` y `A`, se requiere un reviewer externo para security, legal y firma/release; la fecha usa la ruta conservadora.

## Registro de riesgos

| Riesgo | Prob. | Impacto | Señal temprana | Prevención/respuesta | Owner |
|---|---:|---:|---|---|---|
| Rediseño del transporte Telegram excede estimación | Alta | Crítico | capability/proxy no pasa cross-tenant al 1 Sep | mantener registro cerrado; cortar alpha; no parchear con cifrado cliente | BE/Security |
| Certificados Apple/Windows llegan tarde | Media | Crítico | no disponibles el 27 Ago | mover a 30 Oct; no distribuir unsigned | DE/RO |
| Migración JSON→Postgres pierde/duplica | Media | Crítico | dry-run difiere o rollback falla | snapshot, idempotencia, quarantine, doble comparación | BE/OP |
| Merge rompe funciones Cloud/Web | Alta | Alto | contrato/capability o 4 conflictos fallan | integrar por slices y bisectar; no merge ciego | FE/DE/QA |
| Billing diverge de Stripe | Media | Crítico | eventos huérfanos/duplicados o ledger ≠ Stripe | idempotencia, outbox/reconciliation, pause payments | BE/Finance |
| Bot/master se satura o cruza tenant | Media | Crítico | queue/lease/error sube, ceiling alcanzado | admission control, per-bot ceiling, waitlist, revoke | BE/OP |
| Safari/iPhone consume RAM por fallback | Alta | Alto | memory/crash en archivo grande | streaming/límites; recortar soporte con copy explícito | FE/QA |
| Firma/notarización rompe nested runtimes | Media | Alto | codesign/notary falla o app no inicia | firmar en orden, entitlements mínimos, clean-device CI | DE |
| Legal/copy no coincide con conducta | Media | Crítico | placeholder o deletion/payment claim falso | revisión tras implementar, documentos versionados | LF/RO |
| Solo developer se convierte en cuello de botella | Alta | Alto | gates sin reviewer y tareas paralelas atrasadas | fecha 30 Oct, external reviewers, WIP limit | RO |
| Herramientas dev vulnerables comprometen build | Media | Alto | audit critical/high o action mutable | upgrade/pin/scan/SBOM y runner protegido | OP/QA |
| P0 aparece durante beta/soft launch | Media | Crítico | data/security/payment anomaly | stop, kill switch, incident, rollback, nueva RC | Incident owner |

## Caminos de contingencia

### Si el 4 de septiembre no pasa seguridad

- No alpha remota; demo local con datos sintéticos.
- Mantener registro, pagos y uploads públicos cerrados.
- El plan del 9 de octubre se reestima por el blocker, no por días “perdidos”.

### Si Stripe no está listo el 18 de septiembre

- Opción A: mover el lanzamiento pagado.
- Opción B: preview pública free-only con pricing/CTA/copy retirados y quotas coherentes.
- No existe opción de cobrar y conciliar manualmente.

### Si firma Windows o macOS no está lista el 23 de septiembre

- Si el objetivo sigue siendo simultáneo: mover todo el lanzamiento.
- Si RO cambia explícitamente el alcance: publicar Web como preview y marcar desktop “coming later” sin distribuir unsigned.
- Una firma Tauri `.sig` no sustituye confianza de OS.

### Si Safari/iPhone no cumple memoria/performance

- Corregir streaming y repetir beta; o reducir la matriz soportada con copy público y detección.
- No anunciar “Web móvil” solo porque el login cabe a 390 px.

### Si capacidad Telegram es insuficiente

- Activar waitlist/admission, limitar uploads/sesiones y escalar solo tras medir.
- No multiplicar bots compartidos hasta probar aislamiento y rotation.

### Si aparece un P0 después del soft launch

- Congelar registro/pagos/uploads según blast radius.
- Rollback de artefacto/deploy y preservar datos/evidencia.
- Notificar status/afectados, reconciliar dinero/datos y crear nueva RC.

## Confirmaciones del propietario pendientes

Antes de marcar GO, el owner debe aportar evidencia fechada sobre:

- protecciones GitHub, reviewers, environments, secrets, retention y ownership de release repo;
- dominio/DNS/TLS/WAF/proxy, hosts reales, regiones de datos y contratos de proveedores;
- procedencia del backup operativo rastreado y rotación/remediación relacionada;
- Apple Developer ID y Authenticode: custodia, expiración, timestamp y clean-device results;
- private key del updater, match con public key, backup, rotation y kill switch;
- Stripe live, productos/precios/tax/refunds/disputes/webhooks/reconciliation y owner financiero;
- entidad, marca, jurisdicciones, edad, Privacy/Terms/refund/DPA/subprocesadores y licencias;
- soporte, security/abuse contact, cobertura y autoridad de recuperación;
- ownership/políticas Telegram, storage/rate limits, concurrencia esperada y drills;
- OS/arquitecturas/DAWs/navegadores realmente soportados y hardware disponible.

Hasta entonces su estado es **`needs owner confirmation`**, nunca “listo”.

## Fuentes externas de criterios

- [Tauri — Windows code signing](https://tauri.app/distribute/sign/windows/): la firma del instalador/publisher es distinta de la firma del updater y evita una experiencia de descarga no confiable.
- [Tauri — macOS code signing](https://v2.tauri.app/distribute/sign/macos/) y [Apple — notarizing macOS software](https://developer.apple.com/documentation/security/notarizing-macos-software-before-distribution): Developer ID, hardened runtime, notarización, stapling y Gatekeeper para distribución directa.
- [Stripe — Checkout subscriptions](https://docs.stripe.com/payments/checkout/build-subscriptions), [webhooks](https://docs.stripe.com/webhooks?lang=node), [subscription webhooks](https://docs.stripe.com/billing/subscriptions/webhooks?locale=en-GB) e [idempotency](https://docs.stripe.com/api/idempotent_requests): el redirect no es fuente de verdad; eventos firmados, duplicados y reintentos deben manejarse server-side.
- [OWASP — Session Management](https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html), [Forgot Password](https://cheatsheetseries.owasp.org/cheatsheets/Forgot_Password_Cheat_Sheet.html), [XSS](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html), [CSRF](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Site_Request_Forgery_Prevention_Cheat_Sheet.html) y [HTTP Headers](https://cheatsheetseries.owasp.org/cheatsheets/HTTP_Headers_Cheat_Sheet.html): base del gate de sesión/navegador.
- [Cloudflare Pages — Git integration](https://developers.cloudflare.com/pages/get-started/git-integration/), [custom domains](https://developers.cloudflare.com/pages/configuration/custom-domains/) y [rollbacks](https://developers.cloudflare.com/pages/configuration/rollbacks/): opción propuesta, no cuenta confirmada.
- [Railway — PostgreSQL](https://docs.railway.com/databases/postgresql) y [backups/restores](https://docs.railway.com/guides/postgres-backups-restores): opción propuesta; backup y restore probado siguen siendo responsabilidades separadas.

## Estado final esperado

- [ ] Rama `1.0.0` integrada y protegida.
- [ ] Web pública responsive, accesible y segura.
- [ ] Windows firmado, instalado y actualizable.
- [ ] macOS Developer ID/notarizado/stapled y probado.
- [ ] Datos migrados, respaldados y restaurados.
- [ ] Cuentas recuperables, exportables y eliminables.
- [ ] Pagos y quotas reconciliados, o alcance free-only verdadero.
- [ ] Dominio, legal, soporte, status y monitoreo activos.
- [ ] Capacidad demostrada; no una cantidad arbitraria de bots.
- [ ] Dos betas, soft launch y soak sin P0/P1.
- [ ] Go/no-go firmado y BeatGaler publicado con rollback listo.



