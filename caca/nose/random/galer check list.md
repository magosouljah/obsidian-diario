
# OLD
## BeatGaler — Plan de Testing basado en la pirámide

## Orden de trabajo

1. Unit Tests
2. Component Tests
3. Integration Tests
4. End-to-End Tests
5. Manual Testing

Regla:

> No subimos de nivel innecesariamente si algo puede probarse en una capa inferior.

Y:

> Manual Testing se deja para el final, salvo que sea indispensable para desbloquear algo.

---

## NIVEL 1 — UNIT TESTS
## Base de la pirámide
## Principalmente White Box

Objetivo:

Probar funciones pequeñas, aisladas, rápidas y deterministas.

Estos deben ser la mayor cantidad de tests de BeatGaler.

---

## Metadata / validaciones

- [ ] Validar BPM
- [ ] Validar Key
- [ ] Validar Tags
- [ ] Sanitizar Beat Name
- [ ] Sanitizar Filename
- [ ] Sanitizar Paths
- [ ] Sanitizar Metadata
- [ ] Sanitizar URLs
- [ ] Unicode
- [ ] Emojis
- [ ] Nombres extremadamente largos
- [ ] Windows reserved names
- [ ] Caracteres especiales
- [ ] HTML payloads
- [ ] JS/XSS payloads
- [ ] SQL-like payloads
- [ ] Shell-like payloads
- [ ] Path Traversal strings

Tipo:

`White Box`

---

## Background procedural

- [ ] Mismo `beat.id` → mismo fondo
- [ ] Renombrar beat no cambia fondo
- [ ] Distribución 2 colores ≈ 45%
- [ ] Distribución 3 colores ≈ 35%
- [ ] Distribución 4 colores ≈ 20%
- [ ] Saturación dentro de límites
- [ ] Luminosidad dentro de límites
- [ ] Harmony generator válido
- [ ] Fondo siempre determinista
- [ ] Negro base correcto

Tipo:

`White Box`

---

## Playback state

- [ ] `uploading` bloquea Play
- [ ] `playback_preparing` bloquea Play
- [ ] `synced` permite Play
- [ ] `error` no permite estados inválidos
- [ ] Queue no salta playback gate
- [ ] Next/Previous respetan estados

Tipo:

`White Box`

---

## Internal state machine

- [ ] `local`
- [ ] `pending_upload`
- [ ] `uploading`
- [ ] `synced`
- [ ] `pending_update`
- [ ] `error`
- [ ] `downloading`
- [ ] `offline_available`
- [ ] `playback_preparing`
- [ ] `deleting`
- [ ] `pending_delete`
- [ ] `conflict`

Probar transiciones válidas e inválidas.

Tipo:

`White Box`

---

## Cache / LRU

- [ ] LRU elimina el archivo correcto
- [ ] Cache no supera límite
- [ ] Archivo reproduciéndose no se elimina
- [ ] `clear cache`
- [ ] Actualización de access time
- [ ] Cache entry corrupta

Tipo:

`White Box`

---

## Index / Tombstones

- [ ] Merge de índices
- [ ] Tombstone gana contra snapshot viejo
- [ ] Beat eliminado no resucita
- [ ] Nombre reutilizable con ID nuevo
- [ ] Empty library válida
- [ ] Campos desconocidos preservados
- [ ] Stale version no sobrescribe versión nueva

Tipo:

`White Box`

---

## PROJECT / ZIP

- [ ] Reconocer `.flp`
- [ ] Reconocer `.als`
- [ ] Reconocer `.logicx`
- [ ] Reconocer `.ptx`
- [ ] Reconocer `.ptf`
- [ ] Detectar Project File anidado
- [ ] Ignorar `Backup`
- [ ] Ignorar `Backups`
- [ ] ZIP sin Project File = inválido
- [ ] ZIP con Project File = válido
- [ ] ZIP Slip detection
- [ ] ZIP Bomb limits
- [ ] MIME/file-type validation

Tipo:

`White Box`

---

## Export

- [ ] Builder de `[BPM Key]`
- [ ] Metadata merge
- [ ] Genre merge
- [ ] Filename sanitization
- [ ] Folder `(1)` collision resolver
- [ ] WAV chunk preservation logic

Tipo:

`White Box`

---

## Accounts

- [ ] Password hashing helpers
- [ ] Token expiration
- [ ] Token rotation logic
- [ ] Email code expiration
- [ ] Email code one-time use
- [ ] Referral validation
- [ ] Self referral blocked
- [ ] Member Number allocation logic
- [ ] Plan entitlement calculation
- [ ] Quota calculation
- [ ] Upgrade/Downgrade rules

Tipo:

`White Box`

---

## NIVEL 2 — COMPONENT TESTS
## Principalmente White Box + algo de Black Box

Objetivo:

Probar una pieza visible o módulo completo sin levantar BeatGaler entero.

---

## Review Beat

- [ ] Modal aparece
- [ ] Metadata se llena
- [ ] Loading states
- [ ] Save disabled hasta estar listo
- [ ] Cancel
- [ ] Save All
- [ ] Tags editables
- [ ] Errores visibles
- [ ] Multiple beats navigation
- [ ] Primer Review aparece inmediatamente

Tipo:

`White Box + Black Box`

---

## BeatCard

- [ ] Play disabled cuando corresponde
- [ ] Loading state
- [ ] Green complete
- [ ] Upload error `!`
- [ ] Error muestra razón
- [ ] Space Bar no deja borde blanco extraño
- [ ] Artwork real
- [ ] Procedural background
- [ ] Sin iniciales en procedural
- [ ] Project indicator 📦
- [ ] Incomplete warning
- [ ] Drag target

Tipo:

`White Box + Black Box`

---

## Player

- [ ] Play
- [ ] Pause
- [ ] Seek
- [ ] Volume
- [ ] Next
- [ ] Previous
- [ ] Queue
- [ ] Space Play/Pause
- [ ] Range slider cursor correcto

Tipo:

`Black Box`

---

## Trash UI

- [ ] Lista correcta
- [ ] Restore
- [ ] Empty Trash
- [ ] Loading
- [ ] Error
- [ ] Background cleanup status
- [ ] Human-readable beat names

Tipo:

`Black Box`

---

## Settings / Account

- [ ] Login fields
- [ ] Email
- [ ] Password
- [ ] MFA
- [ ] Google
- [ ] X
- [ ] Profile Photo
- [ ] Member Number
- [ ] Joined Date
- [ ] Plan
- [ ] Usage quotas
- [ ] Referrals
- [ ] Logout
- [ ] Sessions

Tipo:

`Black Box`

---

## Startup UI

- [ ] Una sola pantalla inicial de loading
- [ ] Startup Gate
- [ ] Primeros beats aparecen correctamente
- [ ] Progressive Reveal
- [ ] Un beat fallido no bloquea el resto

Tipo:

`Black Box`

---

## NIVEL 3 — INTEGRATION TESTS
## Mezcla fuerte White Box + Black Box

Objetivo:

Comprobar que varios subsistemas funcionan juntos correctamente.

---

## Import → Index

- [ ] Import MP3 → SQLite → Telegram Index
- [ ] Import WAV → MP3 generated → Telegram
- [ ] Artwork → Index
- [ ] Metadata → Index
- [ ] PROJECT → Manifest → Index
- [ ] Primer beat en biblioteca vacía

Tipo:

`White Box + Black Box`

---

## Bulk Import multi-folder

MUY IMPORTANTE.

- [ ] 10 carpetas
- [ ] 20 beats
- [ ] 50 beats
- [ ] Partial failures
- [ ] Retry solo fallidos
- [ ] No duplicados
- [ ] UI count = Index count
- [ ] Index count = Telegram content esperado
- [ ] Error reason visible

Tipo:

`Black Box con inspección White Box`

---

## Review Beat Performance

- [ ] 1 beat
- [ ] 10 beats
- [ ] 50 beats
- [ ] Primer modal aparece antes de trabajo pesado
- [ ] Metadata restante llega progresivamente
- [ ] UI no se congela

Medir:

`select files → Review visible`

Tipo:

`Black Box performance`

---

## Upload → Playback

- [ ] Upload
- [ ] `PLAYBACK_PREPARING`
- [ ] MASTER ready
- [ ] Upload Complete
- [ ] Primer Play funciona
- [ ] No falso `Beat unavailable`

Tipo:

`Black Box + White Box logs`

---

## Trash ↔ Telegram

- [ ] Remove
- [ ] Trash
- [ ] Restore
- [ ] Empty Trash
- [ ] Tombstone
- [ ] Telegram cleanup
- [ ] Restart
- [ ] No resurrection

Tipo:

`Black Box + White Box state verification`

---

## PROJECT

- [ ] Drop FLP
- [ ] Upload
- [ ] Manifest
- [ ] Restart
- [ ] 📦 aparece
- [ ] Open Project
- [ ] Replace
- [ ] Cancel
- [ ] Backup excluded

Tipo:

`Black Box`

---

## Export

- [ ] MP3 source → export
- [ ] WAV source → export
- [ ] Metadata preservation
- [ ] Artwork preservation
- [ ] PROJECT reconstruction
- [ ] Everything
- [ ] `(1)` collision

Tipo:

`Black Box`

---

## Cache + Playback

- [ ] Cold
- [ ] Warm
- [ ] Hot
- [ ] Cache eviction
- [ ] Playback mientras eviction
- [ ] Cache clear
- [ ] Restart

Tipo:

`Black Box + White Box metrics`

---

## Offline

- [ ] Disconnect
- [ ] Cached Play
- [ ] Uncached Play
- [ ] Metadata edit
- [ ] Import
- [ ] Upload Pending
- [ ] Reconnect
- [ ] Queue resume
- [ ] Index remains correct

Tipo:

`Black Box`

---

## Multi-device conflicts

- [ ] PC A cambia beat
- [ ] PC B cambia mismo beat
- [ ] Version conflict
- [ ] Merge compatible changes
- [ ] Conflict state
- [ ] User choice where needed

Tipo:

`Black Box`

---

## Client ↔ Telegram direct

- [ ] Client upload directo
- [ ] Client download directo
- [ ] Host no relaya bytes
- [ ] Auth server sigue controlando permissions
- [ ] Otro usuario no puede leer archivos ajenos
- [ ] Revocation works

Tipo:

`Black Box + White Box network inspection`

---

## Accounts / Auth

- [ ] Register → DB
- [ ] Login → session
- [ ] Logout → revoked
- [ ] MFA
- [ ] Password reset
- [ ] Email Verification
- [ ] Session persistence
- [ ] Session revoke

Tipo:

`Black Box`

---

## Member Number

- [ ] 100 registros concurrentes
- [ ] 100 números únicos
- [ ] Delete #42
- [ ] Next user = #101
- [ ] Nunca reciclar

Tipo:

`Black Box + DB verification`

---

## Referrals

- [ ] A invita B
- [ ] B Signup
- [ ] B Verify
- [ ] B pays
- [ ] A receives reward
- [ ] Refund
- [ ] Reward adjustment
- [ ] Self Referral blocked

Tipo:

`Black Box`

---

## Plans / Entitlements

- [ ] Free
- [ ] Entry
- [ ] Highest
- [ ] Upgrade
- [ ] Downgrade
- [ ] Expired
- [ ] Canceled
- [ ] Payment Failed
- [ ] Simultaneous quota requests
- [ ] LocalStorage plan manipulation does nothing

Tipo:

`Black Box`

---

## Auto-Updater / Migrations

- [ ] Old schema → new schema
- [ ] Old app → update
- [ ] Library survives
- [ ] Settings survive
- [ ] Failed migration recovery
- [ ] Failed update recovery

Tipo:

`Black Box + White Box DB inspection`

---

## NIVEL 4 — END-TO-END TESTS
## Principalmente Black Box

Objetivo:

Usar BeatGaler como lo usaría un usuario real.

Aquí levantamos:

- Desktop
- Backend
- Accounts
- Telegram
- Web cuando exista
- Database
- Full auth

---

## E2E — Primer usuario

- [ ] Install
- [ ] Register
- [ ] Email Code
- [ ] Login
- [ ] First Run
- [ ] Import first beat
- [ ] Review Beat
- [ ] Save
- [ ] Wait upload
- [ ] Play
- [ ] Restart
- [ ] Beat sigue ahí

Tipo:

`Black Box`

---

## E2E — Beat completo

- [ ] Import WAV
- [ ] Generate MP3
- [ ] Artwork
- [ ] Metadata
- [ ] PROJECT
- [ ] Restart
- [ ] Play
- [ ] Open Project
- [ ] Download Everything
- [ ] Trash
- [ ] Restore
- [ ] Permanent Delete

Tipo:

`Black Box`

---

## E2E — Bulk Library

- [ ] Import 20 beats
- [ ] Import 50 beats
- [ ] Multiple folders
- [ ] Retry failures
- [ ] Restart
- [ ] Search
- [ ] Filter
- [ ] Playback random beats
- [ ] Trash several
- [ ] Export several

Tipo:

`Black Box`

---

## E2E — Offline

- [ ] Login connected
- [ ] Disconnect
- [ ] Use cached library
- [ ] Edit
- [ ] Queue upload
- [ ] Reconnect
- [ ] Everything syncs correctly

Tipo:

`Black Box`

---

## E2E — Security / Two Users

User A + User B.

- [ ] A cannot see B library
- [ ] A cannot edit B
- [ ] A cannot delete B
- [ ] A cannot download B
- [ ] A cannot obtain B Telegram data
- [ ] Direct API attacks fail

Tipo:

`Black Box`

---

## E2E — Web + Desktop

- [ ] Login Web
- [ ] Change beat
- [ ] Desktop sync
- [ ] Change Desktop
- [ ] Web sync
- [ ] Concurrent edit
- [ ] Conflict resolution

Tipo:

`Black Box`

---

## E2E — Subscription

- [ ] Free signup
- [ ] Web works
- [ ] Desktop blocked
- [ ] Upgrade Entry
- [ ] Desktop unlocked
- [ ] Upgrade Highest
- [ ] Higher quotas active
- [ ] Downgrade
- [ ] No data deleted

Tipo:

`Black Box`

---

## E2E — Update

- [ ] Install older BeatGaler
- [ ] Create library
- [ ] Update
- [ ] Migration
- [ ] Restart
- [ ] Library intact
- [ ] Play
- [ ] PROJECT
- [ ] Download

Tipo:

`Black Box`

---

## NIVEL 5 — MANUAL TESTING
## Punta de la pirámide
## IGNORAR HASTA EL FINAL

Estas cosas no vamos a gastar tiempo automatizándolas ahora.

---

## Visual / UX

- [ ] Fondos procedurales se ven bonitos
- [ ] Cantidad de negro correcta
- [ ] Colores elegantes
- [ ] Spinner visualmente perfectamente centrado
- [ ] Startup Reveal se siente bonito
- [ ] Review Beat se siente instantáneo
- [ ] Animaciones agradables
- [ ] Empty states
- [ ] General polish

---

## Branding

- [ ] Nombre oficial
- [ ] Logo
- [ ] Icon
- [ ] Trademark review
- [ ] Domain
- [ ] Social names

---

## Product decisions

- [ ] Precio Free / Entry / Highest
- [ ] Límites exactos
- [ ] Referral rewards
- [ ] Fair Use
- [ ] Trial
- [ ] Public/private profile choices

---

## Legal

- [ ] Privacy Policy final
- [ ] Terms final

---

## Manual security

- [ ] Manual Pentest
- [ ] Strix findings review
- [ ] Human abuse exploration

---

## Clean Machine

- [ ] Instalar manualmente en PC limpio
- [ ] Instalar manualmente en Mac limpio
- [ ] Verificar experiencia real

---

## WHITE BOX TESTING

Principalmente:

- Unit Tests
- State machines
- Index merge
- Tombstones
- Cache
- Metadata functions
- Sanitization
- ZIP validation
- Quotas
- Referral logic
- Member Number allocation
- Migration internals
- Logs/state assertions

Nos permite saber:

> “¿El código interno hace exactamente lo que debería?”

---

## BLACK BOX TESTING

Principalmente:

- Component Tests
- Integration Tests
- End-to-End Tests

Nos permite saber:

> “Sin importar cómo esté construido por dentro, ¿BeatGaler hace lo correcto desde afuera?”

Ejemplo:

`Upload Beat`

No nos importa inicialmente qué función interna se ejecutó.

Solo comprobamos:

- aparece
- se sube
- está en Telegram
- está en Index
- reproduce
- sobrevive restart

---

## ESTRUCTURA FINAL QUE QUEREMOS

                    Manual
                      ▲
                     / \
                    /   \
                  E2E Tests
                  /       \
             Integration Tests
               /           \
            Component Tests
             /               \
          Unit Tests Unit Tests
        ────────────────────────

Muchos Unit Tests.

Menos Component Tests.

Menos Integration Tests.

Pocos E2E.

Muy poco Manual.

---

## FASE 1 — EMPEZAMOS AQUÍ

## Unit Tests

Primer paquete recomendado:

- [ ] Metadata Validation
- [ ] Beat Name / Tag / Path Security
- [ ] Internal Beat States
- [ ] Tombstones / Index merge
- [ ] PROJECT ZIP classification
- [ ] Backup filtering
- [ ] Procedural background determinism
- [ ] Cache / LRU
- [ ] Export filename / metadata helpers
- [ ] Playback Readiness
- [ ] Member Number allocator
- [ ] Referral validation
- [ ] Plan entitlement logic
- [ ] Email verification-code logic

---

## FASE 2

## Component Tests

- [ ] BeatCard
- [ ] Review Beat
- [ ] Player
- [ ] Trash
- [ ] Settings / Account
- [ ] Startup Loader

---

## FASE 3

## Integration Tests

- [ ] Import → Telegram Index
- [ ] Bulk Multi-folder Import
- [ ] Upload → First Play
- [ ] Trash → Tombstone
- [ ] PROJECT
- [ ] Export
- [ ] Offline / Reconnect
- [ ] Cache / Playback
- [ ] Accounts
- [ ] Plans
- [ ] Referrals
- [ ] Migrations
- [ ] Direct Client ↔ Telegram

---

## FASE 4

## End-to-End

- [ ] Complete first-user flow
- [ ] Complete beat lifecycle
- [ ] Bulk library flow
- [ ] Offline flow
- [ ] Two-user security flow
- [ ] Web ↔ Desktop flow
- [ ] Subscription flow
- [ ] Update flow

---

## FASE 5 — SOLO AL FINAL

## Manual

- [ ] Visual polish
- [ ] Branding
- [ ] Pricing decisions
- [ ] Legal
- [ ] Manual Pentest
- [ ] Clean Machine
      
      
      
# new

# Plan maestro de automatización de tests

## Objetivo final

Quiero que terminemos con esto:

```text
                MANUAL
                  ▲
                  │
               E2E real
                  ▲
                  │
             Integration
                  ▲
                  │
              Component
                  ▲
                  │
               Unit
──────────────────────────────────

          GitHub Actions
                 │
                 ▼
     ❌ NO PASA = NO SE PUBLICA
```

Y que normalmente tú solo necesites hacer:

```powershell
# Ejecuta absolutamente toda la batería automática local de BeatGaler
npm test
```

Mientras que GitHub la ejecute automáticamente en cada push/PR.

---

# FASE 0 — Construir la infraestructura

Esta sería **la primera cosa que implementaría**.

No escribiría todavía 200 tests.

Primero hacemos que BeatGaler tenga un sistema serio donde meterlos.

### Stack que usaría

**TypeScript / lógica frontend:** Vitest.

Tiene sentido especialmente aquí porque BeatGaler ya usa Vite + TypeScript. Vitest reutiliza ese ecosistema y soporta TS/JSX y coverage. ([Vitest](https://vitest.dev/guide/?utm_source=chatgpt.com "Getting Started | Guide"))

**Frontend que llama Tauri:** Vitest + mocks oficiales de Tauri.

Tauri tiene soporte específico para interceptar IPC con `mockIPC`, así que podemos probar muchas operaciones que hoy parecen requerir abrir Desktop sin levantar realmente la aplicación. ([Tauri](https://v2.tauri.app/develop/tests/mocking/?utm_source=chatgpt.com "Mock Tauri APIs"))

**Rust:** `cargo test`.

**Componentes React:** Vitest Browser/Component Testing.

Vitest tiene soporte actual para component testing de React. ([Vitest](https://vitest.dev/guide/browser/component-testing?utm_source=chatgpt.com "Component Testing | Guide"))

**Desktop E2E real:** WebdriverIO + Tauri.

Aquí haría un cambio respecto a lo que quizá hubiéramos elegido antes: la documentación actual de Tauri recomienda WebdriverIO con `@wdio/tauri-service`, y actualmente soporta Windows, Linux y macOS, además de permitir ejecutar comandos Tauri, capturar logs y trabajar con múltiples instancias. ([Tauri](https://v2.tauri.app/develop/tests/webdriver/?utm_source=chatgpt.com "WebDriver"))

**Web futura:** Playwright.

No lo usaría como driver principal del Desktop si Tauri ya tiene una ruta específica mejor, pero sí para BeatGaler Web. Playwright automatiza Chromium, Firefox y WebKit y permite paralelizar tests. ([Playwright](https://playwright.dev/?utm_source=chatgpt.com "Playwright: Fast and reliable end-to-end testing for modern ..."))

---

# FASE 1 — Convertir lo actual en `Test Core`

Esto lo haría **sin borrar tus regresiones actuales**.

Actualmente tienes cosas como:

```text
scripts/
├── regression-dragdrop.ts
├── regression-playback-readiness.ts
├── regression-beat-runtime-state.ts
├── regression-telegram-retry.cjs
├── regression-direct-manager-only.mjs
└── run-regressions.mjs
```

Eso tiene muchísimo valor.

Pero algunas de esas pruebas son más bien **architecture guards** que unit tests.

Por ejemplo, hoy `run-regressions.mjs` comprueba incluso que determinados strings o patrones sigan existiendo dentro de `App.tsx` y del parche WRY.

Eso yo **NO lo eliminaría**.

Lo clasificaría:

```text
tests/
├── unit/
├── component/
├── integration/
├── e2e/
├── fixtures/
├── helpers/
└── guards/
```

Y tus regresiones actuales pasarían conceptualmente a:

```text
tests/guards/
```

### Por qué conservarlas

Porque protegen decisiones arquitectónicas muy delicadas de BeatGaler:

- Tauri Native Drop
    
- WRY como único Windows Drop owner
    
- Pinterest Option 2
    
- CF_HDROP fast path
    
- no staging para archivos locales
    
- playback no marcado prematuramente
    
- runtime states
    
- retry
    
- transport architecture
    

Un unit test puede decir:

> esta función funciona.

El guard puede decir:

> nadie volvió a introducir la arquitectura vieja.

**Necesitamos ambos.**

---

# FASE 2 — Unit tests masivos

Aquí obtendríamos el mayor ROI.

La mayor parte de lo que pusiste en Nivel 1 puede quedar **100% automatizada y correr en segundos**.

Además tu código ya tiene varios módulos perfectos para empezar.

## Paquete 1 — código que YA está aislado

Primero atacaría:

```text
src/lib/metadataValidation.ts
src/lib/proceduralBeatBackground.ts

src/features/playback/playbackReadiness.ts
src/features/state/beatRuntimeState.ts

src/features/dragdrop/nativeDropArbiter.ts
src/features/dragdrop/nativeExternalImage.ts
src/features/dragdrop/externalDropEffect.ts

cloud-server/plans.js
cloud-server/telegram-retry.js
cloud-server/transport-pool.js
cloud-server/master-storage.js
```

Son candidatos naturales porque no necesitas levantar toda la aplicación.

### Metadata

Automatizar:

```text
BPM
Key
Tags

Unicode
Emoji
Long strings
Windows names
Path traversal
HTML
JS
SQL-ish strings
Shell-ish strings
```

Aquí usaría **parameterized tests**.

En lugar de:

```text
test 1
test 2
test 3
...
```

una tabla puede alimentar 50–100 ataques diferentes automáticamente.

---

# FASE 3 — Property / Fuzz testing

Esta es una adición importante a tu plan.

No quiero que nosotros tengamos que imaginar cada string raro que podría romper BeatGaler.

Podemos hacer que la computadora genere miles.

Ejemplo:

```text
Beat Name:
    10,000 strings aleatorios

Tag:
    10,000 strings aleatorios

Filename:
    Unicode
    null-ish characters
    símbolos
    slash
    backslash
    rutas absurdamente largas
```

Y definir propiedades:

```text
sanitize(x) jamás genera path traversal

sanitize(x) jamás devuelve Windows reserved path inválido

validate(x) jamás lanza una excepción

sanitize(sanitize(x)) === sanitize(x)
```

Este tipo de test podría encontrar bugs que ni tú ni yo pensamos manualmente.

Lo incluiría especialmente en:

- sanitización
    
- filenames
    
- tags
    
- metadata
    
- ZIP
    
- URLs
    
- index
    
- state transitions
    

---

# FASE 4 — State machine tests

Esto es crítico para BeatGaler.

Ya tienes:

```text
pending_upload
uploading
synced
pending_update
error
downloading
offline_available
playback_preparing
deleting
pending_delete
conflict
```

Y v0.5.0 ya tiene `beatRuntimeState.ts`.

En lugar de probar solamente casos conocidos, hacemos una **matriz de transición completa**.

Por ejemplo:

```text
                  → uploading → synced → error → deleting ...

local
pending_upload
uploading
synced
pending_update
error
...
```

Cada combinación queda clasificada:

```text
✅ válida
❌ inválida
```

Después hacemos un test que recorra **todas**.

Esto automáticamente detectaría cosas como:

```text
deleting → playback
error → playing
uploading → play
pending_delete → update
```

aunque el bug aparezca meses después.

---

# FASE 5 — Index tests con una biblioteca falsa

Este merece su propio mini-framework.

Crearíamos fixtures:

```text
tests/fixtures/libraries/

empty.json
one-beat.json
100-beats.json
deleted-beats.json
conflicts.json
old-schema.json
corrupt-index.json
unknown-fields.json
```

Así cada test puede cargar un estado conocido.

Automatizamos:

- merge
    
- tombstones
    
- stale versions
    
- ID nuevo con nombre viejo
    
- unknown fields
    
- library vacía
    
- versiones conflictivas
    
- beat eliminado que intenta resucitar
    
- índice corrupto
    
- migraciones
    

Esto sería muy importante para proteger **Galer T-Library Schema v2**.

---

# FASE 6 — PROJECT ZIP torture suite

Aquí podemos automatizar prácticamente todo.

Crearíamos ZIPs dinámicamente durante el test:

```text
valid-flp.zip
valid-ableton.zip
nested-project.zip
backup-only.zip
no-project.zip
zip-slip.zip
huge-file.zip
many-files.zip
weird-unicode.zip
```

Y también generarlos sobre la marcha.

Probar:

```text
FLP
ALS
logicx
PTX
PTF

nested folders
Backup/
Backups/

ZIP Slip
ZIP Bomb limits
wrong MIME
renamed executable
long names
Unicode
```

No tienes que guardar 100 ZIPs físicos.

El test puede fabricarlos, probarlos y destruirlos.

---

# FASE 7 — Component testing

Solo después de tener bien cubierta la lógica.

Componentes principales:

```text
BeatCard
Review Beat
Player
Trash
Settings
Account
Startup
```

Aquí NO queremos probar que el botón sea bonito.

Queremos probar comportamiento.

## Ejemplo BeatCard

Un test podría decir:

```text
Given:
    state = uploading

Render BeatCard

Expected:
    Play disabled
    uploading indicator visible
```

Después:

```text
state = synced

Expected:
    Play enabled
```

Después:

```text
state = error
reason = "MASTER unavailable"

Expected:
    error indicator visible
    reason accessible
```

Todo sin arrancar Desktop.

---

# FASE 8 — Mock de Tauri

Esto nos va a permitir automatizar mucho más de lo que parecería posible.

Tauri proporciona mocks específicos para frontend/IPC. ([Tauri](https://v2.tauri.app/develop/tests/mocking/?utm_source=chatgpt.com "Mock Tauri APIs"))

Entonces un component/integration test podría hacer:

```text
BeatCard
     ↓
invoke("open_project")
     ↓
FAKE TAURI
     ↓
return success
```

O:

```text
invoke("download_beat")
     ↓
throw NETWORK_ERROR
```

Y comprobar que UI responde correctamente.

Eso significa que podemos simular:

- filesystem
    
- dialogs
    
- commands
    
- errores
    
- respuestas lentas
    
- downloads
    
- uploads
    

sin levantar la infraestructura real.

---

# FASE 9 — Integration tests con servicios falsos

Esta capa es donde ahorraría **muchísima dependencia externa**.

No todos los tests de:

```text
Import → cloud
```

deben usar el almacenamiento real.

Tendríamos dos modos.

### Integration Fake

```text
BeatGaler
  ↓
Fake Cloud API
  ↓
Fake storage/index
```

Rápido y determinista.

Lo podemos ejecutar en cada commit.

### Integration Real

```text
BeatGaler
  ↓
test backend
  ↓
real transport
  ↓
isolated test vault
```

Más lento.

Se ejecutaría menos frecuentemente.

---

# FASE 10 — Una `Test Library` completamente desechable

Esto creo que va a ser una de las mejores cosas que podemos construir.

Crear:

```text
BeatGaler Test Environment
```

con:

```text
Test User A
Test User B

Test Library A
Test Library B

Test Vault A
Test Vault B
```

Nunca usar tus datos reales.

Antes de cada suite:

```text
RESET
```

Después:

```text
CLEANUP
```

Así podemos probar permanent delete, corrupción, conflictos, etc. sin miedo.

---

# FASE 11 — Bulk Import automatizado

Esto es P0 en términos de reliability.

Tus `dev-beats/` existentes ya son el principio perfecto.

Actualmente tienes beats de prueba como:

```text
Ambient Beat
Boom Bap
Drill Vibe
Future Bass
Hardtrap
Jazz Hop
LoFi Chill
Trap King
```

Yo convertiría eso en un **fixture generator**.

Por ejemplo:

```text
generate-library 1
generate-library 10
generate-library 20
generate-library 50
generate-library 500
```

Los beats podrían usar pequeños assets sintéticos.

Así automáticamente probamos:

```text
1
10
20
50
100
500
```

sin mantener cientos de archivos manualmente.

---

# FASE 12 — Performance tests automáticos

Esta parte de tu checklist NO debería quedarse manual.

Solo la apreciación de:

> “se siente instantáneo”

es manual.

Pero el tiempo sí puede automatizarse.

Definiríamos budgets.

Por ejemplo, conceptualmente:

```text
1 beat:
select → skeleton < X ms

10 beats:
select → skeleton < X ms

50 beats:
select → skeleton < X ms
```

Y adicionalmente:

```text
UI long task máximo
metadata first ready
all metadata ready
first playable
```

Entonces GitHub puede decir:

```text
❌ PERFORMANCE REGRESSION

Review Visible
baseline: 42 ms
current: 237 ms
```

Eso me parece muchísimo mejor que esperar a que tú notes:

> “se volvió lento otra vez.”

---

# FASE 13 — Regression budgets

No pondría thresholds ultra estrictos desde el primer día.

Primero:

```text
registramos baseline
```

Después:

```text
FAIL solamente si empeora > 20%
```

Más adelante:

```text
hard SLO
```

Así CI no se vuelve insoportable por variabilidad entre máquinas.

---

# FASE 14 — Cloud-server unit tests

Aquí v0.5.0 tiene un hueco bastante grande.

Actualmente:

```json
"test": "echo \"Error: no test specified\" && exit 1"
```

Por tanto pondría cobertura primero alrededor de:

```text
plans.js
telegram-retry.js
transport-pool.js
master-storage.js
```

Especialmente `transport-pool.js`.

Automatizaría:

### Pool fairness

```text
Bot01 gets 1
Bot02 gets 1
Bot03 gets 1

antes de:

Bot01 gets 2
```

### Session lease

```text
heartbeat
heartbeat lost
5 min timeout
cleanup
```

### Token/session behavior

```text
session begins
same credential maintained
session continues
session ends
cleanup/revoke
```

### Concurrencia

```text
100 simultaneous requests
300 simultaneous requests
```

Y verificar:

```text
no double assignment
no corrupted pool-state
no lost vault assignment
```

---

# FASE 15 — Fault injection

Esto lo añadiría a tu plan.

En vez de esperar a que Internet falle realmente:

```text
upload()
```

hacemos que el test pueda ordenar:

```text
FAIL AFTER 10%
FAIL AFTER 99%
TIMEOUT
CONNECTION RESET
SERVER 500
INVALID INDEX
MASTER MISSING
CACHE CORRUPT
```

Y comprobamos qué hace BeatGaler.

Esto es perfecto para:

- Upload
    
- Download
    
- Index
    
- reconnect
    
- project
    
- artwork
    
- trash
    
- retries
    

---

# FASE 16 — Offline automatizado

No quiero que estés apagando Wi-Fi manualmente para cada prueba.

Crearía una abstracción de red en nuestros tests:

```text
network = ONLINE
network = OFFLINE
network = HIGH_LATENCY
network = DROP_NEXT_REQUEST
```

Entonces:

```text
start online
↓
download beat
↓
mark offline
↓
network OFF
↓
restart app
↓
assert beat visible
↓
assert play works
```

Los últimos smoke tests sí pueden apagar tráfico real.

Pero el 95% se puede simular.

---

# FASE 17 — Desktop E2E real

Aquí sí arrancamos BeatGaler real.

La ruta actual recomendada por Tauri es WebdriverIO + su integración Tauri. ([Tauri](https://v2.tauri.app/develop/tests/webdriver/?utm_source=chatgpt.com "WebDriver"))

Los primeros E2E serían muy pocos.

## Smoke

```text
launch
library opens
no fatal error
close
```

## First User

```text
launch
login/register fixture
import
Review
Save
upload
play
restart
beat remains
```

## Lifecycle

```text
Import
Edit
Play
Download
Project
Trash
Restore
Delete
Restart
```

## Two users

WebdriverIO/Tauri soporta configuraciones útiles para múltiples instancias, por lo que podemos aprovecharlo más adelante para A/B y conflictos. ([Tauri](https://v2.tauri.app/develop/tests/webdriver/?utm_source=chatgpt.com "WebDriver"))

```text
Desktop A
Desktop B

same beat
concurrent mutation
conflict
```

---

# FASE 18 — Los E2E NO deben ser 500 tests

Este punto es importantísimo.

No convertiría cada combinación en E2E.

Por ejemplo:

**NO:**

```text
100 E2Es distintos para BPM inválido
```

**SÍ:**

```text
100 unit tests de BPM
1 E2E que confirme que error llega correctamente a UI
```

Exactamente siguiendo tu regla:

> No subir de nivel si puede probarse abajo.

---

# FASE 19 — GitHub Actions como guardia

Ahora mismo tus workflows principales están concentrados en builds.

Yo agregaría:

```text
PR / push
│
├── lint/typecheck
│
├── unit-ts
│
├── unit-rust
│
├── unit-cloud
│
├── architecture-guards
│
├── component
│
├── integration-fake
│
└── build
```

Todo esto debería ser obligatorio antes de merge/release.

Tauri también documenta ejecución de tests WebDriver dentro de CI, incluido soporte en GitHub Actions. ([Tauri](https://v2.tauri.app/es/develop/tests/webdriver/ci/?utm_source=chatgpt.com "Continuous Integration - GitHub Actions"))

---

# FASE 20 — Dividir CI en Fast y Full

Esto evita que testear sea molesto.

### `test:fast`

Cada vez que cambias código:

```text
Unit
Guards
TypeScript
Rust unit
```

Objetivo:

**ultrarrápido.**

### `test`

Antes de subir:

```text
Fast
Component
Integration Fake
```

### `test:full`

GitHub / release:

```text
Fast
Component
Integration
Desktop E2E
Performance
Security
Migration
```

---

# FASE 21 — Coverage, pero sin obsesionarnos

Vitest soporta coverage directamente. ([Vitest](https://vitest.dev/guide/?utm_source=chatgpt.com "Getting Started | Guide"))

No pondría inmediatamente:

```text
95% coverage obligatorio
```

Porque solo terminaríamos escribiendo tests basura.

Empezaría así:

```text
Critical modules → 90%+
General logic → 75%+
UI glue → sin requisito agresivo
```

Pero más importante:

### Coverage funcional

Cada feature crítica debe tener:

```text
happy path
failure path
recovery path
```

Eso vale mucho más que un número bonito.

---

# FASE 22 — Mutation Testing más adelante

Cuando tengamos cientos de unit tests, podemos hacer algo todavía más brutal.

El test runner modifica artificialmente código:

```ts
if (x > 60)
```

se convierte en:

```ts
if (x >= 60)
```

y pregunta:

> ¿algún test detectó el cambio?

Si todos los tests siguen verdes:

```text
nuestros tests no son suficientemente buenos
```

Esto no lo haría ahora.

Pero sí después de estabilizar Unit Tests.

---

# FASE 23 — Security completamente automatizable

Muchísimo de lo que pusiste como security puede salir del manual.

Automatizaría:

- XSS payload corpus
    
- traversal
    
- ZIP Slip
    
- malicious filenames
    
- unauthorized API
    
- cross-user access
    
- quota bypass
    
- plan local manipulation
    
- malformed JSON
    
- huge payload
    
- expired token
    
- revoked token
    
- reused verification code
    
- self referral
    

Y la prueba más importante:

```text
User A token
+
User B resource ID
=
DENIED
```

En cada endpoint.

---

# FASE 24 — Migraciones

Crearíamos snapshots reales de versiones antiguas:

```text
fixtures/migrations/
├── v0.3.x/
├── v0.4.x/
└── v0.5.x/
```

CI hace:

```text
load old data
↓
start current migration
↓
verify current schema
↓
verify beats
↓
verify metadata
↓
verify project
↓
verify playback reference
```

Eso protege una de las cosas más peligrosas de cualquier app con datos persistentes:

**actualizar sin perder bibliotecas.**

---

# FASE 25 — Qué SÍ dejaría manual

Después de automatizar todo esto, el manual queda muchísimo más pequeño.

Manual:

```text
¿Los backgrounds son bonitos?

¿La animación se siente bien?

¿Review se siente instantáneo?

¿El producto parece premium?

¿El flujo es confuso?

PC limpio real

Mac limpio real

human pentest exploratorio
```

Incluso Clean Machine puede tener automatización parcial, pero conservaría una pasada humana previa al release.

---

# Mi orden exacto para BeatGaler

No implementaría tu documento entero de golpe.

Haría esto:

```text
1. Test infrastructure
        ↓
2. Migrar regressions actuales → guards
        ↓
3. Vitest
        ↓
4. metadataValidation
        ↓
5. beatRuntimeState
        ↓
6. playbackReadiness
        ↓
7. proceduralBackground
        ↓
8. drag/drop pure logic
        ↓
9. index / tombstones
        ↓
10. ZIP / project
        ↓
11. cloud plans
        ↓
12. transport pool
        ↓
13. cache / LRU
        ↓
14. export helpers
        ↓
15. React components
        ↓
16. fake Tauri integration
        ↓
17. fake backend integration
        ↓
18. real test environment
        ↓
19. bulk tests
        ↓
20. performance tests
        ↓
21. fault injection
        ↓
22. offline/reconnect
        ↓
23. desktop E2E
        ↓
24. two-user/security E2E
        ↓
25. updater/migrations
        ↓
26. manual final pass
```

# Lo que automatizaríamos de tu documento

Mi objetivo sería aproximadamente:

|Área|Automatización objetivo|
|---|--:|
|Unit|**~100%**|
|Component|**~95%**|
|Integration|**~90–95%**|
|E2E|**~90% de los flujos definidos**|
|Performance|**~90%**|
|Security funcional|**~90%+**|
|Migration|**~100%**|
|Visual taste|**baja / manual**|
|Product decisions|**manual**|
|Human pentest|**manual**|

No significa 95% line coverage. Significa **95% de las verificaciones que escribiste ejecutables sin que tú tengas que tocarlas.**

---

# El cambio más importante al plan original

Tu documento piensa principalmente en:

```text
Unit
Component
Integration
E2E
Manual
```

Yo le agregaría **cuatro sistemas transversales**:

```text
                   TEST PYRAMID
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
 Architecture       Fault           Performance
   Guards          Injection         Regression
                        │
                        ▼
                  Fuzz / Property
```

Porque BeatGaler tiene precisamente muchos problemas donde esos cuatro tipos son extremadamente valiosos.

---

# Resultado que quiero al terminar

Tú haces un cambio aparentemente inocente en `App.tsx`.

GitHub responde:

```text
✅ 486 Unit Tests
✅ 82 Component Tests
✅ 41 Integration Tests
✅ 9 Desktop E2E Tests
✅ 14 Architecture Guards
✅ 27 Security Tests
✅ 12 Migration Tests

❌ PERFORMANCE

Bulk import 20 beats:
Review skeleton

Expected: < 100 ms
Received: 391 ms

Release blocked.
```

**Ese es el punto al que llevaría BeatGaler.**

Y creo que el próximo movimiento concreto debería ser **solo FASE 0 + FASE 1 + el primer paquete de Unit Tests**, sin tocar todavía E2E. Eso nos construye la fábrica que luego permite añadir cientos de tests muchísimo más rápido.