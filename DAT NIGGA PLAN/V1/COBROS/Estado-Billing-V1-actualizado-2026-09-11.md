# Estado maestro — BeatGaler Billing V1

**Actualizado:** 11 de septiembre de 2026  
**Repositorio:** `magosouljah/BeatGaler`  
**Rama de trabajo:** `billing/v1-policy`  
**HEAD actual:** `38e959cade4f1b16f6655443fd316126d433dd0e`  
**PR de validación:** `#140 — Billing V1: resolver, policy tests and persistence foundation`  
**Estado del PR:** abierto, **draft**, no mergeado.

hmmmmmmmm. El estado anterior decía que sólo estaban terminadas las Tareas 1 y 2. Eso ya quedó obsoleto: **las Tareas 1, 2, 3, 4 y 5 están terminadas dentro del alcance definido para cada una**.

La distinción importante es esta:

- **Tareas 1–2:** política y catálogo comercial definidos.
- **Tarea 3:** resolver puro de acceso implementado.
- **Tarea 4:** tests del resolver/políticas escritos y ejecutados con PASS real.
- **Tarea 5:** fundación PostgreSQL de billing preparada y validada contra PostgreSQL real aislado.
- **Todavía NO:** Polar real, checkout nuevo, webhooks nuevos, wiring del resolver al runtime, aplicación de `0011` sobre la base real, producción ni E2E de compra completo.

---

## Estado Git actual

### Rama

La rama sigue siendo:

`billing/v1-policy`

Históricamente se separó del trabajo de membresía persistente bot ↔ vault cuando ese trabajo estaba en:

`direct/persistent-vault-assignment @ a112563646d61940c7c16e025702329c1219b4f7`

Ese dato sigue siendo histórico; ya **no** describe el HEAD actual.

### Base actual del PR

El PR #140 compara contra:

`integration-v0.9.0-alpha.4 @ 7cbd4a5afd34b619fb508a264b0796a9764c9ff3`

### HEAD actual de billing

`38e959cade4f1b16f6655443fd316126d433dd0e`

### Estado de integración

- PR #140 abierto.
- Draft.
- No mergeado.
- La rama contiene el trabajo de Tareas 3–5 por encima del baseline `7cbd4a5`.
- No se aplicó `0011` a producción ni a la base PostgreSQL real usada por BeatGaler.
- No se tocó la base empleada para la migración persistente de bots.

---

# Tarea 1 — Política Billing V1

## 1. Cerré la política de Billing V1

Creé:

`BLUEPRINT/BILLING-V1-POLICY.md`

Commit de esta parte:

`d54352339bf853c2656962f55c3bbf2c707f0ea1`

Ese commit sólo añadió documentación de billing. No tocó código runtime.

### Planes definidos

||Free|Paid Entry|Highest Paid|
|---|--:|--:|--:|
|Precio mensual|$0|**$6.99 USD**|**$11.99 USD**|
|Beats incluyendo Trash|20|100|Sin límite comercial|
|Nuevo PROJECT ZIP|No|Sí|Sí|
|PROJECT ZIP máx.|—|1,000,000,000 bytes|1,900,000,000 bytes|
|YouTube/día|3|10|Sin límite|
|YouTube/mes|31|60|Sin límite|
|Bulk|`none`|`limited`|`full`|
|Early Access|No|No|Sí|

Además decidí explícitamente que **V1 no tendrá límites comerciales de dispositivos ni sesiones simultáneas**. Los límites técnicos/de seguridad siguen siendo otra cosa.

Esto además corrige una diferencia con el `plans.js` histórico, que todavía contiene límites de dispositivos/sesiones y tamaños binarios antiguos.

---

## 2. Bienvenida

La bienvenida quedó definida como un **grant interno de BeatGaler**, no como un trial de Polar.

Reglas:

- 7 días.
    
- Nivel Paid Entry.
    
- Sin tarjeta.
    
- Sin checkout.
    
- Una sola vez por usuario elegible.
    
- Empieza al activar/verificar la cuenta.
    
- Reinstalar, volver a conectar OAuth, cambiar email o volver a iniciar sesión no reinicia los 7 días.
    
- Comprar durante la bienvenida no extiende los 7 días ni retrasa el cobro.
    
- Cuando vence, se vuelve al mejor acceso que siga existiendo.
    

El código histórico ya tenía la idea de 7 días de Paid Entry, pero la política nueva define exactamente cómo debe funcionar.

---

## 3. Definí qué realmente concede Paid

Quedó prohibido conceder acceso por un redirect de checkout.

Ni:

`checkout success redirect`

ni:

`checkout.created`

son evidencia suficiente.

Paid sólo aparece cuando BeatGaler tiene evidencia financiera confirmada del período y esa información está proyectada en PostgreSQL.

También dejé explícito que:

`current_period_end`

**no significa automáticamente “este período está pagado”.**

---

## 4. Cancelación

Cancelación normal:

`Paid ──cancel──> Paid hasta paid_through ──vence──> Free/grant`

Es decir:

- cancelar no quita el acceso inmediatamente;
    
- mantiene el nivel comprado hasta acabar el período ya pagado;
    
- después se recalcula el acceso;
    
- puede deshacerse la cancelación antes del final si el proveedor lo permite;
    
- **no se borra ningún archivo**.
    

Separé además la cancelación normal de una **terminación administrativa inmediata**, que sí puede retirar el acceso comercial inmediatamente, pero tampoco borra datos.

---

## 5. Pago fallido y gracia

### Primera compra fallida

No concede Paid.

Si el usuario todavía tiene bienvenida u otro grant, ese grant continúa normalmente.

### Renovación fallida

Definí:

**7 días de gracia.**

Durante esos siete días conserva exactamente el **último plan que sí pagó**.

Por ejemplo:

`Paid Entry pagado → intenta renovar Highest → falla`

Durante gracia sigue siendo:

`Paid Entry`

No se le concede Highest gratis.

Además:

- la gracia empieza en el primer `past_due_at` de ese período;
    
- los retries del proveedor no reinician los siete días;
    
- si paga, se recupera normalmente;
    
- si vence la gracia, baja a grants válidos o Free;
    
- errores/timeout del proveedor no se interpretan automáticamente como Free ni como Paid infinito.
    

El billing actual todavía no sabe hacer esto: su resolver histórico sólo considera `active` y `trialing` como acceso pagado.

---

## 6. Refunds

Elegí la política:

**retirar acceso, conservar datos.**

### Refund completo del período actual

Si el pago que sostiene el acceso actual queda invalidado:

`Paid → recalcular acceso`

Puede terminar en Free, bienvenida u otro grant.

Pero:

**NO borrar beats.  
NO borrar PROJECT.  
NO borrar Trash.**

Si tenía 80 beats y termina en Free 20:

`80 / 20 — over quota`

Puede seguir usando lo existente, pero no crear nuevas identidades hasta bajar dentro del límite.

### Refund parcial

Por defecto **no quita acceso**.

Si soporte decide explícitamente que ese refund parcial también termina el servicio, será una acción administrativa distinta.

### Refund histórico

Un refund de un mes anterior no puede cancelar automáticamente el período actual.

### Refund pendiente

No se considera completado hasta tener confirmación.

---

## 7. Cambios de plan

Definí una V1 intencionalmente simple.

### Free → Paid

Inmediato **después de confirmar el pago**.

### Paid Entry ↔ Highest Paid

Cambio al **siguiente período**.

Nada de prorrateos inmediatos en V1.

Ejemplo:

`Paid Entry → pedir Highest`

sigue Paid Entry hasta renovar.

Si la renovación de Highest se paga:

`→ Highest`

Si falla:

`→ gracia de Paid Entry`

### Paid → Free

Es básicamente una cancelación al final del período.

---

## 8. Regla única conceptual de acceso

Definí la jerarquía:

`free < paid_entry < highest_paid`

El plan efectivo debe ser el máximo entre:

1. Free.
    
2. Suscripción comercial válida.
    
3. Gracia válida del último tier pagado.
    
4. Grants activos, como bienvenida.
    

No se suman cuotas.

Ejemplo:

`Free 20 + grant Paid Entry 100`

no significa:

`120 beats`

Significa simplemente:

`Paid Entry = 100`.

---

## 9. Dejé dos cosas explícitamente pendientes

### Annual

El sistema ya podrá representarlo, pero **no se vende todavía**.

Pendientes:

- precio Paid Entry anual;
    
- precio Highest anual;
    
- fecha/política de lanzamiento;
    
- transiciones mensual ↔ anual.
    

No inventé ningún descuento.

### Bulk Paid Entry

Continúa siendo:

`limited`

pero todavía no inventé cuántos videos puede contener un lote.

---

# Tarea 2 — Catálogo comercial configurable

Después creé:

`cloud-server/billing-commercial-catalog.js`

y:

`BLUEPRINT/BILLING-V1-CATALOG.md`

Además:

`cloud-server/tests/billing-commercial-catalog.test.cjs`

El delta desde el final de Tarea 1 son únicamente esos tres archivos.

---

## 10. Separé plan de oferta comercial

Esto es importante.

Antes el checkout existente prácticamente hacía:

`paid_entry = producto`

y mezclaba:

- plan;
    
- price ID;
    
- proveedor;
    
- moneda;
    
- trial;
    
- tax.
    

El checkout viejo todavía funciona de esa forma.

Ahora separé las cosas conceptualmente:

`PLAN`  
→ qué puede hacer el usuario

`OFFER`  
→ qué puede comprar

`PROVIDER MAPPING`  
→ qué Product/Price de Polar corresponde a esa oferta

Así cambiar Polar no debería cambiar la definición de Paid Entry.

---

## 11. Ofertas internas creadas

Actualmente existen:

```text
paid_entry_monthly_v1
highest_paid_monthly_v1
paid_entry_annual_v1
highest_paid_annual_v1
```

Mensuales:

```text
paid_entry_monthly_v1
plan = paid_entry
interval = month
currency = usd
amountMinor = 699
salesEnabled = true
```

```text
highest_paid_monthly_v1
plan = highest_paid
interval = month
currency = usd
amountMinor = 1199
salesEnabled = true
```

Anuales:

```text
interval = year
amountMinor = null
salesEnabled = false
pendingReason = ANNUAL_PRICE_AND_LAUNCH_PENDING
```

Esto está implementado en el nuevo catálogo.

---

## 12. Polar quedó configurado como proveedor V1

El catálogo reconoce:

```text
provider = polar
```

y dos ambientes:

```text
sandbox
production
```

Pero **no he creado absolutamente nada en Polar**.

No existen todavía:

- productos Polar;
    
- precios Polar;
    
- API keys;
    
- webhooks Polar;
    
- checkout Polar;
    
- portal Polar.
    

Eso corresponde a tareas posteriores.

---

## 13. Mapping separado por ambiente

Una oferta puede mapearse server-side a:

```text
productId
priceId
```

Por ejemplo conceptualmente:

```text
paid_entry_monthly_v1
    ↓
Polar sandbox
    productId = ...
    priceId   = ...
```

Eso permite que sandbox y producción tengan IDs distintos.

Nada de esto viene del frontend.

---

## 14. Añadí `checkoutReady`

Una oferta sólo puede estar lista para checkout cuando se cumplen las dos cosas:

```text
salesEnabled = true
+
providerMapping existe
```

Entonces:

```text
checkoutReady = true
```

Una oferta mensual sin Price ID de Polar todavía dará:

```text
checkoutReady = false
```

Y aunque alguien accidentalmente configure IDs para annual:

```text
salesEnabled = false
```

por lo que **annual continúa sin venderse**.

---

## 15. El catálogo falla cerrado

Añadí validaciones para impedir:

- proveedor desconocido;
    
- ambiente distinto de sandbox/production;
    
- oferta desconocida;
    
- plan inexistente;
    
- vender Free;
    
- intervalo inválido;
    
- moneda distinta de USD;
    
- oferta activa sin precio;
    
- mapping de una oferta inexistente;
    
- IDs de proveedor vacíos/inválidos;
    
- intentar checkout de una oferta deshabilitada;
    
- intentar checkout sin mapping de proveedor.
    

El módulo sigue siendo completamente puro: no hace requests, no toca DB y no concede acceso.

---

## 16. Tests que escribí

Creé tests para comprobar el nuevo catálogo:

`cloud-server/tests/billing-commercial-catalog.test.cjs`

Cubren, entre otras cosas:

- precios mensuales exactos;
    
- annual deshabilitado;
    
- mapping sandbox;
    
- oferta habilitada pero sin provider mapping ≠ checkout ready;
    
- rechazo de configuraciones desconocidas.
    


### Actualización de evidencia de tests

El estado anterior decía correctamente que, en aquella sesión, los tests del catálogo sólo estaban escritos y todavía no se habían ejecutado. **Eso ya quedó superado por trabajo posterior.**

Estado actual:

- `cloud-server/tests/billing-commercial-catalog.test.cjs`: **5/5 PASS real**.
- `cloud-server/tests/billing-access-resolver.test.cjs`: **14/14 PASS real**.
- Total conjunto de catálogo + resolver: **19/19 PASS, 0 fallos**.

Por tanto, ya no aplica la frase antigua “PASS confirmado: no todavía”.

---

# Tarea 3 — Resolver único de acceso puro ✅

## 17. Archivo creado

Creé:

`cloud-server/billing-access-resolver.js`

Commits relevantes de esta etapa:

- `47eb76423c386a76a8e9e880498af91c59d1ccf5` — creación inicial del resolver.
- `22e6a3d0eacbcd5b029ac3d2d73ac222979b9d0a` — cierre de Tarea 3 y ajuste del catálogo comercial para validar contra el catálogo V1 nuevo.

El módulo es deliberadamente **puro**.

No hace:

- queries PostgreSQL;
- requests a Polar;
- lecturas de Auth;
- llamadas a bots;
- operaciones Direct;
- lecturas implícitas del reloj;
- mutaciones de runtime.

El caller debe pasar explícitamente el instante del servidor mediante `now`.

---

## 18. Catálogo de acceso V1 dentro del resolver

El resolver usa el catálogo de acceso aprobado, no los límites históricos de `plans.js`.

### Free

```text
plan = free
rank = 0
upload_project = false
bulk_youtube_upload = none
early_access = false
max_beats = 20
max_project_zip_bytes = 0
youtube_uploads_per_day = 3
youtube_uploads_per_month = 31
```

El `0` de PROJECT en Free es un techo fail-closed. La autorización principal sigue siendo:

`upload_project = false`

### Paid Entry

```text
plan = paid_entry
rank = 1
upload_project = true
bulk_youtube_upload = limited
early_access = false
max_beats = 100
max_project_zip_bytes = 1_000_000_000
youtube_uploads_per_day = 10
youtube_uploads_per_month = 60
```

### Highest Paid

```text
plan = highest_paid
rank = 2
upload_project = true
bulk_youtube_upload = full
early_access = true
max_beats = null
youtube_uploads_per_day = null
youtube_uploads_per_month = null
max_project_zip_bytes = 1_900_000_000
```

`null` significa **sin límite comercial del plan**, no ausencia de controles técnicos/antiabuso.

---

## 19. Regla real para conceder acceso comercial

El resolver **no confía en `status=active`**.

Una suscripción comercial sólo aporta acceso si existe un plan conocido y hay cobertura financiera válida.

### Paid normal

Debe existir:

```text
paid_through > now
```

Además, una invalidación comercial ya efectiva puede retirar esa fuente.

### Gracia

Debe cumplirse:

```text
past_due_at <= now
AND
grace_until > now
```

Durante esa gracia se conserva el plan almacenado que representa el último nivel realmente pagado.

### Lo que NO basta

Ninguno de estos valores por sí solo concede Paid:

```text
status = active
status = trialing
current_period_end futuro
checkout redirect success
checkout.created
```

Esto materializa en código la política cerrada en Tarea 1.

---

## 20. Invalidaciones comerciales

El resolver entiende:

`access_invalidated_at`

Si:

```text
access_invalidated_at <= now
```

la fuente comercial deja de aportar acceso.

Esto permite representar, por ejemplo:

- refund completo confirmado del período que sostiene el acceso;
- terminación administrativa inmediata;
- invalidación financiera explícita.

Si la invalidación está programada para el futuro, también sirve como frontera para `nextRecalculationAt`.

---

## 21. Grants

Cada grant puede aportar un plan si:

```text
starts_at <= now
expires_at > now
revoked_at es null o > now
```

Un grant con plan desconocido, timestamps inválidos o intervalo imposible no se convierte en acceso válido.

Fuentes típicas:

- bienvenida;
- promoción futura;
- concesión administrativa temporal.

No se creó una tabla `grants` nueva: el diseño sigue reutilizando `entitlements` como grants.

---

## 22. Selección del plan efectivo

El resolver parte siempre de:

`Free`

Después compara:

- fuente comercial válida;
- gracia válida;
- grants activos.

Y elige el plan con **rank más alto**.

Ejemplo:

```text
suscripción Paid Entry válida
+
grant Highest Paid válido
=
Highest Paid
```

No suma cuotas.

Otro ejemplo:

```text
suscripción Highest Paid válida
+
grant Paid Entry
=
Highest Paid
```

El grant inferior no reduce la suscripción.

---

## 23. Estado comercial separado de plan efectivo

El resultado distingue conceptos que antes podían confundirse.

Devuelve, entre otros:

```text
commercialPlanId
commercialAccessPlanId
commercialAccessState
effectivePlanId
label
capabilities
quotas
accessSources
nextRecalculationAt
billing
```

`commercialAccessState` puede representar:

```text
none
paid
grace
invalidated
unverified
```

Por ejemplo, una fila puede decir comercialmente `highest_paid`, pero si no tiene evidencia financiera suficiente:

```text
commercialPlanId = highest_paid
commercialAccessState = unverified
effectivePlanId = free   // salvo grants
```

Eso evita convertir una afirmación comercial no demostrada en permisos.

---

## 24. Próxima fecha de recálculo

El resolver devuelve:

`nextRecalculationAt`

Puede quedar determinada por:

- `paid_through`;
- `grace_until`;
- invalidación futura;
- expiración de un grant;
- revocación futura;
- comienzo futuro de un grant;
- comienzo futuro de una gracia cuando corresponde.

La expiración no depende de que un cron cambie físicamente una fila a Free en el segundo exacto del vencimiento.

La autorización puede recalcular usando `now` cada vez que corresponda.

---

## 25. Información de renovación/cancelación preservada

El bloque `billing` del resultado conserva metadata relevante como:

```text
providerStatus
paidThrough
pastDueAt
graceUntil
accessInvalidatedAt
invalidationReason
currentPeriodEnd
endedAt
cancelAtPeriodEnd
nextPlanId
nextInterval
nextPlanEffectiveAt
```

Esto permite mostrar estado comercial sin usarlo automáticamente como autoridad de acceso.

---

## 26. Cambio importante en el catálogo comercial

`cloud-server/billing-commercial-catalog.js`

ahora valida `planId` contra:

`BILLING_V1_ACCESS_CATALOG`

y no contra los límites históricos de `plans.js`.

Esto evita que una oferta comercial nueva termine heredando accidentalmente:

- límites viejos de dispositivos;
- límites viejos de sesiones;
- tamaños binarios anteriores;
- otras reglas históricas que no pertenecen a Billing V1.

---

# Tarea 4 — Tests completos del resolver y políticas ✅

## 27. Archivo de tests

Creé:

`cloud-server/tests/billing-access-resolver.test.cjs`

El objetivo de esta tarea no fue sólo escribir tests: **se ejecutaron realmente**.

---

## 28. Casos cubiertos por los 14 tests del resolver

Entre los escenarios cubiertos están:

1. Free como baseline cuando no existe ninguna fuente válida.
2. Bienvenida Paid Entry activa.
3. Bienvenida vencida.
4. Suscripción cubierta por `paid_through`.
5. Cancelación que conserva Paid hasta acabar el período ya pagado.
6. Primera compra fallida que no concede Paid.
7. Renovación fallida con gracia.
8. Upgrade pendiente a Highest que falla: la gracia conserva Paid Entry, no regala Highest.
9. Invalidación/refund completo que retira la fuente comercial y recalcula.
10. Grants simultáneos: gana el nivel jerárquico más alto.
11. Highest mantiene cuotas ilimitadas comerciales donde corresponde.
12. Cálculo de `nextRecalculationAt`.
13. `status=active` sin evidencia financiera suficiente no concede Paid.
14. `current_period_end` futuro por sí solo tampoco concede Paid.

---

## 29. Resultado real de tests de Tarea 4

Se ejecutaron contra el código del HEAD correspondiente de la tarea.

Resultado:

```text
billing-access-resolver: 14 / 14 PASS
billing-commercial-catalog: 5 / 5 PASS
------------------------------------
total: 19 / 19 PASS
fail: 0
```

En esa validación se usó Node 22.

El HEAD con Tarea 4 cerrada quedó en:

`b3b9d0e0a1b4da035cd232501c750cd9c4f143f2`

---

# Tarea 5 — Fundación PostgreSQL de Billing V1 ✅

## 30. Qué significa “Tarea 5 terminada”

Significa:

- inventariamos las migraciones presentes en la rama;
- comprobamos que `0001`–`0010` ya existían;
- no reescribimos ninguna de ellas;
- añadimos una migración nueva exclusivamente de billing;
- añadimos una prueba PostgreSQL aislada;
- ejecutamos la prueba contra PostgreSQL real;
- comprobamos idempotencia y constraints;
- comprobamos que los gates PostgreSQL de Direct siguen funcionando.

**NO significa** que la migración ya se haya aplicado a la base real de BeatGaler.

---

## 31. Inventario previo de migraciones

La rama tenía:

```text
0001_control_plane.sql
0002_auth_identity_compat.sql
0003_control_plane_cutover.sql
0004_control_plane_cutover_stage.sql
0005_direct_capabilities.sql
0006_billing_webhooks.sql
0007_entitlement_reservations.sql
0008_billing_reconciliation.sql
0009_startup_routing.sql
0010_persistent_transport_assignment.sql
```

Por tanto el número siguiente disponible fue:

`0011`

Se verificó contra las ramas vigentes antes de escribirlo para evitar elegir un número a ciegas.

---

## 32. Tablas de billing que ya existían antes de 0011

### `entitlements`

Ya existía desde `0001`.

La política nueva decidió reutilizarla como tabla de grants.

### `billing_webhook_events`

Ya existía desde `0006`, junto con `billing_webhook_subjects`.

Su conversión al inbox durable definitivo queda para Tarea 8.

### `billing_subscription_state`

Ya existía desde `0007`, pero con un modelo mucho más simple.

### `entitlement_reservations`

Ya existía desde `0007`.

No se expandió como acumulador universal; el plan nuevo pretende deprecar ese uso.

### `billing_reconciliation_exceptions`

Ya existía desde `0008` y se conserva para inconsistencias/ambigüedades que no puedan repararse automáticamente.

---

## 33. Migración nueva

Creé:

`cloud-server/migrations/0011_billing_v1_foundation.sql`

Commit inicial de la migración:

`219935b4ff841553ab3ed77645d91fd1da3ac40f`

La migración está delimitada transaccionalmente y entra al runner existente con checksum en `schema_migrations`.

---

## 34. Expansión de `billing_subscription_state`

Se mantiene **una fila por usuario**, en vez de crear otra tabla competidora para la suscripción actual.

La fundación V1 añade soporte para:

```text
provider
provider_environment
offer_id
current_period_start
paid_through
past_due_at
grace_until
ended_at
next_plan_id
next_interval
next_plan_effective_at
access_invalidated_at
access_invalidation_reason
last_synced_at
local_version
```

Además conserva los campos históricos que siguen siendo necesarios, como:

```text
provider_customer_id
provider_subscription_id
plan_id
status
cancel_at_period_end
current_period_end
updated_at
```

---

## 35. Constraints importantes de suscripción

Entre otras cosas, el esquema impone:

- planes conocidos;
- proveedor V1 reconocido;
- ambiente `sandbox` o `production`;
- intervalos conocidos;
- períodos temporales coherentes;
- gracia temporal coherente;
- invalidación con motivo consistente;
- versión local positiva;
- identidad externa de suscripción única por proveedor + ambiente;
- una fila que pretende representar estado comercial pagado no puede depender solamente de `status` sin la evidencia requerida por el modelo.

Esto alinea persistencia con el resolver de Tarea 3.

---

## 36. `entitlements` convertido hacia grants V1

No se creó una tabla `grants` paralela.

Se amplió `entitlements` con conceptos como:

```text
source_key
revoked_at
revocation_reason
issued_by_user_id
issued_at
```

Y se incorporaron reglas para:

- identidad estable del grant;
- unicidad `user_id + source + source_key`;
- expiración real de grants V1;
- revocación consistente;
- consulta por usuario/expiración;
- una bienvenida por usuario mediante índice único parcial.

Los `source_key` históricos reciben una identidad de compatibilidad basada en el ID previo.

---

## 37. Nueva tabla `billing_customers`

Se añadió para poder representar un customer del proveedor **antes** de que exista una suscripción.

Guarda, entre otros:

```text
id
user_id
provider
provider_environment
provider_customer_id
external_id
created_at
updated_at
```

Reglas importantes:

- FK al usuario;
- un usuario no tiene dos customers para el mismo proveedor/ambiente;
- un customer externo no puede pertenecer a dos usuarios;
- email no se usa como clave de propiedad.

---

## 38. Nueva tabla `billing_checkout_requests`

Se añadió para idempotencia y recuperación de timeouts/ambigüedad.

Conceptos principales:

```text
user_id
request_id
offer_id
request_hash_sha256
provider
provider_environment
state
provider_checkout_id
provider_checkout_url
expires_at
result
last_error_code
last_error_redacted
created_at
updated_at
```

Estados preparados:

```text
OPEN
CREATING
READY
AMBIGUOUS
CONSUMED
EXPIRED
FAILED
```

Reglas importantes:

- PK por `user_id + request_id`;
- hash SHA-256 válido;
- oferta V1 conocida;
- checkout externo único cuando existe;
- una solicitud no resuelta por usuario para el flujo de suscripción;
- `READY` exige información suficiente para recuperar el checkout;
- un timeout ambiguo puede seguir siendo `AMBIGUOUS` en lugar de crear otro checkout automáticamente.

---

## 39. Nueva tabla `billing_payments`

Se añadió una proyección financiera mínima.

No pretende ser un ledger contable completo.

Puede representar:

```text
provider_payment_id
provider_order_id
provider_invoice_id
user_id
provider_subscription_id
offer_id
period_start
period_end
amount_minor
currency
status
refunded_amount_minor
invalidated_at
invalidation_reason
created_at
updated_at
```

Reglas relevantes:

- identidad externa de pago única por proveedor/ambiente;
- intervalos válidos;
- refund no puede superar el importe relevante;
- invalidaciones deben ser coherentes;
- permite distinguir pago actual, refund parcial, refund completo e histórico.

No almacena PAN, CVV ni datos bancarios sensibles.

---

## 40. Lo que deliberadamente NO entró en 0011

No añadí todavía:

`library_beats`

ni:

`youtube_operations`

Esas tablas pertenecen a la integración real de cuotas/cardinalidad y YouTube, no a esta fundación inmediata.

Tampoco convertí todavía `billing_webhook_events` al inbox durable completo de Tarea 8.

---

## 41. Test PostgreSQL aislado

Creé:

`cloud-server/tests/billing-v1-migrations.integration.cjs`

Commit:

`1fe2d13d569c12a59d2e9a237c7b5c8890e1f01e`

El test no usa la base real de BeatGaler.

Hace lo siguiente:

1. Conecta a un PostgreSQL de pruebas.
2. Crea una base con nombre aleatorio.
3. Ejecuta el runner real de migraciones.
4. Aplica `0001` → `0011`.
5. Ejecuta el runner una segunda vez.
6. Confirma que la segunda pasada no reaplica migraciones.
7. Revisa el ledger `schema_migrations` y sus checksums.
8. Valida tablas/columnas/constraints relevantes.
9. Inserta datos de prueba.
10. Provoca violaciones esperadas para demostrar que los constraints realmente bloquean estados inválidos.
11. Cierra conexiones.
12. Elimina la base efímera.

---

## 42. Constraints demostrados en PostgreSQL real

El test confirmó, entre otras cosas, que PostgreSQL rechaza:

- reutilizar el mismo customer externo para dos usuarios;
- reutilizar la misma suscripción externa para dos usuarios;
- emitir dos bienvenidas al mismo usuario;
- mantener dos checkouts no resueltos simultáneamente para el mismo usuario;
- registrar un refund mayor al importe relevante;
- usar un `request_hash_sha256` inválido.

Los errores correspondientes aparecen en el log de PostgreSQL **porque son provocados deliberadamente por el test**. No son fallos de la suite.

---

## 43. Workflow dedicado de migraciones

Creé:

`.github/workflows/billing-v1-migrations.yml`

Commit inicial:

`f7c4bfa52123c53d2911bdb922b1854053d4d363`

El workflow usa:

- Ubuntu 24.04;
- Node 22;
- PostgreSQL 18;
- `npm ci` del `cloud-server`;
- checkout del HEAD exacto del PR;
- base efímera creada por el test.

---

## 44. Primer intento del workflow: fallo de infraestructura corregido

El primer run no llegó a PostgreSQL ni al test.

Falló durante setup porque se había usado por error un SHA incompleto/inválido de:

`actions/checkout`

GitHub devolvió esencialmente:

```text
Unable to resolve action actions/checkout@...
```

No fue un error de `0011`.

Lo corregí usando el pin válido ya empleado por workflows recientes del mismo repo:

```text
actions/checkout@3d3c42e5aac5ba805825da76410c181273ba90b1
```

El commit de corrección fue:

`38e959cade4f1b16f6655443fd316126d433dd0e`

Éste es el HEAD actual.

---

## 45. Resultado real de PostgreSQL 18

El segundo run sí llegó a ejecutar todo.

Entorno observado:

```text
PostgreSQL 18.6
Node 22.23.2
Ubuntu 24.04
```

Resultado del test dedicado:

```text
Billing V1 migrations apply cleanly and enforce the isolated PostgreSQL schema
PASS 1 / 1
FAIL 0
```

Por tanto existe evidencia real de que:

- `0001`–`0011` aplican limpiamente sobre una base fresca;
- el runner registra checksums;
- la segunda ejecución es idempotente;
- los constraints V1 probados funcionan.

---

## 46. Compatibilidad con la migración persistente de bots

Tocar `cloud-server/migrations/**` también disparó el workflow existente:

`Direct - Persistent Vault Assignment`

El gate PostgreSQL de ese workflow pasó.

Pasaron:

- real PostgreSQL assignment integration;
- legacy lazy PostgreSQL rollout integration;
- existing `postgres-live.integration`;
- Direct capability PostgreSQL contract.

También pasó el Cloud unit gate de ese workflow.

Conclusión:

**la fundación de billing no rompió los contratos PostgreSQL verificados del trabajo persistente bot ↔ vault.**

---

## 47. PR de validación

Abrí:

`PR #140 — Billing V1: resolver, policy tests and persistence foundation`

Estado actual:

```text
base = integration-v0.9.0-alpha.4
base SHA = 7cbd4a5afd34b619fb508a264b0796a9764c9ff3
head = billing/v1-policy
head SHA = 38e959cade4f1b16f6655443fd316126d433dd0e
state = open
draft = true
merged = false
```

Se abrió como **draft** para obtener validación de CI.

No lo mergeé automáticamente.

---

# Estado CI del HEAD actual

## 48. Gates verdes

Para:

`38e959cade4f1b16f6655443fd316126d433dd0e`

están confirmados como SUCCESS:

```text
Billing V1 Migrations
Direct - Persistent Vault Assignment
D6 - Cross-Process Authorization
D7 - Direct Capability Authorization
Probe - Task 5.1 Productive Temp Auth Compile
F0 - 0.20 HEAD Secret Scan
```

Esto da evidencia adicional de que el cambio no rompió esos contratos concretos.

---

## 49. Gate general todavía rojo: `Test - Desktop Portability`

El workflow general:

`Test - Desktop Portability`

terminó en:

`FAILURE`

Esto **no cambia el resultado del gate específico de Billing V1 Migrations**, pero significa que el PR completo todavía no debe describirse como “todo CI verde”.

### Fallo concreto que sí pude clasificar

En `Backend package unit gates` hubo:

```text
126 tests
125 pass
1 fail
```

El test que falla está en:

`cloud-server/tests/billing-polar.test.cjs`

Caso:

`billing/polar enforces server-side catalog, canonical patch authorization, and durable webhook identity`

El assertion esperaba el código histórico:

`DIRECT_CREATE_SESSION_FORBIDDEN`

pero el runtime actual devolvió:

`DIRECT_TRANSPORT_AUTH_MISSING`

Esto parece una **desalineación de contrato/assertion heredado con el estado actual de Direct auth**, no un error demostrado de la migración `0011`.

Debe diagnosticarse antes de mergear el PR final; no voy a esconderlo ni a marcar el PR entero como verde.

### Otros jobs rojos del workflow general

El run también reportó fallo en:

- Web shared CI gate;
- Windows portability;
- Supply-chain advisory audit.

En esta revisión no obtuve logs utilizables de esos tres jobs, por lo que **no asigno causa sin evidencia**.

Jobs del mismo workflow que sí terminaron verdes incluyeron Android portability, macOS portability y Rust stable/formatting.

---

# Importante — qué NO demuestra todavía Tarea 5

## 50. No se aplicó 0011 a los datos reales

La prueba fue contra una base fresca y efímera.

Por tanto aún falta antes de una aplicación real:

1. Inventariar filas actuales de `billing_subscription_state`.
2. Inventariar `entitlements` históricos, especialmente grants sin expiración.
3. Identificar procedencia real de planes actuales.
4. Identificar referencias externas verdaderas de Polar, si existen.
5. Retirar el escritor histórico de Auth sobre `entitlements` antes del cutover correspondiente.
6. Preservar las fechas originales de bienvenida/promociones válidas.
7. No convertir un dev-switch antiguo en una suscripción pagada.
8. No regalar/reiniciar siete días a todas las cuentas.
9. Reconciliar suscripciones reales con el proveedor cuando exista integración de Polar.

### Riesgo concreto a revisar antes de aplicar sobre una DB histórica

El modelo V1 exige que los grants ordinarios caduquen y que estados comerciales pagados tengan evidencia suficiente.

Por eso una base histórica con, por ejemplo:

- `entitlements.expires_at = NULL`;
- filas `active` sin `paid_through`/oferta válida;
- grants escritos por Auth con procedencia ambigua;

puede necesitar transformación/reconciliación previa.

**El PASS sobre base fresca no autoriza aplicar `0011` ciegamente sobre producción.**

---

# Lo que NO he conectado todavía

## 51. Polar sigue sin existir operativamente

Todavía no se crearon en Polar:

- productos;
- prices;
- API keys;
- webhook endpoints/configuration;
- checkout real;
- portal;
- sandbox customer flows;
- producción.

El catálogo sólo sabe **representar** mappings Polar server-side.

---

## 52. Resolver todavía no es autoridad runtime

`resolveBillingAccess()` existe y está probado, pero todavía no está conectado como autoridad única a:

- Auth;
- rutas de servidor;
- Account;
- Settings;
- uploads;
- downloads;
- playback;
- creación de beats;
- PROJECT;
- YouTube;
- Direct capabilities.

Ninguna ruta debe considerarse migrada al nuevo resolver sólo porque el módulo ya existe.

---

## 53. Checkout nuevo todavía no existe

Aunque `billing_checkout_requests` ya puede persistir idempotencia, falta implementar el flujo real que:

- recibe una request estable;
- resuelve la oferta;
- crea/recupera customer;
- llama a Polar sandbox;
- persiste estado antes/después de la llamada;
- recupera timeouts;
- no duplica checkout;
- devuelve URL/resultado de forma idempotente.

Eso corresponde a Tarea 7, después del adaptador Polar sandbox de Tarea 6.

---

## 54. Webhooks V1 todavía no están migrados

`billing_webhook_events` existe históricamente, pero todavía falta convertirlo al inbox durable definido por la política nueva:

- proveedor + ambiente;
- identidad real del evento;
- digest del cuerpo;
- payload validado mínimo;
- identidad de usuario/suscripción resuelta;
- `received_at` / `processed_at`;
- estados `RECEIVED/PROCESSING/PROCESSED/FAILED/IGNORED`;
- retry;
- lease de procesamiento;
- error estable/redactado.

`billing_webhook_subjects` sigue siendo una pieza histórica a deprecar, no la solución final de orden global.

---

## 55. Lifecycle comercial runtime todavía falta

La política y el resolver ya saben representar:

- Paid normal;
- cancelación;
- gracia;
- refund/invalidation;
- cambio de plan al siguiente período;
- grants;

pero todavía falta el código que traduzca eventos reales de Polar a esas proyecciones PostgreSQL.

---

## 56. Cuotas de beats todavía no están impuestas por PostgreSQL V1

Todavía no existe `library_beats` V1.

Por tanto falta implementar la autoridad de cardinalidad para:

```text
activos + Trash + purga pendiente + reservas
```

con la semántica definida:

- alta nueva +1;
- retry de la misma alta +0 adicional;
- mover a Trash +0;
- restaurar misma identidad +0;
- purga confirmada −1;
- restaurar una identidad ya purgada = nueva alta.

El cliente nunca debe ser autoridad mediante un `beatCount` enviado por frontend.

---

## 57. PROJECT runtime todavía no aplica la política nueva

La regla aprobada es:

```text
upload_project = true
AND
tamaño real <= max_project_zip_bytes
```

pero falta conectar esa autorización al flujo real de escritura/reemplazo PROJECT.

Después de downgrade a Free, los PROJECT existentes deben conservarse/descargarse/eliminarse, pero no reemplazarse ni volver a subirse.

---

## 58. YouTube V1 todavía no está integrado

Todavía falta:

`youtube_operations`

más la reserva/confirmación de cuota por día/mes UTC.

La unidad definida sigue siendo:

**un video cuya subida a YouTube quedó confirmada**.

No cuentan preview/render/request HTTP individual.

---

## 59. Áreas del producto que no fueron modificadas por estas tareas de billing

La implementación de Tareas 1–5 no reescribió por motivos comerciales:

- membership persistente bot ↔ vault;
- pool de bots;
- provisioning de bots;
- credenciales Direct;
- transporte Direct;
- playback;
- downloads;
- INDEX;
- Trash;
- helper Desktop.

Sí se añadió una migración al mismo sistema PostgreSQL y por eso se ejecutaron gates de Direct para comprobar compatibilidad, pero no se cambió intencionalmente su arquitectura funcional.

---

# Pendientes de política que siguen abiertos

## 60. Annual

Sigue representable pero no vendible.

Pendientes:

- precio Paid Entry anual;
- precio Highest anual;
- descuento, si se decide alguno;
- fecha/política de lanzamiento;
- transición mensual ↔ anual.

No se inventó ningún valor.

---

## 61. Bulk de Paid Entry

Sigue siendo:

`limited`

pero falta definir el número exacto de videos permitidos por lote.

No se inventó todavía.

---

# Estado del plan actualizado

## 62. Progreso

**1. ✅ Políticas Billing V1**  
Cerradas y documentadas.

**2. ✅ Catálogo comercial configurable**  
Ofertas internas, Polar como proveedor lógico, mappings por ambiente, fail-closed y tests.

**3. ✅ Resolver único de acceso puro**  
Jerarquía Free/Paid/grants, `paid_through`, gracia, invalidación, capacidades, cuotas y próxima recalculación.

**4. ✅ Tests completos de resolver/políticas**  
14/14 resolver + 5/5 catálogo = 19/19 PASS real.

**5. ✅ Migraciones billing — fundación preparada y validada**  
`0011_billing_v1_foundation.sql`, integración PostgreSQL aislada, PostgreSQL 18.6 PASS e idempotencia comprobada. **No aplicada a DB real.**

**6. ⬜ Polar sandbox**  
Siguiente tarea.

**7. ⬜ Checkout persistente/idempotente**

**8. ⬜ Webhooks durable inbox**

**9. ⬜ Lifecycle comercial**

**10. ⬜ Reconciliación/logs**

**11. ⬜ E2E sandbox**

---

# Próximo trabajo exacto

## Tarea 6 — Adaptador Polar sandbox

El siguiente paso debe mantenerse separado del runtime general al principio.

Objetivo:

1. Definir el adaptador server-side de Polar.
2. Configurar exclusivamente `sandbox`.
3. Mantener API keys sólo server-side.
4. Resolver mappings de `paid_entry_monthly_v1` y `highest_paid_monthly_v1` sin confiar en IDs enviados por frontend.
5. No habilitar annual.
6. Implementar primitives necesarias para customer/checkout/subscription/payment/webhook verification sin conceder acceso directamente.
7. Añadir tests con respuestas controladas/fakes donde corresponda.
8. No conectar todavía toda la UI ni convertir redirect de checkout en autoridad.

Antes de hacer checkout real, el adaptador debe dejar claro qué datos provienen de BeatGaler y cuáles de Polar.

---

# Veredicto actual

Billing V1 ya no está solamente en fase de diseño.

Tenemos:

```text
POLÍTICA          ✅
CATÁLOGO          ✅
RESOLVER          ✅
TESTS DE DOMINIO  ✅
SCHEMA PG V1      ✅ preparado
PG AISLADO        ✅ probado
POLAR REAL        ⬜
CHECKOUT NUEVO    ⬜
WEBHOOKS NUEVOS   ⬜
LIFECYCLE RUNTIME ⬜
E2E SANDBOX       ⬜
PRODUCCIÓN        ⬜
```

La frontera correcta ahora es:

**Tareas 1–5 terminadas. Tarea 6 es la siguiente.**

Pero el PR #140 todavía debe permanecer tratado como trabajo en validación/integración porque el workflow general `Test - Desktop Portability` tiene fallos pendientes de clasificar/corregir, aunque los gates específicos de Billing V1 y PostgreSQL/Direct estén verdes.
