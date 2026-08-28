# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar y publicar BeatGaler lo más rápido posible **sin rebajar gates reales**.
> Este archivo es el tablero de ejecución. El detalle técnico vive en la fase aplicable y en GitHub; no se duplica aquí.

## Lectura rápida obligatoria

### Para cualquier trabajo
1. Leer **este archivo completo**.
2. Leer **solo la fase activa** y la tarea que se va a ejecutar.
3. Consultar el estado actual necesario en GitHub / Issue #41.
4. Leer `Gates - Publicación y contingencias.md` **solo** cuando la tarea afecte release, seguridad, go/no-go o contingencias.
5. Abrir `00 - Contexto global y criterios.md`, fases futuras o documentación histórica **solo si la tarea lo necesita**.

### JOBS
`Eres JOBS. Lee !!!PLAN y continúa.` ya **NO significa releer Fases 0–7 + todo el Registro + todo Gates** en cada ciclo.

JOBS normalmente lee:
- `Plan Maestro.md`;
- fase activa;
- últimos avances relevantes;
- Issue #41.

JOBS hace auditoría completa de `!!!PLAN` solo al **cambiar de fase**, detectar una **contradicción/desincronización**, aparecer un **gate nuevo real**, o por petición explícita del usuario.

### Archivo protegido
`Plan Maestro 2208 copy DONT TOUCH .md` es histórico. **No modificar ni usar como plan vigente.**

---

## Reglas no negociables

1. No saltar dependencias ni gates reales.
2. No marcar `[x]` sin evidencia verificable.
3. Antes de un cambio técnico: auditoría read-only del estado real.
4. Después de un cambio técnico relevante: pruebas afectadas + CI aplicable.
5. Cada avance que cambie estado actualiza: **Plan Maestro + fase activa + Registro de avances**.
6. No duplicar logs/diffs extensos en `!!!PLAN`; usar PR, Actions e Issue #41 como evidencia detallada.
7. Ningún P0/P1 abierto al publicar.
8. JOBS solo modifica `!!!PLAN`; WOZ decide/ejecuta código, arquitectura e infraestructura.

**Precedencia si hay conflicto:** Estado/reglas de este Plan → gate/checklist de fase activa → Gates → Contexto. GitHub/runtime decide los hechos técnicos actuales.

---

## Estado vivo — AHORA

- **Fase activa:** Fase 0 — Contención e integración.
- **Release público:** 🔴 `NO-GO`.
- **BeatGaler:** `integration-v0.8.0-alpha.1` @ `a968122127c584b5557b25e70a21eb64f75b3c0e`, versión `0.8.0-alpha.1`.
- **Tarea 5.1:** `[x]`.
- **Tarea 5.2:** `[x]` — **CERRADA por síntesis WOZ/RO** en Issue #41 comment `5448976400`. Los 4/4 criterios WAVE 3 quedaron aceptados. No repetir restore/cutover/migrations/durability restart/key rotation para 5.2 salvo evidencia nueva que invalide el resultado.
- **Tarea 2.2:** `[ 🟡 ]` **P0 / foco técnico inmediato**. WOZ/RO aprobó `GO` para purga histórica **selectiva y coordinada**; falta ejecución destructiva + cleanup GitHub-side + verificación post-purge.
- **Tarea 1.2:** `[ 🟡 ]` **P1 / paralelo externo**. Release governance, dominio/DNS/support/status, Authenticode, revisión legal/seguridad independiente y matriz física/testers siguen pendientes. Apple Developer = `PENDING — DEFERRED`.
- **Fase 1:** bloqueada hasta cerrar los gates restantes de Fase 0.

### Fase 0 — tablero

| Tarea | Estado |
|---|---|
| 0.1 Congelar evidencia | [x] |
| 0.2 Checkpoint interno / NO-GO | [x] |
| 1.1 Decisiones de negocio | [x] |
| 1.2 Dependencias externas de release | [ 🟡 ] P1 |
| 2.1 Contención inmediata | [x] |
| 2.2 Historial Git / incidente | [ 🟡 ] P0 |
| 3.1 Base integrada | [x] |
| 3.2 Contrato plataforma | [x] |
| 4.1 Required CI | [x] |
| 4.2 Supply chain | [x] |
| 5.1 Trust boundary / Direct | [x] |
| 5.2 PostgreSQL + recovery + secrets | [x] |

---

## NEXT — orden de ejecución

### 1. WOZ — Tarea 2.2 `[ 🟡 ]` P0
Ejecutar la purga histórica selectiva autorizada respetando el procedimiento de Fase 0. No convertirla en rewrite genérico y no revocar credenciales solo por la evidencia actual.

**Salida:** historial sensible identificado ya no alcanzable, cleanup GitHub-side realizado cuando aplique, fresh-clone verification + Required CI verdes.

### 2. RO/JOBS — Tarea 1.2 `[ 🟡 ]` P1 en paralelo
Cerrar dependencias que realmente bloquean release, sin distraer a WOZ del P0:
- corregir governance/provenance del canal público de releases;
- dominio/DNS/support/status;
- Windows Authenticode;
- reservas de revisión legal + seguridad independiente;
- matriz anónima 12–20 testers / hardware físico;
- Apple Developer sigue diferido hasta reactivación explícita.

### 3. Security follow-up antes de release
Rotar el OAuth client secret que fue visible al operador durante troubleshooting de WAVE 3. Su valor **no** debe registrarse en GitHub/`!!!PLAN`.

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

## Bloqueos de release que siguen vivos

No son el trabajo principal de hoy, pero **no deben olvidarse**:
- 2.2 historial Git;
- 1.2 release governance/dependencias externas;
- OAuth secret rotation de seguimiento;
- deuda GPL `telegram@2.26.22` → `@cryptography/aes@0.1.1`;
- regresión de carga inicial asociada a 12.1;
- capacity gate 2×;
- revisión independiente externa;
- firma/notarización y pruebas físicas antes de anunciar soporte público de cada plataforma.

---

## Invariantes de producto/arquitectura

- Telegram es implementación interna oculta; UI habla de **Cloud / Galer Cloud / Storage / Library**.
- Schema visible/interno preferido: **Galer T-Library Schema v2**.
- Web es una app Web pura: **sin Tauri ni Desktop helper**.
- Media viaja **device ↔ provider directo**; Galer Cloud no relaya bytes de beats/proyectos.
- Permanent auth/control secrets permanecen control-side; cliente usa temporary auth.
- Shared-bot es fallback solo cuando no hay bots libres; exclusividad por vault es el camino normal.
- BeatGaler v1 no se publica como free-only; si billing no pasa gates, se retrasa.
- YouTube es objetivo v1 tanto en Desktop como Web y Web no puede resolverlo llamando Tauri.

---

## Roles mínimos

- **JOBS:** dueño de `!!!PLAN`, prioridad, limpieza y coordinación AAA/BBB. No toca producto/infra.
- **WOZ:** jefe técnico e integrador; decide arquitectura, implementación, infraestructura y aceptación técnica.
- **AAA / BBB:** paquetes independientes; no cambian gates ni marcan tareas `[x]` por sí solos.
- **Issue #41:** coordinación/handoffs/blockers. No duplicar allí ni aquí datos secretos.

Detalles solo cuando hagan falta: `Equipo multi-IA - Roles y coordinación.md`.

---

## Estados

`[ ]` pendiente · `[ 🟡 ]` en progreso · `[ ⚠️ ]` técnicamente hecho pero gate/evidencia pendiente · `[ 🔴 ]` bloqueado · `[ ⏸️ ]` pausado · `[x]` cerrado con evidencia.

---

## Mapa de fases

- **Fase 0:** ACTIVA — faltan 2.2 y 1.2.
- **Fases 1–7:** no leer ni ejecutar todavía salvo dependencia explícita. Se activan una por una.

**Principio de velocidad:** si una información no cambia prioridad, dependencia, gate, riesgo aceptado, evidencia o NEXT, no pertenece al camino operativo del Plan Maestro.