# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible **sin rebajar gates reales**.
> Este archivo es el tablero de ejecución. El detalle técnico vive en la fase aplicable y en GitHub; no se duplica aquí.

## Lectura rápida obligatoria

### Para cualquier trabajo
1. Leer **este archivo completo**.
2. Leer **solo la fase activa** y la tarea que se va a ejecutar.
3. Consultar el estado actual necesario en GitHub / Issue #41.
4. Leer `Gates - Publicación y contingencias.md` **solo** cuando la tarea afecte release, seguridad, go/no-go o contingencias.
5. Abrir contexto/fases futuras/histórico solo si la tarea lo necesita.

### JOBS
JOBS normalmente lee: `Plan Maestro.md` → fase activa → últimos avances relevantes → Issue #41.
Hace auditoría completa solo al cambiar de fase, detectar contradicción/desync, aparecer un gate nuevo real o por petición explícita del RO.

### Archivo protegido
`Plan Maestro 2208 copy DONT TOUCH .md` es histórico. **No modificar ni usar como plan vigente.**

---

## Reglas no negociables

1. No saltar dependencias ni gates reales.
2. No marcar `[x]` sin evidencia verificable.
3. Antes de un cambio técnico: auditoría read-only del estado real.
4. Después de un cambio técnico relevante: pruebas afectadas + CI aplicable.
5. Cada avance que cambie estado actualiza: **Plan Maestro + fase activa + Registro de avances**.
6. No duplicar logs/diffs extensos en `!!!PLAN`; usar PR, Actions e Issue #41.
7. Ningún P0/P1 abierto al publicar.
8. **JOBS solo modifica `!!!PLAN`**; WOZ decide/ejecuta código, arquitectura e infraestructura.
9. Modo autónomo: preflight factual, idempotencia, evidence-before-claim, STOP conditions, gate transaction y watchdog.

**Precedencia:** este Plan → gate/checklist de fase activa → Gates → Contexto. GitHub/runtime decide los hechos técnicos actuales.

---

## Estado vivo — AHORA

- **Fase activa:** **Fase 1 — Seguridad, cuentas y datos durables**.
- **Día activo:** **Día 6 — CLOSEOUT de autorización tenant y abuso**.
- **Release público:** 🔴 `NO-GO`.
- **BeatGaler / integración actual:** `integration-v0.8.0-alpha.1` @ `23bded948c4377b28fc48a72378816968d4cd413`, versión `0.8.0-alpha.1`.
- **D6 implementación integrada:**
  - PR #44 / 6.2 integrado en `9dd76a9d43e72c2295667a3661ce5a1cff7a4826`: abuse controls + KDF asíncrono; sin `scryptSync` en request path.
  - PR #43 / 6.1 integrado en `23bded948c4377b28fc48a72378816968d4cd413`: autorización session-bound + ownership + coordinación PostgreSQL cross-process + compatibilidad final con 6.2.
  - Head final pre-merge #43 `5cfec64d756caf73ad3d57f4bb943e7adaabf6bd`: compile, D6 cross-process y Required CI = `SUCCESS`.
- **Checks del head ya integrado `23bded9...`:**
  - compile run #128 (`33194215442`) = `SUCCESS`;
  - D6 cross-process run #4 (`33194215463`) = `SUCCESS`;
  - Required CI / Desktop Portability run #363 (`33194215450`) = **IN_PROGRESS**; Web/shared, PostgreSQL/recovery y supply-chain ya `SUCCESS`; runners nativos siguen ejecutándose.
- **Gate D6:** `PENDING` únicamente hasta que Required CI #363 cierre y WOZ publique la transacción estructurada del gate. **JOBS no autoacepta el gate.**
- **5.1:** `[x]`.
- **5.2:** `[x]` — cierre WOZ/RO Issue #41 comment `5448976400`; no repetir evidencia aceptada salvo invalidación nueva.
- **2.2:** `[ 🟡 ]` tail externo no bloqueante: GitHub Support + verificación final de inaccesibilidad. No marcar `[x]` sin ambas evidencias.
- **1.2:** `[ 🟡 ]` carril externo de release; Apple Developer sigue `PENDING — DEFERRED`.

---

## Fase 1 — FAST LANE obligatorio

`6.1 ∥ 6.2` → **Gate D6** → `7.1 ∥ 7.2` → **Gate D7** → `8.1 ∥ 8.2` → **Gate D8** → `9.1 ∥ 9.2` → **Gate D9** → `10.1` → `10.2`.

**Regla de velocidad:** preparar asignaciones por adelantado, pero **no ejecutar un Día posterior antes del PASS estructurado del gate anterior**. En cuanto WOZ publica PASS válido, JOBS sincroniza y el siguiente Día arranca sin pedir permiso adicional.

### AHORA — WAVE F1-D6 CLOSEOUT

- **WOZ — PRIMARY:** vigilar Required CI #363 sobre `23bded9...`; si termina `SUCCESS`, publicar `GATE: D6 / STATUS: PASS` con evidencia exacta. Si falla, resolver únicamente la regresión atribuible dentro de scope D6 y repetir evidencia.
- **AAA:** `LIBRE / BLOQUEADO POR D6`. No reabrir 6.2 ya integrado. Al D6 PASS → **7.2**.
- **BBB:** `LIBRE / BLOQUEADO POR D6`. No reauditar 6.1 sin delta nuevo. Al D6 PASS → **review independiente de 7.1**.
- **JOBS:** mantener `!!!PLAN`; en cuanto exista D6 PASS válido, activar Día 7 y publicar `WOZ NEXT` sin ciclo de espera adicional.

### AUTO-UNLOCK — Día 7

Al D6 PASS:
- **WOZ:** 7.1 — capabilities cortas, scope user/vault/op/object, revocación/rotación, ceilings, deny-by-default; integración y decisión D7.
- **AAA:** 7.2 — ataque de aislamiento: A vs B, replay, expiry, clock skew, sesión cerrada, bot quarantined, scans de bundles/workers/logs/memoria serializada.
- **BBB:** review independiente READ ONLY de 7.1; findings reproducibles, sin duplicar implementación.
- **JOBS:** coordina handoffs y exige gate D7 estructurado.

### AUTO-UNLOCK — Día 8

Al D7 PASS:
- **WOZ:** 8.1 PRIMARY + integración — sesión Web segura, CSRF, manejo 401 vs offline/timeout, inventory/revoke/rotation.
- **AAA:** 8.2 — lifecycle implementable sin decisión externa: verification/reset one-shot/expiry/anti-enumeration, MFA recovery, reauth, notifications, export/delete/revocation/cleanup/retention/receipt.
- **BBB:** review independiente de 8.1 y del delta crítico de 8.2; abuse/replay/session audit.
- **Regla 8.2:** si falta proveedor/credencial/decisión legal real, aislar ese checkbox como `RO DECISION REQUIRED` y continuar todo lo independiente; no inventar proveedor ni política.
- **JOBS:** coordina y sincroniza D8 solo tras decisión WOZ/RO válida.

### AUTO-UNLOCK — Día 9 / REUSE-FIRST

Al D8 PASS:
1. **JOBS** prepara la matriz administrativa `REQUISITO | EVIDENCIA 5.2 | REUSE/GAP` sin decidir equivalencia técnica.
2. **WOZ** valida técnicamente cada REUSE/GAP y solo implementa GAP literal.
3. **AAA** verifica adversarialmente cualquier GAP real de 9.1/9.2.
4. **BBB** revisa independientemente que ningún checkbox se marque por similitud temática y que no se repitan drills ya aceptados.

Reutilizar cuando satisfaga literalmente: PostgreSQL autoridad, migrations/versionado/constraints, importer/idempotencia/rollback, durabilidad/restart, barrera fail-closed. **No repetir migration/cutover/rollback rehearsal/durability restart para recrear evidencia.**

### AUTO-UNLOCK — Día 10 / REUSE-FIRST

Al D9 PASS:
- **10.1 primero.** JOBS prepara mapa; WOZ valida gaps y ejecuta solo lo no cubierto; AAA prueba gaps; BBB revisa evidencia independiente.
- Reusar: PITR restore aislado, RPO ~7 min, RTO `3643 s`, keyring multiversión, alarmas/on-call, rotation operator y rollback authority.
- No repetir restore/cutover/migrations/restart/key rotation si el requisito ya está literalmente cubierto.
- **10.2 después de 10.1:** JOBS compila checklist; WOZ emite recomendación técnica; BBB actúa como revisor independiente; **RO decide alpha interna**.
- Alpha interna ≠ release público. Publicación sigue `NO-GO` hasta sus gates separados.

---

## Gate D6 requerido

- identidad `user / installation / tenant` derivada de sesión validada;
- auth + autorización + límites antes de trabajo costoso;
- ownership por objeto;
- matriz `401 / 403 / 413 / 429`;
- pruebas cross-tenant;
- **cero acceso o mutación cross-tenant** en suite adversarial.

**Hasta D6 PASS estructurado:** no iniciar 7.x.

---

## Evidencia compacta que no se debe reabrir

### 5.1 `[x]`
PRs #11–#28. Temporary auth productiva Web/Desktop; secretos permanentes no llegan al cliente. Transferencia directa probada de **1,992,294,400 bytes** con `galer_cloud_file_bytes=0`. Riesgos residuales shared-bot fallback y cleanup >48 h aceptados/documentados.

### 5.2 `[x]`
PRs #29–#42 + WAVE 3:
- PostgreSQL = autoridad productiva; rollback/durabilidad aceptados independientemente;
- restore PITR representativo: **RPO ~7 min**, **RTO 3643 s**;
- keyring productivo multiversión: activa `2`, versiones `1,2`, lectura de ciphertext v1 verificada;
- alarmas RDS críticas + on-call/rotation/rollback authority aceptados;
- cierre global WOZ/RO: Issue #41 comment `5448976400`.

---

## Tail externo / release que sigue vivo

No bloquea la ejecución interna de Fase 1, pero sí publicación cuando aplique:
- 2.2 hasta cierre administrativo final;
- 1.2 release governance/dependencias externas;
- rotación del OAuth client secret visible durante troubleshooting WAVE 3; no registrar su valor;
- deuda GPL `telegram@2.26.22` → `@cryptography/aes@0.1.1`;
- regresión de carga inicial asociada a 12.1;
- capacity gate 2×;
- revisión independiente externa;
- firma/notarización y pruebas físicas antes de soporte público por plataforma.

---

## Invariantes de producto/arquitectura

- Telegram es implementación interna oculta; UI habla de **Cloud / Galer Cloud / Storage / Library**.
- Schema preferido: **Galer T-Library Schema v2**.
- Web pura: **sin Tauri ni Desktop helper**.
- Media: **device ↔ provider directo**; Galer Cloud no relaya bytes de beats/proyectos.
- Permanent auth/control secrets quedan control-side; cliente usa temporary auth.
- Shared-bot es fallback solo cuando no hay bots libres; exclusividad por vault es camino normal.
- BeatGaler v1 no se publica free-only; si billing no pasa gates, se retrasa.
- YouTube es objetivo v1 Desktop/Web y Web no puede resolverlo llamando Tauri.

---

## Roles mínimos

- **JOBS:** dueño de `!!!PLAN`, prioridad, limpieza, coordinación AAA/BBB. No toca producto/infra.
- **WOZ:** jefe técnico/integrador; arquitectura, implementación, infraestructura y aceptación técnica.
- **AAA / BBB:** paquetes independientes; no cambian gates ni marcan cierre global.
- **RO / usuario:** autoridad final sobre alcance, riesgo aceptado y go/no-go.
- **Issue #41:** coordinación/handoffs/blockers; sin secretos.

---

## Estados

`[ ]` pendiente · `[ 🟡 ]` en progreso · `[ ⚠️ ]` técnicamente hecho pero gate/evidencia pendiente · `[ 🔴 ]` bloqueado · `[ ⏸️ ]` pausado · `[x]` cerrado con evidencia.

---

## Mapa de fases

- **Fase 0:** `[ 🟡 ]` residual/administrativa; trabajo técnico necesario para avanzar concluido.
- **Fase 1:** **ACTIVA — Día 6 CLOSEOUT**.
- **Fases 2–7:** no ejecutar todavía.

**Principio de velocidad:** si una información no cambia prioridad, dependencia, gate, riesgo aceptado, evidencia o NEXT, no pertenece al camino operativo.