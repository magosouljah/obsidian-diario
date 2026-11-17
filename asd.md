# BeatGaler — Registro de intención, diferencias y decisiones

**Fecha:** 17 de noviembre de 2026  
**Proyecto:** BeatGaler Web — migración del INDEX de Telegram a PostgreSQL  
**Propósito:** conservar las instrucciones y decisiones del propietario para mostrarlas a otra IA o desarrollador. **No es un plan de implementación ni autoriza cambios.**

## 1. Intención original del propietario

> **Solo quería sustituir el INDEX de Telegram por PostgreSQL como autoridad del catálogo. No quería rehacer los sistemas que ya funcionaban, especialmente el transporte directo de Telegram, el reproductor, el streaming y las cachés.**

El cambio de autoridad del catálogo **no autoriza por sí mismo** cambiar arquitectura de transporte, experiencia del reproductor, diseño, archivos o comportamiento de la biblioteca. Se deben identificar las diferencias, explicar sus consecuencias y **consultar al propietario** cuáles recuperar, mantener o mejorar. No repetir entrevistas ni decisiones que ya quedaron expresamente resueltas.

La regla es **recuperar lo necesario con la menor cantidad de cambios**, sin deshacer las mejoras útiles de PostgreSQL. La fase actual es de **identificación de cambios**, no de planificación o implementación.

## 2. Diferencias conocidas: antes y después

| Área | Antes: INDEX / Web legacy | Después: catálogo PostgreSQL | Observación / decisión |
|---|---|---|---|
| Autoridad de metadatos | INDEX almacenado en Telegram | PostgreSQL | **Cambio buscado: conservar PostgreSQL.** Telegram sigue almacenando medios. |
| Transporte de audio | El navegador se conectaba directamente a Telegram con Worker MTProto | El servidor BeatGaler descarga desde Telegram para el navegador | **Cambio no buscado: el propietario eligió recuperar transporte directo (opción B).** |
| Reproducción | Streaming progresivo mediante MediaSource; empezaba antes de bajar todo | Descarga Blob completo y verifica SHA-256 antes de sonar | Recuperar streaming, adaptado a referencias SQL; no restaurar INDEX. |
| Prefetch por visibilidad | Prefijos de audio de tarjetas visibles/cercanas | No está conectado | Evaluar si sigue siendo útil; **no usar hover**. |
| Precarga al iniciar | Coordinador preparaba referencias iniciales desde biblioteca cacheada | No existe equivalente en catálogo | No confundir con streaming. Su recuperación **no está decidida**. |
| Caché de audio | Hasta 100 MB RAM por sesión y prefijos de 64 KiB | Blob temporal; liberado puede volver a descargarse | Recuperar respuesta rápida, evaluar nueva estrategia. |
| Siguiente canción | Mecanismos antiguos de prefetch por posición | Se resuelve ID, no bytes | Revisar si aporta algo con nueva caché; sin duplicar trabajo. |
| Portadas | Miniaturas ≤250 KB en caché persistente Cache API | Originales con LRU en RAM de 32 MiB | **Preferencia expresada:** cachear localmente todas las portadas, en calidad original, de forma persistente. |
| Portadas al recargar | Podían cargarse de almacenamiento local | Se solicitan nuevamente | Evitar solicitudes repetidas a Telegram mientras exista caché válida. |
| Inicio de biblioteca | Presentación cacheada en localStorage | Espera la primera consulta SQL | Diferencia detectada; **el propietario aún no ha elegido** si recuperar caché inicial. |
| Ajustes de caché | Controles conectados al sistema legacy | Muestran 0/100 MB, y Clear/límite no operan sobre la nueva caché | Corregir para que indiquen y controlen recursos reales. |
| Toolbar Liquid Glass | Motor de Design Studio | Mismo motor/shaders/preset | Se vio gris temporalmente, pero **ya volvió a ser transparente**. No modificar sin nueva evidencia. |
| Fondo del vidrio | Muestrea las portadas cargadas bajo la barra | Mismo principio, dependiente de carga de portadas | Posible dependencia, **no defecto visual actualmente confirmado**. |
| Búsqueda y filtros | Limitados al subconjunto materializado de la página legacy | Globales mediante SQL | **Mejora que no se solicita revertir.** |
| Navegación por biblioteca | Páginas legacy | Gallery continua virtualizada con caché acotada | **Mejora aprobada: conservar.** |

**Grado de evidencia:** cuadro consolidado de informes de inspección de código aportados en la conversación, no pruebas funcionales nuevas ejecutadas por este documento. No asumir que cada defecto apareció exclusivamente por la migración.

## 3. Decisiones e intenciones ya expresadas

### A. Transporte y reproducción

- **Decisión:** retornar a **lecturas y escrituras directas Navegador ↔ Telegram** (opción **B** elegida en la entrevista), conservando **PostgreSQL como autoridad del catálogo**. El usuario de BeatGaler **no debe iniciar sesión en Telegram**.
- Recuperar el streaming, aprovechando la implementación legacy donde sea compatible; reproducciones Web de BeatGaler son **MP3**, no WAV.
- El propietario acepta la exposición de la **clave temporal MTProto** que exige el transporte directo; **no** ha autorizado ignorar los posibles daños a archivos de terceros. La clave temporal inspeccionada (≤15 minutos, renovada por heartbeat) daba poderes del bot, incluso borrar o leer donde fuera miembro. En legacy, `bot_token`, `api_hash` y clave permanente permanecían del lado del servidor.
- **Situación pendiente:** resolver cómo limitar el riesgo entre usuarios con el **pool de 80 bots disponible**. El propietario descartó la viabilidad de imponer **un bot exclusivo para cada usuario**; expresó que los bots deben compartirse lo menos posible. **No se ha aprobado todavía una política exacta de asignación o aislamiento.**
- **Advertencia técnica:** que la interfaz solo muestre lecturas, o restringir en nuestro código las escrituras, no limita las capacidades reales de una clave MTProto expuesta. La protección de los archivos y el acceso entre usuarios necesitan comprobación específica.
- Se descubrió una posible carrera al cambiar rápidamente de canción: una solicitud anterior puede terminar tarde y sustituir la nueva. **Hipótesis de código pendiente de prueba.**

### B. Posible caché compartida de prefijos

- **Idea del propietario a evaluar, NO arquitectura definitiva:** archivo compartido en Telegram con los **primeros 128 KiB de cada MP3**, indexados por beat y versión. Se podría leer por rangos o descargar completo y persistir localmente.
- A 500 beats, solo los prefijos suman **62,5 MiB (≈65,5 MB)**, sin contar índice/cabeceras ni sobrecarga del empaquetado. A 320 kbps, 128 KiB son unos **3,3 segundos** aproximadamente.
- Objetivo: iniciar rápido **cualquier beat aleatorio, incluso nunca reproducido**; por eso una caché que solo aprende de reproducciones previas no satisface por sí sola la intención.
- Evaluar costo de regeneración, fragmentos desactualizados, acceso directo al audio original para beats nuevos/modificados, y empalme exacto de bytes. **No hay decisión** sobre frecuencia de actualización, descarga completa frente a rangos o elección final frente a otras estrategias.
- No se quiere prefetch por hover. Precarga de vecinos/visibilidad queda abierta solo si aporta valor real y no duplica la caché.

### C. Metadatos

- **Deseado:** Telegram conserva el audio sin metadatos añadidos por BeatGaler; PostgreSQL conserva los metadatos del beat. **Al descargar**, generar una copia MP3/WAV con los metadatos compatibles incrustados, sin cambiar el original almacenado en Telegram.
- **Defectos detectados en código:** el importador Web no interpreta estrellas `POPM` ni incorpora `rating` al plan de importación; las descargas del catálogo guardan el Blob crudo sin incrustar metadatos.
- Reutilizar donde corresponda el exportador ID3 legacy para título, BPM, Key, tags, estrellas y portada. Validar convenciones de estrellas `POPM` (hay diferencias entre Web y Rust) y limitaciones de metadatos WAV. **No inferir que cualquier lector de audio mostrará las estrellas de igual manera.**
- Importación de estrellas y exportación con metadata son requisitos del propietario, pero **no autorizan cambios en el audio de Telegram**.

### D. Portadas y ajustes

- **Preferencia del propietario:** mantener **todas las portadas originales** en caché persistente local. No optimizar para usuarios con poco almacenamiento sacrificando esa intención; tratar explícitamente fallos de cuota o evicción del navegador.
- Cachear por identidad de cuenta y versión del **archivo de portada**, invalidando cuando cambie esa portada y sin mezclar bibliotecas.
- El panel de Settings no debe mostrar métricas ficticias ni acciones sin efecto.
- La Toolbar se ve bien actualmente; **no tocar shaders/preset/fondo** por el episodio gris anterior.

## 4. Lo que NO está decidido

- Política exacta para compartir y asignar los 80 bots y cómo mitigar el acceso entre usuarios al restaurar MTProto directo.
- Si el archivo único de prefijos supera al streaming directo con caché local; si se descarga entero, por rangos o de manera híbrida; y cuándo se actualiza.
- Recuperar o no precarga inicial, prefetch por visibilidad, precarga del siguiente beat y caché inicial de metadatos.
- Detalles de compatibilidad de exportación WAV, mapeo de estrellas y metadatos según reproductor.

## 5. Instrucción para futuras IA / IDE

**No empieces un nuevo diseño ni un `/grill-me` general.** Primero compara la Web legacy con `src/features/library/catalog/` y el código asociado al transporte, reproducción, caché, importación y descargas; enumera **cambios no requeridos por sustituir INDEX por PostgreSQL**, separados de las mejoras deliberadas y de defectos sin fecha demostrada. Presenta diferencias concretas y consecuencias breves para que **el propietario decida** qué vuelve, qué se mantiene y qué se mejora.

**No implementar, desplegar, modificar producción, AWS o Telegram real ni realizar borrados por este registro.** Una decisión de dirección no es prueba de viabilidad ni autorización operativa. Preservar Landing, Gallery, Playbar y la arquitectura del catálogo PostgreSQL salvo cambio expresamente aprobado.

---

**Procedencia:** declaraciones y decisiones expresas del propietario en la conversación del 17-11-2026, más dos informes de inspección de código facilitados en ella. Los datos de implementación mencionados deben revalidarse contra el commit concreto antes de ejecutar cualquier cambio.
