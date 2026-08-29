# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE LA NOCHE

**Terminar Fases 0, 1, 2, 3 y 4 o reducirlas al mínimo número factual de blockers externos antes del amanecer.**

Prioridades:
1. terminar F0–F4;
2. sencillez;
3. limpieza.

No rebajar gates para fingir progreso.

## PODER OPERATIVO NOCTURNO

Por autorización RO de esta sesión:
- JOBS dirige AAA, BBB y WOZ;
- JOBS puede leer y reescribir `NOCHE - JOBS.md`, `NOCHE - AAA.md`, `NOCHE - BBB.md` y `NOCHE - WOZ.md`;
- JOBS asigna el trabajo de cada worker para el siguiente despertar;
- JOBS puede cambiar el área de un worker al inicio de un ciclo si mejora el camino crítico y no crea overlap;
- cada cambio material de owner se registra claramente;
- JOBS conserva sus límites normales: no implementa código BeatGaler, no toca infraestructura y no inventa soluciones técnicas de WOZ.

## RUTINA OBLIGATORIA AL DESPERTAR

1. Leer COMPLETO:
   - `!!!PLAN/Plan Maestro.md`;
   - fase(s) activas relevantes;
   - `!!!PLAN/Registro de avances.md`;
   - `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`;
   - `!!!PLAN/NOCHE - Protocolo de orquestación.md`;
   - los cuatro markdowns `NOCHE - *.md`.
2. Leer Issue #41 desde el último ciclo.
3. Verificar HEAD real de `integration-v0.8.0-alpha.1`.
4. Verificar PRs/CI/heads de todos los workers activos.
5. Procesar resultados del ciclo previo.
6. Actualizar `!!!PLAN` cuando exista estado confirmado nuevo.
7. Recalcular el camino crítico completo F0–F4.
8. Escribir exactamente una asignación vigente por worker que pueda avanzar.
9. No asignar dos workers a la misma pieza material.
10. Registrar el ciclo en `LOG DE DECISIONES`.

## SNAPSHOT FACTUAL DE ARRANQUE

> Este snapshot es solo bootstrap. En cada ciclo GitHub/Issue #41 debe revalidarse.

- F0: cerrada históricamente; no reabrir sin nueva evidencia material.
- Integración al snapshot: `integration-v0.8.0-alpha.1 @ 6c4499d124a64d138e791ea4abf0091766dde7e9`.
- F1 / D8: PASS.
- F1 / D9: WOZ handoff Issue #41 `5460959369` = `DONE / PASS`, sin nuevo código por REUSE-FIRST.
- F1 / D10: siguiente frente natural; 10.1 puede auditar/reutilizar evidencia, 10.2 contiene alpha y decisión final RO.
- F2 / 11.2: AAA creó PR #54 `aaa/f2-11.2-auth-ui @ e5aefa9fb6bda8a3f0e44c15ec7ae13084502ab5`; handoff `5460950384` = PENDING solo por finalización de Required CI #459 al último check.
- F2 restantes después de 11.2: 12.1; 13.1/13.2; 14.1/14.2; 15.1/15.2/15.3.
- F3: Días 16–20 permanecen mayormente abiertos; contienen dependencias externas reales de producción/pagos/legal además de trabajo técnico.
- F4 / 21.1+21.2: BBB exact head #51 `362d69811da112c3b73f68c2e736455b05ed5dc4`, evidence técnica verde; PR sigue `OPEN / DRAFT` al handoff `5460933229`, por lo que integración PENDING.
- F4 después de 21: Día 22 signing Windows; Día 23 signing/notarization macOS; Día 24 updater/provenance/rollback; Día 25 matriz/freeze. Algunos requieren credenciales/membership/acciones externas.
- Release público: NO-GO.

## CAMINO CRÍTICO DE ARRANQUE

### AAA — área inicial F2
Primero cerrar/revalidar PR #54 / 11.2. Si queda DONE, JOBS elige en el siguiente ciclo el slice F2 dependency-safe con mayor impacto para cerrar F2, evitando overlap con otros workers.

### BBB — área inicial F4
Primero cerrar #51. Si continúa Draft, registrar `BLOCKED_HUMAN_ACTION` y no desperdiciar el turno reruneando CI verde. En el siguiente ciclo JOBS puede asignar a BBB trabajo F4 independiente que no invalide #51 si el plan/gates lo permiten.

### WOZ — área inicial F1
D9 ya PASS. Siguiente candidato: D10.1 REUSE-FIRST. No ejecutar alpha D10.2 ni decisión RO implícitamente. Si F1 queda reducido a decisión RO/externa, JOBS puede mover WOZ explícitamente a F3 técnico/operación en un ciclo posterior.

## TABLERO VIVO

### AAA
- AREA: F2 / Web + UX
- CURRENT_ASSIGNMENT: `NIGHT-AAA-001`
- EXPECTED_STATE: ver `NOCHE - AAA.md`
- LAST_RESULT: pendiente de primer ciclo nocturno
- NEXT_CANDIDATES: 12.1 → 13.x → 14.x → 15.x según dependencias y baseline real

### BBB
- AREA: F4 / Desktop + release chain
- CURRENT_ASSIGNMENT: `NIGHT-BBB-001`
- EXPECTED_STATE: ver `NOCHE - BBB.md`
- LAST_RESULT: pendiente de primer ciclo nocturno
- NEXT_CANDIDATES: 21 closure; después 22–25 solo cuando prerequisitos reales permitan trabajo útil

### WOZ
- AREA: F1 / Security + durable data
- CURRENT_ASSIGNMENT: `NIGHT-WOZ-001`
- EXPECTED_STATE: ver `NOCHE - WOZ.md`
- LAST_RESULT: D9 PASS previo al sistema nocturno
- NEXT_CANDIDATES: D10.1; luego D10.2 solo con autoridad aplicable; posible F3 técnico por reasignación JOBS

## BLOCKERS GLOBALES DE ARRANQUE

1. **PR #51 Draft:** requiere transición humana/flujo GitHub válido a Ready; no cambiar head/base al hacerlo.
2. Certificados/signing/notarization pueden requerir memberships/credenciales externas; no inferir disponibilidad.
3. F3 pagos/legal puede requerir Stripe, decisiones legales, DNS/provider state y RO.
4. D10.2 alpha final conserva decisión RO.

## REGLA DE UTILIZACIÓN

Si un worker queda PENDING esperando CI o una acción externa durante un ciclo completo, JOBS debe evaluar si existe otra tarea verdaderamente independiente para su próximo turno. No dejar capacidad ociosa por costumbre, pero tampoco crear overlap o deuda.

## CIERRE DE CADA CICLO JOBS

Actualizar:

```text
CYCLE_ID: NIGHT-JOBS-NNN
INTEGRATION_HEAD:
AAA_LAST:
BBB_LAST:
WOZ_LAST:
PLAN_UPDATES:
OWNER_CHANGES:
NEW_ASSIGNMENTS:
BLOCKERS:
CRITICAL_PATH_NEXT_HOUR:
CYCLE_FINISHED_AT:
```

## LOG DE DECISIONES

### NIGHT-JOBS-000 — bootstrap
- Sistema nocturno creado.
- Áreas iniciales separadas: AAA=F2, BBB=F4, WOZ=F1.
- Se reconoce D9 PASS, AAA #54 PENDING CI y BBB #51 PENDING Draft.
- Próximo ciclo JOBS debe revalidar todo; este snapshot no autoriza claims futuros por sí solo.
