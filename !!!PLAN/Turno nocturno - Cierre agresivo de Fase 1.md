# BeatGaler — Turno nocturno / cierre agresivo de Fase 1

> Complementa `Equipo multi-IA - Roles y coordinación.md` → `Modo autónomo / turno nocturno`. No cambia roadmap, requisitos, gates, autoridad de roles ni orden de Fase 1.

## Objetivo nocturno

El objetivo de cada noche autónoma es **cerrar el máximo número de gates consecutivos posible**, idealmente completar toda Fase 1, sin rebajar evidencia ni saltar dependencias.

Orden inmutable:

`6.1 ∥ 6.2` → `D6` → `7.1 ∥ 7.2` → `D7` → `8.1 ∥ 8.2` → `D8` → `9.1 ∥ 9.2` → `D9` → `10.1` → `10.2`.

Un Día posterior no se ACTIVA antes del PASS del gate anterior. Sí se permite **pre-stage de coordinación**: preparar assignments, matriz REUSE/GAP, evidencia esperada y artefactos read-only para que el siguiente ciclo empiece inmediatamente después del PASS.

## Principio de throughput

JOBS debe optimizar siempre el **camino crítico del gate activo**.

Prioridad, en este orden:
1. blocker material que impide PASS del gate actual;
2. evidencia obligatoria faltante para ese gate;
3. review independiente del delta que puede cerrar el blocker;
4. CI/integración necesaria para decisión del gate;
5. solo después, trabajo secundario dentro del mismo Día.

Findings que no bloquean el gate se registran y se posponen al momento correcto del roadmap. No deben consumir ciclos mientras exista un blocker crítico más directo.

## Regla detecta → resuelve

Un blocker nuevo puede ocupar como máximo un ciclo de descubrimiento antes de convertirse en trabajo de resolución.

- Ciclo N: agente detecta blocker con evidencia reproducible.
- Siguiente ejecución disponible del owner técnico: debe **resolverlo o producir evidencia nueva que demuestre por qué no es resoluble todavía**.
- JOBS no puede reenviar simplemente `continúa`, `sigue pendiente` o `reintenta`.
- Si la orden original no produjo progreso, JOBS emite `CORRECTIVE ASSIGNMENT` con una acción concreta.

Un blocker conocido no debe sobrevivir varias rondas únicamente como texto repetido.

## Assignment orientado a cierre

Toda orden autónoma de JOBS debe responder:

```text
CLOSURE ASSIGNMENT
ROLE: <AAA | BBB | WOZ>
GATE: <D6 | D7 | D8 | D9 | D10>
TASK: <tarea exacta>
CRITICAL_BLOCKER: <único blocker principal>
DO_NOW: <acción concreta que puede cerrar o reducir el blocker>
DO_NOT: <trabajo ya aceptado / fuera de scope / re-review innecesario>
EVIDENCE_REQUIRED: <prueba exacta de cierre>
ARTIFACT_TO_REUSE: <PR/rama/SHA/test existente>
STOP_WHEN: <condición>
NEXT_IF_PASS: <acción inmediata hacia gate>
NEXT_IF_FAIL: <evidencia nueva que JOBS necesita>
```

Preferir **un blocker principal por owner** antes que listas difusas de tareas.

## Review incremental

BBB no debe reauditar desde cero en cada ciclo.

Después de un review válido:
- findings ya corregidos + aceptados no se reabren sin delta/evidencia nueva;
- BBB revisa únicamente el nuevo SHA/delta y requisitos aún no probados;
- review completo solo ante cambio arquitectónico material o desync factual.

Objetivo: que el review sea una etapa de cierre, no un loop infinito.

## Integración rápida de WOZ

Cuando estén presentes:
- implementación necesaria;
- review requerido;
- tests afectados verdes;
- Required CI aplicable verde;
- requisitos del gate demostrados;

WOZ debe priorizar integración + decisión estructurada del gate en esa misma ejecución. No debe diferir el cierre por trabajo secundario no bloqueante.

Si falta exactamente una evidencia, WOZ debe nombrarla como `LAST BLOCKER` y asignar el siguiente movimiento más corto para producirla.

## Pre-stage del Día siguiente

Mientras el gate actual está en validación final, JOBS puede preparar sin activar:
- owner de cada tarea del siguiente Día;
- scope/out-of-scope;
- ramas/PRs que deberán reutilizarse si existen;
- tests/evidencia requeridos;
- matriz REUSE/GAP cuando aplique;
- orden de reviews.

Formato:

```text
PRE-STAGED — DO NOT START BEFORE GATE PASS
NEXT_GATE: <D+1>
WOZ: <assignment preparada>
AAA: <assignment preparada>
BBB: <review preparada>
REUSE: <evidencia ya disponible>
GAPS: <solo gaps conocidos>
```

En cuanto JOBS verifica PASS del gate actual, convierte ese pre-stage en asignación ACTIVA sin esperar intervención humana, salvo `RO DECISION REQUIRED`.

## REUSE-FIRST agresivo para Día 9 y Día 10

D9/D10 no deben convertirse en repetición de Fase 0/5.2.

JOBS debe construir primero:

`REQUISITO → evidencia aceptada → REUSE | GAP`

Evidencia ya disponible incluye, cuando satisfaga literalmente el requisito:
- PostgreSQL autoridad productiva;
- migrations/versionado/constraints;
- importer/idempotencia/rollback;
- durability restart + fail-closed;
- PITR restore representativo;
- RPO ~7 min;
- RTO 3643 s;
- keyring multiversión;
- observabilidad/on-call/rollback authority.

Solo un `GAP` literal recibe trabajo nuevo. Está prohibido repetir restore, cutover, migrations, durability restart o key rotation únicamente para recrear evidencia aceptada.

## Escalada temprana

Un blocker que requiera RO, credencial externa, proveedor externo o acción humana no debe descubrirse al final de la noche.

En el primer ciclo donde sea verificable:

```text
RO DECISION REQUIRED
DECISION:
WHY_BLOCKING_CURRENT_GATE:
OPTIONS:
RECOMMENDATION:
CAN_CONTINUE_WITHOUT_IT: yes | no
```

Si existen otras tareas seguras dentro del mismo Día que no dependan de esa decisión, JOBS las mantiene avanzando en paralelo.

## Definición de una noche exitosa

Orden de éxito:
1. Fase 1 cerrada con evidencia válida;
2. si no, máximo número de gates consecutivos cerrados;
3. si un gate queda abierto, debe quedar reducido al menor número de blockers materiales posible;
4. cero claims no verificados;
5. cero duplicación relevante;
6. cada blocker restante tiene owner + acción concreta + evidencia requerida.

`Muchos comentarios`, `muchos reviews` o `muchas horas ejecutadas` no son métricas de éxito. **Gates cerrados y blockers eliminados sí.**
