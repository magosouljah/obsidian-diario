Yo lo dividiría en **5 fases**, y no pasaríamos a la siguiente sin evidencia.

### Fase 1 — Entender exactamente los 3 arranques

No tocar comportamiento.

Añadir/ajustar tracing para saber, en los tres escenarios:

```
APP_START
CACHE_AVAILABLE
AUTH_RESTORE_BEGIN
AUTH_RESTORE_DONE

DIRECT_CODE_IMPORT_BEGIN
DIRECT_CODE_IMPORT_DONE

DIRECT_PREPARE_BEGIN
session/start #1
crypto/wasm ready
Telegram authorization
session/start #2
bind complete
DIRECT_PREPARE_DONE

WORKER_CREATE
WORKER_MODULE_READY
WORKER_INITIALIZE_BEGIN
WORKER_INITIALIZE_DONE

ACTIVATE_BEGIN
bot lease reused? sí/no
invite/promote ejecutado? sí/no
membership confirmed
ACTIVATE_DONE

VERIFY_BEGIN
VERIFY_DONE
DIRECT_READY

CARDS_VISIBLE
PLAY_CLICK
FIRST_CHUNK
PLAYING
```

Además registraríamos cosas como:

```
startup_type = cold | warm | reload

library_cache = hit/miss
auth_session = restored/new
server_lease = new/reused
lease_state = ASSIGNING/ACTIVE
```

Esto nos quitaría muchas suposiciones.

---

### Fase 2 — Hacer una matriz de rendimiento

Probar varias veces cada situación.

Algo así:

|Situación|Cards|Direct READY|Click → Playing|
|---|---|---|---|
|1. Cold|?|?|?|
|2. Warm/cache|?|?|?|
|3. Reload|?|?|?|

Y dentro de `Direct READY` separar:

```
import
prepare
worker
activate
verify
```

Entonces sabremos cuál optimización tiene realmente valor.

---

### Fase 3 — Primera optimización segura

Esta es la que **ya parece correcta arquitectónicamente**, aunque igualmente la mediríamos primero.

Para el caso 2:

```
restauración de sesión termina
              ↓
      ┌───────┴────────┐
      ↓                ↓
mostrar cache      iniciar Direct
      ↓                ↓
cards visibles       READY
```

No:

```
restaurar
↓
cargar biblioteca
↓
mostrar app
↓
esperar window.load
↓
250 ms
↓
Direct
```

También precargaríamos el **código/Worker** antes, porque cargar código no significa todavía abrir una sesión de Telegram.

Eso conserva:

```
prepare
↓
initialize
↓
activate
↓
verify
```

sin romper el contrato actual.

---

### Fase 4 — Optimizar el caso reload/lease ACTIVE

Solo después de medir.

Ahora mismo parece que el backend puede recordar:

```
mismo navegador
mismo vault
mismo bot
lease todavía ACTIVE
```

pero aun así repetimos bastante trabajo.

Aquí investigaría si podemos hacer:

```
lease ACTIVE encontrada
↓
inicializar nuevo Worker
↓
confirmar que ese bot sigue siendo miembro válido
↓
READY
```

en lugar de repetir siempre:

```
invite
promote
confirm
```

Pero esto **no se debe eliminar a ciegas**, porque puede existir una dependencia MTProto importante con ese evento.

Primero trace + prueba.

---

### Fase 5 — Solo si todavía hace falta: persistencia IndexedDB

Aquí entraríamos en lo que mencionas.

Podríamos estudiar guardar temporalmente:

```
temp auth key
MTProto session id
DC
salt
counters / sesión necesaria
expiry
lease generation
```

en IndexedDB.

Entonces un reload podría intentar:

```
IndexedDB session
+
server ACTIVE lease
↓
resume
↓
verify
↓
READY
```

y si cualquier cosa no coincide:

```
fallback seguro
↓
cold Direct initialization
```

Pero yo pondría esto **al final**, porque añade bastante complejidad y superficie de seguridad para arreglar principalmente el escenario 3.

---

## Prioridades

Yo las dejaría así:

```
P0 — Instrumentar correctamente los 3 escenarios

P1 — Optimizar el caso 2:
     cache + auth restaurada
     Direct empieza inmediatamente y en paralelo

P2 — Preload del Worker/código para esconder tiempo muerto

P3 — Investigar por qué ACTIVE lease repite ~1.1 s de activate

P4 — Mejorar cold start donde sea posible

P5 — IndexedDB/resume MTProto únicamente si sigue haciendo falta
```

Y definiría el objetivo principal de #97 como:

> **En una apertura normal con cache y sesión válida, las cards aparecen inmediatamente desde cache y Direct se prepara en paralelo, de modo que el primer Play normalmente ocurra con Direct READY y `click → playing < 1.5 s`.**

Ese me parece un objetivo mucho más correcto que “hacer que F5 conecte instantáneamente”.