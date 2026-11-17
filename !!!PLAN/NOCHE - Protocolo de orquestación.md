# BeatGaler — Protocolo de orquestación nocturna

**Sesión:** `NIGHT-2026-08-29`  
**Autoridad:** decisión RO explícita en conversación del 2026-08-29.  
**Jefe de la noche:** **JOBS**.

## Meta global

Maximizar la probabilidad de llegar al amanecer con **Fases 0, 1, 2, 3 y 4 cerradas o con el mínimo número posible de blockers reales**, sin rebajar requisitos ni fabricar evidencia.

Orden de prioridad:
1. **Terminar F0–F4.**
2. **Sencillez:** camino mínimo, REUSE-FIRST, cero trabajo ceremonial.
3. **Limpieza:** sin duplicados, sin owners solapados, sin deuda creada solo para avanzar rápido.

La meta es deliberadamente agresiva. Si un prerequisito externo impide cerrar algo (certificados, cuentas de proveedor, decisión RO, etc.), el éxito de la noche es dejar ese blocker reducido, factual y accionable; nunca marcarlo DONE por conveniencia.

## Arquitectura de la noche

JOBS dirige. AAA, BBB y WOZ son workers ejecutores.

- JOBS puede leer/escribir los cuatro markdowns nocturnos y el resto de `!!!PLAN` dentro de su autoridad normal.
- AAA/BBB/WOZ **no se autoasignan trabajo**.
- Cada worker ejecuta únicamente `ASIGNACIÓN VIGENTE` de su markdown.
- Al terminar su turno, el worker actualiza únicamente su propio `NOCHE - <ROL>.md`, deja evidencia y se detiene.
- Excepción RO nocturna: AAA/BBB/WOZ pueden escribir **solo su markdown nocturno** dentro de `!!!PLAN` para reportar el turno. No adquieren permiso para editar Plan Maestro, fases, Gates, Registro ni markdowns de otros roles.
- JOBS procesa los resultados en su siguiente ciclo y decide la siguiente asignación.

## Cadencia fija

Ciclo nominal de 60 minutos:

- `T+00` — **JOBS**: preflight global, lee resultados, actualiza tablero y asignaciones.
- `T+15` — **AAA**: ejecuta su asignación vigente, reporta y STOP.
- `T+30` — **BBB**: ejecuta su asignación vigente, reporta y STOP.
- `T+45` — **WOZ**: ejecuta su asignación vigente, reporta y STOP.
- `T+60` — **JOBS**: comienza el siguiente ciclo.

El desfase de 15 minutos **no crea dependencia secuencial**. Los workers deben trabajar áreas diferentes. Su ventaja es que cada turno ve GitHub/Issue #41 más reciente.

Si un turno se ejecuta tarde, no se falsea el reloj: se hace preflight factual y se procesa la asignación vigente una sola vez.

## Assignment IDs

Toda orden JOBS debe usar un ID monotónico por worker:

- `NIGHT-AAA-001`, `NIGHT-AAA-002`, ...
- `NIGHT-BBB-001`, `NIGHT-BBB-002`, ...
- `NIGHT-WOZ-001`, `NIGHT-WOZ-002`, ...

Un worker solo procesa una asignación si:
- `ASSIGNMENT_STATUS: ASSIGNED`;
- el ID no figura ya como procesado en su historial.

Al terminar cambia el estado a `DONE`, `BLOCKED`, `PENDING` o `STALLED` y registra ese mismo Assignment ID. Esto evita ejecutar dos veces una orden vieja.

## Reparto y aislamiento

En cada ciclo JOBS busca máximo paralelismo con mínimo overlap.

Reglas:
1. Un archivo/rama/PR o slice material tiene un solo owner en un ciclo.
2. JOBS no asigna simultáneamente a dos workers cambios sobre el mismo núcleo cuando pueda evitarlo.
3. Si una tarea quedó esperando CI/proveedor/acción humana, JOBS puede en el siguiente ciclo dejarla PENDING y asignar al worker otra pieza independiente de su área.
4. Cambio de área/owner se decide únicamente al inicio de un ciclo JOBS y se registra en los markdowns afectados + Issue #41 si es material.
5. Un worker nunca roba una tarea porque quedó dependency-ready.

Áreas iniciales recomendadas para esta sesión:
- **AAA:** F2 — Web / UX / frontend de producto.
- **BBB:** F4 — Desktop / packaging / release chain.
- **WOZ:** F1 — seguridad/datos; tras cierre factual de F1, JOBS puede moverlo a F3 técnico/operación si no crea overlap.
- **JOBS:** coordinación global, `!!!PLAN`, sequencing, owners y cierre documental; sin producto/infra.

JOBS puede redistribuir estas áreas para maximizar F0–F4, pero debe hacerlo explícitamente y sin dos owners simultáneos sobre la misma pieza.

## Preflight obligatorio de cada turno

Antes de actuar:
1. leer `!!!PLAN/Plan Maestro.md` y la fase/área aplicable;
2. leer su markdown nocturno completo;
3. leer Issue #41 desde el último timestamp relevante;
4. verificar `integration-v0.8.0-alpha.1` HEAD real;
5. verificar PR/rama/head/base/CI aplicables;
6. duplicate-check;
7. comprobar si otro owner ya procesó la pieza;
8. comprobar que el Assignment ID sigue vigente.

GitHub/runtime más reciente prevalece sobre texto nocturno stale. Si el dato material no se puede verificar: `PENDING`.

## REUSE-FIRST / camino mínimo

Antes de crear rama, PR, script, drill o nueva implementación:
- buscar evidencia/artefacto existente;
- reutilizar si satisface literalmente el requisito;
- no repetir CI/drill productivo solo para fabricar evidencia nueva;
- no abrir PR duplicado;
- no reescribir una solución estable sin gap material.

## Evidence-before-claim

Nunca declarar `DONE`, `PASS`, `INTEGRATED`, `[x]` o fase cerrada sin evidencia aplicable.

Cuando corresponda registrar:
- branch/head SHA;
- base exacta;
- PR;
- tests;
- CI exact-head;
- runtime/staging/provider evidence;
- merge SHA;
- `UNVERIFIED` explícito.

## Política de integración y carreras

Antes de integrar:
1. verificar head exacto del candidate;
2. verificar HEAD de integración;
3. verificar que la evidencia verde corresponde a esa combinación;
4. si cambió materialmente el baseline, refresh/union y CI aplicable de nuevo;
5. usar el flujo de integración autorizado del owner;
6. comprobar el SHA resultante después de merge.

JOBS no bypassa integraciones técnicas que correspondan al owner.

## Qué hace un worker al terminar

Debe escribir en su markdown:

```text
LAST_PROCESSED_ASSIGNMENT: NIGHT-<ROL>-NNN
TURN_STATUS: DONE | BLOCKED | PENDING | STALLED
BASE_BEFORE:
HEAD_AFTER:
PR:
CHANGES:
TESTS:
CI:
EVIDENCE:
UNVERIFIED:
BLOCKERS:
RECOMMENDATION_TO_JOBS:
TURN_FINISHED_AT:
```

Después **STOP**. No toma la siguiente tarea por sí mismo.

## Qué hace JOBS cada hora

1. Preflight global factual.
2. Lee los tres resultados nocturnos.
3. Procesa handoffs de Issue #41 que hayan aparecido.
4. Sincroniza `!!!PLAN` cuando existe cambio factual que lo amerite.
5. Recalcula camino crítico F0→F4.
6. Busca tres piezas simultáneas con mínimo overlap.
7. Escribe una nueva `ASIGNACIÓN VIGENTE` para cada worker que pueda progresar.
8. Si un worker está bloqueado, reduce el blocker o lo mueve explícitamente a otra pieza independiente.
9. Mantiene su propio tablero y log de decisiones.
10. No espera perfección documental antes de asignar trabajo dependency-safe; primero conserva el sistema trabajando, luego sincroniza sin mentir.

## STOP global

La sesión nocturna solo termina cuando ocurra uno:
- F0–F4 están factual y documentalmente cerradas según sus gates reales;
- no queda ningún trabajo ejecutable sin una decisión/credencial/acción externa del RO;
- el RO detiene la sesión.

El release público continúa sujeto a sus gates propios. Completar F0–F4 no autoriza por sí solo publicación pública.

## Blockers humanos conocidos

Un blocker de proceso que requiera UI/credencial humana se registra de inmediato para que el RO pueda resolverlo una sola vez y devolver autonomía a la noche.

Para el arranque de esta sesión, PR #51 se ha observado `OPEN / DRAFT`; el connector disponible no ha podido ejecutar Draft→Ready. Mientras siga Draft, BBB no puede integrarlo por el flujo autorizado. La acción humana mínima es poner #51 en **Ready for review** sin cambiar head/base.

## Fuente de verdad

Orden de autoridad factual:
1. runtime/proveedor cuando el requisito es productivo;
2. GitHub actual (branch/PR/SHA/CI);
3. Issue #41 handoffs;
4. `!!!PLAN` sincronizado;
5. markdown nocturno.

El markdown nocturno es un **buzón operativo**, no una licencia para contradecir evidencia más reciente.
