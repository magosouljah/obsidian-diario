Fase 7 — Funciones exclusivas de Desktop  
Estas funciones deben ocultarse mediante capacidades:  
Abrir proyectos en FL Studio o Ableton.  
Reveal in Explorer/Finder.  
Monitorear carpetas.  
Acceso libre al filesystem.  
Actualizador nativo.  
Drag & drop nativo WRY.  
Configuración de carpetas locales.  
Helper local.  
Caché nativa.  
No deben eliminarse del código Desktop.  
Fase 8 — Offline Web  
Decidir si se soportará.  
Si se implementa:  
PWA.  
IndexedDB o Cache Storage.  
Límites de almacenamiento del navegador.  
Available Offline.  
Remove Offline.  
Recuperación al reconectar.  
Resolución de conflictos.  
No debe reutilizarse directamente el sistema offline de Desktop.  
Fase 9 — Seguridad y cuotas  
Antes de producción:  
Validar todos los permisos en servidor.  
Aplicar límites según plan.  
Límite máximo de beats.  
Límite de PROJECT.  
Dispositivos activos.  
Sesiones simultáneas.  
Rate limits.  
Protección contra operaciones duplicadas.  
Expiración de sesiones.  
Revisar revoke y rotación.  
Sanitizar completamente errores visibles.  
Nunca mostrar la implementación interna de Galer Cloud.  
Fase 10 — Responsive y navegadores  
Probar y adaptar:  
Chrome.  
Safari.  
Firefox.  
iPhone.  
iPad.  
Pantallas pequeñas.  
Touch.  
Drag & drop.  
Selector de archivos.  
Reproductor.  
Modales.  
Settings.  
Fase 11 — Rendimiento  
Optimizar:  
Inicio rápido.  
Biblioteca progresiva.  
Portadas lazy.  
Reproducción inmediata.  
Upload reanudable si es necesario.  
Memoria controlada con archivos grandes.  
Cancelación.  
Recuperación después de perder internet.  
Fase 12 — Publicación  
Finalmente:  
Hosting Web.  
Dominio.  
HTTPS.  
Galer Cloud en VPS.  
Logs.  
Métricas.  
Backups.  
CI/CD.  
Builds separados Web/Desktop desde el mismo repositorio.  
Siguiente tarea exacta  
Implementar la biblioteca Web dentro de `WebAdapter`.  
Objetivo inmediato:  
Iniciar sesión en BeatGaler Web y mostrar los mismos beats, metadata y portadas que actualmente aparecen en Desktop, usando Galer T-Library como source of truth y sin depender de Tauri ni de rutas locales.  
Después se conectará `Review Beat → Save → subida directa`.