
# Beat Galer — Checklist antes del lanzamiento

## Prioridad 0 — No publicar si esto falla

- [ ] Cero pérdida de beats o metadata
- [ ] Índice de Telegram confiable
- [ ] Recuperación del índice si el local se corrompe
- [ ] Operaciones atómicas
- [ ] Backups del índice
- [ ] Detección de inconsistencias
- [ ] Errores claros y visibles

---

## Prioridad 1 — Flujo principal

- [ ] Importar MP3
- [ ] Importar WAV
- [ ] Convertir WAV → MP3 automáticamente
- [ ] Guardar WAV original como HQ
- [ ] Importar proyectos FL Studio
- [ ] Importar samples / stems / carpetas
- [ ] Reconocer correctamente cada slot
- [ ] Agregar archivos después a un beat existente
- [ ] Reemplazar archivos sin duplicados
- [ ] Eliminar archivos individuales
- [ ] Editar nombre, BPM, key, tags y metadata
- [ ] Cambiar artwork
- [ ] Guardar correctamente en Telegram
- [ ] Actualizar el índice
- [ ] Reflejar cambios inmediatamente en la UI

---

## Prioridad 2 — Reproducción

- [ ] Play / Pause confiable
- [ ] Seek
- [ ] Siguiente / anterior
- [ ] Volumen
- [ ] Streaming progresivo
- [ ] Reproducir antes de terminar la descarga
- [ ] Caché local de MP3 recientes
- [ ] Prefetch inteligente
- [ ] No descargar toda la biblioteca al iniciar
- [ ] Limitar descargas en segundo plano

> [!goal]
> El objetivo es que presionar **Play** se sienta prácticamente instantáneo.

---

## Prioridad 3 — Descargas y exportación

- [ ] Descargar MP3
- [ ] Descargar WAV
- [ ] Descargar proyecto
- [ ] Exportar beat completo
- [ ] Reconstruir estructura de carpetas
- [ ] Incluir samples / stems
- [ ] Mostrar progreso
- [ ] Cancelar descargas
- [ ] Reintentar descargas fallidas
- [ ] Verificar integridad del archivo descargado

---

## Prioridad 4 — Uploads a Telegram

- [ ] Cola de uploads
- [ ] Progreso por archivo
- [ ] Reintentos automáticos
- [ ] Pausar / reanudar cuando sea posible
- [ ] Uploads sin congelar la UI
- [ ] Manejar pérdida de conexión
- [ ] Evitar duplicados al reintentar
- [ ] Actualizar índice correctamente
- [ ] Estados:
  - [ ] Pendiente
  - [ ] Subiendo
  - [ ] Terminado
  - [ ] Error

---

## Prioridad 5 — Rendimiento y caché

- [ ] Cachear artworks
- [ ] Metadata disponible inmediatamente
- [ ] Cachear MP3 recientes
- [ ] Lazy loading
- [ ] Virtualización para bibliotecas grandes
- [ ] No bloquear UI con FFmpeg
- [ ] No bloquear UI con operaciones de archivos
- [ ] Skeletons donde sean necesarios
- [ ] Precarga inteligente

> [!important]
> Beat Galer debería seguir sintiéndose rápido incluso con miles de beats.

---

## ~~Prioridad 6 — Automatización del flujo de trabajo~~

- [ ] Monitorear carpetas seleccionadas
- [ ] Usar eventos del sistema operativo
- [ ] No escanear constantemente
- [ ] Detectar WAV recién exportado
- [ ] Detectar mp3 recién exportado
- [ ] Detectar cambios en FLP
- [ ] Relacionar archivo nuevo con el beat correcto
- [ ] Preguntar antes de reemplazar:
  - `Se detectó una nueva versión. ¿Actualizar?`
- [ ] Poder apagar el monitoreo
- [ ] Mantener consumo de CPU mínimo

> [!note]
> Esta función puede esperar a una versión posterior si necesitas lanzar rápido.

---

## Prioridad 7 — Biblioteca

- [ ] Búsqueda
- [ ] Filtro por BPM
- [ ] Filtro por Key
- [ ] Filtro por tags
- [ ] Filtro por fecha
- [ ] Filtro por archivos disponibles
- [ ] Ordenamiento
- [ ] Multi-selección
- [ ] Acciones en lote
- [ ] Detección de duplicados
- [ ] Indicador de beats incompletos

---

## Prioridad 8 — Papelera

- [ ] Trash
- [ ] Restaurar beat
- [ ] Vaciar papelera
- [ ] Confirmación antes de eliminar permanentemente
- [ ] Definir qué pasa con archivos de Telegram
- [ ] Evitar referencias huérfanas

---

## Prioridad 9 — Estado interno de sincronización

Cada beat debería poder tener estados internos como:

- `local`
- `pending_upload`
- `uploading`
- `synced`
- `pending_update`
- `error`
- `downloading`
- `offline_available`

El usuario no necesariamente tiene que ver todos estos estados.

Beat Galer sí debe conocerlos.

---

## Prioridad 10 — Offline y conectividad

- [ ] Detectar ausencia de internet
- [ ] Evitar errores repetitivos
- [ ] Reproducir archivos cacheados offline
- [ ] Guardar operaciones pendientes
- [ ] Sincronizar cuando vuelva internet
- [ ] Resolver cambios hechos mientras estaba offline

---

## Prioridad 11 — Conflictos

Caso:

> El mismo beat cambia desde dos computadoras.

Beat Galer debe saber:

- [ ] Qué versión es más reciente
- [ ] Si los cambios pueden fusionarse
- [ ] Cuándo preguntarle al usuario
- [ ] Evitar que información vieja sobrescriba información nueva

---

## Prioridad 12 — Integración con FL Studio

- [ ] Detectar FL Studio
- [ ] Abrir `.flp` desde Beat Galer
- [ ] Descargar proyecto si no existe localmente
- [ ] Descomprimir automáticamente
- [ ] Abrir cuando esté listo
- [ ] Manejar proyectos con samples

---

## Prioridad 13 — Procesamiento local

- [ ] FFmpeg correctamente empaquetado
- [ ] WAV → MP3 confiable
- [ ] Procesamiento en background
- [ ] Cancelar procesamiento
- [ ] No congelar React
- [ ] Limpiar archivos temporales
- [ ] Manejar archivos grandes

---

## Prioridad 14 — Cuentas

- [ ] Registro
- [ ] Login
- [ ] Logout
- [ ] Recuperar contraseña
- [ ] Sesión persistente
- [ ] Cerrar sesiones
- [ ] Separar datos entre usuarios
- [ ] Proteger librerías de otros usuarios
- [ ] Manejar tokens de forma segura
- [ ] Nunca guardar contraseñas directamente

---

## Prioridad 15 — Seguridad

- [ ] No exponer token de Telegram en frontend
- [ ] No guardar secretos dentro del JavaScript distribuido
- [ ] Validar acciones sensibles en backend / Rust
- [ ] Sanitizar nombres de archivos
- [ ] Sanitizar rutas
- [ ] Evitar path traversal
- [ ] Validar archivos recibidos
- [ ] Proteger endpoints
- [ ] Rate limiting cuando corresponda
- [ ] No guardar secretos en logs

> [!danger]
> Seguridad sí es requisito de lanzamiento si Beat Galer será usado por otras personas.

---

## Prioridad 16 — Actualizaciones

- [ ] Auto-updater
- [ ] Detectar versión nueva
- [ ] Descargar actualización
- [ ] Instalar de forma segura
- [ ] No destruir biblioteca
- [ ] Migrar datos automáticamente

---

## Prioridad 17 — Migraciones

Ejemplo:

Antes:

```json
{
  "name": "...",
  "mp3": "...",
  "wav": "..."
}
Después:

```json
{
  "name": "...",
  "mp3": "...",
  "wav": "...",
  "status": "...",
  "notes": "...",
  "projectVersion": 2
}
```

Necesitas:

- [ ] Versionar el esquema
- [ ] Crear migraciones
- [ ] Probar migraciones
- [ ] Recuperarse de una migración fallida

---

## Prioridad 18 — Logs y diagnóstico

- [ ] Logs locales
- [ ] Timestamps
- [ ] Registrar eventos importantes
- [ ] Registrar versión de Beat Galer
- [ ] Exportar diagnóstico
- [ ] Logs fáciles de leer
- [ ] Nunca incluir secretos

---

## Prioridad 19 — Pruebas de estrés y errores

Probar:

- [ ] Internet se corta durante upload  
- [ ] Cerrar Beat Galer durante upload
- [ ] Telegram responde con error
- [ ] WAV enorme
- [ ] Importar 100 beats
- [ ] Importar 1,000 archivos
- [ ] Emojis en nombres
- [ ] Nombres extremadamente largos
- [ ] Caracteres especiales
- [ ] Archivos con mismo nombre
- [ ] Archivo corrupto
- [ ] Artwork enorme
- [ ] Proyecto sin samples
- [ ] MP3 faltante
- [ ] Índice local eliminado
- [ ] Índice desactualizado
- [ ] Sin internet
- [ ] Disco lleno
- [ ] Reinicio durante operación
- [ ] Actualización desde versión anterior

---

## Prioridad 20 — UX mínima
- [ ] Loading states claros
- [ ] Errores claros
- [ ] Confirmaciones para acciones destructivas
- [ ] Progress bars reales
- [ ]  Deshabilitar botones cuando corresponda
- [ ] Tooltips
- [ ] Estado de biblioteca vacía
- [ ] Indicador offline
- [ ] Indicador de sincronización
- [ ] Evitar doble ejecución de acciones

---

## Prioridad 21 — Instalador
- [ ] Instalador limpio
- [ ] Icono final
- [ ] Nombre definitivo
- [ ] Versión correcta
- [ ] Desinstalador
- [ ] Rutas correctas
- [ ]  Evitar permisos de administrador innecesarios
- [ ] Probar instalación limpia
- [ ] Probar actualización sobre una instalación existente 

---

## Prioridad 22 — Primera ejecución
- [ ] Que el usuario entienda qué hacer
- [ ] Configurar Telegram si aplica
- [ ] Elegir carpeta local
- [ ] Importar primer beat fácilmente
- [ ] Llegar a reproducción rápidamente
- [ ] Evitar tutoriales largos e innecesarios

---

# Versión 1.1+

Estas funciones son buenas, pero no deberían impedir publicar la 1.0.
	
- [ ] Historial de versiones
- [ ] Links públicos
- [ ] Colaboración
- [ ] Librerías compartidas
- [ ] Estadísticas
- [ ] API
- [ ] Plugins
- [ ] Web app
- [ ] Multi-dispositivo avanzado
- [ ] Más DAWs
- [ ] IA
- [ ] Recomendaciones
- [ ] Dashboard  

---

# 🚀 Si tengo que lanzar esta semana

## Las 10 condiciones obligatorias

-  **1. Beat Galer no pierde datos**
    
-  **2. Importar funciona correctamente**
    
-  **3. Telegram sincroniza correctamente**
    
-  **4. MP3 reproduce correctamente**
    
-  **5. WAV / FLP / Samples quedan en sus slots correctos**
    
-  **6. Editar un beat no rompe el índice**
    
-  **7. Descargar y exportar funcionan**
    
-  **8. Una falla de internet no destruye nada**
    
-  **9. La app se recupera correctamente después de cerrarse**
    
-  **10. Una actualización futura no destruye bibliotecas existentes**
    

---

# Regla principal de Beat Galer 1.0

> [!success]  
> **La versión 1.0 no necesita hacer cien cosas.**
> 
> Necesita hacer sus funciones principales de forma extremadamente confiable.
> 
> Lo peor que puede hacer Beat Galer no es verse feo.
> 
> Lo peor que puede hacer es perderle un beat al usuario.