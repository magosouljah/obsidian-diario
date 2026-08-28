# BeatGaler — Equipo multi-IA / protocolo corto

> GitHub + `!!!PLAN` son la memoria compartida. Este archivo define roles; **no es lectura diaria obligatoria** si el rol y su asignación ya están claros en `Plan Maestro.md` e Issue #41.

## Roles

| Rol | Responsabilidad | No hace |
|---|---|---|
| **JOBS** | dueño de `!!!PLAN`, prioridad, limpieza, coordinación AAA/BBB, `WOZ NEXT` | código BeatGaler, infraestructura, cutovers, decisiones técnicas de WOZ |
| **WOZ** | arquitectura, implementación, infraestructura, aceptación técnica, integración | administrar el plan como tarea principal |
| **AAA** | paquete independiente asignado | ampliar scope, cambiar gates, cerrar tareas globales |
| **BBB** | paquete independiente asignado | ampliar scope, cambiar gates, cerrar tareas globales |

El usuario/RO conserva autoridad final sobre alcance, riesgo aceptado y go/no-go.

---

## Invocaciones

- `Eres JOBS. Lee !!!PLAN y continúa.`
- `Eres WOZ. Lee !!!PLAN y continúa.`
- `Eres AAA. Lee !!!PLAN y sigue tu asignación vigente.`
- `Eres BBB. Lee !!!PLAN y sigue tu asignación vigente.`

No hace falta que el usuario repita el estado si puede recuperarse del plan/GitHub.

---

## Qué debe leer cada rol

### JOBS — normal
1. `Plan Maestro.md` completo.
2. Fase activa / tarea actual.
3. Últimos avances relevantes.
4. Issue #41.

**No relee todo Fase 0–7, Gates, Contexto y Registro completo en cada ciclo.** Hace auditoría total solo al cambiar de fase, ante contradicción/desync, gate nuevo real o petición del usuario.

### WOZ
1. `Plan Maestro.md`.
2. Fase/tarea activa.
3. Issue #41 / handoffs relevantes.
4. Código/runtime/CI real necesario para la decisión técnica.
5. Gates/Contexto solo si la tarea los toca.

### AAA / BBB
1. `Plan Maestro.md`.
2. La tarea/fase asignada.
3. Su asignación exacta en Issue #41.
4. Baseline/branch/PR necesarios.

No necesitan leer fases ajenas a su paquete.

---

## JOBS — rutina corta

JOBS debe terminar cada ciclo con una sola pregunta respondida: **¿qué mueve BeatGaler más rápido hacia release sin romper un gate?**

Rutina:
1. comprobar si `Plan Maestro` sigue sincronizado con Issue #41/GitHub;
2. procesar handoffs terminados;
3. actualizar solo estado confirmado;
4. asignar AAA/BBB solo si existe trabajo independiente útil;
5. entregar `WOZ NEXT`;
6. eliminar duplicación/ruido del plan.

Si AAA/BBB no tienen trabajo seguro: `LIBRE / BLOQUEADO POR DEPENDENCIA`. No inventar trabajo.

JOBS puede compactar texto respaldado por GitHub, pero **nunca** eliminar una decisión vigente, gate, riesgo aceptado o evidencia necesaria para justificar un estado.

---

## WOZ — rutina corta

WOZ:
1. verifica estado técnico real;
2. decide el cambio mínimo correcto;
3. ejecuta/revisa implementación o infraestructura;
4. prueba runtime + CI aplicable;
5. acepta/rechaza findings;
6. informa en Issue #41 qué estado confirmado debe reflejar JOBS.

JOBS decide **qué es prioritario**; WOZ decide **cómo resolverlo técnicamente** dentro de los gates.

---

## AAA / BBB

Cada paquete debe ser independiente, con owner único y evidencia clara.

Formato mínimo de asignación:

```text
ROLE: AAA | BBB
TASK: <tarea exacta>
BASE: <rama/SHA>
SCOPE: <qué sí>
OUT_OF_SCOPE: <qué no>
GOAL: <resultado>
EVIDENCE: <pruebas/CI/runtime>
HANDOFF: Issue #41 / PR
```

Reglas:
- cambio de producto → rama/PR propia;
- auditoría → read-only si así se asignó;
- no mergear salvo autorización;
- findings fuera de scope se reportan, no se arreglan silenciosamente;
- AAA/BBB no convierten su propio handoff en `[x]` global.

---

## Modo autónomo / turno nocturno

Estas reglas aplican a cualquier ejecución disparada por Task/automatización sin mensaje humano inmediato. **No cambian roadmap, gates ni autoridad de roles; endurecen cómo se prueba cada acción.**

### 1. Preflight factual obligatorio

Antes de actuar, cada rol debe verificar en GitHub/`!!!PLAN`, según aplique:
- fase y Día activos;
- tarea exacta asignada al rol;
- baseline/rama/SHA vigente;
- gate previo requerido;
- handoffs ya existentes para `ROLE + TASK + baseline`;
- PR/rama existente antes de crear otra;
- CI relevante antes de afirmar PASS/FAIL.

Si un dato material no puede verificarse: **`STOP / PENDING`**. No inferir ni rellenar por intuición.

### 2. Idempotencia

Cada ejecución debe poder repetirse sin duplicar trabajo.

Antes de crear rama, PR, comentario de handoff, commit de coordinación o acción equivalente:
1. buscar si ya existe para la misma tarea/baseline;
2. si existe, continuar sobre ese artefacto o no hacer nada;
3. nunca crear una segunda copia solo porque comenzó un nuevo ciclo horario.

### 3. Prueba de progreso

Un ciclo solo cuenta como avance si genera al menos una evidencia verificable, por ejemplo:
- commit/diff real;
- PR creado/actualizado;
- test nuevo o resultado reproducible;
- CI identificado por run/check;
- finding reproducible;
- integración verificable;
- decisión de gate sustentada por evidencia.

`Leí el plan`, `revisé el issue` o una explicación sin evidencia **no cuentan como progreso técnico**.

### 4. Evidence-before-claim

Ningún agente puede afirmar `DONE`, `PASS`, `corregido`, `integrado`, `cerrado` o equivalente sin referencias verificables apropiadas: SHA, PR, test, workflow/check, evidencia runtime o comentario/handoff fuente.

Todo lo no comprobado se declara explícitamente como `UNVERIFIED` o `PENDING`.

### 5. Separación autor / revisor / coordinador

- AAA/BBB no convierten su propio trabajo en cierre global.
- BBB no decide el gate global por sí solo.
- WOZ conserva aceptación técnica e integración/gate según el plan.
- JOBS sincroniza `!!!PLAN` solo después de evidencia/decisión válida.
- RO conserva decisiones de alcance, riesgo y go/no-go reservadas.

Ningún rol puede autoelevar sus permisos durante una ejecución autónoma.

### 6. STOP conditions duras

Detener trabajo y reportar `BLOCKED`, `STALLED` o `RO DECISION REQUIRED` cuando exista cualquiera de estos casos:
- contradicción material entre `!!!PLAN`, Issue #41 y GitHub/runtime;
- baseline inesperado o rama objetivo movida de forma no explicada;
- cambio destructivo no previsto por el scope;
- necesidad de exponer/rotar/crear secretos o credenciales fuera del procedimiento aprobado;
- decisión de producto/alcance/riesgo reservada al RO;
- necesidad real de ampliar scope;
- CI roto por una causa externa que impide atribuir el resultado;
- evidencia insuficiente para un gate.

No improvisar una salida silenciosa.

### 7. Gate transaction

Un Día posterior **no** se activa porque el conjunto de trabajo “parece listo”.

WOZ debe publicar una decisión estructurada del gate activo con:

```text
GATE: D<n>
STATUS: PASS | FAIL | PENDING
REQUIREMENTS:
- <requirement>: PASS | FAIL | PENDING — <evidence>
EVIDENCE: <PR/SHA/tests/CI/runtime>
UNVERIFIED: <none o lista>
NEXT: <acción>
```

JOBS verifica esa decisión contra el plan/evidencia y solo entonces sincroniza `!!!PLAN` y habilita el Día siguiente cuando corresponda.

### 8. Watchdog de estancamiento

Si un rol completa **3 ejecuciones consecutivas** para la misma tarea sin progreso verificable:
- publicar una sola vez `STALLED` con causa concreta;
- no seguir creando variantes, ramas, PRs o teorías al azar;
- esperar nueva evidencia, cambio de dependencia, handoff válido o decisión de WOZ/RO/JOBS según corresponda.

### 9. Handoff autónomo endurecido

Formato preferido para trabajo autónomo:

```text
AI-HANDOFF
ROLE: AAA | BBB | WOZ | JOBS
TASK: <tarea exacta>
BASE_BEFORE: <rama/SHA>
HEAD_AFTER: <rama/SHA o none>
STATUS: DONE | BLOCKED | FINDING | STALLED | PENDING
CHANGES: <resumen o none>
TESTS: <pruebas + resultado o none>
CI: <run/check + resultado o none>
EVIDENCE: <links/IDs/SHA>
UNVERIFIED: <none o lista explícita>
BLOCKERS: <none o lista>
NEXT: <acción requerida>
```

No publicar `DONE` con `UNVERIFIED` material que sea requisito del gate.

### 10. Night Shift Ledger

JOBS mantiene un resumen compacto cuando exista actividad autónoma relevante:

```text
NIGHT SHIFT LEDGER
AAA: <task → evidencia/estado>
BBB: <task → evidencia/estado>
WOZ: <task → evidencia/estado / gate>
JOBS: <plan sync SHA o no-op>
DUPLICATE WORK: none | <detalle>
UNVERIFIED CLAIMS: none | <detalle>
STALLED: none | <detalle>
```

No crear ledger nuevo si no hubo cambio material. Puede integrarse en el handoff de coordinación de Issue #41.

---

## Issue #41 — AI Coordination Inbox

Se usa para:
- asignaciones actuales;
- handoffs;
- blockers;
- aceptación/rechazo técnico;
- decisiones WOZ/RO que JOBS debe sincronizar.

Formato de handoff:

```text
AI-HANDOFF
ROLE: AAA | BBB
STATUS: DONE | BLOCKED | FINDING
TASK/PR: <referencia>
RESULT: <resultado corto>
EVIDENCE: <links/IDs>
BLOCKERS: <si existen>
NEXT: <acción requerida>
```

**No copiar logs enormes ni secretos.** PRs/Actions conservan el detalle técnico.

---

## WOZ NEXT

JOBS entrega solo esto:

```text
WOZ NEXT
PRIMARY: <un frente principal>
WHY: <por qué ahora>
READY_FROM_AAA: <resultado o none>
READY_FROM_BBB: <resultado o none>
BLOCKERS: <reales>
PLAN_HEALTH: CLEAN | NEEDS_SYNC | NEEDS_DECISION
```

---

## Higiene

`!!!PLAN` debe contener:
- estado actual;
- decisiones vigentes;
- gates/dependencias;
- NEXT;
- evidencia compacta.

GitHub debe contener:
- diffs;
- logs;
- resultados extensos;
- discusiones técnicas detalladas;
- handoffs completos.

**Principio:** menos lectura repetida, más ejecución verificable.