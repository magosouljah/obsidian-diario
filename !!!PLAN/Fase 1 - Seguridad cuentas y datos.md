# Fase 1 — Seguridad, cuentas y datos durables

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas originales:** 31 de agosto–4 de septiembre.  
**Objetivo operativo vigente:** cerrar los P0 de confianza y alcanzar un alpha interno restaurable, intentando completar Fase 1 agresivamente en 1 día mediante el paralelismo permitido **sin cambiar orden, dependencias, gates ni alcance**.

**Estado:** `[ 🟡 ]` — **ACTIVA por decisión explícita del RO el 28 de agosto de 2026.**  
**Día activo:** **Día 6**.  
**Baseline:** `integration-v0.8.0-alpha.1` @ `b9c2317297ff3c0f7a6246ac97517fa978f6caea`.  
**Required CI post-rewrite:** run **#314** (`33148873459`) = `SUCCESS`.

## Orden obligatorio

`6.1 ∥ 6.2` → **Gate D6** → `7.1 ∥ 7.2` → **Gate D7** → `8.1 ∥ 8.2` → **Gate D8** → `9.1 ∥ 9.2` → **Gate D9** → `10.1` → `10.2`.

- Paralelismo únicamente dentro del mismo Día.
- **No iniciar un Día posterior antes de aprobar el gate anterior.**
- JOBS coordina; WOZ decide técnicamente e integra.
- Release público permanece 🔴 `NO-GO`; completar Fase 1 no autoriza publicación.

---

## Día 6 — ACTIVO — Autorización tenant y abuso

**Resultado:** cada operación usa identidad derivada del servidor y límites previos al trabajo costoso.

### Asignación vigente

- **WOZ — PRIMARY:** 6.1 — Unificar middleware de autorización. También integra compatibilidad con 6.2 y decide técnicamente el cierre de Día 6.
- **AAA:** 6.2 — Abuse controls + suite adversarial.
- **BBB:** 6.1 — auditoría/review independiente del authorization boundary; comenzar **READ ONLY**.
- **JOBS:** coordina handoffs, mantiene `!!!PLAN` y entrega `WOZ NEXT`.

### Tarea 6.1 [P0 · BE] — Unificar middleware de autorización

- [ ] Derivar user/installation/tenant solo de sesión validada; ignorar IDs de cuerpo para autorización.
- [ ] Autenticar y autorizar antes de Multer, Telegram, lookup de artwork o creación de topic.
- [ ] Añadir ownership por objeto y borrar endpoints legacy no usados.

### Tarea 6.2 [P0 · BE/QA] — Abuse controls

- [ ] Rate limit por IP/cuenta/tenant, delays progresivos y límites de upload/concurrencia.
- [ ] Mover scrypt síncrono fuera del event loop o usar implementación asíncrona controlada.
- [ ] Probar credential stuffing, IDs ajenos, bodies inválidos, **1.99 GB exactos + justo por encima del límite** y race conditions sin ejecutar cargas destructivas.

**Dependencias:** ADR de Día 5 / trust-boundary aceptado en 5.1.  
**Evidencia:** matriz 401/403/413/429 y pruebas cross-tenant.

### Gate D6 — requerido para pasar a Día 7

- [ ] identidad `user / installation / tenant` derivada de sesión validada;
- [ ] auth + autorización + límites antes de trabajo costoso;
- [ ] ownership por objeto;
- [ ] matriz `401 / 403 / 413 / 429`;
- [ ] pruebas cross-tenant;
- [ ] **cero acceso o mutación cross-tenant en suite adversarial**.

**Gate D6:** PENDING. **No iniciar 7.x todavía.**

Cuando WOZ/RO acepte D6:
- AAA → 7.2;
- BBB → review independiente de 7.1;
- WOZ → 7.1 + integración.

---

## Día 7 — BLOQUEADO POR D6 — Data plane seguro

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

**Dependencias:** Gate D6 aprobado.  
**Evidencia:** threat tests y escaneo de artefactos.  
**Gate D7:** 0 secretos de infraestructura en cliente y 0 operaciones fuera del scope.

**Asignación al aprobar D6:** WOZ → 7.1 + integración; AAA → 7.2; BBB → review independiente de 7.1.

---

## Día 8 — BLOQUEADO POR D7 — Sesión y ciclo de cuenta

**Resultado:** sesiones Web endurecidas y cuentas recuperables/controlables.

### Tarea 8.1 [P0/P1 · BE/FE] — Sesión Web

- [ ] Migrar a cookie HttpOnly/Secure/SameSite o mecanismo equivalente revisado; CSRF explícito.
- [ ] Distinguir 401/expiry de offline/timeout; no borrar una sesión válida por error transitorio.
- [ ] Session inventory, revoke-one/revoke-all y rotación tras eventos sensibles.

### Tarea 8.2 [P1 · BE/FE/LF] — Lifecycle completo

- [ ] Email verification, forgot/reset con tokens one-shot/expiry y respuesta anti-enumeración.
- [ ] MFA recovery codes, reautenticación para email/password/delete y notificaciones.
- [ ] Export y delete con revocación, provider cleanup, retención/tombstone y recibo.

**Dependencias:** Gate D7 aprobado; email provider/plantillas y decisiones legales donde 8.2 las necesite.  
**Evidencia:** E2E de happy/abuse/replay y auditoría de sesión.  
**Gate D8:** usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

---

## Día 9 — BLOQUEADO POR D8 — PostgreSQL y migración reversible

**Resultado:** el backend deja de depender de JSON monolítico.

### Regla REUSE-FIRST obligatoria

Antes de cambiar código o repetir operaciones, construir una matriz por requirement: `REQUISITO 9.x → EVIDENCIA FASE 0/5.2 → REUSE | GAP`.

Evidencia válida a mapear cuando satisfaga literalmente el requisito:
- PostgreSQL ya es autoridad productiva;
- schema/migrations versionadas/constraints/índices integrados en PRs #29–#42;
- importer dry-run/idempotente/checksums/quarantine donde aplique;
- rollback/current-PG readiness ya aceptado;
- durabilidad a través de restart y barrera fail-closed ya aceptada.

**Solo un GAP literal genera trabajo nuevo. No repetir migration, cutover, rollback rehearsal ni durability restart únicamente para recrear evidencia ya aceptada.**

### Tarea 9.1 [P0 · BE/OP] — Esquema y migrador

- [ ] Crear migrations versionadas, constraints, índices y transacciones.
- [ ] Importador JSON con dry-run, checksums, idempotencia, quarantine y reporte por registro.
- [ ] Cifrar/proteger MFA/OAuth; hashes de sesión siguen no reversibles.

### Tarea 9.2 [P0 · QA/OP] — Cutover ensayado

- [ ] Snapshot antes, migración staging, comparación de conteos y checks funcionales.
- [ ] Simular fallo a mitad y ejecutar rollback sin perder datos.
- [ ] Desactivar fallback que convierte corrupción en servicio vacío.

**Dependencias:** Gate D8 aprobado; PostgreSQL staging/autoridad y ADR de datos.  
**Evidencia:** matriz REUSE/GAP + reporte de migración, diff lógico y rollback exitoso para cualquier GAP real.  
**Gate D9:** migración repetible y reversible; ningún JSON actúa como autoridad de producción.

---

## Día 10 — BLOQUEADO POR D9 — Restore y alpha interna

**Resultado:** checkpoint original convertido en evidencia, no marketing.

### Regla REUSE-FIRST obligatoria

Antes de ordenar nueva infraestructura/prueba, mapear cada requirement de 10.1/10.2 contra evidencia WAVE 3 aceptada:
- PostgreSQL autoridad productiva;
- backup/PITR y restore aislado representativo;
- **RPO ~7 min**;
- **RTO 3643 s**;
- keyring multiversión con activa `2`, versiones `1,2` y lectura de ciphertext v1;
- alarmas RDS críticas, on-call, rotation operator y rollback authority aceptados.

**No repetir restore, cutover, migrations, durability restart ni key rotation únicamente para recrear evidencia.** Verificar/implementar solo requisitos no cubiertos literalmente, por ejemplo configuración backup cifrada, estrategia índice/media, retention/off-provider copy/backup-failure alert o core flows del entorno restaurado si no están ya demostrados.

### Tarea 10.1 [P0 · OP/QA] — Backup y restore

- [ ] Backup cifrado de Postgres/configuración y estrategia para índice/media Telegram.
- [ ] Restaurar en entorno aislado, medir RPO/RTO y ejecutar core flows.
- [ ] Verificar acceso, retention, off-provider copy y alerta por backup fallido.

### Tarea 10.2 [P0 · RO/Security reviewer] — Decidir alpha

- [ ] Revisar gates D2–D10, P0 nuevos y evidencia independiente.
- [ ] Si pasa: 3–5 usuarios internos, datos sintéticos, invitación, sin pagos; cualquier acceso de plan se concede como suscripción/entitlement real regalado, no como plan free-only.
- [ ] Si falla: demo local; comunicar deslizamiento sin ampliar alcance.

**Orden obligatorio Día 10:** primero 10.1; **solo después** 10.2.  
**Dependencias:** Gate D9 aprobado y gates anteriores vigentes.  
**Evidencia:** mapa REUSE/GAP, evidencia nueva solo para gaps, checklist P0 y decisión firmada.  
**Gate final Fase 1:** servicio restaurable y alpha contenida; esto **no autoriza lanzamiento público**.

---

## Evidencia de Fase 0 reutilizable — no reabrir por costumbre

| Requirement potencial | Evidencia aceptada disponible |
|---|---|
| PostgreSQL autoridad | Productiva, aceptada en cierre 5.2 |
| Migrations/versionado | PRs #29–#42 |
| Importer/rollback | Importer idempotente + rollback/current-PG evidence aceptada |
| Durability | Restart controlado + barrier fail-closed aceptados |
| PITR restore | Restore aislado representativo aceptado |
| RPO | ~7 min |
| RTO | 3643 s |
| Keyring multiversión | activa `2`, versiones `1,2`, lectura v1 verificada |
| Observabilidad/ownership | alarmas RDS críticas + on-call/rotation/rollback authority |

**Criterio:** `REUSE` solo cuando la evidencia satisface exactamente el checkbox; `GAP` cuando falta una parte concreta. La similitud temática no permite marcar `[x]`.
