

**Fecha de la auditoría: 11 de septiembre de 2026.**

**Recomendación:** evolucionar las piezas útiles existentes, usar **Polar como proveedor principal**, mantener **PostgreSQL como autoridad operativa del acceso** y separar las políticas de producto del transporte.

Hay dos prerrequisitos que impiden tratar esta etapa como “conectar un proveedor”:

1. **Las escrituras actuales de Direct no tienen una frontera confiable que pueda imponer cuotas contra un cliente manipulado.**
    
2. **YouTube existe principalmente mediante Tauri; no encontré un flujo Web equivalente listo para proteger y vender.**
    

El diseño siguiente contempla ambos. No doy por resueltos esos problemas ni propongo ocultarlos detrás de pruebas simuladas.

No modifiqué código, archivos, ramas, configuración ni productos. Ejecuté únicamente los cuatro archivos de tests existentes de billing: **27 tests pasaron**. No ejecuté migraciones ni pruebas contra pagos reales o sandbox.

---

# 1. Estado real actual

## 1.1 Rama de referencia

Consulté las ramas y PRs en GitHub, contrasté sus SHAs con los objetos locales y comparé ancestry.

|Referencia|SHA observado|Interpretación|
|---|---|---|
|Rama predeterminada de GitHub: `integration-v0.9.0-alpha.3`|`8c738d8`|No es la más avanzada.|
|`integration-v0.9.0-alpha.4`|`8314f66`|Base de integración más reciente.|
|Checkout habitual: `fix/web-dev-cloud-origin-source-of-truth`|`eb4f749`|Incluye cuatro commits posteriores a alpha.4.|
|`direct/persistent-vault-assignment`|`a112563`|Rama más avanzada y relevante para este diseño.|

La rama persistente contiene el checkout habitual: **0 commits exclusivos del checkout y 75 exclusivos de la rama persistente**. Frente a alpha.4, está **79 commits por delante, sin divergencia**.

El worktree adicional está en `E:\777\app\beatvault-persistent`. Había cambios locales ajenos en el helper de transporte; el checkout habitual también tenía modificaciones de diagnóstico. No los alteré.

PRs relevantes:

- [#139: corrección del origen Cloud en Web dev](https://github.com/magosouljah/BeatGaler/pull/139): abierto, draft.
    
- [#135: corrección anterior de loopback](https://github.com/magosouljah/BeatGaler/pull/135): abierto, draft.
    
- [#138: contrato de descarga Direct](https://github.com/magosouljah/BeatGaler/pull/138): mergeado.
    
- [#134: carrera de resolución Cloud durante startup](https://github.com/magosouljah/BeatGaler/pull/134): mergeado.
    
- [#132: integración de trabajo PostgreSQL y fiabilidad](https://github.com/magosouljah/BeatGaler/pull/132): mergeado.
    

Para `a112563`, GitHub reportó correctos los checks de PostgreSQL persistent assignment, Cloud unit y Direct/Web regression. **Eso acredita esos checks; no demuestra que Etapas 1 y 2 estén cerradas con usuarios reales.**

La referencia de este documento es [el commit](https://github.com/magosouljah/BeatGaler/commit/a112563646d61940c7c16e025702329c1219b4f7) `[a112563](https://github.com/magosouljah/BeatGaler/commit/a112563646d61940c7c16e025702329c1219b4f7)`, no la rama predeterminada.

## 1.2 Qué existe y qué falta

|Área|Estado comprobado|
|---|---|
|Catálogo|Tres planes, cuotas y capacidades server-side.|
|Bienvenida|Grant de siete días de Paid Entry en el modelo histórico.|
|Auth/Account|Devuelve el plan calculado desde `user.planState`.|
|PostgreSQL|Tiene `entitlements`, suscripciones, eventos de webhook, reservas y excepciones de reconciliación.|
|Checkout|Contrato genérico con selección server-side e identidad asociada al usuario.|
|Webhooks|Contrato de verificación, deduplicación y transacción. Sin integración concreta de proveedor.|
|Entitlements de billing|Otro cálculo de plan, basado únicamente en estado de suscripción.|
|Reservas|Suma genérica acumulada; no representa correctamente todas las cuotas.|
|Reconciliación|Detecta divergencias y registra excepciones; no repara el estado.|
|UI|Comparación básica, sin precios reales ni checkout operativo; botones de simulación.|
|Provider SDK|No hay SDK de Polar, Lemon Squeezy o Stripe en las dependencias Cloud inspeccionadas.|
|Enforcement|No encontré el catálogo conectado a las mutaciones reales de biblioteca o YouTube.|
|Tests|Hay contratos unitarios. No equivalen a integración PostgreSQL ni E2E de proveedor.|

Fuentes del código: [planes](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/cloud-server/plans.js), [checkout](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/cloud-server/billing-checkout.js), [webhook](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/cloud-server/billing-webhook.js), [entitlements](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/cloud-server/billing-entitlements.js) y [reconciliación](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/cloud-server/billing-reconciliation.js).

## 1.3 El problema de autoridad es real, pero tiene un matiz importante

No es exacto decir simplemente “Auth usa JSON y billing usa PostgreSQL”.

Cuando está activo el cutover PostgreSQL, la capa de compatibilidad reconstruye `user.planState` desde la tabla `entitlements`. Por tanto, ese camino puede tener PostgreSQL detrás.

El problema es que **existen dos modelos independientes de acceso**:

- `publicPlanState(user)` combina `basePlanId` y grants.
    
- `effectiveBillingPlan(subscription)` consulta otro estado y sólo reconoce `active/trialing`.
    

No existe una proyección única conectada a ambos consumidores.

Además, `replaceAuthSnapshot()` ejecuta un `**DELETE FROM entitlements**` **y repuebla la tabla desde el snapshot de Auth**. Añadir grants mediante SQL sin retirar esa escritura podría perderlos en una persistencia posterior de Auth. Es una dependencia obligatoria del primer trabajo de billing, no una limpieza opcional. [Runtime PostgreSQL actual](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/cloud-server/postgres-control-plane-runtime.js).

Otros defectos concretos:

- El evaluador de suscripciones no considera el final de período.
    
- El evaluador histórico puede atribuir una caducidad temporal a un plan base equivalente que no caduca.
    
- El identificador de bienvenida basado sólo en tiempo no es una buena identidad global persistente.
    
- Las reservas reutilizadas sólo comparan cantidad; no comprueban correctamente usuario y recurso.
    
- Las reservas no tienen ventanas diarias/mensuales ni recuperación completa de abandonos.
    
- El webhook genérico presupone un envelope parecido al de Stripe: no es verdaderamente neutral.
    
- Ordenar por timestamp del objeto no resuelve el orden entre factura, suscripción y refund.
    
- Reconciliation sólo compara cliente, suscripción, estado y plan: faltan períodos, cancelación, pagos y refunds.
    

## 1.4 Rutas que parecen importantes, pero están deshabilitadas

Las rutas históricas:

- `/beats/upload`
    
- `/projects/upload`
    
- `/cloud-files/upload`
    

son interceptadas por el arranque real y devuelven **410**. Poner checks allí no protegería los uploads actuales.

El punto de entrada relevante es [el arranque real del servidor](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/cloud-server/server.js), junto con [la desactivación de uploads legacy](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/cloud-server/legacy-media-upload-disable.js).

## 1.5 El bloqueo real del enforcement de almacenamiento

El navegador:

- recibe una sesión temporal de Direct;
    
- envía archivos mediante `sendMedia`;
    
- publica y fija el índice mediante `pinMessage`;
    
- ejecuta importaciones, ediciones y Trash en el cliente.
    

La API de capacidades valida identidad, sesión y tipo de operación, pero no incorpora el contenido completo de la mutación ni la cuota. Telegram tampoco conoce esas capacidades de BeatGaler.

**Conclusión arquitectónica:** agregar un check a `/transport/operation/begin` mejora el comportamiento del cliente oficial, pero no convierte una credencial de escritura entregada al navegador en una credencial restringida por cuota.

También hay una carrera de índice: leer `expectedMessageId`, comprobarlo y publicar después no constituye por sí solo un compare-and-swap atómico entre dos clientes.

Fuentes: [capacidades](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/cloud-server/direct-capability-boundary.js), [worker Web](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/src/features/cloud/webTransport.worker.ts) y [operaciones de biblioteca](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/src/features/cloud/webGalerCloudTransport.ts).

## 1.6 YouTube no está donde el prompt podría hacer pensar

El producto existente sube videos **a YouTube**. No encontré una importación desde YouTube equivalente a esas cuotas.

Las llamadas actuales pasan por Tauri; sin `invoke`, varias devuelven “Tauri not available”. El flujo incluye render y upload resumible en Rust.

Por tanto:

- no debe diseñarse una cuota de “YouTube import” sin precisar la operación;
    
- proteger un endpoint Cloud inexistente no completa la feature;
    
- portar YouTube a Web es un trabajo de producto separado, aunque billing deba ofrecerle la política y la persistencia.
    

Fuentes: [puente Tauri](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/src/lib/tauri.ts) y [implementación Rust](https://github.com/magosouljah/BeatGaler/blob/a112563646d61940c7c16e025702329c1219b4f7/src-tauri/src/commands.rs).

---

# 2. Decisiones de producto confirmadas

|Característica|Free|Paid Entry|Highest Paid|
|---|---|---|---|
|Mensual objetivo|Gratis|USD 6.99|USD 11.99|
|Beats, incluyendo Trash|20|100|Sin límite de plan|
|Nuevo PROJECT ZIP|No|Sí|Sí|
|Tamaño potencial/máximo PROJECT|500 MB, inactivo|1 GB|1.9 GB|
|YouTube por día|3|10|Sin límite de plan|
|YouTube por mes|31|60|Sin límite de plan|
|Bulk YouTube|`none`|`limited`|`full`|
|Early Access|No|No|Sí|

Reglas adicionales:

- El precio se configura en un único flujo server-side.
    
- El frontend nunca decide precio, pago ni acceso.
    
- Trash consume slots.
    
- Downgrade conserva los beats y su uso habitual.
    
- Los PROJECT existentes siguen disponibles después del downgrade.
    
- Cancelar al final del período conserva acceso hasta su vencimiento.
    
- Refund que invalida el pago retira el acceso comercial correspondiente.
    
- No se ha aprobado borrar datos tras refund.
    
- Bienvenida: aproximadamente siete días de Paid Entry sin exigir tarjeta.
    
- Preferencia por no limitar dispositivos ni sesiones en V1.
    

**Precisión pendiente de unidades:** el código usa múltiplos binarios y `1900 MiB`; eso no equivale exactamente a “1.9 GB”. Recomiendo fijar límites decimales de 500 000 000, 1 000 000 000 y 1 900 000 000 bytes y hacer que UI, documentación y servidor coincidan. No convertirlo silenciosamente.

---

# 3. Decisiones todavía abiertas

Estas son decisiones de producto o prerrequisitos externos; el resto del diseño puede avanzar.

|Decisión|Recomendación|Impacto|
|---|---|---|
|Mensual/anual inicial|**Mensual primero**, catálogo preparado para anual.|El anual se añade después de fijar precio y probar transiciones entre intervalos.|
|Precio anual|Pendiente, sin fórmula inventada.|No publicar CTA anual hasta tener precio real.|
|`limited` de Bulk|Configurar un máximo de videos por lote; falta el valor.|No bloquea billing; sí bloquea habilitar/comercializar ese nivel de Bulk.|
|YouTube en Web V1|Construir el flujo Web antes de anunciar esas prestaciones como disponibles en Web.|Es una dependencia real; si se pospone, requiere recortar explícitamente la oferta.|
|Cambios entre planes pagados|Para la primera versión, **al siguiente período**, usando el portal.|Reduce prorrateos, cobros fallidos de upgrades y refunds de ajustes. Upgrade inmediato sería la siguiente extensión.|
|Gracia por renovación fallida|**Siete días**, contados desde el primer fallo del período.|Sólo para clientes que ya tenían un período pagado.|
|Referral/promo público|Posponer redención pública; dejar grants listos.|Faltan elegibilidad, recompensa, acumulación y controles de abuso.|
|Inicio de bienvenida|Una vez al activar/verificar la cuenta.|No reiniciar al reconectar OAuth, reinstalar o cambiar correo.|
|Refund parcial|No retirar acceso automáticamente.|Excepción administrativa explícita cuando el acuerdo sea terminar el servicio.|
|Frontera de escritura Direct|Escrituras mediante ejecutor confiable.|Prerrequisito de cuotas estrictas.|
|Alta comercial de Polar|Validar elegibilidad, cuenta mexicana y payout real durante onboarding.|Soporte de país no garantiza aprobación de una cuenta concreta.|

### Por qué mensual primero

El anual no exige otro motor de entitlements: una fecha final puede ser mensual o anual.

Lo que añade trabajo es la combinación de:

- precio aún sin decidir;
    
- cambio mensual ↔ anual;
    
- cancelaciones y refunds de períodos largos;
    
- comunicación de renovación;
    
- política de precio anterior;
    
- pruebas adicionales.
    

Dejar `interval` preparado cuesta poco. Vender el anual sin esas decisiones cuesta bastante más.

### Por qué programar cambios entre planes pagados en V1

Es una recomendación deliberada de alcance, no una limitación del proveedor.

Free → Paid sigue siendo inmediato tras pago confirmado. Paid Entry ↔ Highest se programa para la siguiente renovación.

Así el portal resuelve cambios y cancelación sin construir una administración propia. Si se decide que el upgrade inmediato es imprescindible, se añade un endpoint pequeño de cambio con cobro inmediato y pruebas específicas; no hay que rediseñar las cuotas.

---

# 4. Comparación de proveedores

## 4.1 Comparación funcional y operacional

|Criterio|Polar|Lemon Squeezy|Stripe Payments + Billing|
|---|---|---|---|
|Modelo|Merchant of Record|Merchant of Record|BeatGaler es el vendedor; Stripe procesa y factura|
|SaaS mensual/anual|Sí|Sí|Sí|
|Checkout alojado|Sí|Sí|Sí|
|Portal|Pagos, facturas, cancelación y cambios configurables|Pagos, facturas y cambios configurables|Portal maduro y configurable|
|Upgrades/downgrades|Inmediatos, prorrateados o siguiente período|Cambios y prorrateo mediante API/portal|Amplio control, schedules y prorations|
|Cancelar/deshacer|Fin de período; reversible antes del final|Cancelación y reanudación según estado|Ambas modalidades|
|Refunds|Totales/parciales; refund de orden no cancela automáticamente suscripción|Totales/parciales; requiere sincronizar con suscripción|Totales/parciales; refund y cancelación son operaciones separadas|
|Cobros fallidos|Retries y gracia configurables|Retries y dunning incorporados|Smart Retries y recuperación configurable|
|Webhooks|Standard Webhooks; SDK oficial|HMAC del cuerpo; envelope JSON|Firma oficial, event IDs, herramientas maduras|
|Idempotencia de nuestra integración|Debe persistirse en BeatGaler|Debe persistirse en BeatGaler|Persistencia propia más idempotency keys nativas|
|Impuestos indirectos sobre ventas|Los gestiona el MoR|Los gestiona el MoR|Deben configurarse y gestionarse; Tax no convierte automáticamente a Stripe en MoR|
|México|País admitido para payouts|País admitido para payouts bancarios|Stripe México disponible|
|Testing|Sandbox separado|Test mode|Sandboxes, CLI y test clocks|
|SDK Node/TS|Oficial; transición de SDK en curso|Oficial, menor actividad observada|Oficial, mantenido activamente|
|Complejidad para BeatGaler|Baja-media|Baja-media|Media-alta por operación comercial/fiscal|
|Portabilidad|Adaptador simple; migración comercial asistida|Adaptador simple; migración requiere coordinación|Amplio ecosistema, también requiere migración de suscripciones|
|Mejor argumento|SaaS pequeño con menor carga operacional|MoR y portal integrados|Madurez técnica y control|

Fuentes funcionales: [suscripciones Polar](https://polar.sh/docs/features/subscriptions/introduction), [prorrateo Polar](https://polar.sh/docs/features/subscriptions/proration), [portal Lemon Squeezy](https://docs.lemonsqueezy.com/guides/developer-guide/customer-portal), [gestión de suscripciones Lemon Squeezy](https://docs.lemonsqueezy.com/guides/developer-guide/managing-subscriptions) y [suscripciones Stripe](https://docs.stripe.com/billing/subscriptions/webhooks).

México figura en las listas de [Polar](https://polar.sh/docs/merchant-of-record/supported-countries) y [Lemon Squeezy](https://docs.lemonsqueezy.com/help/getting-started/supported-countries). Stripe publica condiciones específicas para [México](https://stripe.com/mx/pricing).

## 4.2 Coste vigente: cuidado con comparativas antiguas

Para una organización nueva, Polar ya no debe presupuestarse automáticamente como “4% + 40¢”.

|Concepto|Polar Starter nuevo|Lemon Squeezy|Stripe México|
|---|---|---|---|
|Base por transacción|5% + USD 0.50|5% + USD 0.50|3.6% + MXN 3|
|Recurrencia|Sin recargo separado en Starter|+0.5%|Billing: +0.7%|
|Tarjeta internacional|+1.5% si no es estadounidense|+1.5% si no es estadounidense|+0.5%|
|Conversión|Depende del payout/conversión|Depende de método y liquidación|+2% cuando se requiere|
|Payout|Costes de Stripe Connect trasladados|Comisiones según banco/PayPal y país|Según condiciones locales|

Polar cambió las condiciones para organizaciones creadas desde el 27 de mayo de 2026. [Anuncio fechado](https://polar.sh/blog/introducing-polar-plans) y [precios actuales](https://polar.sh/resources/pricing).

Lemon añade recargos por suscripción, internacional y PayPal; sus pagos bancarios fuera de EE. UU. tienen una comisión publicada del 1%. [Tarifas Lemon Squeezy](https://docs.lemonsqueezy.com/help/getting-started/fees).

Stripe México publica 3.6% + MXN 3, los suplementos indicados y Billing por separado. [Payments](https://stripe.com/en-mx/pricing), [Billing](https://stripe.com/mx/billing/pricing).

**Ejemplo calculado**, sin impuestos al comprador, payout, conversión ni disputas:

|Venta con tarjeta no estadounidense|Polar Starter|Lemon Squeezy|
|---|---|---|
|USD 6.99|≈ USD 0.95|≈ USD 0.99|
|USD 11.99|≈ USD 1.28|≈ USD 1.34|

La diferencia entre esos MoR es pequeña a estos precios. La tarifa fija pesa más que unas décimas porcentuales. No elegiría proveedor sólo por esa diferencia.

## 4.3 Matices que cambian la recomendación

**Polar:**

- La documentación actual muestra un SDK nuevo en preview.
    
- Encontré `1.0.0-alpha.21` en el monorepo oficial; el repositorio antiguo contiene otro SDK.
    
- Las firmas cambiaron para secretos generados desde el **8 de septiembre de 2026**.
    
- No debe copiarse un ejemplo antiguo sin verificar versión, importaciones y firma. [SDK actual](https://polar.sh/docs/integrate/sdk/typescript), [verificación de webhooks](https://polar.sh/docs/integrate/webhooks/delivery).
    

**Lemon Squeezy:**

- La documentación de entrega enumera tipo, firma y recurso, pero no un event ID independiente como el de Stripe.
    
- El ID de la suscripción no puede usarse como ID de todos sus eventos.
    
- Habría que definir una clave local de deduplicación y sincronizar el recurso.
    
- Su SDK oficial mostró última actividad de push en noviembre de 2024: no prueba abandono, pero exige comprobar cobertura de API y mantenimiento. [Entregas](https://docs.lemonsqueezy.com/help/webhooks/webhook-requests), [SDK](https://github.com/lmsqueezy/lemonsqueezy.js).
    

**Stripe:**

Stripe sí tiene una oferta MoR llamada Managed Payments. No sería correcto afirmar que nunca actúa como MoR. Sin embargo, la lista consultada de ubicaciones empresariales admitidas por esa oferta **no incluye México** y aparece como public preview. No la tomaría como ruta disponible para BeatGaler México sin confirmación. [Managed Payments](https://docs.stripe.com/payments/managed-payments), [elegibilidad](https://docs.stripe.com/payments/managed-payments/how-it-works?locale=en-GB).

## 4.4 Recomendación

**Polar como primera opción**, por reducir la operación fiscal de ventas internacionales y resolver checkout, portal y suscripción sin añadir una plataforma propia.

La recomendación tiene dos gates concretos:

1. Onboarding y payout viables para la entidad real de BeatGaler.
    
2. SDK/API fijados y aprobados en sandbox, incluyendo firmas actuales, refunds y cambios de período.
    

**Stripe es la alternativa técnica preferida** si se prioriza madurez/control y BeatGaler puede asumir la operación comercial/fiscal adicional. Lemon Squeezy queda como alternativa MoR válida.

No recomiendo instalar tres adaptadores desde V1.

## 4.5 Lock-in real

Un adaptador reduce dependencia del código; no elimina la dependencia comercial.

Polar documenta migración asistida de clientes y métodos de pago, pero los productos y suscripciones deben recrearse. También documenta una retención de payouts de 120 días durante offboarding. Eso debe entrar en la decisión financiera. [Migrar fuera de Polar](https://polar.sh/docs/migrate-away).

El MoR gestiona impuestos de la venta al comprador. Las obligaciones propias de BeatGaler en México deben revisarse con su contador; no desaparecen por usar MoR.

---

# 5. Software y repositorios reutilizables

Verifiqué las licencias de los SDK y ejemplos indicados.

|Clasificación|Repositorio|Qué reutilizar|Qué no reutilizar|Licencia y riesgo|
|---|---|---|---|---|
|**UTILIZAR TAL CUAL**|[Polar SDK actual](https://github.com/polarsource/polar/tree/main/sdk/typescript)|Cliente API, tipos y verificación de firma|No adoptar sus beneficios como autoridad de cuotas|MIT específica del SDK. Preview: fijar versión y comprobar contratos.|
|**REFERENCIA / compatibilidad**|[Polar SDK anterior](https://github.com/polarsource/polar-js)|Entender integración previa y diferencias|No mezclar snippets con el SDK nuevo|MIT. Evitar iniciar sobre ejemplos incompatibles.|
|**REFERENCIA**|[Polar adapters](https://github.com/polarsource/polar-adapters)|Flujo checkout/portal/webhook|No introducir otro framework ni migrar Auth|Apache-2.0. La documentación actual depreca adaptadores de varios frameworks.|
|**ALTERNATIVA, SIN INSTALAR AHORA**|[stripe-node](https://github.com/stripe/stripe-node)|SDK y verificación oficiales si se elige Stripe|No abstraerlo antes de necesitarlo|MIT; actividad reciente.|
|**REFERENCIA**|[Stripe subscription-use-cases](https://github.com/stripe-samples/subscription-use-cases)|Secuencias de suscripción y pruebas de integración|No copiar servidor ni modelo de cuentas entero|MIT; ejemplo, no aplicación de producción terminada.|
|**ALTERNATIVA, SIN INSTALAR AHORA**|[lemonsqueezy.js](https://github.com/lmsqueezy/lemonsqueezy.js)|Cliente oficial si se elige Lemon|No asumir cobertura de novedades|MIT; actividad observada menor.|
|**REFERENCIA**|[Lemon nextjs-billing](https://github.com/lmsqueezy/nextjs-billing)|Portal, sincronización y organización del flujo|No importar Next.js, Auth u ORM por este trabajo|MIT; actividad en 2026.|
|**NO USAR COMO PLATAFORMA**|[Polar completo](https://github.com/polarsource/polar)|Consultar comportamiento cuando la documentación no baste|No autoalojar un MoR|Apache-2.0 a nivel principal; enorme alcance operacional.|
|**NO USAR**|[Lago](https://github.com/getlago/lago)|Como máximo, conceptos de metering|No añadir otro sistema de facturación|AGPL-3.0; sobredimensionado para tres planes.|

### Reutilización interna

Conservar y evolucionar:

- catálogo de planes;
    
- validación server-side de checkout;
    
- conceptos de identidad e idempotencia;
    
- tabla de suscripción;
    
- tabla de grants existente;
    
- infraestructura de eventos de webhook;
    
- tablas de operaciones, jobs y auditoría, cuando sirvan;
    
- escenarios de tests actuales.
    

No conservar el comportamiento sólo porque ya tiene tests.

### Licencia de BeatGaler

GitHub no identifica una licencia global y el paquete Cloud declara ISC. Eso no demuestra que todo el repositorio tenga esa licencia.

Usar dependencias MIT/Apache y conservar sus avisos es distinto de copiar código. Cualquier adaptación debe registrar origen, versión y licencia. No propongo introducir código AGPL en BeatGaler.

---

# 6. Arquitectura propuesta

## 6.1 Componentes mínimos

1. **Adaptador de Polar:** traduce API y eventos.
    
2. **Billing BeatGaler:** identidad comercial, checkout y proyección persistente.
    
3. **Resolver de acceso:** función única que combina suscripción y grants.
    
4. **Políticas de operaciones:** beats, PROJECT, YouTube, Bulk y Early Access.
    
5. **Ejecutor confiable:** realiza o controla efectivamente la escritura.
    
6. **Un procesador pequeño de tareas persistidas en PostgreSQL:** webhooks, reconciliación y recuperación.
    

No hacen falta Redis, Kafka, microservicios de billing, event sourcing general ni motor de reglas.

```
flowchart TD
    UI["Web / Desktop futuro / Mobile futuro"]
    API["API BeatGaler autenticada"]
    AD["Adaptador Polar"]
    PR["Polar: checkout, portal y cobros"]
    WH["Webhook: verificar y persistir"]
    JOB["Procesador de tareas PostgreSQL"]
    DB[("PostgreSQL")]
    POL["Resolver único de acceso y políticas"]
    OP["Operaciones confiables de biblioteca / YouTube"]
    ST["Almacenamiento y APIs externas"]

    UI --> API
    API --> AD
    AD --> PR
    PR --> WH
    WH --> DB
    DB --> JOB
    JOB --> AD
    JOB --> DB
    API --> POL
    POL --> DB
    API --> OP
    OP --> POL
    OP --> ST
    OP --> DB
```

## 6.2 Adaptador pequeño

Responsabilidades concretas:

- leer ofertas del proveedor;
    
- crear o recuperar checkout;
    
- crear portal;
    
- verificar/normalizar webhook;
    
- consultar cliente, suscripción y órdenes;
    
- revocar una suscripción cuando el refund lo requiera.
    

No crear una interfaz de cien métodos para todas las posibilidades de Stripe, Polar y Lemon.

Los estados originales del proveedor pueden conservarse para diagnóstico. La aplicación consume un contrato propio de acceso con fechas y motivos.

## 6.3 Frontera confiable para almacenamiento

La recomendación es **mover las mutaciones sensibles a un ejecutor controlado por BeatGaler**, dejando las políticas fuera de membership.

Ese ejecutor controla:

- nuevas identidades de beat;
    
- uploads de assets;
    
- sustituciones;
    
- publicación del índice;
    
- Trash y borrado permanente.
    

No basta con que el servidor apruebe una intención mientras el navegador conserva credenciales con las que puede ejecutar otras escrituras.

**Regla de salida:** el cliente no puede retener el mismo principal de transporte con permisos arbitrarios de escritura.

Las lecturas pueden seguir siendo Direct sólo si existe una identidad efectivamente restringida a lectura y se demuestra en pruebas adversariales. Si Telegram no permite esa separación en el esquema utilizado, las llamadas que requieren el principal escritor deben ejecutarse del lado confiable. No doy por existente una capacidad de Telegram que no se ha probado.

Este trabajo afecta al transporte por una razón de seguridad concreta. El cálculo de planes, los pagos y PostgreSQL no deben depender de cómo se invite un bot o se mantenga su membership.

---

# 7. Sources of truth

|Concepto|Autoridad exacta|
|---|---|
|Precio objetivo del negocio|Decisión comercial de BeatGaler|
|Importe efectivamente cobrable|Precio/producto activo del proveedor|
|Ofertas permitidas en BeatGaler|Configuración server-side que mapea oferta interna a IDs del proveedor|
|Precio mostrado|Copia verificada de esa oferta; nunca dato elegido por el cliente|
|Definición de Free/Paid Entry/Highest|Catálogo de políticas de BeatGaler|
|Pago realizado, refund y disputa|Proveedor|
|Estado externo de suscripción|Proveedor|
|Estado que usa una petición para autorizar|Proyección validada en PostgreSQL|
|Período pagado|Pago confirmado y cobertura temporal persistida en PostgreSQL|
|Temporary grant|Tabla `entitlements`, propiedad exclusiva del dominio de acceso|
|Effective plan|Resolver único usando PostgreSQL y reloj del servidor|
|Capacidad/entitlement efectivo|Catálogo BeatGaler aplicado al resultado del resolver|
|Beat usage|Identidades persistidas y verificadas en PostgreSQL, incluyendo Trash|
|Slots pendientes de upload|Operaciones/identidades reservadas en PostgreSQL|
|PROJECT permitido|Entitlement efectivo al admitir y finalizar la mutación|
|Tamaño PROJECT|Bytes reales verificados por el ejecutor, comparados contra catálogo|
|YouTube diario/mensual|Operaciones de YouTube persistidas, con ventanas UTC|
|Bulk|Política BeatGaler; no una propiedad del proveedor|
|Early Access|Catálogo más acceso efectivo, comprobado server-side|
|Archivo físico|Almacenamiento|
|Membership bot ↔ vault|Subsistema Direct correspondiente|
|UI|Representación del estado; ninguna autoridad comercial|

**Proveedor y PostgreSQL no son dos autoridades competidoras:** el proveedor determina los hechos financieros; PostgreSQL conserva su proyección validada para autorizar sin consultar al proveedor en cada operación.

`current_period_end` no prueba que ese período esté pagado. Algunos proveedores avanzan el período antes de cobrar.

---

# 8. Modelo PostgreSQL

## 8.1 Tablas existentes que sobreviven

### `billing_subscription_state`

Mantener una fila por usuario para su suscripción comercial actual. No añadir otra tabla que compita con ella.

Añadir:

- `provider`, `provider_environment`;
    
- IDs de oferta/producto/precio;
    
- `current_period_start`;
    
- `paid_through`;
    
- `past_due_at`, `grace_until`;
    
- `ended_at`;
    
- próximo plan/intervalo y fecha de aplicación;
    
- motivo y fecha de invalidación del acceso comercial;
    
- `last_synced_at`;
    
- versión local monotónica para detectar actualizaciones concurrentes.
    

Conservar estado original y plan comercial por separado de la elegibilidad de acceso.

Constraints:

- FK a `users`;
    
- unicidad del ID de suscripción por proveedor y ambiente;
    
- intervalos temporales válidos;
    
- planes conocidos;
    
- ningún estado activo puede interpretarse como Paid sin oferta reconocida y evidencia financiera suficiente.
    

Un refund de una suscripción anterior no puede aplicarse a la actual sólo porque comparte usuario.

### `entitlements`

**Reutilizarla como tabla de grants. No crear** `**grants**` **en paralelo.**

Añadir:

- `source_key`;
    
- `revoked_at`, `revocation_reason`;
    
- datos mínimos de emisor administrativo, cuando aplique.
    

Constraints:

- `UNIQUE(user_id, source, source_key)`;
    
- índice único parcial para bienvenida por usuario;
    
- expiración posterior al inicio;
    
- índice por usuario y expiración.
    

Los grants ordinarios de V1 caducan. No emitir `base_plan` pagados permanentes.

### `billing_webhook_events`

Convertirla en inbox durable.

Añadir:

- proveedor y ambiente;
    
- identidad real del evento;
    
- digest del cuerpo;
    
- payload validado mínimo necesario;
    
- identidad de usuario/suscripción resuelta;
    
- `received_at`, `processed_at`;
    
- estado `RECEIVED/PROCESSING/PROCESSED/FAILED/IGNORED`;
    
- `next_attempt_at`, lease de procesamiento y último código de error.
    

La clave única debe incluir proveedor/ambiente/evento. No asumir que IDs de test y producción nunca colisionan.

### `billing_reconciliation_exceptions`

Conservar para casos ambiguos o inconsistencias no reparables automáticamente. No generar una excepción nueva por cada comprobación del mismo problema.

### `direct_operations`, `garbage_journal`, `jobs`, `audit_events`

Reutilizar selectivamente.

En `direct_operations`, separar el **ID estable de negocio** de la sesión/lease temporal. Un retry tras reconnect no debe convertirse en otra importación.

La existencia de una tabla `jobs` no implica que ya exista un runner operativo: hay que comprobarlo e implementar sólo el consumidor necesario.

## 8.2 Tablas nuevas justificadas

### `billing_customers`

Necesaria antes de que exista una suscripción.

- Usuario, proveedor, ambiente, customer ID y external ID.
    
- Unicidad por usuario/proveedor/ambiente.
    
- Un customer externo no pertenece a dos usuarios.
    

No usar email como clave de propiedad.

### `billing_checkout_requests`

Persistencia de idempotencia y recuperación de timeouts.

- Usuario, request ID, oferta, hash de petición.
    
- Estado, checkout externo, caducidad y resultado recuperable.
    
- `UNIQUE(user_id, request_id)`.
    
- Una solicitud abierta por usuario para el flujo de suscripción.
    

Estados ambiguos deben seguir siendo ambiguos hasta reconciliarse; no crear otro checkout automáticamente.

### `billing_payments`

Proyección financiera mínima, no un ledger contable.

Por orden/factura relevante:

- proveedor/ambiente/payment ID;
    
- usuario y subscription ID;
    
- oferta y período al que corresponde;
    
- importe neto, moneda y estado;
    
- total reembolsado confirmado;
    
- referencia de invalidación/disputa.
    

Permite diferenciar devolución completa, parcial e histórica.

No almacenar PAN, CVV, copias completas de facturas ni detalles bancarios.

### `library_beats`

Registro mínimo de identidades y ciclo de vida para imponer cardinalidad.

- Usuario/vault/beat ID.
    
- Estado: reservado, activo, Trash, purga pendiente o purgado.
    
- Operación de creación.
    
- Referencias mínimas verificadas de assets relevantes.
    
- Fechas y revisión.
    

Clave única: `(vault_id, beat_id)`.

Un beat purgado conserva tombstone suficiente para impedir que un índice viejo lo restaure gratuitamente. Restaurar un backup con una identidad ya purgada es una nueva alta a efectos de cuota.

No duplicar aquí toda la metadata creativa de la biblioteca.

### `youtube_operations`

Sólo cuando se integre el flujo real de YouTube.

- Usuario y business operation ID.
    
- Hash de petición, canal y entrada.
    
- Día/mes UTC de reserva.
    
- Estado reservado, en ejecución, completado, liberado o incierto.
    
- ID del video.
    
- Referencia protegida de sesión resumible.
    
- Lease, intentos y marcas temporales.
    

Unicidad por usuario/operación y por resultado externo cuando corresponda.

## 8.3 Qué deprecar

- `billing_webhook_subjects` como solución de orden global.
    
- `entitlement_reservations` como acumulador universal.
    
- `entitlements.source='base_plan'` como fuente pagada independiente.
    
- Persistencia de grants mediante snapshots de Auth.
    
- `planState` como estado escribible de producción.
    

Las migraciones `0001`–`0010` no deben reescribirse. Los números siguientes se asignarán contra la rama vigente al implementar.

## 8.4 Migración segura

1. Inventariar filas reales, grants, referencias externas y procedencia de los planes.
    
2. Retirar el escritor de Auth sobre `entitlements`.
    
3. Convertir bienvenida/grants preservando fechas originales.
    
4. No convertir un antiguo dev-switch en una suscripción pagada.
    
5. No reiniciar siete días a todas las cuentas.
    
6. Reconciliar suscripciones que realmente existan en el proveedor.
    
7. Tratar planes históricos sin procedencia como una excepción explícita: conservar temporalmente sólo mediante grant de migración documentado si se decide.
    
8. Inicializar beats desde un índice verificado por un proceso confiable, incluyendo Trash.
    
9. Bloquear altas si el conteo está sin inicializar o es inconsistente; mantener lectura.
    
10. Cambiar todos los lectores al resolver único.
    
11. Retirar definitivamente la compatibilidad de escritura.
    

La vuelta atrás debe mantener el nuevo ownership de grants. **No es seguro volver a un binario que ejecute el borrado global de** `**entitlements**`**.**

---

# 9. Lifecycle de suscripción

## 9.1 Alta y checkout

1. Cuenta activada → Free más grant de bienvenida.
    
2. El cliente elige una oferta interna.
    
3. El servidor autentica, valida oferta y persiste la solicitud.
    
4. Crea o recupera el checkout del cliente correcto.
    
5. Redirige al checkout alojado.
    
6. El retorno muestra “Confirmando pago”.
    
7. Webhook y sincronización verifican el pago.
    
8. PostgreSQL se actualiza.
    
9. La UI consulta el mismo acceso que usarán las operaciones.
    

**Ni el redirect ni** `**checkout.created**` **otorgan Paid.**

## 9.2 Renovación

- El nuevo período sólo se considera financiado después de confirmar su pago.
    
- Un webhook perdido se recupera por reconciliación.
    
- La fecha del siguiente cobro y `paid_through` son conceptos separados.
    
- El evento duplicado no extiende dos veces el acceso.
    

## 9.3 Cancelación

|Acción|Resultado|
|---|---|
|Cancelar renovación|Mantener acceso hasta final del período pagado|
|Deshacer cancelación antes del final|Continuar suscripción|
|Finalizar inmediatamente mediante operación administrativa|Retirar la fuente comercial desde ese momento|
|Llegar al final cancelado|Resolver Free o grants aún válidos|
|Refund|Aplicar política de invalidación; no confundir con cancelación|

## 9.4 Cambios de plan

Para V1:

- Free → Paid: inmediato después del pago.
    
- Paid Entry ↔ Highest: siguiente período.
    
- Mostrar plan actual, cambio pendiente, fecha e importe futuro.
    
- Cobrar y conceder el nuevo nivel cuando corresponda la renovación.
    
- Si falla ese pago, la gracia conserva el último nivel pagado; **no concede gratis un upgrade pendiente**.
    
- Bloquear cambios adicionales mientras haya un estado financiero ambiguo.
    

Polar dispone de `next_period`. Su portal usa la configuración de prorrateo de la organización; se debe fijar explícitamente, no aceptar el default sin revisar. [Prorrateo](https://polar.sh/docs/features/subscriptions/proration).

## 9.5 Failed payment

Recomendación:

- Primer pago fallido: no hay acceso comercial; sobreviven los grants válidos.
    
- Renovación fallida: siete días de gracia.
    
- Inicio: primer `past_due_at` de ese período, no recepción de cada webhook.
    
- Los retries no reinician el plazo.
    
- Pago recuperado: actualizar cobertura y retirar el aviso.
    
- Gracia agotada: fallback a Free/grants.
    
- Revocación definitiva del proveedor: terminar acceso comercial.
    
- Fallo de API del proveedor: no inventar cancelación ni acceso indefinido.
    

Polar documenta retries acumulados a los días 2, 7, 14 y 21, con gracia configurable independiente. BeatGaler no debe implementar otro calendario de cobros. [Recuperación de pagos](https://polar.sh/docs/features/subscriptions/failed-payments).

Lemon Squeezy documenta cuatro retries durante dos semanas. Stripe ofrece Smart Retries. [Lemon](https://docs.lemonsqueezy.com/help/online-store/recovery-dunning), [Stripe](https://docs.stripe.com/billing/subscriptions/webhooks).

## 9.6 Refund: recomendación B

|Alternativa|Evaluación|
|---|---|
|A. Borrar inmediatamente los beats extra|Rechazada: irreversible, difícil de atribuir y muy sensible a errores/eventos tardíos|
|B. Conservar y marcar over-quota|**Recomendada**: simple, reversible y coherente con downgrade|
|C. Congelar/archivar una parte|Añade selección de archivos, estados y restauración; innecesario|
|D. Gracia de acceso Paid|No cumple la intención de retirada inmediata del acceso invalidado|
|E. Conservar datos y revisar casos financieros ambiguos|Complemento necesario de B|

Reglas:

- Refund confirmado que invalida el pago del período vigente → retirar esa fuente comercial.
    
- Refund parcial → mantener acceso por defecto.
    
- Refund de un período antiguo → no invalidar automáticamente otro período pagado.
    
- Refund solicitado o pendiente → no tratarlo como completado.
    
- Disputa abierta → revisión o suspensión comercial reversible, sin borrar archivos.
    
- Grants independientes siguen su propio ciclo.
    
- Un evento antiguo de pago no puede reactivar un período cuyo pago quedó invalidado.
    

**Particularidad de Polar:** devolver una orden de suscripción no termina la suscripción. BeatGaler debe registrar la retirada local y ejecutar una revocación externa idempotente cuando corresponda, para evitar futuros cobros. La tarea se persiste en la misma transacción que la decisión local. [Refunds Polar](https://polar.sh/docs/features/refunds).

“Inmediato” significa al conocer y procesar el hecho confirmado. Ningún sistema puede reaccionar antes de recibirlo; por eso importan el inbox durable y la reconciliación.

---

# 10. Entitlements y cuotas

## 10.1 Resolver único

Una función de dominio recibe:

- estado comercial persistido;
    
- cobertura pagada/gracia;
    
- grants;
    
- instante del servidor;
    
- catálogo.
    

Devuelve:

- plan comercial;
    
- plan efectivo;
    
- capacidades y cuotas;
    
- fuentes de acceso;
    
- próxima fecha en que debe recalcularse;
    
- información de renovación/cancelación.
    

Regla básica:

> El plan efectivo es el nivel más alto entre Free, la fuente comercial actualmente válida y los grants activos no revocados.

No sumar 20 + 100 beats. No fusionar niveles arbitrariamente. El catálogo actual es jerárquico y basta con eso.

Un grant Paid Entry no reduce Highest. Un grant equivalente no hace caducar antes una suscripción que sigue vigente.

La expiración se evalúa al autorizar. No depende de que un cron “cambie a Free” exactamente a medianoche.

## 10.2 Bienvenida y promociones

**Bienvenida como grant interno**, no trial del proveedor:

- siete días;
    
- sin checkout ni tarjeta;
    
- una vez por usuario elegible;
    
- inserción idempotente;
    
- no acumulación por registros OAuth repetidos.
    

Comprar durante bienvenida inicia una suscripción normal. El grant no extiende automáticamente su período ni difiere el primer cobro.

Las promociones futuras usarán la misma tabla de grants. El subsistema de códigos sólo verificará elegibilidad y emitirá un grant; no calculará permisos por su cuenta.

No conservar como decisiones aprobadas los premios actuales de `CODE_POLICY`: el código ya contiene cantidades y niveles de referral que no están confirmados en esta solicitud.

## 10.3 `max_beats`: cardinalidad

Cuenta por propietario, no por pestaña, instalación ni bot:

> Beats activos + beats en Trash + purgas aún no liberadas.

Las reservas de altas pendientes se añaden al comprobar capacidad disponible, pero la UI puede mostrarlas separadas.

|Operación|Cambio de slots|
|---|---|
|Crear/importar un beat nuevo|+1|
|Añadir otra variante a un beat existente|0, sujeto a políticas de assets|
|Duplicar un beat|+1|
|Mover a Trash|0|
|Restaurar desde Trash|0|
|Renombrar/organizar/editar metadata|0|
|Purga confirmada|−1|
|Restaurar una identidad ya purgada desde backup|Nueva alta|
|Retry del mismo alta|0 adicional|

### Concurrencia

Dentro de una transacción corta:

1. Bloquear la fila estable del usuario.
    
2. Resolver acceso.
    
3. Buscar operación/beat existente.
    
4. Contar identidades y reservas.
    
5. Validar capacidad.
    
6. Insertar reserva identificada.
    

Desde 19/20, dos altas simultáneas permiten sólo una. Desde 20/20, ninguna.

No mantener la transacción abierta mientras se transmite un ZIP.

### Over-quota

Con 80/20:

- lectura, playback, descarga y metadata siguen permitidas;
    
- Trash y restauración de la misma identidad siguen permitidos;
    
- no se crean identidades nuevas;
    
- no existe una “licencia permanente para volver siempre a 80”;
    
- tras purgar hasta 19, vuelve a poder agregarse uno.
    

El servidor no acepta `beatCount` enviado por el cliente como prueba de uso.

## 10.4 PROJECT: capacidad más tamaño por archivo

Para escribir contenido PROJECT nuevo deben cumplirse ambas condiciones:

1. `upload_project=true`.
    
2. Tamaño real dentro del límite del plan.
    

Después de downgrade a Free:

|Acción|Permitida|
|---|---|
|Descargar ZIP existente|Sí|
|Conservar referencia y editar metadata|Sí|
|Eliminar ZIP|Sí|
|Reemplazarlo, incluso por uno menor|No|
|Subir nueva versión|No|
|Eliminarlo y volverlo a subir|No|
|Restaurar el beat desde Trash con el mismo ZIP|Sí|
|Recuperar automáticamente una transferencia todavía no confirmada|Revalidar permiso antes de convertirla en asset|

Un nombre `.zip` o un `kind` del cliente no define la autoridad. El servidor valida rol, ownership, tamaño y referencia.

No introducir en V1 un historial ilimitado de versiones PROJECT.

## 10.5 YouTube: uso temporal

Unidad: **un video cuya subida a YouTube quedó confirmada**, aunque esté privado o programado.

- No contar render.
    
- No contar preview.
    
- No contar cada request HTTP.
    
- No devolver cuota porque el usuario borre después el video.
    
- Un lote consume una unidad por video, no una por lote.
    

Ventanas:

- día natural UTC;
    
- mes natural UTC;
    
- ambos intervalos semiabiertos;
    
- no son ventanas móviles ni períodos de suscripción.
    

### Reserva → completar o liberar

Aquí sí hacen falta reservas: una subida larga tiene efectos externos y concurrencia.

1. Preparar el contenido.
    
2. Antes de iniciar la subida externa, reservar una unidad.
    
3. Comprobar día y mes en la misma transacción bajo el mismo lock de usuario.
    
4. Asociar la operación a ambas ventanas.
    
5. Iniciar una única sesión resumible.
    
6. Confirmar resultado externo.
    
7. Completar ambas cuotas atómicamente.
    
8. Liberar sólo si el fallo/cancelación se conoce con certeza.
    

Una subida que cruza medianoche pertenece a las ventanas reservadas al iniciarse. Un trabajo programado para mañana reserva cuando empieza a ejecutarse, no al programarlo.

### Timeouts y crashes

“Timeout” no significa “falló”.

Si el proceso muere después del upload:

- recuperar la misma sesión resumible;
    
- consultar su estado;
    
- completar si existe el resultado;
    
- no iniciar otra subida por defecto;
    
- mantener `uncertain` hasta resolver, sin presentarlo como consumo final.
    

Google documenta cómo consultar una sesión interrumpida y recuperar incluso la respuesta de una subida ya terminada. [Protocolo resumible](https://developers.google.com/youtube/v3/guides/using_resumable_upload_protocol).

Highest también registra resultados para idempotencia y diagnóstico; simplemente omite la comparación contra límites comerciales.

Un cambio de plan no reinicia el uso del día/mes.

## 10.6 Bulk

- Free: rechazar solicitudes de lote.
    
- Paid Entry: límite configurable, pendiente de valor.
    
- Highest: sin límite comercial de tamaño de lote, pero con ejecución por páginas y concurrencia acotada.
    
- Cada video conserva su operation ID.
    
- Cada resultado consume cuota individual.
    
- El batch no puede ocultar cientos de operaciones dentro de un único permiso.
    

“Full” no significa lanzar miles de procesos simultáneos.

## 10.7 Early Access

Debe existir una lista server-side de features Early Access.

La autorización comprueba:

- feature habilitada;
    
- usuario autenticado;
    
- `early_access=true`;
    
- permiso sobre el recurso concreto.
    

La UI usa la misma información para mostrar controles, pero las rutas están protegidas independientemente.

No etiquetar como Early Access una función exclusivamente local y afirmar que esconder su botón es una protección fuerte.

## 10.8 Dispositivos y sesiones

No imponer límites comerciales en V1.

Retirar esos campos de la oferta y su presentación. Mantener:

- expiración de sesiones;
    
- logout y revocación;
    
- detección/rate limiting de abuso;
    
- límites técnicos de operaciones concurrentes.
    

El límite actual de capacidades simultáneas es control operacional; no debe reinterpretarse como “número de dispositivos pagados”.

---

# 11. Enforcement map

|Operación real|Punto de enforcement requerido|
|---|---|
|Registro / primera activación|Servicio de cuentas emite bienvenida idempotente|
|`/plans/me` y Account|Resolver único, sin leer un `basePlanId` independiente|
|Checkout|Oferta allowlisted y cliente derivado de sesión|
|Portal|Customer ID obtenido de PostgreSQL para el usuario autenticado|
|`commitImportedBeat`|Reserva de identidad antes de escribir; confirmación confiable|
|Upload genérico|Operación, beat, rol, tamaño y destino autorizados|
|`commitBeatEdit`|Comprobar delta: metadata vs nuevo asset; PROJECT protegido|
|`replaceLibraryIndex`|Publicador confiable, revisión esperada y delta validado|
|`/transport/index/commit`|Aceptar sólo resultado de operación conocida/verificada; no conteo del cliente|
|`trash_move`|Ownership, transición activa → Trash, sin liberar slot|
|`trash_restore`|Misma identidad en Trash; sin nueva alta|
|`trash_purge`|Borrado explícito, recuperación segura y liberación única|
|Reimportar backup|Diferenciar identidad existente, Trash y purgada|
|Duplicación|Alta nueva|
|YouTube simple|Reserva atómica de día/mes antes del upload|
|YouTube bulk|Capability de lote más autorización de cada video|
|Early Access|Middleware/policy en cada operación protegida|
|APIs administrativas|Autorización administrativa separada y auditoría|
|Clientes Desktop antiguos|No pueden conservar una ruta de escritura que eluda las cuotas|

### Dos controles necesarios

- **Admisión:** evita gastar infraestructura en una operación ya prohibida.
    
- **Finalización:** verifica que el resultado corresponde al permiso y que sigue siendo publicable.
    

Una operación iniciada como Paid y finalizada después de perder el derecho no debe publicar un PROJECT nuevo sin revalidación. Los bytes temporales no se convierten por ello en un asset permanente; se limpian mediante recuperación segura.

No se borra un asset previamente confirmado como consecuencia de esa revalidación.

---

# 12. Seguridad, webhooks y observabilidad

## 12.1 Controles mínimos

|Amenaza|Control|
|---|---|
|Precio/plan alterado|Oferta interna allowlisted; mapping server-side|
|Checkout ajeno|Identidad derivada de sesión y binding persistido|
|Portal ajeno|Nunca aceptar customer ID desde el frontend|
|Webhook falsificado|Verificador oficial sobre raw body|
|Replay|Timestamp de firma y evento único persistido|
|Evento duplicado|Inserción y transición idempotentes|
|Evento desordenado|Sincronizar agregado actual; no confiar sólo en timestamp|
|IDOR de beats/assets|Ownership en servidor|
|CSRF|Protección existente para rutas autenticadas mutantes|
|Secretos|Gestor/configuración server-side; nunca bundle Web|
|Dev backdoor|Retirar ruta productiva de cambio de plan|
|Cliente Direct manipulado|Frontera de escritura confiable|
|Dos pestañas|Transacción/lock en PostgreSQL|
|Retry con otro contenido|Hash de petición; devolver conflicto|
|Base de datos indisponible|Rechazar nuevas operaciones protegidas; no recurrir a JSON|

La ruta webhook se excluye de autenticación de usuario/CSRF, pero conserva firma, límites de cuerpo y controles de tráfico.

## 12.2 Responsabilidad exacta del webhook

**Recepción:**

1. Capturar bytes originales antes de `express.json`.
    
2. Verificar firma y headers.
    
3. Comprobar proveedor/ambiente.
    
4. Normalizar identidad.
    
5. Persistir inbox en transacción.
    
6. Responder éxito sólo después de persistir.
    

**Procesamiento:**

1. Reclamar evento con lease recuperable.
    
2. Resolver usuario/suscripción usando bindings confiables.
    
3. Consultar estado actual cuando sea necesario.
    
4. Aplicar transición financiera, acceso y auditoría en una transacción.
    
5. Marcar procesado.
    
6. Reintentar fallos temporales.
    

Polar recomienda responder rápido y documenta desactivación del endpoint tras fallos consecutivos. Esto justifica el inbox PostgreSQL, no una cola externa. [Entrega de webhooks](https://polar.sh/docs/integrate/webhooks/delivery).

### Orden y concurrencia

Todos los eventos que afecten al acceso de un usuario se sincronizan bajo la misma exclusión por usuario.

Para evitar que una consulta antigua sobrescriba una nueva:

- serializar la consulta y aplicación mediante un lock asesor de sesión con timeout acotado;
    
- abrir la transacción SQL sólo para aplicar el resultado;
    
- liberar el lock siempre y no devolver una conexión bloqueada al pool;
    
- ante pérdida de conexión, abandonar ese intento.
    

La recepción de otros eventos continúa sin esperar ese procesamiento.

Refunds confirmados mantienen una marca de invalidación financiera que una actualización genérica `active` no puede borrar.

## 12.3 Idempotencia de checkout: limitación importante

El código actual genera una key, pero eso no demuestra que el proveedor seleccionado la ejecute.

No encontré una garantía equivalente a la idempotencia de Stripe para creación de checkout en los contratos de Polar inspeccionados. Por eso:

- persistir el request antes de llamar;
    
- bloquear doble creación por usuario;
    
- incluir un identificador interno en metadata server-side;
    
- reutilizar la sesión conocida;
    
- tras timeout, buscar/reconciliar la sesión creada;
    
- no reenviar ciegamente el POST;
    
- mantener el estado incierto si no puede demostrarse el resultado.
    

Sin una garantía externa, no se puede prometer “exactamente una creación” sólo con una transacción local. Sí puede evitarse exponer una segunda sesión cobrable mientras se resuelve la primera.

## 12.4 Reconciliación

Un procesador pequeño, dentro del despliegue Node:

- inbox: procesamiento continuo;
    
- estados pendientes/atrasados: revisión cada cinco minutos;
    
- barrido paginado de clientes comerciales: diario;
    
- acción manual por usuario/suscripción;
    
- refresh acotado tras retorno de checkout;
    
- sin consulta al proveedor en cada login o playback.
    

El barrido debe incluir checkouts pendientes y clientes sin suscripción local: recorrer sólo suscripciones conocidas no encuentra una compra cuyo webhook inicial se perdió.

Reparar automáticamente divergencias inequívocas. Registrar excepciones para:

- binding contradictorio;
    
- oferta desconocida;
    
- múltiples suscripciones inesperadas;
    
- refund de interpretación ambigua.
    

No convertir un error de red en “el proveedor confirma que es Free”.

## 12.5 Logging

Eventos estructurados mínimos:

- `checkout_started`, `checkout_pending`, `checkout_confirmed`;
    
- `webhook_received`, `webhook_duplicate`, `webhook_invalid_signature`;
    
- `subscription_transition`, `access_changed`;
    
- `quota_denied`, `quota_reserved`, `quota_committed`, `quota_released`;
    
- `refund_confirmed`, `access_revoked`;
    
- `reconciliation_mismatch`, `reconciliation_repaired`.
    

Incluir usuario interno, operation ID, event ID, proveedor, estado anterior/nuevo, motivo y duración.

No loguear tokens, URLs firmadas completas, payloads financieros completos ni datos de tarjeta.

Alertar por:

- inbox detenido o creciente;
    
- eventos fallidos sin recuperación;
    
- revocación pendiente después de refund;
    
- checkout incierto persistente;
    
- divergencia de conteo;
    
- indisponibilidad de PostgreSQL.
    

---

# 13. Testing strategy

## 13.1 Unitarios

Pruebas de tablas y funciones puras:

- catálogo exacto;
    
- ausencia de límites comerciales de devices;
    
- combinación de suscripción/grants;
    
- expiración en límites exactos;
    
- cancelación futura;
    
- gracia sin extensión por retries;
    
- refund parcial/completo/histórico;
    
- mapping de productos y estados desconocidos;
    
- reglas de PROJECT;
    
- ventanas UTC;
    
- ids y colisiones.
    

Conservar los escenarios útiles actuales, corrigiendo aquellos que consagran una política incorrecta.

## 13.2 Integración PostgreSQL real

Base aislada, con migraciones reales:

- registro concurrente no duplica bienvenida;
    
- dos procesos no crean dos checkouts abiertos;
    
- desde 19/20 sólo una de dos altas termina admitida;
    
- desde 20/20 ninguna;
    
- Trash no libera;
    
- restore no incrementa;
    
- purge libera exactamente una vez;
    
- colisión de ID entre usuarios no reutiliza reserva;
    
- cuotas diaria y mensual se actualizan juntas;
    
- grant nuevo sobrevive a login, logout y persistencia de Auth;
    
- reinicio recupera inbox y operaciones inciertas;
    
- cancelación/expiración funcionan sin evento puntual;
    
- los locks se liberan al fallar.
    

Los fake pools actuales no sustituyen estas pruebas.

## 13.3 Integración de webhook

HTTP real con orden real de middleware y firma criptográfica:

- cuerpo correcto;
    
- cuerpo alterado;
    
- firma incorrecta;
    
- timestamp vencido;
    
- duplicado secuencial y concurrente;
    
- crash después de recepción;
    
- crash antes/después de aplicar;
    
- llegada invertida;
    
- eventos distintos con el mismo timestamp;
    
- refund antes de actualización de suscripción;
    
- evento de una suscripción antigua;
    
- ambiente incorrecto;
    
- tipo desconocido;
    
- API temporalmente indisponible.
    

## 13.4 Provider sandbox E2E

Obligatorio antes de cerrar billing:

1. Cuenta sin grant activo → Free.
    
2. Checkout real de sandbox.
    
3. Pago con tarjeta de prueba.
    
4. Webhook real entregado.
    
5. PostgreSQL cambia.
    
6. UI muestra Paid.
    
7. Operación Paid real permitida.
    
8. Cancelación en portal.
    
9. Acceso conservado hasta final.
    
10. Expiración y fallback.
    
11. Refund completo vigente y revocación.
    
12. Refund parcial sin pérdida automática de acceso.
    
13. Pago fallido y recuperación.
    
14. Cambio de plan programado.
    
15. Retry/retorno de checkout sin segunda suscripción.
    

Polar dispone de un sandbox separado con credenciales distintas. Sus emails de prueba tienen restricciones de destinatarios que deben considerarse al validar notificaciones. [Sandbox Polar](https://polar.sh/docs/integrate/sandbox).

No afirmar que un test clock de Stripe controla Polar. Para eventos temporales, usar ciclos cortos admitidos en sandbox o herramientas documentadas, más pruebas con reloj inyectado en integración local.

## 13.5 App y transporte

- Dos cuentas independientes.
    
- Dos tabs y dos procesos servidor.
    
- HTTP manual que omite la UI.
    
- Cliente que intenta usar `replace_index` para introducir beats adicionales.
    
- PROJECT oculto bajo otro rol.
    
- Índice antiguo que intenta recuperar purgados.
    
- Caída durante upload, publicación, confirmación y purge.
    
- Cuenta 80/20 conserva playback, descarga, edición y Trash.
    
- Cliente antiguo no evade la frontera.
    
- Revocación Paid no interrumpe lectura de material conservado.
    

**Una prueba de cuotas sólo es válida si atraviesa la operación real, no un endpoint de prueba que la aplicación nunca usa.**

---

# 14. Relación con el resto de V1

|Trabajo|Momento|
|---|---|
|Resolver, catálogo y contratos|Puede comenzar ya|
|Separar grants de Auth|Puede comenzar ya; imprescindible antes de escribir grants nuevos|
|Adaptador, checkout y webhooks|Puede desarrollarse en paralelo con fiabilidad Web|
|Migraciones de billing|Independientes de membership, con coordinación del número de migración|
|Conteo y frontera de mutación|Después de identificar los problemas reales de Etapa 1; coordinado con Etapa 2|
|Enforcement final sobre Direct|Requiere contrato estable y pruebas adversariales de escritura|
|YouTube Web|Línea de trabajo propia; no es una simple tarea de billing|
|UI comercial|Puede avanzar contra contrato estable, sin habilitar ventas|
|Cobro en producción|Después de fiabilidad, enforcement y sandbox E2E|

La rama persistente añade ownership del bot en `vaults`, estados de membership y retiro del antiguo cap de leases. Billing no debe leer esos estados para decidir si alguien es Paid.

Pero tampoco puede declarar segura una cuota si el transporte todavía permite escribir al margen de la autoridad.

Etapa 1 termina con evidencia, incluso si falla. Esa evidencia debe decidir el alcance de Etapa 2 antes de validar el último tramo de cuotas.

---

# 15. Plan step-by-step

Los nombres de archivos nuevos son orientativos. Cada step debe producir un cambio acotado con evidencia propia; no requiere que el mismo agente ejecute toda la etapa.

## STEP 0 — Congelar evidencia y cerrar el contrato de lanzamiento

**Objetivo:** establecer la base exacta y las decisiones que condicionan la implementación.

**Por qué existe:** la rama predeterminada está atrasada y hay dos prerrequisitos de producto ocultos.

**Áreas:** documentación de arquitectura, roadmap, inventario de rutas y migraciones.

**Implementar:** registrar SHA vigente, diferencias pendientes, esquema real, disponibilidad YouTube Web y decisión sobre cambios de plan al siguiente período. Fijar unidades de PROJECT y registrar `limited` como pendiente.

**No tocar:** aplicación, proveedor ni base de producción.

**Tests:** verificar ancestry y reproducir el inventario de consumidores.

**Terminado:** existe una base inequívoca y una lista corta de gates, sin tratar drafts como integración terminada.

**Dependencias:** ninguna.

**Cuándo:** ahora.

**Riesgo:** bajo; evita ejecutar todo el plan sobre una base equivocada.

---

## STEP 1 — Validar la frontera de escritura antes de diseñar su implementación

**Objetivo:** cerrar el contrato del ejecutor confiable.

**Por qué existe:** ningún cálculo SQL impide escrituras que no pasan por él.

**Áreas:** capacidades Direct, worker Web, helper Desktop, publicación del índice y credenciales temporales.

**Implementar:** prueba técnica aislada que documente qué puede hacer el cliente con su sesión; decidir qué credenciales permanecen server-side; definir el contrato de mutaciones y su confirmación. Probar si las lecturas pueden conservar Direct con permisos realmente limitados.

**No tocar:** políticas comerciales, allocation ni membership persistente salvo la coordinación imprescindible de permisos.

**Tests:** intentar upload/pin/delete sin autorización BeatGaler; demostrar denegación en el diseño elegido.

**Terminado:** hay un camino concreto donde el cliente no puede ejecutar escrituras arbitrarias. Una recomendación de “validar en frontend” no cumple.

**Dependencias:** STEP 0.

**Cuándo:** ahora; su ejecución se coordina con Etapa 2.

**Riesgo:** alto. Puede revelar un cambio real de transporte; debe conocerse antes de estimar la etapa.

---

## STEP 2 — Dar ownership exclusivo de grants al dominio de acceso

**Objetivo:** impedir que Auth reescriba los grants.

**Por qué existe:** el snapshot actual puede borrar cambios realizados por billing.

**Áreas:** runtime PostgreSQL de Auth, compatibilidad JSON, importador legacy y tabla `entitlements`.

**Implementar:** retirar lectura/escritura comercial del snapshot; migrar grants con identidades estables; emitir bienvenida idempotente desde activación de cuenta; conservar las fechas originales.

**No tocar:** contraseñas, OAuth o esquema de sesiones más allá de la separación necesaria.

**Tests:** insertar grant, ejecutar cambios Auth y reiniciar; el grant permanece. Registro concurrente produce una bienvenida.

**Terminado:** ninguna persistencia Auth ejecuta borrados/reemplazos de grants; no hay escritura de `basePlanId`.

**Dependencias:** STEP 0.

**Cuándo:** ahora, independiente del transporte.

**Riesgo:** alto por el alcance de la compatibilidad existente.

---

## STEP 3 — Implementar catálogo definitivo y resolver único

**Objetivo:** una sola respuesta a “qué puede hacer ahora”.

**Por qué existe:** los dos evaluadores actuales divergen.

**Áreas:** planes, entitlements de billing, serializers de Account y `/plans/me`.

**Implementar:** función pura de acceso, fechas de pago/gracia/cancelación, grants revocados, `null` como ilimitado y capacidades reales. Retirar devices/sessions comerciales.

**No tocar:** cobros externos ni operaciones de almacenamiento.

**Tests:** matriz completa de fuentes y límites temporales, incluyendo grant del mismo nivel.

**Terminado:** Account, plans y servicios reciben la misma estructura y resultado; ningún consumidor decide Paid por su cuenta.

**Dependencias:** STEP 2.

**Cuándo:** ahora.

**Riesgo:** medio; afecta contratos de UI y backend.

---

## STEP 4 — Añadir persistencia comercial y catálogo de ofertas

**Objetivo:** preparar identidad, pagos y solicitudes durables.

**Por qué existe:** el checkout actual no persiste su resultado y la tabla de suscripción es insuficiente.

**Áreas:** migraciones siguientes, suscripciones, clientes, pagos y checkout requests.

**Implementar:** columnas, constraints e índices de la sección 8; configuración de ofertas `product + interval + version`; validación contra precios del proveedor; precio público derivado de datos verificados.

**No tocar:** crear productos reales ni cambiar suscriptores existentes.

**Tests:** migración sobre base nueva y fixture legado; IDs duplicados, usuario inexistente y oferta desconocida.

**Terminado:** ninguna solicitud usa cantidades/IDs externos elegidos por cliente; existen constraints para todos los bindings.

**Dependencias:** STEP 2; contrato de STEP 3.

**Cuándo:** ahora.

**Riesgo:** medio; requiere conocer si hay filas comerciales reales.

---

## STEP 5 — Integrar y fijar el SDK de Polar en sandbox

**Objetivo:** validar el proveedor con el runtime real.

**Por qué existe:** hay una transición de SDK y firma muy reciente.

**Áreas:** dependencias Cloud y adaptador Polar.

**Implementar:** versión exacta probada, API explícita, ambiente obligatorio, consulta de ofertas/cliente/suscripción, checkout, portal y verificación de eventos.

**No tocar:** Auth, esquema de grants ni framework de frontend. No instalar adaptadores de otros proveedores.

**Tests:** Node del proyecto, CommonJS/ESM, firma actual, secreto antiguo cuando aplique, API de sandbox y errores tipados.

**Terminado:** matriz de compatibilidad documentada; ninguna dependencia `latest`/`next` flotante; credenciales live y sandbox no se mezclan.

**Dependencias:** STEP 4 y acceso sandbox disponible.

**Cuándo:** paralelo con trabajo de fiabilidad.

**Riesgo:** medio; preview del SDK y aprobación comercial.

---

## STEP 6 — Crear inbox de webhooks y proyección de suscripción

**Objetivo:** recibir hechos financieros sin perderlos.

**Por qué existe:** el webhook actual es un contrato no conectado.

**Áreas:** arranque/middleware, inbox, procesador y tablas comerciales.

**Implementar:** raw body antes del parser, firma oficial, event ID correcto, persistencia antes de responder, leases recuperables, normalización y sincronización serializada por usuario.

**No tocar:** cuotas ni conceder acceso por redirect.

**Tests:** firma real, duplicados concurrentes, entrega invertida, crash y binding incorrecto con PostgreSQL real.

**Terminado:** matar el proceso después de recibir el evento no lo pierde; repetirlo no duplica efectos.

**Dependencias:** STEPS 3–5.

**Cuándo:** ahora.

**Riesgo:** alto; es la frontera entre dinero y permisos.

---

## STEP 7 — Completar checkout, portal e idempotencia

**Objetivo:** habilitar el flujo comercial alojado.

**Por qué existe:** generar una key en memoria no resuelve timeouts ni ownership.

**Áreas:** servicios de checkout/portal y rutas autenticadas.

**Implementar:** request persistido, hash de petición, exclusión por usuario, recuperación de sesión incierta, portal del customer correcto, URLs permitidas y estado de confirmación.

**No tocar:** tarjetas, CVV, formularios bancarios ni entitlements por redirección.

**Tests:** doble-click, dos tabs, petición alterada, timeout después de crear, customer ajeno y suscriptor que intenta otro checkout.

**Terminado:** retries reutilizan la operación; un estado incierto no produce otra sesión ofrecida al usuario.

**Dependencias:** STEPS 4–6.

**Cuándo:** ahora.

**Riesgo:** medio-alto por los resultados externos ambiguos.

---

## STEP 8 — Cerrar cancelación, cambios, failures y refunds

**Objetivo:** completar todos los estados comerciales V1.

**Por qué existe:** `active → Paid` es insuficiente.

**Áreas:** proyector, resolver, pagos, portal y tareas de revocación.

**Implementar:** cancelación al período, undo, cambio programado, cobertura pagada, gracia de siete días, refund completo/parcial/histórico y revocación externa durable.

**No tocar:** borrar beats, archivar contenido o añadir prorrateo propio.

**Tests:** límite exacto de período, renovación fallida, grace replay, upgrade pendiente sin pagar, refund tardío y evento antiguo que intenta reactivar.

**Terminado:** cada transición tiene resultado de acceso verificable y ningún refund dispara borrado.

**Dependencias:** STEPS 3, 6 y 7.

**Cuándo:** ahora.

**Riesgo:** alto; requiere fixtures basadas en payloads reales del proveedor.

---

## STEP 9 — Crear registro de beats y reserva atómica de altas

**Objetivo:** imponer cardinalidad correcta.

**Por qué existe:** reservas acumuladas e índices del cliente no representan posesión actual.

**Áreas:** `library_beats`, operaciones persistidas e inicialización desde índice verificado.

**Implementar:** identidad única, conteo con Trash, reservas de altas, lock por usuario, tombstones y estado de inicialización.

**No tocar:** catalogar cada metadata de biblioteca en otra base ni depender del bot asignado.

**Tests:** 19/20 con dos procesos, batch parcialmente admitido, colisión entre usuarios, retry con otra sesión, restauración de backup.

**Terminado:** nunca se admiten más altas que capacidad disponible; estado no inicializado bloquea altas.

**Dependencias:** STEPS 1 y 3.

**Cuándo:** puede prepararse ya; integración después de evidencia de Etapa 1.

**Riesgo:** alto por la importación del inventario existente.

---

## STEP 10 — Implementar escrituras confiables e integrar PROJECT

**Objetivo:** aplicar las políticas en el camino que realmente escribe.

**Por qué existe:** checks sobre rutas legacy o sólo sobre el cliente son insuficientes.

**Áreas:** ejecutor de mutaciones, import/edit Web, upload, publicación del índice y compatibilidad Desktop.

**Implementar:** operación estable con payload/destino acotados; tamaño real; confirmación server-side; publicación serializada; revalidación final; recuperación de efectos externos.

**No tocar:** playback, scheduler o allocation salvo lo exigido por el contrato aprobado en STEP 1.

**Tests:** bypass sin UI, PROJECT disfrazado, índice manipulado, dos publicadores, crash tras upload y cliente antiguo.

**Terminado:** todas las rutas de escritura comercialmente relevantes atraviesan una autoridad efectiva; no queda una credencial de escritura que las evite.

**Dependencias:** STEPS 1 y 9; contrato Direct estable de Etapa 2.

**Cuándo:** después de fijar esa frontera.

**Riesgo:** alto; es el mayor trabajo ajeno al proveedor de pagos.

---

## STEP 11 — Integrar Trash, purge y recuperación

**Objetivo:** conservar datos y evitar evasiones de slots.

**Por qué existe:** una implementación incorrecta de Trash deshace la cuota.

**Áreas:** operaciones Trash, índice y recuperación/garbage journal.

**Implementar:** mover/restaurar sin cambio de slots; purge idempotente; liberar sólo cuando el borrado definitivo esté confirmado; manejar purga pendiente; impedir resurrección desde índices viejos.

**No tocar:** borrados automáticos por plan o refund.

**Tests:** 80/20, move/restore repetidos, purge concurrente, fallo parcial y recuperación tras restart.

**Terminado:** limpiar libera exactamente lo confirmado; ninguna restauración ordinaria duplica identidades.

**Dependencias:** STEPS 9 y 10.

**Cuándo:** con cierre de fiabilidad de Trash en Etapa 2.

**Riesgo:** alto por tratarse de eliminación solicitada por el usuario.

---

## STEP 12 — Integrar YouTube y Bulk con ejecución real

**Objetivo:** proteger videos realmente subidos, no eventos del frontend.

**Por qué existe:** la feature actual depende de Tauri y no tiene autoridad Cloud de uso.

**Áreas:** flujo YouTube, `youtube_operations`, ejecución resumible y UI.

**Implementar:** reserva diaria/mensual conjunta; business IDs; persistencia de sesión; verificación de video; liberación cierta; estado incierto; política de lote. Mantener OAuth y credenciales amplias del lado confiable.

**No tocar:** construir una plataforma genérica de render/jobs ni afirmar que el port Web ya existe.

**Tests:** doble-click, retries, crash después de upload, cambio de UTC, éxito parcial de lote y downgrade con uso previo.

**Terminado:** un video real confirma una unidad y un fallo confirmado ninguna; el flujo Web funciona si se comercializa en Web.

**Dependencias:** STEP 3, esquema PostgreSQL y flujo YouTube Web confiable.

**Cuándo:** políticas ahora; cierre después del trabajo de producto YouTube Web.

**Riesgo:** alto. Render/OAuth/Web deben descomponerse en su propio plan antes de ejecutar este step; no ocultarlos dentro de una tarea de quotas.

---

## STEP 13 — Proteger Early Access y completar UI de planes

**Objetivo:** alinear experiencia y autorización.

**Por qué existe:** la UI actual es una simulación de arquitectura.

**Áreas:** Account, Settings, comparación de planes y endpoints Early Access.

**Implementar:** precios desde servidor, plan comercial/efectivo diferenciados, bienvenida, uso con Trash, over-quota, renovación, cancelación, cambio pendiente y portal. Proteger una feature Early Access concreta server-side.

**No tocar:** copiar visualmente X ni mostrar anual/Bulk/YouTube como disponibles si faltan sus gates.

**Tests:** frontend coincide con servidor, CTA correcto, 80/20 y endpoint Early Access invocado manualmente.

**Terminado:** desaparecen simulaciones DEV; toda promesa de la página coincide con una capacidad disponible.

**Dependencias:** STEPS 3, 7 y 8; STEPS 10–12 para sus features.

**Cuándo:** UI puede avanzar en paralelo; habilitación después de gates.

**Riesgo:** medio.

La referencia de X devolvió 403 durante la investigación. La propuesta de UX se basa en el flujo solicitado y los portales verificados, no en una inspección visual que no pude realizar.

---

## STEP 14 — Reconciliación, observabilidad y retirada de dev-switch

**Objetivo:** operar billing sin depender de entregas perfectas.

**Por qué existe:** puede perderse un webhook, quedar una operación incierta o habilitarse una ruta de prueba.

**Áreas:** runner, excepciones, logs, configuración y rutas de desarrollo.

**Implementar:** revisiones pendientes/diarias, reparación inequívoca, alertas, acción manual interna y fixtures/factories de test. Retirar `/plans/dev-switch` de producción.

**No tocar:** fingerprinting ni panel administrativo completo.

**Tests:** evento perdido recuperado, outage sin falso downgrade, grant no reescrito y proceso productivo con variable antigua de dev-switch activada.

**Terminado:** la ruta devuelve 404 incluso con esa variable; se detecta/repara una divergencia sembrada; los logs no contienen secretos.

**Dependencias:** STEPS 6–8.

**Cuándo:** antes del E2E final.

**Riesgo:** medio.

---

## STEP 15 — Cerrar la etapa con sandbox y operaciones reales

**Objetivo:** demostrar Billing V1 completo.

**Por qué existe:** 27 tests de contratos no prueban una compra ni una cuota productiva.

**Áreas:** sandbox, aplicación, PostgreSQL aislado y almacenamiento de prueba.

**Implementar:** automatización/documentación de los journeys de la sección 13; capturar IDs de compra/evento/operación y resultados; repetir con dos cuentas y dos procesos.

**No tocar:** producción ni sustituir el proveedor por mocks durante el journey principal.

**Tests:** compra, acceso, cancelación, expiración, refund, fallo de pago, retry, over-quota y enforcement adversarial.

**Terminado:** evidencia completa, sin pasos manuales ocultos para cambiar planes o arreglar base de datos. Toda feature comercializada tiene un journey real.

**Dependencias:** STEPS 8, 10, 11, 13 y 14; STEP 12 si YouTube/Bulk se incluyen en la oferta Web.

**Cuándo:** después de los gates de fiabilidad de Etapa 2.

**Riesgo:** medio si los anteriores están cerrados; alto si se intenta usar para descubrir toda la arquitectura al final.

---

# Próximos tres pasos concretos

1. **Fijar la base y validar la frontera de escritura de Direct.** Partir del sucesor vigente de `a112563`, documentar qué escrituras permite la sesión del navegador y decidir el ejecutor confiable antes de añadir checks de cuota.
    
2. **Separar grants de la persistencia de Auth e implementar el resolver único.** Es el primer cambio de billing que puede ejecutarse independientemente de membership y elimina el riesgo de perder grants.
    
3. **Hacer el spike de Polar en sandbox con SDK/API fijados.** Verificar México/onboarding, firma actual, checkout recuperable, portal, refund y cambio al siguiente período antes de comprometer la implementación completa.
    

Estos son los próximos trabajos propuestos; no se implementaron en esta sesión.

---

# Veredicto

**1. ¿Evolucionar o reemplazar?**  
Evolucionar el catálogo, tablas y contratos útiles. Reemplazar el cálculo duplicado de acceso, la persistencia de grants por snapshots y las reservas universales. Cerrar aparte la frontera real de escritura.

**2. ¿Qué proveedor?**  
Polar, por reducir operación comercial y resolver el flujo SaaS alojado. Con gates de onboarding y SDK/sandbox. Stripe si se prefiere madurez/control y se acepta la carga adicional.

**3. ¿Qué reutilizar?**  
Catálogo, validaciones de checkout, escenarios de tests, PostgreSQL, tabla de grants, tabla de suscripción, operaciones persistidas y SDK oficial.

**4. ¿Qué deprecar?**  
`basePlanId` escribible, dev-switch productivo, suma genérica de reservas, timestamp como solución universal de orden y precios/planes simulados en UI.

**5. ¿Qué construir nosotros?**  
Un resolver de acceso, proyección financiera mínima, idempotencia durable, cardinalidad de beats, política PROJECT, uso YouTube y autorización efectiva de operaciones.

**6. ¿Camino más corto a una V1 confiable?**  
Mensual, checkout/portal alojados, bienvenida interna, cambios pagados al siguiente período, un proveedor, PostgreSQL, datos conservados y gates reales de almacenamiento/sandbox.

**7. ¿Qué posponer?**  
Anual hasta fijar precio, upgrade inmediato con prorrateo, referrals públicos, cupones complejos, dispositivos/sesiones comerciales, plataformas de metering y facturación propia.

**No posponer ni disfrazar:** autoridad única, escritura confiable, refunds sin borrado, concurrencia real y la disponibilidad efectiva de cualquier feature que se anuncie como parte del plan.