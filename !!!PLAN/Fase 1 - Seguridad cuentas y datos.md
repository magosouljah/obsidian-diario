# Fase 1 — Seguridad, cuentas y datos durables

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Objetivo operativo vigente:** cerrar los P0 de confianza y alcanzar un alpha interno restaurable lo más rápido posible mediante el paralelismo permitido, **sin cambiar orden, dependencias, gates ni alcance**.

**Estado:** `[ 🟡 ]` — ACTIVA por decisión RO del 28 de agosto de 2026.  
**Día activo:** **Día 6 — CLOSEOUT**.  
**Integración actual:** `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`.  
**Release público:** 🔴 `NO-GO`.

## Orden obligatorio

`6.1 ∥ 6.2` → **Gate D6** → `7.1 ∥ 7.2` → **Gate D7** → `8.1 ∥ 8.2` → **Gate D8** → `9.1 ∥ 9.2` → **Gate D9** → `10.1` → `10.2`.

- Paralelismo únicamente dentro del mismo Día.
- No iniciar Día posterior antes de PASS estructurado del gate anterior.
- JOBS coordina y preasigna; WOZ decide técnicamente, integra y publica gate.
- En cuanto un gate pasa, el Día siguiente arranca sin pedir permiso adicional.

---

## Día 6 — CLOSEOUT — Autorización tenant y abuso

**Resultado:** cada operación usa identidad derivada del servidor y límites previos al trabajo costoso.

### Estado técnico confirmado

- **6.2 / PR #44:** integrado en `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`; abuse controls + KDF asíncrono; `scryptSync` eliminado del request path.
- **6.1 / PR #43:** integrado en `23bded948c4377b28fc48a72378816968d4cd413`; session-bound authz + ownership + coordinación PostgreSQL cross-process + compatibilidad conjunta con 6.2.
- Head final pre-merge #43 `5cfec64d756caf73ad3d57f4bb943e7adaabf6bd`: compile, D6 cross-process y Required CI = `SUCCESS`.
- Head integrado `23bded9...`: compile run #128 (`33194215442`) = `SUCCESS`; D6 cross-process #4 (`33194215463`) = `SUCCESS`; Required CI #363 (`33194215450`) sigue `IN_PROGRESS`.

### Tarea 6.1 [P0 · BE] — `[ ⚠️ ]` integrada; gate pendiente

- [⚠️] Derivar user/installation/tenant solo de sesión validada; ignorar IDs de cuerpo para autorización.
- [⚠️] Autenticar y autorizar antes de trabajo costoso.
- [⚠️] Ownership por objeto + eliminación/contención de legacy aplicable.

### Tarea 6.2 [P0 · BE/QA] — `[ ⚠️ ]` integrada; gate pendiente

- [⚠️] Rate limit por IP/cuenta/tenant, delays progresivos y límites upload/concurrencia.
- [⚠️] KDF de password asíncrono/controlado fuera del bloqueo síncrono del request path.
- [⚠️] Credential stuffing, IDs ajenos, bodies inválidos, 1.99 GB exactos/+1 y race/concurrency sin carga destructiva.

### Gate D6

- [⚠️] identidad `user / installation / tenant` derivada de sesión validada;
- [⚠️] auth + autorización + límites antes de trabajo costoso;
- [⚠️] ownership por objeto;
- [⚠️] matriz `401 / 403 / 413 / 429`;
- [⚠️] pruebas cross-tenant;
- [⚠️] cero acceso o mutación cross-tenant en suite adversarial.

**Gate D6:** `PENDING` solo por cierre de Required CI #363 + decisión estructurada WOZ. JOBS no lo autoacepta.

### Asignación NOW

- **WOZ — PRIMARY:** comprobar #363; `SUCCESS` → publicar `GATE D6 PASS` estructurado. `FAIL` → corregir solo regresión atribuible D6 y repetir evidencia.
- **AAA:** `LIBRE / BLOQUEADO POR D6`; no reabrir #44 sin delta/finding nuevo.
- **BBB:** `LIBRE / BLOQUEADO POR D6`; no reauditar #43 sin delta nuevo.
- **JOBS:** sincronizar PASS y activar Día 7 inmediatamente cuando WOZ lo publique.

---

## Día 7 — AUTO-UNLOCK tras D6 PASS — Data plane seguro

**Resultado:** navegador/desktop no reciben identidad Telegram compartida y solo operan con capabilities acotadas.

### 7.1 [P0 · BE] — WOZ PRIMARY

- [ ] Capacidades cortas limitadas por usuario, vault, operación y objeto.
- [ ] Rotación/revocación al terminar lease, logout, password change, delete o incidente.
- [ ] Revocación operativa validada antes de escalar flota; no forzar revocaciones peligrosas sin compromiso confirmado.
- [ ] Ceilings por bot/tenant + deny-by-default.

### 7.2 [P0 · QA/Security] — AAA

- [ ] Capability A contra vault/objeto B.
- [ ] Replay, expiración, clock skew, sesión cerrada y bot quarantined.
- [ ] Bundles/workers/logs/memoria serializada sin bot token/API hash.

### BBB

Review independiente READ ONLY de 7.1. Finding reproducible → Issue #41/PR; no duplicar implementación.

### Gate D7

**0 secretos de infraestructura en cliente y 0 operaciones fuera del scope.** WOZ integra y publica gate estructurado.

---

## Día 8 — AUTO-UNLOCK tras D7 PASS — Sesión y ciclo de cuenta

**Resultado:** sesiones Web endurecidas y cuentas recuperables/controlables.

### 8.1 [P0/P1 · BE/FE] — WOZ PRIMARY

- [ ] Cookie HttpOnly/Secure/SameSite o equivalente revisado; CSRF explícito.
- [ ] Distinguir 401/expiry de offline/timeout; no borrar sesión válida por error transitorio.
- [ ] Session inventory, revoke-one/revoke-all y rotación tras eventos sensibles.

### 8.2 [P1 · BE/FE/LF] — AAA

- [ ] Email verification; forgot/reset one-shot/expiry; anti-enumeración.
- [ ] MFA recovery codes; reauth para email/password/delete; notificaciones.
- [ ] Export/delete con revocación, provider cleanup, retención/tombstone y recibo.

### BBB

Review independiente de 8.1 + delta crítico de 8.2; abuse/replay/session audit.

### Regla de bloqueo parcial 8.2

Si falta proveedor, credencial o decisión legal real: reportar `RO DECISION REQUIRED` para ese checkbox y continuar todo lo independiente. **No inventar proveedor/política.**

### Gate D8

Usuario puede verificar, recuperar, exportar y borrar sin intervención manual insegura.

---

## Día 9 — AUTO-UNLOCK tras D8 PASS — PostgreSQL/migración reversible

**Resultado:** ningún JSON actúa como autoridad de producción.

### REUSE-FIRST obligatorio

Antes de cambiar código: `REQUISITO | EVIDENCIA FASE 0/5.2 | REUSE/GAP | ACCIÓN`.

- **JOBS:** prepara matriz administrativa y referencias; no decide equivalencia técnica.
- **WOZ:** valida REUSE/GAP y ejecuta solo GAP literal.
- **AAA:** prueba adversarialmente gaps reales 9.1/9.2.
- **BBB:** review independiente de matriz/evidencia; evita repetir trabajo ya aceptado.

### 9.1 [P0 · BE/OP]

- [ ] Migrations versionadas, constraints, índices y transacciones.
- [ ] Importador JSON dry-run/checksums/idempotencia/quarantine/reporte.
- [ ] MFA/OAuth protegidos; hashes de sesión no reversibles.

### 9.2 [P0 · QA/OP]

- [ ] Snapshot/migración staging/conteos/checks funcionales.
- [ ] Fallo a mitad + rollback sin pérdida.
- [ ] Fallback de corrupción fail-closed; no servicio vacío silencioso.

### Evidencia reutilizable

PostgreSQL autoridad productiva; PRs #29–#42; migrations/constraints; importer idempotente; rollback/current-PG; durabilidad restart; barrera fail-closed.

**No repetir** migration, cutover, rollback rehearsal ni durability restart solo para recrear evidencia.

### Gate D9

Migración repetible/reversible y ningún JSON como autoridad productiva.

---

## Día 10 — AUTO-UNLOCK tras D9 PASS — Restore y alpha interna

**Resultado:** servicio restaurable y decisión alpha contenida.

### 10.1 [P0 · OP/QA] — PRIMERO

- [ ] Backup cifrado Postgres/config y estrategia índice/media.
- [ ] Restore aislado + RPO/RTO + core flows.
- [ ] Acceso, retention, off-provider copy y alerta backup fallido.

**REUSE-FIRST:** mapear PITR restore aceptado, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call, rotation operator y rollback authority. Solo GAP literal genera trabajo.

Asignación: JOBS prepara mapa; WOZ valida/ejecuta gaps; AAA prueba gaps; BBB revisa evidencia.

### 10.2 [P0 · RO/Security reviewer] — SOLO DESPUÉS DE 10.1

- [ ] Revisar gates D2–D10, P0 nuevos y evidencia independiente.
- [ ] Si pasa: alpha interna 3–5 usuarios, datos sintéticos, invitación, sin pagos; entitlement real regalado, no free-only.
- [ ] Si falla: demo local; comunicar deslizamiento sin ampliar alcance.

Asignación: JOBS compila checklist; WOZ recomendación técnica; BBB revisión independiente; **RO toma la decisión final de alpha**.

**Fase 1 final:** técnicamente cerrable cuando 10.2 tenga decisión válida. Esto **no autoriza lanzamiento público**.

---

## Evidencia Fase 0/5.2 reutilizable — no reabrir por costumbre

| Requirement potencial | Evidencia aceptada |
|---|---|
| PostgreSQL autoridad | Productiva, cierre 5.2 |
| Migrations/versionado | PRs #29–#42 |
| Importer/rollback | Idempotencia + rollback/current-PG |
| Durability | Restart + barrier fail-closed |
| PITR restore | Restore aislado representativo |
| RPO | ~7 min |
| RTO | 3643 s |
| Keyring | activa `2`, versiones `1,2`, lectura v1 |
| Observabilidad/ownership | alarmas RDS + on-call/rotation/rollback authority |

**Criterio:** REUSE solo si satisface literalmente el checkbox; similitud temática no permite `[x]`.