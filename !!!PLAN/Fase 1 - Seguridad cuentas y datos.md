# Fase 1 — Seguridad, cuentas y datos durables

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 31 de agosto–4 de septiembre  
**Objetivo:** cerrar los P0 de confianza y alcanzar un alpha interno restaurable.

## Día 6 — 31 de agosto — Autorización tenant y abuso

**Resultado:** cada operación usa identidad derivada del servidor y límites previos al trabajo costoso.

### Tarea 6.1 [P0 · BE] — Unificar middleware de autorización

- [ ] Derivar user/installation/tenant solo de sesión validada; ignorar IDs de cuerpo para autorización.
- [ ] Autenticar y autorizar antes de Multer, Telegram, lookup de artwork o creación de topic.
- [ ] Añadir ownership por objeto y borrar endpoints legacy no usados.

### Tarea 6.2 [P0 · BE/QA] — Abuse controls

- [ ] Rate limit por IP/cuenta/tenant, delays progresivos y límites de upload/concurrencia.
- [ ] Mover scrypt síncrono fuera del event loop o usar implementación asíncrona controlada.
- [ ] Probar credential stuffing, IDs ajenos, bodies inválidos, **1.99 GB exactos + justo por encima del límite** y race conditions sin ejecutar cargas destructivas.

**Dependencias:** ADR de Día 5.  
**Evidencia:** matriz 401/403/413/429 y pruebas cross-tenant.  
**Gate de salida:** cero acceso o mutación cross-tenant en suite adversarial.

## Día 7 — 1 de septiembre — Data plane seguro

**Resultado:** navegador y desktop ya no reciben una identidad Telegram compartida.

### Tarea 7.1 [P0 · BE] — Implementar mediación/capabilities

- [ ] Emitir capacidades cortas limitadas por usuario, vault, operación y objeto.
- [ ] Rotar/revocar al terminar lease, logout, password change, delete o incidente.
- [ ] Implementar y validar revocación operativa antes de escalar la flota hacia ~80 bots; no forzar revocaciones durante las pruebas actuales salvo compromiso confirmado.
- [ ] Añadir ceilings por bot/tenant y deny-by-default.

### Tarea 7.2 [P0 · QA/Security reviewer] — Validar aislamiento

- [ ] Intentar usar capability de A contra vault/objeto de B.
- [ ] Probar replay, expiración, clock skew, sesión cerrada y bot quarantined.
- [ ] Verificar que bundles, workers, logs y memoria serializada no contienen bot token/API hash.

**Dependencias:** Día 6.  
**Evidencia:** threat tests y escaneo de artefactos.  
**Gate de salida:** 0 secretos de infraestructura en cliente y 0 operaciones fuera del scope.

## Día 8 — 2 de septiembre — Sesión y ciclo de cuenta

**Resultado:** sesiones Web endurecidas y cuentas recuperables/controlables.

### Tarea 8.1 [P0/P1 · BE/FE] — Sesión Web

- [ ] Migrar a cookie HttpOnly/Secure/SameSite o mecanismo equivalente revisado; CSRF explícito.
- [ ] Distinguir 401/expiry de offline/timeout; no borrar una sesión válida por error transitorio.
- [ ] Session inventory, revoke-one/revoke-all y rotación tras eventos sensibles.

### Tarea 8.2 [P1 · BE/FE/LF] — Lifecycle completo

- [ ] Email verification, forgot/reset con tokens one-shot/expiry y respuesta anti-enumeración.
- [ ] MFA recovery codes, reautenticación para email/password/delete y notificaciones.
- [ ] Export y delete con revocación, provider cleanup, retención/tombstone y recibo.

**Dependencias:** email provider/plantillas y decisiones legales.  
**Evidencia:** E2E de happy/abuse/replay y auditoría de sesión.  
**Gate de salida:** usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

## Día 9 — 3 de septiembre — PostgreSQL y migración reversible

**Resultado:** el backend deja de depender de JSON monolítico.

### Tarea 9.1 [P0 · BE/OP] — Esquema y migrador

- [ ] Crear migrations versionadas, constraints, índices y transacciones.
- [ ] Importador JSON con dry-run, checksums, idempotencia, quarantine y reporte por registro.
- [ ] Cifrar/proteger MFA/OAuth; hashes de sesión siguen no reversibles.

### Tarea 9.2 [P0 · QA/OP] — Cutover ensayado

- [ ] Snapshot antes, migración staging, comparación de conteos y checks funcionales.
- [ ] Simular fallo a mitad y ejecutar rollback sin perder datos.
- [ ] Desactivar fallback que convierte corrupción en servicio vacío.

**Dependencias:** PostgreSQL staging y ADR de datos.  
**Evidencia:** reporte de migración, diff lógico y rollback exitoso.  
**Gate de salida:** migración repetible y reversible; ningún JSON actúa como autoridad de producción.

## Día 10 — 4 de septiembre — Restore y alpha interna

**Resultado:** checkpoint original convertido en evidencia, no marketing.

### Tarea 10.1 [P0 · OP/QA] — Backup y restore

- [ ] Backup cifrado de Postgres/configuración y estrategia para índice/media Telegram.
- [ ] Restaurar en entorno aislado, medir RPO/RTO y ejecutar core flows.
- [ ] Verificar acceso, retention, off-provider copy y alerta por backup fallido.

### Tarea 10.2 [P0 · RO/Security reviewer] — Decidir alpha

- [ ] Revisar gates D2–D10, P0 nuevos y evidencia independiente.
- [ ] Si pasa: 3–5 usuarios internos, datos sintéticos, invitación, sin pagos; cualquier acceso de plan se concede como suscripción/entitlement real regalado, no como plan free-only.
- [ ] Si falla: demo local; comunicar deslizamiento sin ampliar alcance.

**Dependencias:** Días 2–9.  
**Evidencia:** video/log de restore, checklist P0 y decisión firmada.  
**Gate de salida:** servicio restaurable y alpha contenida; esto no autoriza lanzamiento público.
