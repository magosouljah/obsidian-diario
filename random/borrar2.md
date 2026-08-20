# BeatGaler — Checklist actual

## Estado base actual

- [x] Base principal: `BeatGaler-galer-cloud-beta-v0.3.3`
- [x] Versión actual: `0.3.3-beta.1`
- [x] Últimos patches validados considerados parte del estado actual
- [x] `npm run test:regressions` protege bugs ya cerrados

---

# ✅ COMPLETADO

## 1. Arquitectura anti-regresiones

- [x] Regression Shield creado
- [x] Bugs importantes reciben regression test
- [x] Un solo dueño del drag & drop externo
- [x] Eliminadas rutas duplicadas/conflictivas de drag & drop
- [x] Patches intentan tocar solamente el subsistema necesario
- [x] Version guard
- [x] Release guard
- [x] GitHub guard
- [x] Playback guard
- [x] Trash guard
- [x] Project Drop guard
- [x] Cursor guard
- [x] Export metadata guard

---

## 2. Versionado

- [x] `VERSION` es la única fuente de verdad
- [x] `package.json` sincronizado
- [x] `package-lock.json` sincronizado
- [x] `tauri.conf.json` sincronizado
- [x] `Cargo.toml` sincronizado
- [x] `Cargo.lock` sincronizado
- [x] Settings muestra la misma versión
- [x] Product name sincronizado
- [x] Window title sincronizado
- [x] HTML title sincronizado

### Comandos

`npm run version:show`

`npm run version:check`

`npm run version:set -- 0.3.4 beta`

---

## 3. GitHub / ramas

- [x] Comando simple para guardar versión en GitHub
- [x] Rama automática desde `VERSION`
- [x] Rama personalizada soportada
- [x] Se puede aumentar versión dentro de una rama fija
- [x] Corregido `refspec matches more than one`
- [x] No usa force push

### Comando principal

`npm run github:save`

---

## 4. macOS / release infrastructure

- [x] Workflow macOS ya no está amarrado a V8
- [x] Construye el ref seleccionado
- [x] Version guard protege release
- [x] Release guard protege workflow

---

## 5. Pinterest / artwork desde Internet

- [x] Drag desde Pinterest funciona
- [x] Cursor acepta el drop
- [x] Soporte `application/x-pinterest-closeup-image`
- [x] Soporte File virtual de Chromium
- [x] Soporte URL `i.pinimg.com`
- [x] Fallbacks múltiples
- [x] Beat objetivo se conserva aunque WebView2 pierda `event.target`
- [x] Regression Shield específico

---

## 6. Drag & Drop

- [x] HTML5 es el dueño principal
- [x] No hay pipelines compitiendo
- [x] Imagen local funciona
- [x] Pinterest funciona
- [x] Drop sobre beat funciona
- [x] Drop sobre artwork funciona
- [x] Drop zones internos protegidos
- [x] WebView2 recuerda target durante dragover

---

## 7. Startup / Performance

- [x] Rating es el orden inicial
- [x] Primeros 6 beats tienen prioridad
- [x] Artwork listo antes de mostrar beat
- [x] Beats restantes aparecen progresivamente
- [x] Startup Gate bloquea interacción prematura
- [x] Download Cooking implementado
- [x] Arquitectura Cold → Warm → Hot
- [x] Fast Play Path
- [x] Audio Engine Priming
- [x] Playback por localhost
- [x] Download Cooking Diagnostic

### Resultado real medido

- [x] Primeros 512 KB alrededor de `143 ms`
- [x] Startup listo alrededor de `655 ms`
- [x] Click → audio alrededor de `35 ms` cuando está warm

---

## 8. Upload → Play

- [x] Beat subiendo no puede reproducirse
- [x] `PLAYBACK_PREPARING` no puede reproducirse
- [x] Play se habilita cuando MASTER tiene bytes reales
- [x] Eliminado falso `Beat unavailable` después del upload
- [x] Cuando aparece verde, Play funciona al primer intento
- [x] Queue/Next tampoco salta el bloqueo
- [x] `UPLOAD_PLAYBACK_GATE_READY` ocurre antes de `PLAY_CLICK`

---

## 9. Telegram como Source of Truth

- [x] Telegram Index es autoridad
- [x] SQLite es cache/representación local
- [x] Backup del índice
- [x] Recuperación de índice inválido
- [x] Validación del índice
- [x] Primer beat de biblioteca vacía se escribe correctamente
- [x] Bug histórico del primer beat ya no existe

### Prueba realizada

0 beats  
→ subir 1 beat  
→ `/library/get`  
→ `beats.length = 1`

---

## 10. Trash / Remove All

- [x] Remove All funciona al primer intento
- [x] No reaparecen tarjetas sin portada
- [x] Biblioteca vacía es estado válido
- [x] Trash usa nombres humanos
- [x] No muestra IDs `import-xxxx`
- [x] Empty Trash desaparece visualmente al instante
- [x] Puedes seguir usando BeatGaler mientras limpia
- [x] Limpieza física ocurre en background
- [x] Trabajo Rust lento fuera del hilo principal
- [x] Retry automático ante fallo transitorio
- [x] Batch delete
- [x] Topics pueden eliminarse concurrentemente
- [x] `TOPIC_ID_INVALID` se considera eliminado
- [x] Tombstones implementados

---

## 11. Anti-resurrección de beats

- [x] Permanent Delete crea entradas en `deleted[]`
- [x] Snapshot viejo no puede reintroducir beat purgado
- [x] ID eliminado queda tombstoned
- [x] Nombre puede reutilizarse con ID nuevo
- [x] Beat eliminado no vuelve después de restart

---

## 12. PROJECT — Persistencia

- [x] PROJECT guardado en Telegram
- [x] Manifest guardado
- [x] FLP persiste
- [x] ALS soportado
- [x] Indicador 📦 persiste después de restart
- [x] Open Project persiste
- [x] Open Project funciona después de restart
- [x] PROJECT se reconstruye desde Telegram Index

---

## 13. Add / Replace PROJECT

- [x] `.flp` detectado automáticamente
- [x] `.als` detectado automáticamente
- [x] `.logicx` detectado automáticamente
- [x] `.ptx` detectado automáticamente
- [x] `.ptf` detectado automáticamente
- [x] Project File no necesita `What are you adding?`
- [x] Si no existe PROJECT, se agrega directamente
- [x] Si existe Project File, aparece Replace / Cancel
- [x] Cancel funciona
- [x] Replace funciona
- [x] Play bloqueado durante update
- [x] Animación loading
- [x] Termina verde
- [x] Sonido de completado

---

## 14. PROJECT ZIP

- [x] ZIP se inspecciona automáticamente
- [x] ZIP válido requiere Project File
- [x] Project File puede estar dentro de subcarpetas
- [x] ZIP sin Project File se rechaza
- [x] Loading aparece mientras inspecciona
- [x] ZIP existente muestra Replace / Cancel
- [x] Validación puede leer índice del ZIP sin extraer todo

---

## 15. Backup / Backups

- [x] `Backup/` se ignora
- [x] `Backups/` se ignora
- [x] Funciona dentro de carpetas
- [x] Funciona dentro de ZIP
- [x] No se suben al PROJECT
- [x] Usuario recibe aviso
- [x] Backup no cancela un PROJECT válido
- [x] Si el único Project File está dentro de Backup, PROJECT es inválido

---

## 16. Simplificación de Add Files

- [x] MASTER MP3
- [x] WAV HQ
- [x] Add folder to Project
- [x] Loop → Coming Soon
- [x] Stems → Coming Soon
- [x] `Other` eliminado
- [x] Audio/Samples ya no son destinos separados
- [x] Carpetas conservan nombre original dentro de PROJECT

Ejemplo:

My Drums/  
├── kick.wav  
└── snare.wav  

queda:

PROJECT.zip  
└── My Drums/  
    ├── kick.wav  
    └── snare.wav

---

## 17. Samples

- [x] Samples forman parte de PROJECT ZIP/manifest
- [x] No necesitamos duplicar prueba de persistencia

---

## 18. Export MP3

- [x] Descarga MP3
- [x] Filename incluye BPM + Key
- [x] Metadata existente se preserva
- [x] Metadata BeatGaler se agrega como overlay
- [x] No destruye metadata existente innecesariamente

Ejemplo:

`Wild Deer [137 A].mp3`

---

## 19. Export WAV

- [x] Descarga WAV
- [x] Audio PCM permanece intacto
- [x] No recodifica/degrada WAV
- [x] Artwork permanece embebido
- [x] Metadata original preservada
- [x] Metadata del DAW preservada
- [x] BPM preservado/agregado
- [x] Key preservada/agregada
- [x] Tags preservados
- [x] Rating preservado/agregado
- [x] Chunks RIFF importantes preservados
- [x] Filename incluye BPM + Key

Ejemplo:

`Wild Deer [137 A].wav`

### Nota

- [x] Windows Explorer puede no mostrar thumbnail de artwork WAV aunque la imagen esté embebida
- [x] Esto no significa que BeatGaler perdió la portada

---

## 20. Download Everything

- [x] MP3
- [x] WAV
- [x] PROJECT ZIP
- [x] BPM + Key en filenames
- [x] Metadata preservada
- [x] PROJECT sin Backup/Backups
- [x] Segunda descarga no sobrescribe primera
- [x] Crea `Beat Name (1)` cuando corresponde
- [x] Download / Export cerrado

---

## 21. Cursor volumen

- [x] Slider no muestra I-beam
- [x] Solo inputs de texto reciben cursor de texto
- [x] Regression test agregado

---

## 22. Settings / Account

- [x] Settings completo
- [x] Account
- [x] Email
- [x] Password
- [x] MFA
- [x] Google OAuth
- [x] X OAuth
- [x] Username
- [x] Official username con X
- [x] Trash
- [x] Privacy Policy
- [x] Terms of Service
- [x] Tools / diagnostics

---




# ⏳ FALTA

## 23. Pérdida de Internet / Cloud

- [ ] Abrir BeatGaler conectado
- [ ] Cortar Internet
- [ ] Reproducir beat cacheado
- [ ] Intentar reproducir beat no cacheado
- [ ] Editar metadata offline
- [ ] Intentar importar offline
- [ ] Intentar upload offline
- [ ] Reconectar
- [ ] Confirmar que índice no se corrompe
- [ ] Confirmar que no se pierden cambios
- [ ] Definir operaciones que quedan pendientes
- [ ] Definir operaciones que fallan inmediatamente
- [ ] UX clara para Offline / Reconnecting

---

## 24. Stress Test biblioteca grande

- [ ] 6 beats
- [ ] 20 beats
- [ ] 50+ beats
- [ ] 100+ beats después

Medir:

- [ ] tiempo hasta primeros 6
- [ ] startup total
- [ ] CPU
- [ ] RAM
- [ ] red
- [ ] primer Play
- [ ] Play de beat progresivo
- [ ] scroll
- [ ] artwork decoding
- [ ] uploads simultáneos

---

## 25. Startup con fallos parciales

- [ ] Artwork inaccesible en uno de primeros 6
- [ ] MASTER inaccesible en uno de primeros 6
- [ ] Los demás beats deben continuar
- [ ] Error visible sin congelar startup

---

## 26. `AUDIO_ENGINE_PRIME_ERROR` ocasional

- [ ] Investigar primer intento fallido
- [ ] Reducir cientos de ms perdidos
- [ ] Probar con biblioteca grande

Actualmente reintenta y funciona.

---

## 27. Playback Cache / LRU

Ya existe:

- [x] Límite configurable
- [x] Consultar uso
- [x] Limpiar cache
- [x] Default aproximado 2 GB

Falta:

- [ ] Verificar eviction bounded
- [ ] Verificar comportamiento LRU real
- [ ] Superar límite con muchos beats
- [ ] Ver qué archivos elimina
- [ ] No eliminar beat reproduciéndose
- [ ] Confirmar cache no crece indefinidamente

---

# FEATURES DIFERIDAS

## 28. Auto Save / cambios PROJECT

Open Project  
→ modificar en DAW  
→ Save  
→ BeatGaler detecta cambios  
→ subir solamente lo modificado

Pendiente:

- [ ] Detectar FLP modificado
- [ ] Detectar ALS modificado
- [ ] Detectar Logic project modificado
- [ ] Detectar Pro Tools project modificado
- [ ] Detectar nuevas carpetas
- [ ] Detectar Samples nuevos/eliminados
- [ ] Detectar Audio modificado
- [ ] Subir solo cambios
- [ ] Actualizar PROJECT ZIP
- [ ] Actualizar manifest
- [ ] Actualizar Telegram Index
- [ ] Animación/background durante Save

---

## 29. Stems

- [ ] Implementar Stems
- [x] Actualmente `Coming Soon`

---

## 30. Loops

- [ ] Implementar Loops
- [x] Actualmente `Coming Soon`

---

# PUBLIC RELEASE

## 31. Legal

- [ ] Revisar Privacy Policy final
- [ ] Revisar Terms of Service final
- [ ] Buscar placeholders
- [ ] Eliminar `[Developer or company name]` si todavía existe

---

## 32. Dev Tools

- [ ] Decidir qué Tools aparecen en build público
- [ ] Ocultar/eliminar `DEVELOPMENT ONLY`

---

## 33. Limpieza del repositorio

- [ ] Revisar backups accidentales
- [ ] Revisar archivos `.backup`
- [ ] Revisar scripts temporales
- [ ] Revisar carpetas duplicadas
- [ ] Eliminar tooling antiguo

---

## 34. Seguridad antes de publicar

- [ ] Buscar secrets
- [ ] Buscar tokens Telegram
- [ ] Buscar API hashes
- [ ] Buscar session strings
- [ ] Confirmar `.env` ignorado
- [ ] Confirmar logs sin secretos
- [ ] Confirmar installer sin credenciales personales

---

## 35. Build final Windows

Correr:

`npm run test:regressions`

`npm run version:check`

`npm run build`

`cargo check`

`npm run tauri build`

Después:

- [ ] Todo limpio
- [ ] Installer generado
- [ ] Installer probado

---

## 36. Build final macOS

- [ ] CI completo
- [ ] DMG
- [ ] Probar instalación
- [ ] Signing/quarantine final

---

## 37. Máquina limpia

- [ ] PC sin Node
- [ ] PC sin Rust
- [ ] PC sin repo
- [ ] PC sin variables dev
- [ ] Instalar BeatGaler
- [ ] Login
- [ ] Restaurar biblioteca desde Telegram
- [ ] Play
- [ ] Import
- [ ] PROJECT
- [ ] Download
- [ ] Trash
- [ ] Restart

---

# REGLAS DEL PROYECTO

## 38. No trabajar en círculos

- [x] Una fuente de verdad por subsistema
- [x] Un dueño por pipeline
- [x] Bug arreglado → Regression Test
- [x] No tocar subsistemas ajenos sin necesidad
- [x] Modularizar progresivamente
- [x] No hacer mega-refactor innecesario
- [x] No convertir modularidad en microservicios innecesarios
- [x] Antes de arreglar bug → reproducirlo
- [x] Si una feature funciona → no tocarla sin razón
- [x] Usar siempre código más reciente
- [x] Después de muchos patches → crear/pedir ZIP completo nuevo

---

# ORDEN RECOMENDADO DESDE AHORA

- [ ] 1. Offline / pérdida de red / reconexión
- [ ] 2. Stress Test con 20–50 beats
- [ ] 3. Playback Cache / LRU
- [ ] 4. Startup con fallos parciales
- [ ] 5. Investigar `AUDIO_ENGINE_PRIME_ERROR`
- [ ] 6. Limpieza pre-release
- [ ] 7. Security / secrets audit
- [ ] 8. Build limpio Windows
- [ ] 9. Build limpio macOS
- [ ] 10. Instalación en máquina limpia
- [ ] 11. Después: Auto Save / cambios PROJECT
- [ ] 12. Después: Stems / Loops