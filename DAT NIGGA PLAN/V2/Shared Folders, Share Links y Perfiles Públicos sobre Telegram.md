

> Estado: propuesta conceptual / no oficial  
> Objetivo: permitir compartir, colaborar y publicar beats en BeatGaler sin romper la arquitectura actual de transferencia directa con Telegram.

---

## 1. Principio principal

BeatGaler utiliza Telegram como data plane para almacenar y servir archivos.

El flujo normal es:

```text
Usuario
  ↓
Bot temporal
  ↓
Vault de Telegram
```

Los archivos viajan directamente entre el usuario y Telegram.

No queremos convertir BeatGaler Cloud en un servidor por el que tengan que pasar todos los MP3, WAV, proyectos y demás archivos.

BeatGaler debe funcionar principalmente como:

```text
CONTROL PLANE
```

para:

```text
identidad
ownership
permisos
shares
folders
roles
leases
publicaciones
coordinación de bots
```

mientras Telegram continúa siendo:

```text
DATA PLANE
```

para:

```text
almacenamiento
transferencia
streaming
downloads
forward/copy de archivos
```

---

# PARTE I — OWNERSHIP

## 2. Todo beat tiene un dueño

Cada beat tiene siempre un único dueño canónico.

El dueño es la persona cuyo vault contiene la copia canónica del beat.

Ejemplo:

```text
Beat A
owner: Purple
vault: Vault Purple

Beat B
owner: Juan
vault: Vault Juan

Beat C
owner: Ana
vault: Vault Ana
```

La regla fundamental es:

> El ownership de un beat está determinado por su vault canónico.

Compartir un beat, publicarlo o permitir que otra persona lo edite no cambia automáticamente su dueño.

---

## 3. El vault siempre contiene la copia canónica

Ejemplo:

```text
Vault Purple
└── Beat A ← CANÓNICO
```

Puede haber copias temporales o públicas en otros chats de Telegram:

```text
Vault Purple
└── Beat A ← CANÓNICO

Share Room
└── Beat A ← COPIA TEMPORAL

Public Pool
└── Beat A ← COPIA PÚBLICA
```

Pero solo:

```text
Vault Purple
```

define dónde vive el beat original.

---

## 4. Ownership y permisos son cosas diferentes

### Ownership

Responde:

```text
¿De quién es este beat?
¿En qué vault vive?
```

### Permissions

Responde:

```text
¿Quién puede verlo?
¿Quién puede descargarlo?
¿Quién puede editarlo?
¿Quién puede administrarlo dentro de una carpeta?
```

Ejemplo:

```text
Beat A
owner: Purple

Juan:
edit = true
```

Juan puede editar Beat A sin convertirse en su dueño.

La regla es:

> Ownership determina pertenencia y ubicación canónica.  
> Permissions determinan qué acciones puede realizar otra persona.

---

# PARTE II — SHARED FOLDERS

## 5. Las carpetas son colecciones lógicas

Una carpeta compartida no tiene que existir físicamente dentro de Telegram.

Puede ser simplemente:

```text
Folder "Album"

Beat A
Beat B
Beat C
```

Internamente:

```text
Folder "Album"

Beat A → owner Purple → Vault Purple
Beat B → owner Juan   → Vault Juan
Beat C → owner Ana    → Vault Ana
```

Por tanto, una misma carpeta puede contener beats pertenecientes a diferentes personas.

---

## 6. Las carpetas no poseen los beats

La carpeta únicamente contiene referencias.

Ejemplo:

```text
Folder "Album"
│
├── Beat A → Vault Purple
├── Beat B → Vault Juan
└── Beat C → Vault Ana
```

La carpeta nunca se convierte en la ubicación canónica de los beats.

La regla es:

> La carpeta organiza y delega acceso. El ownership permanece en cada beat individual.

---

## 7. Una carpeta no necesita un único dueño

Para evitar confundir ownership de archivos con administración de espacios colaborativos, las carpetas utilizan roles.

Roles iniciales:

```text
Admin
Editor
Viewer
```

Ejemplo:

```text
Folder "Album"

Purple → Admin
Juan   → Admin
Ana    → Editor
Luis   → Viewer
```

---

## 8. Admin

Un Admin puede administrar la carpeta.

Por ejemplo:

```text
renombrar carpeta
invitar miembros
eliminar miembros
cambiar roles
agregar beats
quitar beats de la carpeta
crear share links
revocar share links
configurar permisos
```

Pero:

> Ser Admin de una carpeta no convierte al usuario en dueño de los beats contenidos en ella.

---

## 9. Editor

Un Editor puede modificar beats cuando las reglas de colaboración lo permitan.

Por ejemplo:

```text
Folder "Album"

editors_can_edit_beats = true
```

Entonces:

```text
Beat A
owner = Purple

Juan
role = Editor
```

Juan puede editar Beat A.

Pero después de la edición:

```text
owner = Purple
vault = Vault Purple
```

siguen siendo iguales.

Esto es:

```text
autoridad delegada
```

no transferencia de ownership.

---

## 10. Viewer

Un Viewer puede acceder al contenido según los permisos concedidos.

Por ejemplo:

```text
view = true
download = false
edit = false
```

---

# PARTE III — PERMISOS

## 11. Permisos de contenido

BeatGaler controla los permisos.

Telegram no es la autoridad de permisos de negocio.

Permisos básicos:

```text
view
download
edit
```

---

## 12. View

Permite:

```text
ver metadata
ver artwork
reproducir audio
```

---

## 13. Download

Permite descargar los formatos autorizados.

Ejemplo:

```text
download_mp3 = true
download_wav = false
download_project = false
```

Esto puede evolucionar a permisos separados por slot:

```text
MP3
WAV
Project
Samples
```

---

## 14. Edit

Permite modificar el beat dentro del contexto compartido.

Pero:

> Tener acceso al bot temporal de una Share Room nunca significa tener permiso real para modificar el vault original.

El commit siempre requiere validación de BeatGaler.

---

## 15. Herencia de permisos

Los beats pueden heredar permisos de la carpeta.

Ejemplo:

```text
Folder "Album"

Editors:
view = true
download = true
edit = true
```

Los beats dentro pueden heredar esos permisos automáticamente.

---

## 16. Excepciones por beat

Un beat puede bloquear o modificar la herencia.

Ejemplo:

```text
Folder:
Editors can edit = true

Beat A:
inherit = true

Beat B:
inherit = false
edit_only_owner = true
```

Inicialmente BeatGaler puede mantener esto simple y añadir excepciones únicamente cuando sean necesarias.

---

# PARTE IV — SHARE ROOMS

## 17. Problema de seguridad original

Si BeatGaler entrega al receptor el token de un bot que tiene acceso al vault privado:

```text
Receptor
   ↓
token del bot
   ↓
Vault privado
```

el receptor podría usar ese bot directamente contra Telegram.

Por eso:

> Nunca debemos entregar a un usuario externo las credenciales de un bot que tenga acceso al vault privado original.

---

## 18. Share Rooms temporales

Cuando alguien comparte un beat o carpeta, BeatGaler crea o reserva una zona temporal aislada dentro de Telegram:

```text
Share Room
```

Flujo:

```text
Vault privado
     ↓
forward / copy interno de Telegram
     ↓
Share Room
     ↓
Bot temporal
     ↓
Receptor
```

El receptor únicamente obtiene acceso a:

```text
Bot temporal
+
Share Room
```

Nunca al vault original.

---

## 19. Forward/copy interno

Telegram permite copiar o reenviar mensajes entre chats sin que BeatGaler tenga que:

```text
descargar
↓
procesar
↓
volver a subir
```

El flujo permanece dentro de Telegram:

```text
Vault
  ↓
Telegram
  ↓
Share Room
```

Esto conserva la ventaja principal de BeatGaler:

> Los archivos pesados no necesitan pasar por nuestros servidores.

---

## 20. Pool de Share Rooms

No necesitamos una Share Room permanente por cada carpeta.

Podemos mantener un pool:

```text
Share Room 01
Share Room 02
Share Room 03
...
```

Cuando alguien abre un share:

```text
1. BeatGaler reserva una Share Room libre.
2. Copia/reenvía los beats autorizados.
3. Introduce un bot temporal.
4. Entrega el lease al receptor.
5. El receptor usa Telegram directamente.
```

Al terminar:

```text
1. Expira el lease.
2. Se retira el bot temporal.
3. Se eliminan los mensajes.
4. Se limpia la room.
5. Vuelve al pool.
```

Por tanto necesitamos aproximadamente:

> una Share Room por share activo simultáneamente,

no una por cada share creado históricamente.

---

## 21. Carpetas con múltiples vaults

Una carpeta puede reunir beats provenientes de varios vaults.

Ejemplo:

```text
Vault Purple ─┐
              │
Vault Juan ───┼──→ Share Room
              │
Vault Ana ────┘
```

La Share Room funciona como una representación temporal de esa carpeta.

---

# PARTE V — EDICIONES

## 22. Editar no significa automáticamente hacer commit

Si un usuario modifica algo dentro de una Share Room:

```text
Usuario
  ↓
Share Room
```

eso todavía no significa:

```text
Vault original modificado
```

La Share Room funciona como staging.

---

## 23. Commit seguro al vault

Cuando existe una edición:

```text
Usuario
   ↓
Share Room
   ↓
Nueva versión
```

BeatGaler verifica:

```text
¿qué beat es?
¿quién es el owner?
¿cuál es el vault canónico?
¿el usuario tiene edit=true?
```

Si está autorizado:

```text
Bot interno confiable
   ↓
Vault original
```

El bot interno es diferente del bot temporal cuyo token vio el usuario.

---

## 24. Bot interno confiable

Este bot puede:

```text
leer vaults
escribir vaults
copiar contenido a Share Rooms
devolver cambios a vaults
actualizar mensajes
```

Sus credenciales:

```text
NUNCA
```

se entregan al receptor.

---

## 25. Ejemplo de edición cross-owner

```text
Folder "Album"

Beat A → Purple
Beat B → Juan
```

Juan edita Beat A:

```text
Juan
 ↓
Share Room
 ↓
BeatGaler verifica edit=true
 ↓
BeatGaler resuelve:
Beat A → owner Purple → Vault Purple
 ↓
Bot interno confiable
 ↓
Vault Purple
```

Purple continúa siendo owner.

---

# PARTE VI — LIFECYCLE DE CARPETAS Y BEATS

## 26. El owner retira su beat

Si Purple saca Beat A de una carpeta:

```text
Folder
- Beat A
```

Beat A desaparece de esa carpeta y de futuros Share Rooms asociados.

Pero:

```text
Vault Purple
└── Beat A
```

permanece intacto.

---

## 27. Un Admin elimina un beat ajeno de la carpeta

Puede quitar la referencia:

```text
Folder
- Beat A
```

pero no puede:

```text
delete Beat A from Vault Purple
```

salvo que exista algún permiso explícito completamente diferente para ello.

---

## 28. El owner abandona la carpeta

Por defecto:

> Los beats aportados por esa persona salen de la carpeta cuando abandona.

Podría existir una opción explícita para dejarlos compartidos, pero nunca debería asumirse automáticamente.

---

## 29. Un Editor abandona

Pierde:

```text
view
download
edit
```

según corresponda.

Las ediciones que ya fueron legítimamente committed permanecen.

---

## 30. Revocación de permisos

Si alguien pierde permiso mientras tiene una sesión activa:

```text
permiso revocado
↓
lease deja de renovarse / se invalida
↓
Share Room deja de estar disponible
```

Además:

> Todo commit debe volver a comprobar los permisos justo antes de escribir al vault.

Así evitamos:

```text
usuario tenía permiso
↓
usuario pierde permiso
↓
intenta hacer commit antiguo
```

Ese commit debe rechazarse.

---

## 31. Beat eliminado del vault

Si el owner elimina Beat A:

```text
Vault Purple
- Beat A
```

BeatGaler elimina o invalida todas sus referencias:

```text
folders
share links
publications
active Share Rooms
```

---

## 32. Carpeta eliminada

Eliminar una carpeta:

```text
delete Folder
```

elimina:

```text
colección
membresías
roles
permisos
share links
```

pero nunca elimina los beats originales de sus vaults.

---

## 33. Beat en múltiples carpetas

Un beat puede estar en:

```text
Folder A
Folder B
Folder C
```

Cada carpeta puede tener permisos independientes.

Salir de Folder A no afecta:

```text
Folder B
Folder C
```

---

## 34. Derecho de retirada del owner

El owner siempre conserva el derecho de retirar su propio beat de un espacio compartido.

Ningún Admin debería poder impedir:

```text
owner → remove my beat
```

La regla es:

> La colaboración puede delegar acceso y edición, pero nunca debe eliminar el control fundamental del owner sobre su propio beat.

---

# PARTE VII — SHARE LINKS

## 35. Links compartibles

Un share link puede representar:

```text
beat
o
folder
```

Ejemplo:

```text
beatgaler.com/s/ABC123
```

BeatGaler guarda:

```text
share_id
resource_id
permissions
expiration
status
```

Ejemplo:

```text
share_id: ABC123
resource: folder_52

permissions:
  view: true
  download: true
  edit: false

expiration: null
status: active
```

---

## 36. Abrir un share link

Flujo:

```text
Link
 ↓
BeatGaler valida token
 ↓
resuelve recurso
 ↓
resuelve beats
 ↓
resuelve owners + vaults
 ↓
reserva Share Room
 ↓
forward/copy
 ↓
asigna bot temporal
 ↓
receptor
```

---

## 37. Revocar un share link

Cuando se revoca:

```text
share = revoked
```

BeatGaler debe:

```text
bloquear nuevas sesiones
invalidar sesiones activas
limpiar Share Rooms relacionadas
dejar de renovar leases
```

El contenido original permanece intacto en sus vaults.

---

# PARTE VIII — PERFILES PÚBLICOS

## 38. Perfil público

Un usuario puede tener una página pública:

```text
beatgaler.com/@purple
```

que muestre:

```text
avatar
nombre
bio
links
beats públicos
```

Ejemplo:

```text
@purple

PUBLIC BEATS
├── Beat A
├── Beat F
└── Beat K
```

---

## 39. Publicar no significa exponer el vault

Nunca:

```text
Visitante
↓
Bot
↓
Vault Purple
```

En cambio:

```text
Vault Purple
   ↓
copy/forward
   ↓
Public Telegram Pool
   ↓
Visitante
```

---

## 40. Public Telegram Pool

Podemos mantener uno o varios chats de Telegram dedicados exclusivamente a contenido público.

Ejemplo:

```text
Public Pool 01
Public Pool 02
Public Pool 03
```

A diferencia de las Share Rooms:

> Aquí sí puede ser global porque todo el contenido almacenado dentro ya está destinado a ser público.

No necesitamos aislar Beat A de Beat B si ambos son públicos.

---

## 41. Qué puede hacerse público

Inicialmente:

```text
✓ Audio
✓ Artwork
✓ Metadata
```

No:

```text
✗ Project ZIP
✗ Samples
✗ archivos de producción privados
```

Podríamos permitir:

```text
MP3
WAV
```

dependiendo de configuración.

---

## 42. Permisos públicos

Ejemplo:

```text
public = true

listen = true
download_mp3 = false
download_wav = false
```

Otro beat:

```text
listen = true
download_mp3 = true
download_wav = true
```

Así publicar y permitir descarga son cosas distintas.

---

## 43. Publicación como copia derivada

Ejemplo:

```text
Vault Purple
└── Beat A ← CANÓNICO
        ↓
        ↓ publish
        ↓
Public Pool
└── Beat A ← COPIA PÚBLICA
```

La copia pública no cambia ownership.

---

## 44. Actualizar un beat público

Si el owner modifica el beat:

```text
Vault Purple
   ↓
Bot interno confiable
   ↓
actualiza Public Pool
```

La publicación pública puede sincronizarse con la versión canónica.

---

## 45. Hacer privado nuevamente

Cuando Purple selecciona:

```text
Make Private
```

BeatGaler:

```text
elimina publicación pública
↓
elimina mensaje del Public Pool
↓
elimina referencia pública
↓
desaparece del perfil
```

Pero:

```text
Vault Purple
└── Beat A
```

permanece intacto.

---

# PARTE IX — TRES NIVELES DE ACCESO

## 46. Private

```text
Vault personal
```

Acceso:

```text
owner
```

Es la copia canónica.

---

## 47. Shared

```text
Share Room temporal
```

Acceso:

```text
usuarios concretos
o
share links
```

Permisos:

```text
view
download
edit
```

Puede incluir beats de varios owners.

---

## 48. Public

```text
Public Telegram Pool
```

Acceso:

```text
cualquier visitante autorizado a contenido público
```

Contenido:

```text
audio
artwork
metadata
```

Nunca proyectos privados.

---

# PARTE X — RESPONSABILIDADES

## 49. Telegram

Se encarga de:

```text
almacenar archivos
servir archivos
transportar archivos
streaming
downloads
forward/copy entre chats
```

---

## 50. BeatGaler

Se encarga de:

```text
usuarios
identidad
ownership
vault mappings
folders
folder membership
roles
permissions
shares
share links
public profiles
publications
leases
Share Room allocation
Public Pool allocation
autorización de commits
coordinación de bots
revocaciones
```

---

## 51. Bot temporal de usuario

Puede acceder únicamente al contexto temporal que BeatGaler le asignó.

Por ejemplo:

```text
Share Room
```

Nunca debe tener simultáneamente acceso al vault privado del owner mientras sus credenciales estén expuestas al receptor.

---

## 52. Bot interno confiable

Puede:

```text
Vault → Share Room
Share Room → Vault
Vault → Public Pool
actualizar publicaciones
realizar commits autorizados
```

Sus credenciales permanecen exclusivamente dentro de infraestructura confiable.

---

# PARTE XI — MODELO CONCEPTUAL

## 53. Relaciones principales

```text
USER
 │
 ├── owns VAULT
 │      │
 │      └── owns BEATS
 │
 ├── participates in FOLDERS
 │      │
 │      ├── Admin
 │      ├── Editor
 │      └── Viewer
 │
 └── has PUBLIC PROFILE
        │
        └── publishes selected BEATS
```

---

## 54. Un beat puede aparecer en muchos contextos

```text
                       Beat A
                         │
                  owner = Purple
                         │
                  Vault Purple
                         │
          ┌──────────────┼──────────────┐
          │              │              │
          ▼              ▼              ▼

      Folder A        Folder B      Public Profile
          │              │              │
          ▼              ▼              ▼
     Share Room      Share Room      Public Pool
```

Pero sigue existiendo una única copia canónica:

```text
Vault Purple
```

---

# PARTE XII — FLUJO GENERAL

## 55. Shared Folder

```text
Vault Purple ─┐
              │
Vault Juan ───┼──→ Bot interno confiable
              │
Vault Ana ────┘
                    ↓
                Share Room
                    ↓
               Bot temporal
                    ↓
                  Usuario
```

---

## 56. Edición

```text
Usuario
   ↓
Share Room
   ↓
Nueva versión
   ↓
BeatGaler verifica:
- identidad
- folder
- role
- permissions
- beat owner
- canonical vault
   ↓
Bot interno confiable
   ↓
Vault canónico
```

---

## 57. Publicación

```text
Vault canónico
   ↓
Bot interno confiable
   ↓
Public Pool
   ↓
Perfil público
   ↓
Visitante
```

---

# PARTE XIII — PRINCIPIOS DE SEGURIDAD

## 58. Regla de credenciales

> Ninguna credencial entregada a un usuario externo debe pertenecer a un bot que tenga acceso al vault privado original.

---

## 59. Regla de commits

> Todo cambio hacia un vault debe ser ejecutado por un bot interno confiable después de que BeatGaler vuelva a verificar los permisos.

---

## 60. Regla de ownership

> Ninguna carpeta, share o publicación cambia automáticamente el owner de un beat.

---

## 61. Regla de ubicación

> Todo beat tiene un único vault canónico.

---

## 62. Regla de carpetas

> Una carpeta contiene referencias y permisos; nunca posee físicamente los beats.

---

## 63. Regla de aislamiento

Contenido privado:

```text
Vault
```

Contenido compartido:

```text
Share Room temporal
```

Contenido público:

```text
Public Pool
```

Nunca deben mezclarse accidentalmente.

---

## 64. Regla de retirada

> El owner siempre puede retirar su beat de una carpeta compartida o dejar de publicarlo.

---

# PARTE XIV — IDEA CENTRAL

La arquitectura puede resumirse así:

```text
BEAT
→ tiene un owner
→ vive en un vault canónico


FOLDER
→ es una colección lógica
→ puede contener beats de múltiples owners
→ tiene Admins / Editors / Viewers
→ delega permisos


SHARE ROOM
→ es temporal
→ contiene únicamente el contenido compartido
→ protege los vaults originales


PUBLIC PROFILE
→ muestra beats seleccionados por el owner
→ utiliza copias públicas de audio
→ nunca expone el vault


BEATGALER
→ controla identidad, ownership y permisos


TELEGRAM
→ almacena y transporta los archivos
```

La filosofía general es:

> **El vault conserva ownership y verdad canónica.**

> **Las carpetas organizan y delegan colaboración.**

> **Las Share Rooms aíslan contenido privado durante un share.**

> **Los Public Pools permiten publicar audio sin exponer el vault.**

> **BeatGaler decide quién puede hacer qué; Telegram mueve y almacena los archivos.**

De esta forma BeatGaler puede soportar:

```text
bibliotecas privadas
carpetas colaborativas
share links
edición entre usuarios
perfiles públicos
beats públicos
streaming público
downloads controlados
```

sin abandonar su arquitectura principal basada en transferencia directa con Telegram.