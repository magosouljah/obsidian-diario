# Beat Galer — Checklist antes del lanzamiento — Estado actual

## Progreso general de testing

**≈ 85% completado**
**≈ 15% pendiente**

---

## Prioridad 0 — No publicar si esto falla

- [x] Cero pérdida de beats o metadata — cubierto en gran parte por integration, tombstones, serialized commits y recovery
- [x] Índice confiable
- [x] Recuperación del índice si el local se corrompe
- [x] Operaciones atómicas / commits serializados
- [ ] Backups del índice — falta validación final específica
- [x] Detección de inconsistencias — parcialmente automatizada
- [ ] Errores claros y visibles — falta validación UX/manual completa

**Estado P0: mayormente completo, todavía no cerrado 100%.**

---

## Prioridad 1 — Flujo principal

- [x] Importar MP3
- [x] Importar WAV
- [x] Convertir WAV → MP3 automáticamente
- [x] Guardar WAV original como HQ
- [x] Importar proyectos / validar PROJECT ZIP
- [x] Importar samples / carpetas correctamente
- [x] Samples / Stems / Backup / Audio NO aparecen como beats independientes
- [x] Reconocer correctamente MASTER / HQ / PROJECT / Samples
- [x] Múltiples carpetas Desktop
- [x] MP3-only no absorbe archivos vecinos
- [x] Agregar WAV después a un beat existente
- [x] Reemplazar WAV sin duplicarlo
- [x] Agregar PROJECT después a un beat existente
- [x] Reemplazar PROJECT sin duplicarlo
- [x] Agregar Samples después a un beat existente
- [x] Backup sigue excluido en updates
- [ ] Eliminar archivos individuales — falta sweep final
- [x] Editar nombre, BPM, key, tags y metadata
- [x] Pinterest / external artwork aislado correctamente del import
- [ ] Cambiar artwork — falta journey final completo sobre app real
- [ ] Upload cloud real completo de todos los tipos — falta validación final
- [x] Actualizar índice — integración cubierta
- [x] Reflejar cambios inmediatamente en UI en los flows probados

Además:

- [x] Phase 9A — Import Core
- [x] Phase 9B — Native Drop Contracts
- [x] Phase 9C — Existing Beat Slot Updates
- [x] Phase 9D — Pinterest / External Artwork
- [x] Phase 9E — Desktop Import E2E
- [x] Phase 9 — Critical Import Flows ✅

**Estado P1: muy avanzado. El bloque crítico de Import está CERRADO ✅**

---

## Prioridad 2 — Reproducción

- [x] Play / Pause confiable
- [ ] Seek — falta validación final
- [ ] Siguiente / anterior — falta validación final
- [ ] Volumen — falta validación final
- [x] Streaming / playback readiness
- [x] Arquitectura para reproducir antes de terminar descarga
- [ ] Validación real final de reproducción antes de descarga completa
- [x] Caché local de MP3 recientes
- [x] Prefetch inteligente
- [x] No descargar toda la biblioteca al iniciar
- [x] Limitar descargas en segundo plano — parcialmente cubierto

Además:

- [x] 8B.3 Playback E2E

**Estado P2: bastante avanzado; falta sweep funcional final.**

---

## Prioridad 3 — Descargas y exportación

- [x] Descargar MP3 — lógica existente
- [x] Descargar WAV — lógica existente
- [ ] Descargar PROJECT — prueba completa pendiente
- [x] Exportar beat completo — lógica de export probada
- [x] Reconstruir estructura de carpetas — parcialmente cubierta
- [ ] Incluir Samples / Stems correctamente en export real
- [ ] Mostrar progreso completo
- [ ] Cancelar descargas
- [ ] Reintentar descargas fallidas
- [ ] Verificar integridad del archivo descargado
- [ ] PROJECT inexistente localmente → descargar
- [ ] Extraer PROJECT automáticamente
- [ ] Abrir PROJECT cuando esté listo
- [ ] Validar PROJECT lifecycle completo

**Estado P3: SIGUIENTE BLOQUE PRINCIPAL.**

---

## Prioridad 4 — Uploads

- [x] Cola de uploads
- [x] Progreso por archivo
- [x] Reintentos automáticos
- [ ] Pausar / reanudar cuando sea posible
- [x] Uploads sin congelar UI
- [x] Manejar pérdida de conexión
- [x] Evitar duplicados al reintentar — parcialmente cubierto
- [x] Actualizar índice correctamente
- [x] Estados básicos de upload
- [ ] Upload real bajo condiciones adversas
- [ ] Cerrar app durante upload real
- [ ] Backend devuelve error durante upload real

**Estado P4: avanzado; falta stress / real-world.**

---

## Prioridad 5 — Rendimiento y caché

- [x] Cachear artworks
- [x] Metadata disponible rápidamente
- [x] Cachear MP3 recientes
- [x] Lazy loading — parcial
- [ ] Virtualización para bibliotecas grandes
- [x] No bloquear UI con FFmpeg
- [x] No bloquear UI con operaciones de archivos
- [x] Skeletons
- [x] Precarga inteligente
- [x] Arquitectura shallow-first de Review Beat
- [x] Streaming discovery de imports
- [ ] Validar nuevamente Review Beat con imports reales grandes
- [ ] Importar 100 beats y medir
- [ ] Biblioteca grande / 1000+ archivos

**Estado P5: avanzado, performance/stress real pendiente.**

---

## Prioridad 6 — Automatización del flujo de trabajo

Aplazada para versión posterior.

**Estado: fuera del bloqueo de 1.0.**

---

## Prioridad 7 — Biblioteca

- [x] Búsqueda
- [x] Filtro por BPM
- [x] Filtro por Key
- [x] Filtro por tags
- [x] Filtro por fecha — falta validar exhaustivamente
- [x] Filtro por archivos disponibles — parcialmente validado
- [x] Ordenamiento
- [x] Multi-selección
- [ ] Todas las acciones en lote
- [x] Detección de duplicados
- [x] Indicador de beats incompletos
- [ ] Sweep final del indicador incompleto

**Estado P7: avanzado.**

---

## Prioridad 8 — Papelera

- [x] Trash
- [x] Restaurar beat
- [x] Vaciar papelera
- [x] Confirmación / bloqueo según estado
- [x] Manejo de eliminación del almacenamiento
- [x] Tombstones / prevención de referencias huérfanas
- [x] 8B.5 Trash E2E

**Estado P8: CERRADO ✅**

---

## Prioridad 9 — Estado interno de sincronización

- [x] Estado local
- [x] Estados de upload
- [x] Synced
- [x] Updates pendientes
- [x] Error
- [x] Downloading
- [x] Offline available
- [x] Estados independientes entre sync / download / playback / offline

No necesariamente todos utilizan esos nombres exactos, pero la máquina de estados equivalente existe y está probada.

**Estado P9: CERRADO prácticamente ✅**

---

## Prioridad 10 — Offline y conectividad

- [x] Detectar ausencia de internet
- [x] Evitar errores repetitivos
- [x] Reproducir archivos cacheados offline
- [x] Guardar operaciones pendientes
- [x] Sincronizar cuando vuelve internet
- [x] Resolver / reconciliar operaciones pendientes
- [x] Trash offline / reconnect
- [x] 8B.4 Offline / Reconnect E2E
- [ ] Prueba real cortando físicamente la conexión

**Estado P10: CERRADO automatizadamente ✅**

---

## Prioridad 11 — Conflictos

- [ ] Dos computadoras modificando el mismo beat
- [ ] Determinar versión más reciente
- [ ] Merge cuando sea posible
- [ ] Preguntar al usuario cuando corresponda
- [ ] Evitar overwrite de datos nuevos
- [ ] Protección contra cliente stale

**Estado P11: pendiente.**

---

## Prioridad 12 — Integración con FL Studio / PROJECT

- [x] Detectar / manejar `.flp`
- [x] Detectar PROJECT dentro de carpetas
- [x] Detectar PROJECT ZIP
- [x] Validar ZIP
- [x] Ignorar Backup dentro de PROJECT
- [ ] Abrir `.flp` desde Beat Galer
- [ ] Descargar PROJECT si no existe localmente
- [ ] Descomprimir automáticamente — falta E2E completo
- [ ] Abrir cuando esté listo
- [ ] Manejar proyectos con Samples
- [ ] Lifecycle completo Download → Extract → Open

**Estado P12: parcial; entra en el siguiente bloque de testing.**

---

## Prioridad 13 — Procesamiento local

- [x] FFmpeg empaquetado
- [x] WAV → MP3 implementado
- [x] WAV-only → MASTER MP3 probado en Import E2E
- [x] WAV original → HQ probado
- [x] Procesamiento en background
- [ ] Cancelar procesamiento
- [x] No congelar React — diseño actual
- [x] Limpiar temporales — parcialmente
- [ ] Manejar WAV enorme
- [ ] Manejar fallo de FFmpeg real

**Estado P13: avanzado, no cerrado.**

---

## Prioridad 14 — Cuentas

- [x] Registro
- [x] Login
- [x] Logout
- [ ] Recuperar contraseña — falta validación final
- [x] Sesión persistente
- [x] Cerrar sesiones
- [x] Separar datos entre usuarios
- [x] Proteger librerías
- [x] Tokens manejados fuera de UI
- [x] No guardar contraseñas directamente
- [ ] Revisión final auth/security

**Estado P14: avanzado.**

---

## Prioridad 15 — Seguridad

- [x] No exponer implementación interna / tokens en frontend
- [x] No guardar secretos en JavaScript distribuido
- [x] Validar acciones sensibles backend / Rust
- [x] Sanitizar nombres de archivos
- [x] Sanitizar rutas
- [x] Path traversal / ZIP Slip protegido
- [x] Validar archivos recibidos
- [ ] Auditoría completa de endpoints
- [ ] Rate limiting donde corresponda
- [ ] Auditoría final de logs para cero secretos
- [x] Security fuzz: 5000 casos adversariales
- [x] Malformed images
- [x] URL schemes peligrosos
- [x] Windows reserved names
- [x] BPM / Key fuzz / idempotence
- [x] Pinterest/browser payload aislado de import local

**Estado P15: muy avanzado; falta auditoría final.**

---

## Prioridad 16 — Actualizaciones

- [ ] Auto-updater
- [ ] Detectar versión nueva
- [ ] Descargar actualización
- [ ] Instalar seguramente
- [ ] No destruir biblioteca
- [ ] Mantener compatibilidad
- [ ] Migrar automáticamente

**Estado P16: pendiente importante.**

---

## Prioridad 17 — Migraciones

- [x] Versionado de schema existe
- [ ] Migraciones completas
- [ ] Suite automatizada de migraciones
- [ ] Upgrade desde schema/versiones antiguas
- [ ] Recuperarse de migración fallida
- [ ] Evitar pérdida de biblioteca durante migration

**Estado P17: pendiente importante.**

---

## Prioridad 18 — Logs y diagnóstico

- [x] Logs locales
- [x] Timestamps
- [x] Registrar eventos importantes
- [x] Registrar versión
- [ ] Exportar diagnóstico
- [ ] Logs suficientemente amigables
- [ ] Auditoría final para asegurar cero secretos

**Estado P18: parcial.**

---

## Prioridad 19 — Pruebas de estrés y errores

### Ya cubierto automáticamente

- [x] Caracteres especiales
- [x] Windows reserved names
- [x] Entradas malformadas
- [x] 5000 casos de fuzz adversarial
- [x] ZIP malicioso / path traversal
- [x] Recovery de queue
- [x] Offline / reconnect controlado
- [x] Trash offline / online
- [x] Import discovery determinista
- [x] Múltiples carpetas de import
- [x] Exclusión de Samples / Stems / Backup / Audio
- [x] Native drop contracts
- [x] Pinterest isolation

### Pendiente stress real

- [ ] Internet cortado durante upload real
- [ ] Cerrar Beat Galer durante upload real
- [ ] Backend/cloud responde error real
- [ ] WAV enorme
- [ ] Importar 100 beats
- [ ] Importar 1,000 archivos
- [ ] Archivo corrupto real
- [ ] Artwork enorme
- [ ] Disco lleno
- [ ] Reinicio durante operación
- [ ] Crash durante operación
- [ ] Actualización desde versión anterior

**Estado P19: seguridad/fuzz avanzado; stress real pendiente.**

---

## Prioridad 20 — UX mínima

- [x] Loading states
- [x] Errores básicos
- [x] Confirmaciones destructivas
- [x] Progress
- [x] Deshabilitar botones según estado
- [x] Tooltips
- [x] Empty state
- [x] Indicador offline
- [x] Indicadores de sincronización
- [x] Protección frente a varias ejecuciones — parcialmente cubierta
- [ ] Pasada visual completa
- [ ] Mensajes de error finales
- [ ] Comprobar todos los estados raros manualmente

**Estado P20: avanzado; evaluación visual/manual al final.**

---

## Prioridad 21 — Instalador

- [x] Instalador existente
- [x] Icono
- [x] Nombre
- [x] Versionado centralizado
- [x] Desinstalador / packaging Tauri
- [x] Rutas principales
- [ ] Validar permisos mínimos
- [ ] Instalación limpia real
- [ ] Upgrade sobre instalación existente
- [ ] Verificar que upgrade no toca la biblioteca

**Estado P21: falta release testing real.**

---

## Prioridad 22 — Primera ejecución

- [ ] Validar onboarding completo
- [ ] Primera configuración
- [ ] Elegir carpeta local
- [x] Importar primer beat — flujo de Import ya probado
- [ ] Primer import dentro del onboarding real
- [ ] Llegar a Play rápidamente
- [x] Filosofía de evitar tutorial largo

**Estado P22: pendiente de manual/E2E final.**

---

# Las 10 condiciones obligatorias — Estado actualizado

- [ ] **1. Beat Galer no pierde datos**
  - Muy avanzado.
  - Falta recovery/crash/stress final.

- [x] **2. Importar funciona correctamente**
  - Phase 9 completa.
  - MP3, WAV, folder, múltiples folders y Review cubiertos.

- [x] **3. Cloud sincroniza correctamente**
  - Muy avanzado / integración cubierta.

- [x] **4. MP3 reproduce correctamente**
  - Playback E2E pasó.

- [x] **5. WAV / PROJECT / Samples quedan en sus slots correctos**
  - Cubierto por Phase 9A–9E.

- [x] **6. Editar un beat no rompe el índice**
  - Edit Metadata E2E + Integration.

- [ ] **7. Descargar y exportar funcionan**
  - Siguiente bloque principal.

- [x] **8. Una falla de internet no destruye nada**
  - Offline / Reconnect E2E pasó.

- [ ] **9. La app se recupera correctamente después de cerrarse**
  - Integration cubierta.
  - Falta crash/restart real.

- [ ] **10. Una actualización futura no destruye bibliotecas existentes**
  - Updater + migrations pendientes.

---

# Testing completado hasta ahora

- [x] Phase 1 — Unit Core
- [x] Phase 2 — Drag & Drop + PROJECT ZIP
- [x] Phase 3 — Index / Tombstones + Cache / LRU
- [x] Phase 4 — Export + Procedural + Plans / Direct
- [x] Phase 5 — Security + Fuzz
- [x] Phase 6A — Component Contracts
- [x] Phase 6B — Real DOM
- [x] Phase 7 — Integration
- [x] Phase 8A — Desktop Smoke E2E
- [x] Phase 8B.1 — Controlled Backend
- [x] Phase 8B.2 — Edit Metadata
- [x] Phase 8B.3 — Playback
- [x] Phase 8B.4 — Offline / Reconnect
- [x] Phase 8B.5 — Trash
- [x] Phase 9A — Import Core
- [x] Phase 9B — Native Drop Contracts
- [x] Phase 9C — Existing Beat Slot Updates
- [x] Phase 9D — Pinterest / External Artwork
- [x] Phase 9E — Desktop Import E2E
- [x] Phase 9 — Critical Import Flows ✅
- [x] `npm run check`
- [x] Production build

---

# Phase 9 — Critical Import Flows — CERRADA ✅

- [x] Native local file drop
- [x] Native local folder drop
- [x] Local imports nunca usan `HTML_FALLBACK_STAGING_START`
- [x] Pinterest drag & drop aislado del import local
- [x] Múltiples carpetas en Desktop
- [x] Samples no se detectan como beats separados
- [x] Stems no se detectan como beats separados
- [x] Audio no se detecta como beat separado
- [x] Ignorar `Backup`
- [x] Ignorar `Backups`
- [x] MP3-only no importa archivos vecinos
- [x] WAV-only genera MASTER MP3
- [x] WAV original queda como HQ
- [x] MP3 + WAV matching forman un solo beat
- [x] Agregar WAV posteriormente
- [x] Reemplazar WAV sin duplicar
- [x] Agregar PROJECT posteriormente
- [x] Reemplazar PROJECT sin duplicar
- [x] Agregar Samples posteriormente
- [x] Backup continúa excluido al actualizar PROJECT
- [x] Pinterest nunca crea un beat
- [x] E2E final de Import: 2/2 passing

---

# Siguiente bloque

## Phase 10 — Downloads + PROJECT Lifecycle

### Downloads

- [ ] Descargar MASTER MP3
- [ ] Descargar HQ WAV
- [ ] Descargar PROJECT
- [ ] Descargar Samples / PROJECT completo
- [ ] Progreso de descarga
- [ ] Retry
- [ ] Cancel
- [ ] Validar integridad
- [ ] Manejar descarga interrumpida
- [ ] Evitar archivos parciales/corruptos

### Export

- [ ] Export MP3 real
- [ ] Export WAV real
- [ ] Export Full Project real
- [ ] Export Everything real
- [ ] Reconstruir estructura esperada
- [ ] Mantener Samples
- [ ] Mantener PROJECT
- [ ] Mantener metadata relevante
- [ ] Evitar overwrite accidental
- [ ] Nombres Windows seguros

### PROJECT lifecycle

- [ ] PROJECT no existe localmente
- [ ] Click Open Project
- [ ] Descargar PROJECT
- [ ] Mostrar loading/progreso
- [ ] Verificar ZIP
- [ ] Extraer de forma segura
- [ ] Excluir Backup
- [ ] Localizar `.flp` / proyecto compatible
- [ ] Abrir proyecto
- [ ] Reutilizar proyecto ya descargado
- [ ] Recuperarse de descarga fallida
- [ ] Recuperarse de ZIP corrupto
- [ ] Limpiar temporales correctamente

---

# Bloques principales pendientes antes del release

1. **Phase 10 — Downloads / PROJECT lifecycle**
2. **Stress + recovery / corruption**
3. **Updater + migraciones**
4. **Release / installer / upgrade testing**
5. **Pasada manual final de UX + performance**

---

# Después de llegar al 100% de tests

1. Corregir cualquier bug real descubierto por la batería completa.
2. Hacer la pasada manual final de UX y performance.
3. Cerrar updater + migraciones.
4. Validar instalación limpia.
5. Validar actualización desde una versión anterior.
6. Preparar Release Candidate.
7. Generar builds finales Windows / macOS.
8. Firma de código donde corresponda.
9. Publicar Beat Galer.

---

# Regla principal de Beat Galer 1.0

**Beat Galer 1.0 no necesita hacer cien cosas.**

Necesita hacer sus funciones principales de forma extremadamente confiable.

Lo peor que puede hacer Beat Galer no es verse feo.

**Lo peor que puede hacer es perderle un beat al usuario.**