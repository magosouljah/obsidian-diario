# BeatGaler — Contexto acumulado para decidir cómo terminar V1

## Naturaleza de este documento

Este archivo reúne el contexto que llevó al estado actual de BeatGaler y los distintos intentos de planificación que se han hecho.

Los documentos usados como material son:

- `1.md`
- `2.md`
- `3.md`
- `!!!PLAN.zip`, que contiene varios planes, fases, gates, registros y documentos auxiliares.
- La conversación actual sobre qué significa que BeatGaler esté listo, el miedo a las regresiones, la divergencia Web/Desktop y la posibilidad de reorganizar el código.

Ninguno de esos planes se considera autoridad para decidir el trabajo futuro. Sus checkboxes, estados de tarea, fechas y secuencias representan intentos anteriores de organizar el proyecto. En particular, que una tarea figure como terminada o pendiente no se toma aquí como evidencia del estado real actual del repositorio.

El propósito de este documento es conservar información, motivaciones, preocupaciones, objetivos y contradicciones para que posteriormente pueda razonarse cuál es la forma óptima de terminar BeatGaler.

---

## 1. Situación que llevó a replantear el roadmap

El desarrollo de BeatGaler empezó a sentirse infinito.

La sensación actual no es principalmente que falten ideas o features, sino que el trabajo entra repetidamente en ciclos de reparación: aparece un problema, se corrige, surge otro, se modifica otra parte y queda la duda de si el arreglo anterior rompió algo distinto.

Existe un miedo concreto a este ciclo:

> arreglar una cosa → romper otra → arreglar la nueva → romper otra → continuar indefinidamente.

Esto ha producido dificultad para saber cuál debería ser el siguiente trabajo y para percibir progreso hacia una versión terminada.

El proyecto lleva meses, según lo expresado en la conversación, en una especie de feature freeze: no existe interés en seguir agregando funciones nuevas por agregar funciones. Aun así, el trabajo ha continuado creciendo debido a bugs, refactors, migraciones, arquitectura y problemas diferentes entre plataformas.

En algún momento incluso se ha considerado la posibilidad de comenzar el programa desde cero con una estructura mejor, precisamente por la sensación de que reparar y reorganizar la base existente puede no terminar nunca. No se ha tomado una decisión de reiniciar desde cero.

---

## 2. Dificultad para definir qué significa “terminado”

No existe todavía una definición cerrada y formal de “BeatGaler V1 está terminado”.

Cuando se plantearon varias posibles definiciones —uso personal diario, beta con usuarios reales o lanzamiento público— resultó difícil elegir una sola.

La formulación espontánea del objetivo fue:

> que todo funcione sin errores y que varias personas lo puedan usar al mismo tiempo.

Esa frase refleja dos preocupaciones distintas:

- confiabilidad funcional;
- funcionamiento multiusuario/concurrente.

También existe una tensión entre la expectativa intuitiva de “sin errores” y la experiencia práctica de que corregir errores puede producir regresiones en otras partes del sistema.

El problema de fondo no es únicamente decidir qué features pertenecen a V1. También falta determinar qué nivel de evidencia o estabilidad sería suficiente para dejar de reparar y considerar el producto listo.

---

## 3. Prioridades funcionales expresadas actualmente

El orden de importancia expresado para la experiencia real del producto es el siguiente.

### Prioridad más alta

Abrir la biblioteca y poder escuchar un beat lo más rápido posible.

Esto incluye implícitamente el camino que va desde abrir BeatGaler hasta tener la biblioteca disponible y conseguir que el audio empiece a reproducirse con la menor fricción posible.

### Segunda prioridad

Mantener correctamente el estado.

La persistencia y recuperación del estado se consideran “mega importantes”. La preocupación es que cerrar, recargar, reconectar o continuar usando la aplicación no produzca pérdida, corrupción o comportamiento inesperado del estado que el usuario ya tenía.

### Tercera prioridad

Subir beats y editar metadata.

Estas operaciones forman parte del núcleo de gestión de la biblioteca después de que abrir y escuchar sean confiables.

### Cuarta prioridad

Descargar.

Las descargas/exportaciones son importantes, pero quedan después de startup/playback, estado, upload y edición.

### Prioridad posterior

El resto de los flujos existentes, entre ellos acciones secundarias de biblioteca, Trash, offline u otras capacidades.

Este orden refleja la prioridad actual del usuario y no necesariamente el orden de los roadmaps históricos.

---

## 4. Alcance de producto actualmente expresado

### Multiusuario

La capacidad de que varias personas puedan usar BeatGaler al mismo tiempo forma parte de la idea actual de que el programa esté listo.

No se ha definido en esta conversación una cifra concreta de concurrencia que represente “varias personas”. Algunos planes históricos contienen modelos de capacidad y pools mucho más específicos, pero esas cifras pertenecen a esos planes y no se adoptan automáticamente como requisito actual.

### Pagos, planes y quotas

Pagos, planes y quotas sí se consideran obligatorios para V1.

La idea de lanzar primero una beta pública gratuita sin resolver esta parte no coincide con el alcance expresado actualmente para V1.

### Shared Folders y Public Profile

Shared Folders y Public Profile quedan fuera de V1 y se consideran V2.

### YouTube

YouTube ya fue trabajado anteriormente y existe la percepción de que funciona bastante bien. Sin embargo, no ha sido el foco durante aproximadamente el último mes.

La intención expresada es dejar su revisión para el final. Si al volver a probarlo no causa problemas importantes, el lanzamiento ideal incluiría YouTube.

Por tanto, YouTube ocupa una posición distinta de pagos: se desea en el lanzamiento si continúa funcionando, pero actualmente no es el foco del trabajo diario.

### Desktop

Existe apertura a posponer Desktop como plataforma de lanzamiento.

Sin embargo, existe una preocupación más importante que lanzar o no Desktop: no se quiere que Web y Desktop se conviertan en dos aplicaciones que evolucionan por caminos distintos.

Actualmente se percibe precisamente ese problema: aparecen errores diferentes en Web y Desktop.

La preocupación no es simplemente “Desktop tiene bugs”, sino que las dos plataformas puedan estar dependiendo de caminos, lógica o contratos suficientemente diferentes como para que reparar una no proteja a la otra.

---

## 5. Preocupación central por Web/Desktop

La separación entre Web y Desktop se ha convertido en una fuente de incertidumbre.

Históricamente BeatGaler tiene diferencias legítimas entre plataformas: Desktop dispone de Tauri/Rust, filesystem local, helpers y capacidades nativas; Web debe funcionar sin esas dependencias.

Al mismo tiempo, se desea que ambos productos compartan la mayor cantidad posible de lógica, contratos y comportamiento.

La situación percibida actualmente es que los errores diferentes entre Web y Desktop sugieren que esa frontera puede haberse vuelto demasiado divergente.

Esto genera una pregunta todavía abierta: cuánto debe ser compartido y cuánto debe permanecer específico de plataforma para que BeatGaler sea mantenible sin fingir que Web y Desktop tienen exactamente las mismas capacidades.

El plan histórico incluido en `!!!PLAN.zip` también trató esta tensión. Su arquitectura de lanzamiento buscaba una Web pura que no dependiera de Tauri/helper Desktop, al mismo tiempo que exigía contratos comunes y pruebas por plataforma. Ese enfoque forma parte del historial, no de una decisión actual obligatoria.

---

## 6. Miedo a regresiones

Una regresión, en el sentido usado durante esta conversación, es que una función que ya funcionaba deje de funcionar después de modificar otra parte del programa.

Ejemplo conceptual dentro de BeatGaler:

- se corrige upload;
- upload funciona;
- después se descubre que playback, Reload, cierre o alguna ruta Desktop/Web dejó de funcionar debido al cambio.

La preocupación no es únicamente detectar bugs nuevos. Es no saber con suficiente confianza qué otras partes deben volver a comprobarse después de cada modificación.

Esta preocupación está directamente relacionada con varios planes históricos que intentaron crear pruebas de regresión, integración, gates y contratos compartidos.

---

## 7. Preocupación por la estructura y legibilidad del código

Además de la estabilidad funcional, existe una preocupación fuerte por la organización interna del código.

La pregunta actual es si convendría organizar todo el código antes de continuar, para conseguir una base limpia, fácil de leer y fácil de reparar.

Esta duda surge después de trabajar con archivos muy grandes y responsabilidades mezcladas.

No se trata solamente de estética. La preocupación es que una estructura difícil de entender aumente la posibilidad de:

- cambiar una parte sin comprender sus dependencias;
- crear regresiones;
- tardar demasiado en encontrar causas raíz;
- repetir lógica;
- tener comportamientos distintos entre plataformas;
- necesitar tocar demasiadas áreas para reparar un bug pequeño.

Al mismo tiempo, existe la experiencia de que una reorganización grande también puede convertirse en otra fuente de trabajo interminable.

Esta tensión —limpiar primero frente a estabilizar primero— todavía no está resuelta.

---

# 8. Intento de planificación: `1.md` — migración y reducción de `App.tsx`

`1.md` representa un intento de resolver el problema de mantenibilidad reorganizando el frontend alrededor de responsabilidades más pequeñas.

Su objetivo declarado era organizar el código de BeatGaler y dejar `App.tsx` como una entrada pequeña sin modificar el comportamiento de la aplicación.

El plan estaba dividido en diez grandes partes.

### Parte 1 — Preparación

Buscaba establecer una referencia comprobable del estado de la aplicación, ejecutar pruebas iniciales y preparar cobertura para flujos delicados.

### Parte 2 — Componentes visuales

Buscaba sacar de `App.tsx` ventanas auxiliares, buscador, menús y helpers.

### Parte 3 — Biblioteca y selección

Separaba estado de biblioteca, estados de operación por beat, búsqueda/filtros/tags, selección y reordenamiento.

### Parte 4 — Reproducción

Separaba artwork, preparación/control del audio y cola/navegación.

### Parte 5 — Acciones sobre beats

Separaba metadata/artwork, reemplazo de assets, proyectos, Available Offline, Trash/restore y rename de tags.

### Parte 6 — Descargas y uploads

Separaba exports, recuperación de uploads, pipeline de upload y cola de uploads.

### Parte 7 — Import y Review

Separaba sesión de Review, descubrimiento incremental, Save All/conflictos y entrada de importación Web.

### Parte 8 — Drag & drop

Separaba detección de destino, recepción HTML/browser y recepción nativa.

### Parte 9 — Startup y conexión

Separaba sesión/settings, Reload, bootstrap inicial, reconexión/eventos Cloud y revelado de tarjetas.

### Parte 10 — Cierre de la migración

Buscaba extraer la estructura visual restante, convertir `App.tsx` en una entrada mínima, retirar conexiones temporales y validar el resultado completo.

### Mejoras que el mismo plan dejaba fuera

Después de las diez partes aparecían mejoras posteriores separadas de la migración principal:

- dividir `UploadModal.tsx`;
- simplificar `LibraryUxBridge`;
- separar servicios de `AccountGate` y dividir `lib/tauri.ts`;
- dividir el interior de `Drawer.tsx`;
- investigar concurrencia de borrado masivo y snapshots obsoletos;
- medir consultas repetidas de proyectos antes de optimizarlas.

El documento también establecía la intención de conservar comportamiento, apariencia, formatos, diferencias Web/Desktop, orden de efectos y contratos existentes durante la migración.

Para este contexto se ignoran por completo los `[x]` del archivo. El dato relevante no es si sus tareas se terminaron, sino qué problema intentaba resolver: demasiada responsabilidad concentrada en la raíz del frontend y dificultad para identificar dueños claros de cada flujo.

---

# 9. Intento de planificación: `2.md` — robustez frente a bloqueos y fallos externos

`2.md` nació alrededor de un problema distinto.

El error analizado tenía como causa directa una incompatibilidad de stream en JavaScript: se estaba entregando un `fs.ReadStream` donde `@mtcute/web` esperaba otro contrato.

A partir de ese incidente, el documento planteó una visión de robustez centrada en los límites entre Desktop, Rust, helpers, Cloud y el transporte externo.

Los temas principales del documento fueron:

### Contratos entre librerías

La idea era evitar que el resto de la aplicación dependiera directamente de detalles incompatibles de APIs externas, usando límites/adaptadores explícitos.

### Operaciones externas con final definido

El documento consideraba importantes timeout, cancelación, cleanup, información de etapa y retry solo cuando fuera seguro.

### Estados terminales

Las operaciones de upload debían poder terminar como completadas, fallidas o canceladas, evitando quedarse eternamente en un estado intermedio como `uploading`.

### Pruebas con interfaces reales

El documento señalaba que ciertos mocks no habrían detectado el problema del stream. Por ello daba importancia a pruebas con MP3 real pequeño, helper real, stdin/stdout real, transporte controlado, cierre durante upload, respuestas tardías y datos inválidos.

### Watchdog de operaciones

Aparecía la idea de registrar operación, sesión, PID, etapa, progreso, bytes y deadline para detectar operaciones que dejan de avanzar.

### Logs correlacionados

Se proponía mantener identificadores comunes desde la acción del usuario hasta las distintas etapas del backend/transporte.

### Procesos hijos

El documento prestaba especial atención a cancelación, deadlines, cierre de stdin, kill/reap y helpers huérfanos.

### Fuente y bundle generado

Se señalaba el riesgo de que `transport-helper.source.mjs` y `transport-helper.cjs` dejaran de estar sincronizados.

### Gates antes de integrar

El documento reunía format/lint, typecheck, unit tests, integration tests, Cargo, regresiones Direct, verificación de bundle y `git diff --check` como ejemplos de comprobaciones.

### Dependencias

Se advertía especialmente sobre cambios que afectan streams, abort/cancelación, uploads/downloads, Tauri/WebView, serialización Rust/JavaScript y procesos Node.

### Fallos recuperables

Una operación fallida no debía necesariamente congelar toda la cola ni producir duplicados en storage/índice.

### Revisión de modos de fallo

El documento preguntaba qué ocurre cuando una operación nunca responde, un proceso muere, la app se cierra, internet cae entre upload y commit, una operación se reintenta o un mutex no se libera.

El problema que este plan intentaba resolver no era principalmente tamaño de archivos ni lanzamiento comercial. Era evitar que un fallo local pudiera congelar la aplicación, dejar operaciones vivas o producir estados difíciles de diagnosticar.

---

# 10. Intento de planificación: `3.md` — `commands.rs` como concentración de responsabilidades

`3.md` analiza otro aspecto del mismo incidente.

El documento aclara que el tamaño de `commands.rs` no fue la causa directa del stream incompatible. Sin embargo, describe un archivo de aproximadamente 14.000 líneas que reunía muchas responsabilidades:

- proceso helper;
- stdin/stdout;
- timeouts;
- mutex global;
- sesiones Direct;
- operaciones Cloud;
- heartbeats;
- cierre de la aplicación;
- numerosos comandos Tauri no relacionados.

El problema identificado no era “muchas líneas” por sí solo, sino la concentración de recursos compartidos y lifecycle en un mismo lugar.

Según ese análisis, esta concentración podía aumentar:

- el radio de impacto de los cambios;
- la distancia entre funciones relacionadas;
- la posibilidad de mantener un mutex durante una operación lenta;
- la dificultad de revisar cleanup y rutas de error;
- el acoplamiento de tests;
- los conflictos al modificar el archivo.

El documento imaginaba una separación entre comandos generales, transporte Direct y media, con módulos específicos para runtime, helper process, protocolo, sesión, operaciones y heartbeat.

También dejaba explícito que no veía conveniente dividir las aproximadamente 14.000 líneas en una sola modificación. Su secuencia conceptual era congelar comportamiento con pruebas, extraer un subsistema sin cambiar lógica, comprobar el movimiento y después mejorar lifecycle/mutexes/estados en cambios más pequeños.

Este archivo representa, por tanto, el intento de entender cuánto de la dificultad para corregir errores proviene de la estructura interna y no únicamente del bug visible.

---

# 11. Intento de planificación: `!!!PLAN.zip` — plan maestro de lanzamiento

`!!!PLAN.zip` representa el intento de planificación más amplio.

A diferencia de `1.md`, `2.md` y `3.md`, no se concentra en una sola zona técnica. Intenta cubrir desde arquitectura, seguridad y datos hasta Web, UX, pagos, Desktop, betas, release y operación post-lanzamiento.

El ZIP contiene, entre otros:

- `Plan Maestro.md`;
- una copia anterior extensa del Plan Maestro;
- `00 - Contexto global y criterios.md`;
- Fases 0 a 7;
- `Gates - Publicación y contingencias.md`;
- `Registro de avances.md`;
- un documento específico de una tarea Direct/delete.

Sus fechas, estados y checkboxes son históricos y no se consideran aquí una fotografía autoritativa del repositorio actual.

## 11.1 Imagen de producto que aparece en ese plan

El contexto global del plan describía una base de producto que ya incluía, en diferentes grados:

- biblioteca;
- importación y Review;
- edición;
- reproducción;
- Trash;
- sincronización Cloud;
- modo offline Desktop;
- YouTube;
- updater basado en Tauri;
- pruebas que ya detectaban ciertas regresiones.

Al mismo tiempo, el plan histórico consideraba que el lanzamiento todavía estaba bloqueado por temas de seguridad, sesión Web, persistencia, deploy/restore, legal, firma/notarización y divergencias Web/Desktop.

Esto era una evaluación del momento en que ese plan fue escrito, no una afirmación sobre el estado actual.

## 11.2 Fase 0 — Contención e integración

El objetivo histórico era eliminar ambigüedad, contener exposición y crear una única línea de release.

Incluía:

- congelar evidencia;
- cambiar una fecha pública por checkpoint interno;
- cerrar decisiones de negocio;
- reservar dependencias externas;
- contención de seguridad;
- integración de ramas;
- pruebas de contrato de plataforma;
- CI obligatorio;
- supply chain;
- límites de confianza;
- arquitectura de datos.

## 11.3 Fase 1 — Seguridad, cuentas y datos durables

El objetivo era alcanzar un alpha interno restaurable con P0 de confianza cerrados.

Incluía:

- autorización tenant;
- abuse controls;
- mediación/capabilities;
- aislamiento;
- sesión Web;
- lifecycle de cuenta;
- PostgreSQL y migración;
- cutover;
- backup/restore;
- decisión de alpha.

## 11.4 Fase 2 — Web y UX

El objetivo era conseguir flujos Web completos y una paridad funcional considerada honesta.

Incluía:

- foundations de diseño;
- autenticación;
- bootstrap/load;
- biblioteca;
- persistencia Web;
- Review;
- streaming y memoria;
- player/queue;
- Settings;
- accesibilidad;
- YouTube Web sin depender de Tauri.

Dentro de YouTube Web, el plan separaba contrato/capabilities, adapter Desktop, backend para Web, adapter Web puro, jobs/uploads, UI compartida y tests.

## 11.5 Fase 3 — Producción, pagos y operación

El objetivo histórico era convertir BeatGaler en un servicio operable, cobrable y restaurable.

Incluía:

- staging y producción reproducibles;
- pipeline de promoción;
- Stripe Checkout;
- webhooks;
- entitlements;
- portal/reconciliación;
- identidad pública;
- legal;
- soporte;
- observabilidad;
- capacidad y recovery.

Este plan coincide con el objetivo actual en un punto importante: pagos y planes formaban parte del concepto de V1, no únicamente de una mejora posterior.

## 11.6 Fase 4 — Desktop y release chain

El objetivo era producir artefactos Desktop confiables desde un SHA único.

Incluía:

- manifest/identidad de release;
- compatibilidad/migración;
- firma Windows;
- pruebas en Windows limpio;
- Developer ID para macOS;
- notarización/pruebas físicas;
- updater;
- rollback;
- matriz cross-platform;
- design freeze.

Este alcance histórico era más estricto que la posición actual, donde Desktop podría posponerse como plataforma de lanzamiento siempre que eso no provoque una separación arquitectónica dañina entre Web y Desktop.

## 11.7 Fase 5 — Betas y RC

El objetivo era validar usuarios reales, fallos y operación antes de congelar un release candidate.

Incluía:

- beta guiada;
- observación;
- triage;
- regresión;
- carga;
- fallos deliberados;
- beta no guiada;
- usabilidad real;
- cierre de issues;
- RC inmutable;
- gate formal.

## 11.8 Fase 6 — Lanzamiento

El objetivo era promover el RC sin cambiarlo, observar y abrir gradualmente.

Incluía:

- transacción real controlada;
- disaster rehearsal;
- soft launch;
- observación;
- soak;
- revisión de cohort;
- go/no-go;
- rollout público;
- operación durante las primeras horas.

## 11.9 Fase 7 — Estabilización

El objetivo era proteger datos y dinero después del lanzamiento y convertir feedback en trabajo posterior.

Incluía:

- triage;
- conciliación y restore;
- análisis de capacidad/rendimiento;
- síntesis de UX/support;
- patch candidate;
- postmortem y roadmap siguiente.

## 11.10 Gates históricos de publicación

El archivo de gates agrupaba condiciones relacionadas con:

- fuente y automatización;
- seguridad;
- Web;
- datos y cuentas;
- pagos y planes;
- Windows;
- macOS;
- operación/capacidad/beta;
- identidad/legal.

También contenía métricas, RACI, registro de riesgos y contingencias para casos como:

- fallo de seguridad;
- Stripe no listo;
- firma Desktop no lista;
- problemas Safari/iPhone;
- capacidad insuficiente del transporte;
- YouTube Web incompleto;
- aparición de un P0 después del soft launch.

El “estado final esperado” del plan histórico era considerablemente amplio: Web pública, YouTube Web/Desktop, Windows y macOS firmados, datos migrados/restaurables, cuentas completas, pagos/quotas, legal, soporte, monitoreo, capacidad demostrada, betas, soft launch y rollback.

Ese alcance ayuda a explicar por qué el proyecto podía sentirse como una lista casi infinita incluso cuando muchas capacidades del producto ya funcionaban.

---

# 12. Cómo se relacionan los cuatro intentos de planificación

Los cuatro materiales no son versiones simples del mismo roadmap.

Representan cuatro problemas diferentes que fueron apareciendo durante el desarrollo.

### `1.md`

Problema dominante: `App.tsx` y la estructura del frontend concentran demasiado y dificultan comprender responsabilidades.

### `2.md`

Problema dominante: una operación externa puede fallar o bloquearse de formas difíciles de contener y diagnosticar.

### `3.md`

Problema dominante: `commands.rs` concentra lifecycle, recursos compartidos y transporte, ampliando el impacto de fallos pequeños.

### `!!!PLAN.zip`

Problema dominante: convertir todo BeatGaler en un producto lanzable, seguro, operable, cobrable, cross-platform y validado con usuarios reales.

Por eso los planes pueden parecer acumulativos aunque en realidad nacieron para resolver preocupaciones distintas.

---

# 13. Tensiones y contradicciones que siguen abiertas

Estas tensiones forman parte del contexto y todavía no tienen una resolución definitiva.

## 13.1 “Todo debe funcionar sin errores” frente a una definición operativa de terminado

La definición intuitiva actual usa “sin errores”, pero todavía no existe un umbral concreto que determine cuándo los errores restantes son suficientemente menores como para permitir lanzamiento.

## 13.2 Limpiar arquitectura frente a dejar de refactorizar

Existe el deseo de tener todo el código limpio, fácil de leer y fácil de reparar antes de seguir.

Al mismo tiempo, meses de trabajo alrededor de estructura, migraciones y bugs han contribuido a la sensación de que el proyecto no termina.

## 13.3 Feature freeze frente a trabajo estructural profundo

No se desean nuevas features y el proyecto lleva meses conceptualmente congelado en funcionalidad.

Sin embargo, durante ese mismo periodo se han realizado o planeado migraciones grandes, separación de módulos, hardening, backend, PostgreSQL, Direct y otras modificaciones profundas.

Por tanto, “feature freeze” no ha significado “code freeze”.

## 13.4 Desktop puede esperar frente a Web/Desktop no deben separarse

Desktop podría no ser obligatorio para el primer lanzamiento.

Sin embargo, no se quiere avanzar Web de forma que Desktop quede arquitectónicamente atrás o empiece a fallar por razones completamente diferentes.

## 13.5 Diferencias legítimas de plataforma frente a divergencia accidental

Web necesariamente carece de ciertas capacidades nativas de Desktop.

La duda es dónde termina una diferencia legítima de plataforma y dónde comienza una duplicación/divergencia que aumenta bugs y mantenimiento.

## 13.6 Plan maestro exhaustivo frente a necesidad de sentir avance

El plan de lanzamiento histórico intentó cerrar seguridad, UX, billing, legal, firma, operación, betas y muchas contingencias antes de publicar.

La experiencia actual es que una lista demasiado amplia hace difícil percibir un final.

## 13.7 YouTube deseado frente a foco actual

YouTube se desea en el release si sigue estable, pero no es una prioridad de trabajo inmediata.

## 13.8 Reiniciar desde cero frente a conservar una base que ya contiene mucho trabajo

La idea de reescribir desde cero ha aparecido por frustración con la estructura y los ciclos de bugs.

No existe una decisión tomada y los materiales históricos muestran una base con numerosas capacidades ya implementadas o parcialmente implementadas.

---

# 14. Qué significa “estado” dentro de la preocupación actual

La frase “mantener estado” tiene alta prioridad, pero puede abarcar varias capas distintas que aparecen en los planes históricos:

- biblioteca en memoria;
- versión más reciente de beats;
- metadata;
- orden y selección;
- estado de playback;
- cachés;
- disponibilidad offline;
- uploads interrumpidos;
- jobs/operaciones activas;
- Trash pendiente;
- sesión de usuario;
- conexión/reconexión;
- autoridad Cloud;
- persistencia PostgreSQL;
- índice autoritativo de archivos/beats.

No se ha reducido todavía “mantener estado” a una lista cerrada de invariantes o escenarios que definan éxito.

---

# 15. Qué significa “varias personas al mismo tiempo” dentro del contexto histórico

El objetivo actual incluye multiusuario concurrente.

Los planes anteriores trabajaron conceptos como:

- separación entre usuarios/vaults;
- autorización tenant;
- sesiones;
- pool de transportes;
- admission control;
- fallback compartido;
- waitlist;
- capacidad;
- aislamiento de datos;
- recovery;
- quotas/entitlements.

En algunos registros históricos existen incluso cifras concretas de bots, leases y supuestos de actividad simultánea. Esas cifras fueron parte de experimentos y gates de ese plan; la conversación actual solo fija la necesidad general de que múltiples personas puedan usar el servicio simultáneamente, sin adoptar todavía un objetivo numérico definitivo.

---

# 16. Información histórica sobre seguridad y datos del plan maestro

El plan maestro fue creado en un momento en que la auditoría consideraba importantes, entre otros, los siguientes riesgos o áreas:

- credenciales de infraestructura que podían llegar al cliente;
- rutas legacy antes de autenticación;
- sesión Web reutilizable;
- persistencia basada en JSON;
- ausencia de restore/deploy reproducibles;
- separación y autorización entre usuarios;
- temporary auth para transporte;
- capacidad del pool;
- cleanup físico de assets frente a autoridad del índice;
- PostgreSQL y migración reversible.

Los registros dentro del ZIP contienen trabajo posterior que afirmaba haber corregido o probado parte de esos puntos.

Como los estados del ZIP no se consideran autoridad actual, este documento no afirma cuáles siguen abiertos hoy. Solo conserva que estos fueron problemas reales o percibidos suficientemente importantes como para dominar etapas anteriores del desarrollo.

---

# 17. Información histórica sobre pruebas y validación

A través de los distintos documentos aparece repetidamente la necesidad de pruebas, pero con objetivos diferentes.

`1.md` usa pruebas principalmente para conservar comportamiento durante la extracción de responsabilidades de `App.tsx`.

`2.md` enfatiza pruebas de integración y fallos reales que mocks simples no capturan: streams, helper, stdin/stdout, timeouts, cierre y transporte tardío.

`3.md` relaciona pruebas con la posibilidad de mover subsistemas grandes sin cambiar comportamiento.

`!!!PLAN.zip` convierte las pruebas en gates de integración, seguridad, plataforma, release, beta y operación.

Durante la conversación surgió además la idea de “regresiones principales”, entendida simplemente como volver a comprobar los flujos importantes que ya funcionaban para saber si un arreglo rompió otra cosa.

La duda actual no es si las pruebas son valiosas. La duda es qué conjunto de pruebas y evidencias es suficiente para generar confianza sin convertir cada cambio en una validación interminable de todo el sistema.

---

# 18. Estado emocional/práctico del trabajo

La dificultad actual también es de organización mental.

Se desea poder mirar el proyecto y saber claramente:

- qué importa ahora;
- qué puede esperar;
- qué significa haber terminado una etapa;
- qué significa haber terminado V1;
- cuándo dejar de tocar una parte que ya funciona;
- cómo saber que un arreglo no dañó otra plataforma o flujo.

La cantidad de planes, subplanes, gates, migraciones y registros acumulados ha aumentado el contexto necesario para decidir una tarea pequeña.

La preocupación por arquitectura limpia proviene en parte del deseo de reducir ese costo mental: que el código muestre con claridad dónde vive cada responsabilidad y que reparar una cosa no requiera comprender toda la aplicación.

Al mismo tiempo, existe cansancio con convertir cada problema en otra gran fase de arquitectura.

---

# 19. Preguntas todavía no resueltas

Estas preguntas aparecen directa o indirectamente en la conversación y los planes, sin una respuesta definitiva actual.

1. ¿Cuál es la definición concreta y comprobable de “BeatGaler V1 está terminado”?
2. ¿Qué nivel de bugs/regresiones restantes es compatible con considerarlo listo?
3. ¿Qué significa exactamente “varias personas” en términos de concurrencia/capacidad?
4. ¿Qué invariantes forman parte de “mantener estado” y cuáles son secundarias?
5. ¿Cuánto de la estructura actual debe reorganizarse antes de continuar estabilizando flujos?
6. ¿Cuáles archivos o subsistemas actuales siguen siendo realmente monolíticos después de las migraciones ya realizadas?
7. ¿Hasta qué punto Web y Desktop comparten hoy comportamiento y hasta qué punto se han separado?
8. ¿Qué diferencias Web/Desktop son intencionales y cuáles son deuda accidental?
9. Si Desktop se pospone para el lanzamiento, ¿qué nivel de compatibilidad estructural debe conservarse durante el trabajo Web?
10. ¿Cuál es el conjunto mínimo de regresiones que aporta confianza después de cada cambio?
11. ¿Qué pruebas necesitan ser reales/E2E y cuáles pueden ser unitarias o de integración controlada?
12. ¿Cuáles de los riesgos históricos de seguridad/datos/operación siguen existiendo realmente en el repositorio actual?
13. ¿Qué elementos del enorme plan maestro siguen siendo requisitos reales de V1 y cuáles respondían a un alcance excesivamente amplio?
14. ¿YouTube continúa suficientemente estable para incluirse sin reabrir una etapa grande de desarrollo?
15. ¿Hasta dónde llegan hoy pagos, planes y quotas, que sí forman parte del alcance actual de V1?
16. ¿Reescribir desde cero reduciría complejidad real o simplemente descartaría una base con mucho comportamiento ya resuelto?
17. ¿Qué criterio evita que “limpiar el código antes de lanzar” se convierta en otro trabajo sin final?
18. ¿Qué criterio evita el caso contrario: lanzar sobre una estructura tan difícil de mantener que cada bug futuro genere nuevas regresiones?

---

# 20. Resultado que se busca obtener del próximo razonamiento

El problema a resolver ya no es simplemente “qué tarea sigue” dentro de uno de los planes anteriores.

Se busca determinar, a partir del repositorio actual y de este historial, cuál debería ser el objetivo real de la siguiente etapa de BeatGaler y qué estructura de roadmap permite llegar a V1 sin repetir el ciclo de planificación y reparación indefinida.

Ese razonamiento necesita distinguir al menos cuatro dimensiones que en los planes anteriores quedaron mezcladas:

- funcionamiento real del producto;
- prevención de regresiones;
- mantenibilidad/arquitectura;
- requisitos de lanzamiento comercial y multiusuario.

El punto de partida no es asumir que algún plan anterior es correcto ni asumir que sus tareas están terminadas. El punto de partida es que BeatGaler ya ha pasado por varios intentos de estabilización y organización, y aun así el desarrollador no tiene todavía una sensación confiable de cierre ni una definición simple de qué falta para V1.

---

## Fuentes históricas incluidas

### `1.md`

Roadmap de migración de `App.tsx` y separación del frontend por responsabilidades.

### `2.md`

Análisis de robustez después de un fallo de stream/helper, con foco en contratos, timeout, estados terminales, procesos, tests y recovery.

### `3.md`

Análisis de `commands.rs`, sus aproximadamente 14.000 líneas y la concentración de lifecycle/recursos compartidos.

### `!!!PLAN.zip`

Plan maestro previo con contexto global, fases de contención, seguridad/datos, Web/UX, producción/pagos, Desktop, beta/RC, lanzamiento, estabilización, gates, contingencias y registro histórico.

### Conversación actual

Aporta la percepción actual del problema: desarrollo infinito, miedo a regresiones, feature freeze prolongado, duda sobre limpiar todo antes de seguir, posibilidad de reiniciar desde cero, prioridad extrema de startup/playback y estado, necesidad de multiusuario y billing en V1, Shared Folders/Public Profile para V2, YouTube al final y preocupación por la divergencia Web/Desktop.
