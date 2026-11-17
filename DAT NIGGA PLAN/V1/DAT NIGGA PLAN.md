**V1 será Web**, con biblioteca privada, pagos y cuotas, preparada para múltiples usuarios con cuentas y vaults independientes. Desktop llegará después, manteniendo los contratos comunes. YouTube podrá incluirse donde ya funcione y pase la revisión, sin bloquear el lanzamiento.

El orden es provisional: ajustaremos las etapas según la evidencia y concretaremos cada una al acercarnos a ella.

# 1.  Comprobar el uso real entre cuentas independientes
**Objetivo:** Preparar una prueba repetible con varias cuentas: abrir y escuchar mientras otras suben, editan, descargan y hacen Reload. Verificar aislamiento de datos, sesiones y operaciones; reparto sobre una pool amplia; arranque simultáneo, desconexión de un usuario y saturación.

**Por qué existe:** Las pruebas actuales no demuestran todavía el comportamiento completo bajo carga real. Más bots amplían el reparto, pero hay que medir también los recursos comunes del backend.

**Salida:** Cohorte inicial, navegadores y archivos representativos definidos; resultados medidos; fallos relevantes reproducidos y priorizados. Esta etapa termina con evidencia, aunque encuentre problemas.

# 2. Cerrar la fiabilidad del núcleo Web

**Objetivo:** Resolver los problemas demostrados, priorizando apertura/playback, conservación del estado, uploads y edición, después descargas y Trash. Comprobar recarga, reconexión, reinicio y reintento de operaciones interrumpidas.

**Por qué existe:** El usuario debe poder confiar en lo guardado y utilizar su biblioteca mientras otras cuentas trabajan.

**Salida:** Los recorridos acordados funcionan con la carga objetivo, sin pérdidas, cruces entre cuentas ni bloqueos graves conocidos; los tiempos cumplen los límites fijados tras la medición inicial. Una batería pequeña y repetible protege esas garantías.

# 3. Completar pagos, planes y cuotas

**Objetivo:** Conectar checkout, webhooks y gestión de suscripciones; establecer una única autoridad de permisos y aplicar las cuotas en las operaciones reales, incluyendo reintentos, cancelaciones y cambios de plan.

**Por qué existe:** Los módulos existentes todavía no forman un recorrido comercial completo.

**Salida:** Compra, renovación, cancelación y límites funcionan de extremo a extremo con el proveedor de pruebas; los reintentos no duplican efectos y cambiar de plan conserva los datos según una política explícita.

# 4. Preparar una versión operable

**Objetivo:** Disponer de despliegue reproducible, observación de fallos, recuperación, rollback y soporte básico. Ensayar la restauración de cuentas y biblioteca, incluyendo acceso a sus medios.

**Por qué existe:** Lanzar requiere poder recuperar el servicio y atender problemas reales.
    
**Salida:** Un candidato identificable puede desplegarse, restaurarse y revertirse mediante procedimientos comprobados, con responsables y alertas básicas definidos.
    
# 5. Validar con usuarios y lanzar gradualmente

**Objetivo:** Probar el candidato con una cohorte limitada, verificar el cobro real controlado y ampliar el acceso dentro de la capacidad demostrada.

**Por qué existe:** El uso cotidiano aporta evidencia que las pruebas internas no cubren.

**Salida:** La cohorte completa los recorridos principales durante una ventana acordada, sin incidencias graves pendientes de datos, aislamiento, cobros o uso esencial. Los defectos menores quedan registrados para después.


La edición simultánea del mismo vault queda como robustez secundaria, salvo evidencia de mayor exposición. Los refactors solo entran para resolver problemas concretos de estas etapas; no habrá una fase de “limpiar todo”. Una etapa cerrada se reabre por evidencia relevante, no por nuevas posibilidades de perfeccionamiento.




