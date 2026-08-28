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