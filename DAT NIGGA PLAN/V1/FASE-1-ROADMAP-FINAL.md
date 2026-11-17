# FASE 1 — ROADMAP FINAL PARA CERRARLA

## Objetivo

Terminar la Fase 1 con evidencia real de qué funciona y qué falla con varias cuentas independientes.

**No necesitamos corregir todos los fallos encontrados.**  
Si un problema no impide continuar la prueba, se documenta y pasa a Fase 2.

Baseline actual:

`30bb1ffcff9ccb984c1d54ece2dab3569f264f6b`

Ya tenemos funcionando la infraestructura, 10 cuentas/vaults, pool amplia, playback, seek, uploads, metadata, Reload, transferencia grande y el lifecycle logout/relogin con protección contra INDEX huérfanos y doble writer.

---

# TASK 1 — Terminar recorrido individual + Download Integrity

Completar el recorrido de referencia de una cuenta:

`abrir → playback → seek → upload → metadata → download → Reload → logout → login → lectura autoritativa`

## WAV

- [ ] Descargar WAV real.
- [ ] Calcular SHA-256 del original.
- [ ] Calcular SHA-256 de la descarga.
- [ ] Confirmar hashes idénticos.

## ZIP / Project

- [ ] Preparar ZIP/Project de prueba.
- [ ] Descargar ZIP.
- [ ] Calcular SHA-256 del original.
- [ ] Calcular SHA-256 de la descarga.
- [ ] Confirmar hashes idénticos.

## MP3

Web reconstruye ID3, por lo que no se compara simplemente el archivo completo.

- [ ] Descargar MP3.
- [ ] Validar etiquetas ID3.
- [ ] Comparar el payload de audio origen vs descarga.
- [ ] Confirmar ausencia de corrupción.

## Cierre

- [ ] Ejecutar/consolidar el recorrido individual completo.
- [ ] Guardar tiempos principales.
- [ ] Confirmar mediante lectura autoritativa que lo guardado sigue ahí.

---

# TASK 2 — Aislamiento ofensivo entre 2 cuentas

Usar:

`Account A ↔ Vault A`

`Account B ↔ Vault B`

No basta con comprobar que normalmente ven bibliotecas distintas. Hay que intentar romper el aislamiento.

## Installation

- [ ] B intenta utilizar la installation de A.
- [ ] Confirmar rechazo.
- [ ] Confirmar que A continúa funcionando.

## Session

- [ ] B intenta utilizar el `session_id` de A.
- [ ] Confirmar rechazo.

## Operation

- [ ] B intenta utilizar `operation_id` de A.
- [ ] B intenta finalizar una operation de A.
- [ ] B intenta modificar una operation de A.
- [ ] Confirmar rechazo.

## Archivos / media

- [ ] B intenta utilizar referencias de archivos/media de A.
- [ ] Confirmar que B no recibe bytes de A.
- [ ] Confirmar que B no puede modificar contenido de A.

## Mismo browser profile

- [ ] Login como A.
- [ ] Abrir/reproducir contenido de A.
- [ ] Logout A.
- [ ] Login como B.
- [ ] Confirmar que no aparecen beats de A.
- [ ] Confirmar que no queda playback/progreso de A.
- [ ] Confirmar que no queda caché visible de A.

## Resultado

- [ ] Registrar respuestas de los ataques.
- [ ] Confirmar estado final correcto de ambos vaults.
- [ ] Confirmar que no hubo acceso cruzado.

**Cualquier acceso cruzado de datos o autoridad es blocker de lanzamiento.**

---

# TASK 3 — Startup simultáneo y reparto

Cerrar formalmente la progresión:

`2 → 5 → 10`

## Burst 2

- [ ] Lanzar 2 cuentas dentro de una ventana aproximada de 3 segundos.
- [ ] Confirmar startup.
- [ ] Registrar asignaciones.

## Burst 5

- [ ] Lanzar 5 cuentas.
- [ ] Confirmar startup.
- [ ] Registrar asignaciones.

## Burst 10

- [ ] Lanzar 10 cuentas.
- [ ] Confirmar autenticación de las 10.
- [ ] Confirmar biblioteca utilizable de las 10.
- [ ] Confirmar vault correcto de las 10.
- [ ] Confirmar identidad Direct correcta.
- [ ] Registrar `vault → bot`.
- [ ] Confirmar ausencia de sesiones atascadas.

## Condiciones

- [ ] Probar navegador frío.
- [ ] Probar reapertura con caché.
- [ ] Reiniciar Cloud de forma controlada sin borrar state.
- [ ] Ejecutar primera ráfaga después del restart.
- [ ] Confirmar que no aparecen INDEX locks huérfanos.
- [ ] Repetir el burst de 10 una vez.

No necesitamos repetir muchas veces los bursts de 2 y 5. La evidencia fuerte debe concentrarse en 10 cuentas.

---

# TASK 4 — 30 MINUTOS DE USO MIXTO CON 10 CUENTAS

## ESTA PRUEBA NO SE RECORTA

- [ ] Mantener 10 cuentas/vaults activas durante **30 minutos completos**.

## Distribución inicial

### 4 cuentas — Playback

- [ ] Reproducir audio.
- [ ] Hacer seek.
- [ ] Registrar pausas/interrupciones.

### 2 cuentas — Upload

- [ ] Hacer uploads reales.
- [ ] Registrar duración, bytes, errores y retries.

### 2 cuentas — Metadata + Reload

- [ ] Editar metadata.
- [ ] Guardar.
- [ ] Hacer Reload.
- [ ] Confirmar persistencia autoritativa.

### 2 cuentas — Download

- [ ] Descargar archivos reales.
- [ ] Validar resultado.

## Rotación

Durante los 30 minutos todas las cuentas deben pasar por las funciones principales.

- [ ] Todas reproducen.
- [ ] Todas hacen upload.
- [ ] Todas editan metadata.
- [ ] Todas hacen Reload.
- [ ] Todas descargan.

## Transferencia grande

- [ ] Ejecutar una transferencia grande durante la ventana.
- [ ] Mantener a las demás cuentas trabajando.
- [ ] Confirmar que no provoca bloqueo global.

## Métricas

Por operación/cuenta:

- [ ] Resultado.
- [ ] Latencia.
- [ ] Pausas de audio.
- [ ] Duración/velocidad de transferencia.
- [ ] Errores.
- [ ] Reintentos.

Infraestructura, de forma simple:

- [ ] CPU.
- [ ] Memoria.
- [ ] Conexiones PostgreSQL.
- [ ] Esperas PostgreSQL.
- [ ] Recursos de transporte.

## Performance

Biblioteca caliente:

- [ ] Calcular p95.
- [ ] Registrar máximo.
- [ ] Registrar número de muestras.
- [ ] Comparar con objetivo inicial `p95 ≤ 5 s`.

Primer audio:

- [ ] Calcular p95.
- [ ] Registrar máximo.
- [ ] Registrar número de muestras.
- [ ] Comparar con objetivo inicial `p95 ≤ 2 s`.

**Si estos budgets fallan, documentar `FALLÓ` y continuar. La optimización pertenece a Fase 2.**

## Estado final después de los 30 minutos

- [ ] Confirmar contenido correcto por vault.
- [ ] Confirmar uploads persistidos.
- [ ] Confirmar metadata persistida.
- [ ] Confirmar downloads válidos.
- [ ] Confirmar ausencia de cruces entre cuentas.
- [ ] Confirmar ausencia de INDEX locks huérfanos.
- [ ] Registrar operations pendientes.
- [ ] Registrar leases restantes.

---

# TASK 5 — Fallos de 1 cuenta mientras las otras 9 continúan

## Red durante upload

- [ ] Mantener las otras 9 activas.
- [ ] Iniciar upload en A.
- [ ] Interrumpir la red de A durante el upload.
- [ ] Confirmar que las otras 9 continúan.
- [ ] Recuperar A.
- [ ] Comprobar contenido persistido.
- [ ] Confirmar que lo incompleto se representa correctamente.

## Browser crash

- [ ] Mantener las otras 9 activas.
- [ ] Cerrar abruptamente A sin logout.
- [ ] Esperar la expiración necesaria.
- [ ] Confirmar liberación de operations.
- [ ] Confirmar liberación de INDEX.
- [ ] Confirmar que las otras 9 continúan.
- [ ] Abrir nuevamente A.
- [ ] Confirmar recuperación.

## Logout bajo carga

- [ ] Mantener las otras 9 trabajando.
- [ ] Logout de A.
- [ ] Confirmar que las otras 9 continúan.
- [ ] Login nuevamente de A.
- [ ] Confirmar vault correcto.
- [ ] Confirmar persistencia.

## Reconexión

- [ ] Confirmar que A recupera acceso.
- [ ] Confirmar que conserva todo lo previamente confirmado.
- [ ] Confirmar que no contamina otros vaults.

## Shared bot

Solo si durante la prueba varios vaults comparten el mismo transport bot:

- [ ] Repetir al menos un fallo en esa condición.
- [ ] Confirmar que fallar un vault no rompe al otro.

Una ejecución clara por tipo de fallo es suficiente para Fase 1.

---

# TASK 6 — Verificación final

Cuando terminen las pruebas:

- [ ] Verificar vault correcto de cada cuenta.
- [ ] Verificar archivos esperados.
- [ ] Verificar metadata.
- [ ] Verificar uploads confirmados.
- [ ] Verificar downloads.
- [ ] Verificar que no existen cruces de datos.
- [ ] Registrar operations finales.
- [ ] Registrar INDEX operations finales.
- [ ] Registrar leases finales.
- [ ] Guardar métricas finales.

---

# TASK 7 — Cerrar evidencia de Fase 1

Guardar:

- [ ] SHA final probado.
- [ ] Configuración utilizada.
- [ ] Número de cuentas.
- [ ] Pool/bots utilizados.
- [ ] Fixtures utilizados.
- [ ] Resultados de cada escenario.
- [ ] Métricas.
- [ ] Trazas sin secretos.
- [ ] Estado final de archivos/vaults.
- [ ] Blockers encontrados.
- [ ] Pasos para reproducir cada blocker.

Cada conclusión debe quedar marcada como:

- `COMPROBADO`
- `FALLÓ`
- `PENDIENTE POR INFRAESTRUCTURA`

Un resultado negativo **no impide cerrar Fase 1** si está demostrado y reproducido.

Solo arreglamos ahora un problema si impide continuar obteniendo evidencia o invalida la prueba.

---

# CAMINO CRÍTICO

- [ ] **1. Download integrity**
- [ ] **2. Aislamiento ofensivo**
- [ ] **3. Startup 2 → 5 → 10 + restart**
- [ ] **4. 30 minutos / 10 cuentas / mixed load**
- [ ] **5. Fallos inducidos con otras 9 activas**
- [ ] **6. Verificación final**
- [ ] **7. Clasificar y guardar evidencia**

# → FASE 1 CERRADA CON EVIDENCIA

Después:

# → FASE 2 — CERRAR LA FIABILIDAD DEL NÚCLEO WEB

Fase 2 toma los fallos demostrados aquí y los corrige.
