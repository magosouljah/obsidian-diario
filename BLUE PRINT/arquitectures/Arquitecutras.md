### Núcleo — encontrar y usar

1. ~={purple}**STARTUP**=~ — abrir app → biblioteca visible → app completamente lista.
2. **LIBRARY LOAD / REHYDRATION** — storage/cache → reconstruir estado → renderizar biblioteca.
3. **SEARCH / FILTER / SORT** — acción usuario → estado derivado → resultados visibles.
4. ~={pink}**PLAYBACK START**=~ — Play → encontrar recurso → preparar → primer audio audible.
5. **PLAYBACK CONTINUITY** — cambiar beat → seek → siguiente beat → cache/prefetch.
6. ~={pink}**STREAMING / PREFETCH**=~ — decidir qué audio traer, prioridades, chunks, buffers y cancelaciones.
7. **DOWNLOAD** — pedir archivo → localizar → obtener → verificar → entregar.
8. **EXPORT** — elegir qué exportar → reunir recursos → construir salida → filesystem.

### Construir y organizar

9. ~={yellow}**IMPORT / DRAG & DROP**=~ — archivos/carpetas → detectar → validar → crear lote.
10. ~={yellow}**IMPORT REVIEW**=~ — beat detectado → Review → decisiones → preparación.
11. ~={yellow}**UPLOAD / SAVE NEW BEAT**=~ — Review terminado → procesamiento → persistencia → Cloud → biblioteca.
12. **UPDATE EXISTING BEAT** — editar beat existente → detectar cambios → guardar → sincronizar.
13. **METADATA EDITING** — nombre/BPM/key/rating/tags/etc. → validar → persistir → actualizar vistas.
14. **ARTWORK** — seleccionar/cambiar artwork → procesar → guardar → propagar.
15. **PROJECT + SAMPLES** — importar proyecto → ZIP → abrir → modificar → actualizar → volver a guardar.
16. **BULK OPERATIONS** — selección múltiple → edición/reordenamiento/eliminación → persistencia coherente.
17. **LIBRARY ORGANIZATION** — tags, orden manual, agrupación y cambios que afectan toda la biblioteca.

### Biblioteca confiable

18. ~={green}**SYNC**=~ — comparar estado local/remoto → decidir autoridad → reconciliar → actualizar.
19. **MULTI-DEVICE SYNC** — dispositivo A cambia → Cloud → dispositivo B converge.
20. **OFFLINE AVAILABILITY** — hacer beat offline → descargar recursos → registrar disponibilidad.
21. ~={cyan}**OFFLINE → ONLINE RECONCILIATION**=~ — acciones sin red → reconexión → aplicar intenciones → resolver diferencias.
22. **TRASH / DELETE / RESTORE** — borrar → Trash → restaurar o borrar definitivamente.
23. ~={orange}**DATA RECOVERY / REPAIR**=~ — estado incompleto/corrupto → detectar → reconstruir → volver a estado válido.
24. ~={orange}**NETWORK / CLOUD FAILURE RECOVERY**=~ — timeout/error/interrupción → retry/fallback → recuperar operación.
25. **TRANSFER LIFECYCLE** — upload/download en progreso → pausa/fallo/cancelación/reintento/terminación.
26. **CACHE LIFECYCLE** — cache hit/miss → validar frescura → usar/reemplazar/evict.

### Cuenta y acceso

27. **AUTH** — abrir/login → autenticar → recuperar cuenta → entrar.
28. **SESSION LIFECYCLE** — crear sesión → heartbeat → expiración → logout/cleanup.
29. **DEVICE MANAGEMENT** — registrar dispositivo → límites → revocar → recuperar acceso.
30. **ENTITLEMENTS / QUOTAS** — acción → comprobar plan/límite → permitir/rechazar → contabilizar.
31. **SUBSCRIPTION / BILLING** — plan → pago → entitlement → cambio/cancelación.
32. **ACCOUNT DELETION** — solicitud → invalidar acceso → borrar datos/archivos → cierre definitivo.

### Infraestructura runtime

33. **CLOUD STORAGE WRITE** — recurso nuevo/modificado → almacenamiento → índice → confirmación.
34. **CLOUD STORAGE READ** — necesidad de recurso → resolver ubicación → recuperar → validar.
35. **DIRECT FILE TRANSFER** — obtener capacidad/token → conexión directa → transferencia → cierre/revocación.
36. **PLATFORM CAPABILITY ROUTING** — misma acción → detectar Web/Desktop → escoger implementación apropiada.
37. **DESKTOP FILESYSTEM** — permisos/path → lectura/escritura → errores/recovery.
38. **BACKGROUND WORK / JOBS** — tareas largas → scheduler → progreso → cancelación → resultado.
39. **APP SHUTDOWN** — cerrar app → guardar → terminar operaciones → limpiar sesión/recursos.
40. **APP CRASH / NEXT-START RECOVERY** — crash inesperado → siguiente startup → detectar trabajo incompleto → recuperar.

### Integraciones y producto

41. **YOUTUBE PUBLISH** — beat → metadata/artwork → procesamiento → upload → publicación.
42. **YOUTUBE SCHEDULING** — preset/programación → espera → publicación → resultado/retry.
43. **DESKTOP UPDATE** — detectar versión → descargar → verificar → instalar → reiniciar.
44. **WEB ↔ DESKTOP CONSISTENCY** — acciones equivalentes → contratos compartidos → diferencias de plataforma.
45. **PROGRESS / STATUS PROPAGATION** — backend/transferencia cambia → estado → frontend → feedback al usuario.

### Operación y protección

46. **SECURITY / AUTHORIZATION PATH** — request → identidad → permisos → recurso → respuesta.
47. **USER DATA ISOLATION** — petición → resolver owner/vault → impedir acceso cruzado.
48. **OBSERVABILITY / HEALTH** — evento/error → logs/métricas → diagnóstico → health/status.
49. **SERVER STARTUP / RECOVERY** — servidor inicia → DB/migraciones/dependencias → ready.
50. **DEPLOY / ROLLBACK** — versión nueva → deploy → health → aceptar o volver atrás.