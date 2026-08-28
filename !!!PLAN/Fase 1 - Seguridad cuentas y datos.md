# Fase 1 — Seguridad, cuentas y datos durables

> Leer `Plan Maestro.md`. Desde la decisión RO del 2026-08-28, esta fase conserva sus gates de aceptación pero **ya no monopoliza a todos los agentes**: trabajo independiente de otras fases puede avanzar en paralelo.

**Estado:** `[ 🟡 ]` — CRITICAL PATH.  
**Critical gate:** **D7 — Data plane seguro**.  
**Integración:** `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`.  
**Release público:** 🔴 `NO-GO`.

## Semántica operativa nueva

La secuencia `D6 → D7 → D8 → D9 → D10` sigue definiendo **qué puede cerrarse/aceptarse dentro de Fase 1**. Ya no significa que todos deban esperar para empezar trabajo futuro independiente.

- Un slice que dependa de D7 espera D7.
- Un slice que no dependa de D7 puede avanzar si JOBS lo asigna.
- Nada se marca `[x]` antes de cumplir su evidencia literal.
- WOZ decide integración técnica; JOBS decide prioridad/owner/topología.
- D9/D10 son `REUSE-FIRST`: no repetir drills ya aceptados solo para recrear evidencia.

---

## D6 — `[x] PASS`

**6.1 / PR #43:** integrado en `23bded948c4377b28fc48a72378816968d4cd413`; session-bound authz + ownership + coordinación PostgreSQL cross-process.  
**6.2 / PR #44:** integrado en `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`; abuse controls + KDF asíncrono.  
**Exact-head:** compile #128 `33194215442` SUCCESS; D6 cross-process #4 `33194215463` SUCCESS; Required CI #363 `33194215450` SUCCESS.  
**Gate transaction:** WOZ Issue #41 `5455677550` = PASS.

---

## D7 — ACTIVO — Data plane seguro

**Resultado requerido:** navegador/desktop no reciben identidad de infraestructura compartida y solo operan con capabilities acotadas.

### 7.1 [P0 · BE] — `[ 🟡 ]` WOZ PRIMARY

- [ ] Capabilities cortas limitadas por usuario, vault, operación y objeto.
- [ ] Allowlist / deny-by-default.
- [ ] Lifecycle revoke: lease end, logout, password change, delete, incident.
- [ ] Revocación operativa inmediata control-side sin depender de rotación destructiva shared-bot.
- [ ] Ceilings por bot/tenant.

**BBB finding `5455758175`:** cuatro gaps reproducibles: scope/deny-by-default, lifecycle revoke, ceilings y revocación inmediata. Reuse de auth/session/lease/temp-auth confirmado.

**WOZ NEXT:** reproducir/aceptar/rechazar técnicamente findings y producir delta mínimo verificable. Mantener política shared-bot aceptada.

### 7.2 [P0 · QA/Security] — `[ 🟡 ]` AAA / DEPENDENT SLICE

- [ ] Capability A contra vault/objeto B.
- [ ] Replay, expiry, clock skew, sesión cerrada, bot quarantined.
- [ ] Bundles/workers/logs/memoria serializada sin credenciales permanentes.

**PR #45:** `aaa/task-7.2-transport-isolation-adversarial` @ `1d923c467922231df157bdc42f9aad62405d34ea`; Required CI #364 `33195699165` SUCCESS.

**AAA finding `5455777574`:** boundary productivo no universalmente fail-closed en algunos early-return/fallback; no hay fuga observada actual, sí gap reproducible de hardening. PR #45 añade guards/tests y no corrige producción.

**Estado de asignación:** la parte restante de 7.2 espera contrato real 7.1. Mientras tanto AAA trabaja el slice independiente **F2 / 11.1 Design foundations** asignado por JOBS. PR #45 queda preservado para retorno.

### BBB D7 review

Handoff inicial consumido. BBB no reaudita el mismo head. Re-review D7 se reactiva cuando exista nuevo delta WOZ; mientras tanto BBB trabaja **F4 / 21.1 Release manifest readiness audit READ ONLY**.

### Gate D7 — `PENDING`

Cierre: **0 secretos de infraestructura en cliente y 0 operaciones fuera del scope concedido**. D7 pendiente bloquea cierre D7 y slices técnicamente dependientes; no bloquea trabajo cross-phase independiente.

---

## D8 — Sesión y ciclo de cuenta

**Resultado:** sesiones Web endurecidas y cuentas recuperables/controlables.

### 8.1 [P0/P1 · BE/FE]
- [ ] Cookie HttpOnly/Secure/SameSite o equivalente revisado; CSRF explícito.
- [ ] Distinguir 401/expiry de offline/timeout.
- [ ] Session inventory, revoke-one/revoke-all y rotación tras eventos sensibles.

### 8.2 [P1 · BE/FE/LF]
- [ ] Email verification; forgot/reset one-shot/expiry; anti-enumeración.
- [ ] MFA recovery codes; reauth para email/password/delete; notificaciones.
- [ ] Export/delete con revocación, provider cleanup, retención/tombstone y recibo.

**Regla nueva:** JOBS puede adelantar slices de 8.x que no dependan materialmente del contrato D7. No inventar proveedor/credencial/política; si falta decisión real → `RO DECISION REQUIRED` solo para ese checkbox.

### Gate D8
Usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

---

## D9 — PostgreSQL/migración reversible — REUSE-FIRST

**Resultado:** ningún JSON actúa como autoridad productiva.

### 9.1
- [ ] Migrations versionadas, constraints, índices y transacciones.
- [ ] Importador JSON dry-run/checksums/idempotencia/quarantine/reporte.
- [ ] MFA/OAuth protegidos; hashes de sesión no reversibles.

### 9.2
- [ ] Snapshot/migración staging/conteos/checks funcionales.
- [ ] Fallo a mitad + rollback sin pérdida.
- [ ] Corrupción fail-closed.

**Evidencia reutilizable:** PostgreSQL autoridad productiva; PRs #29–#42; migrations/constraints; importer idempotente; rollback/current-PG; durability restart; barrera fail-closed.

**JOBS puede preparar ya** la matriz administrativa `REQUISITO | EVIDENCIA 5.2 | REUSE/GAP`; WOZ decide equivalencia técnica antes de marcar cualquier checkbox.

### Gate D9
Migración repetible/reversible y ningún JSON como autoridad productiva.

---

## D10 — Restore y alpha interna — REUSE-FIRST

### 10.1
- [ ] Backup cifrado Postgres/config y estrategia índice/media.
- [ ] Restore aislado + RPO/RTO + core flows.
- [ ] Acceso, retention, off-provider copy y alerta backup fallido.

Reusar si satisface literalmente: PITR restore aislado, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call, rotation operator y rollback authority.

### 10.2
- [ ] Revisar gates D2–D10, P0 nuevos y evidencia independiente.
- [ ] Si pasa: alpha interna 3–5 usuarios, sintético, invite-only, sin pagos; entitlement real regalado.
- [ ] Si falla: demo local; comunicar deslizamiento sin ampliar alcance.

RO toma decisión final de alpha. Cerrar F1 no autoriza lanzamiento público.

---

## Evidencia 5.2 reusable

| Requirement | Evidencia aceptada |
|---|---|
| PostgreSQL autoridad | productiva, cierre 5.2 |
| Migrations/versionado | PRs #29–#42 |
| Importer/rollback | idempotencia + rollback/current-PG |
| Durability | restart + barrier fail-closed |
| PITR restore | restore aislado representativo |
| RPO | ~7 min |
| RTO | 3643 s |
| Keyring | activa 2, versiones 1/2, lectura v1 |
| Observabilidad/ownership | alarmas RDS + on-call/rotation/rollback authority |

**Criterio:** solo REUSE literal permite cierre; similitud temática no basta.