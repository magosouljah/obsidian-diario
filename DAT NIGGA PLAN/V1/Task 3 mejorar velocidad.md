# Task 3 mejorar velocidad

**Mi decisión: primero corregir cómo compartimos y conservamos el trabajo; después experimentar con recuperación de las peticiones lentas. No empezaría reduciendo timeouts.**

Revisé el código actual y reanalicé las trazas. Dejé la comparación detallada en este [canvas de decisión](C:/Users/GTA7/.cursor/projects/e-777-app-beatvault/canvases/phase2-task3-playback-decision.canvas.tsx), para comparar las alternativas junto al chat. No modifiqué la aplicación ni ejecuté nuevas corridas reales.

La evidencia añade tres puntos importantes:

- **Hay duplicación demostrada de metadatos durante startup.** Dos rutas solicitan los mismos diez mensajes con apenas 11,4 ms de separación. La caché guarda resultados terminados, pero no comparte resoluciones pendientes.
- **Adoptar un warm no necesariamente acelera su petición.** Play puede heredar la espera de `getMessages` de un batch. Promoverlo cambia su prioridad posterior; no acelera un RPC ya enviado.
- **Los ~9 s no corresponden simplemente a un timeout fijo.** La versión instalada de mtcute ya programa consultas de estado a 1,5 s. Falta separar espera hasta consulta, respuesta de estado y reenvío antes de decidir qué temporizador tendría sentido modificar.

Confirmé también las 185 respuestas con entrada→decode de hasta 11,9 ms. Sólo 70 tienen además envío exacto al WebSocket correlacionado; el caso de 6,67 s no lo tiene. La conclusión sobre el procesamiento de entrada se sostiene, pero no convierte todo el intervalo anterior en “tiempo de Telegram”.

Mi orden propuesto sería:

1. **Unificar resolución, descarga y adopción.**  
    Un registro compartido en el worker debe representar cada resolución de mensaje y cada rango de bytes. Startup, warm y Play se suscriben a ese trabajo; el clic aumenta su prioridad. Cancelar un consumidor no cancela a los demás, y una respuesta antigua no puede afectar al intent actual.
    
    Incluiría aquí conservar el inicio útil de reproducciones parciales y evitar reinstalar el observador en cada Play, comportamiento que sigue presente. Esta intervención elimina desperdicio demostrado, aunque **no elimina la demora de un RPC remoto lento**.
    
2. **Cambiar la política de prefetch mediante una comparación controlada.**  
    Separaría precargar descriptores de descargar audio. Compararía los actuales 14 candidatos/7 lanes con pocos candidatos de alta intención, 1–2 warms y ausencia de audio especulativo durante INDEX.
    
    La prioridad debe actuar principalmente al admitir trabajo y entre chunks, evitando ciclos de abortar y reiniciar. INDEX necesita conservar progreso incluso con clics repetidos. Reducir warms podría empeorar los aciertos de caché: hay que medir esa pérdida frente al ahorro de tráfico y latencia.
    
    También probaría ampliar **sólo los prefijos que no contienen audio útil**, con un límite. Descargar más bytes para todos no está justificado por el caso 101.
    
3. **Experimentar con la cola fría residual, distinguiendo hedge de recuperación.**  
    Un **hedge** mantiene el original y lanza una segunda lectura: conserva la oportunidad de que el primero termine pronto. Lo limitaría al mensaje o rango crítico del Play vigente, con un único intento adicional y presupuesto explícito.
    
    Su problema es que ambas llamadas pueden compartir socket, congestión y fallo. Otro socket tampoco garantiza independencia y añade complejidad. El reenvío rápido después de nueve segundos no demuestra que habría funcionado igual al segundo uno.
    
    La **recuperación de conexión** tiene sentido ante señales concordantes de falta de respuesta en esa conexión; resulta más invasiva porque afecta otros RPC, incluido INDEX. No la activaría únicamente por una petición lenta.
    
    `state 2` sí informa que ese mensaje no fue recibido según el estado remoto, pero no identifica dónde se perdió. mtcute ya coordina su reenvío; añadir otro mecanismo independiente podría multiplicar intentos. [Semántica oficial](https://core.telegram.org/mtproto/service_messages_about_messages).
    
4. **Persistir prefijos útiles para reaperturas.**  
    Tiene una ventaja clara: guardar bytes ya recibidos no añade tráfico MTProto. Empezaría con IndexedDB, identidad/versionado del archivo, cuota y borrado por cuenta. El hit debe poder servir audio sin exigir otro `getMessages`; las referencias remotas caducadas necesitan un refresco separado. [Referencias de archivo](https://core.telegram.org/api/file-references).
    
    Lo adelantaría si predominan las reaperturas. No lo presentaría como solución del primer acceso ausente ni como garantía de continuidad.
    
5. **Considerar audio de preview replicado sólo si el miss frío sigue incumpliendo el objetivo.**  
    Una réplica preparada previamente puede quitar MTProto del primer playback. Un proxy que consulta Telegram en cada miss sólo desplaza la espera. Es una decisión mayor de almacenamiento, sincronización y operación.
    

Con cinco cuentas, siete lanes por worker pueden sumar **35 lanes locales**; un hedge por cuenta puede añadir cinco peticiones simultáneas. Los límites deben contar también reintentos y recuperaciones, sin asumir que un limitador local coordina perfiles separados.

**Elegiría ahora el paso 1 como siguiente implementación y el paso 2 como siguiente experimento.** Para aprobar cualquier mejora mediría click→progreso sostenido, stalls iniciales, p95 por cuenta, INDEX y tráfico total, incluyendo cancelaciones e intentos incompletos. Podemos corregir nuestra arquitectura sin resolver la causa física externa; decidir si hedge o reconnect ayuda exige evidencia experimental adicional.