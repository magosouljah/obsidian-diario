# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 020

- BeatGaler integración observada: `integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`.
- No se procesó merge nuevo en este ciclo.
- Release público: 🔴 `NO-GO`.
- F0: trabajo técnico habilitante cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- F1: D6–D9 PASS; D10.1 external-only por copia off-provider/off-account + read/checksum; D10.2 decisión RO.
- F2: #66 exact-head verde con navegación bounded productiva; `NIGHT-AAA-020` sigue ASSIGNED sin resultado.
- F3: #67 candidate 17.2 existe pero Required CI está rojo por PostgreSQL restored-state verification; `NIGHT-WOZ-019` sigue ASSIGNED sin resultado.
- F4: #63 Required CI general verde pero Windows Import literal rojo dentro del E2E harness; `NIGHT-BBB-019` sigue ASSIGNED sin resultado.

## PREFLIGHT / DUPLICATE-GUARD DEL CICLO

Durante este preflight apareció concurrentemente un `CYCLE 019` ya completo en Issue #41 y en los cuatro ledgers nocturnos. Ese ciclo ya había procesado AAA-019/BBB-018/WOZ-018 y emitido:
- `NIGHT-AAA-020`;
- `NIGHT-BBB-019`;
- `NIGHT-WOZ-019`.

Reread final de los tres ledgers confirma que los tres IDs siguen `ASSIGNMENT_STATUS: ASSIGNED` y todavía no tienen resultado de worker. Por idempotencia, sencillez y ownership fijo, CYCLE 020 **NO los supersede ni emite 021/020/020 artificialmente**. Hacerlo duplicaría/churnearía trabajo antes de ejecución y abriría una carrera entre dos órdenes equivalentes.

Este ciclo sí corrige el desync documental que CYCLE 019 dejó explícitamente pendiente: Plan Maestro, F2, F3, F4 y roles ahora reflejan los heads/CI reales.

## RESULTADOS VIGENTES PROCESADOS

### AAA / `NIGHT-AAA-020` — ASSIGNED / NO RESULT YET
- SAME #66 head `86f9659b0341107496332ada546312611e40ddaa`, base `ed6aab7e...`.
- Production React Previous/Next por cursor bounded ya está en candidate.
- Required CI/Desktop Portability `33278321854`, D6 `33278321859`, D7 `33278321867` = SUCCESS.
- Falta race-check/merge verificable. No se marca integración ni cierre 12.1.

### BBB / `NIGHT-BBB-019` — ASSIGNED / NO RESULT YET
- SAME #63 head `ea00d85d7946da8a27fe336bf738afb9a4bd72d0`, base `ed6aab7e...`.
- F4 Matrix `33277733635`, D6 `33277733621`, D7 `33277733651`, Desktop Portability/Required CI `33277733647` = SUCCESS.
- Windows Import `33277733650` = FAILURE; job `99167313710` pasó setup/exact checkout/official driver bootstrap y falló dentro del existing E2E harness.
- `windows/import` sigue `NOT_COVERED`; no promoción/no merge.

### WOZ / `NIGHT-WOZ-019` — ASSIGNED / NO RESULT YET
- SAME #67 head `22550152e9960c5dad328711b3a8b150301a8c4f`, base `ed6aab7e...`.
- Focal 17.2 `33278423859`, D6 `33278423854`, D7 `33278423851`, temp-auth `33278423880` = SUCCESS.
- Required CI/Desktop Portability `33278423879` = FAILURE por `PostgreSQL live integration + recovery gate`; restored-state verification falló después de dump/encrypt/restore.
- No merge/no 17.2 PASS.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F2 / 12.1 / #66:** race transaction del candidate ya verde; después reducir cold/warm/taxonomy residual con evidencia.
2. **F3 / 17.2 / #67:** corrective mínimo de restored-state verification sin debilitar recovery; fresh Required CI + merge.
3. **F4 / 25.1 / #63:** hallar causa real del E2E Windows Import, PASS literal + applicable CI + merge.
4. **F0/F1:** mantener blockers externos como externos; no repetir drills aceptados.
5. Después: D13–D15, F3 18–20 y F4 25.2/dependencias externas. F5 continúa cerrada.

## TABLERO AAA / BBB / WOZ

| Worker | Estado factual | PRIMARY vigente | CI-FALLBACK |
|---|---|---|---|
| AAA | `NIGHT-AAA-020` ASSIGNED; #66 CI verde, no merge | SAME #66 race-check + merge si combinación sigue válida | `NONE` |
| BBB | `NIGHT-BBB-019` ASSIGNED; Windows Import rojo | SAME #63 log-driven corrective + PASS literal/fresh CI | `NONE` |
| WOZ | `NIGHT-WOZ-019` ASSIGNED; PG recovery gate rojo | SAME #67 smallest recovery corrective + fresh Required CI | `NONE` |

Ownership exclusivo: AAA=#66/F2-12.1; BBB=#63/F4-25.1; WOZ=#67/F3-17.2. No overlap material.

## PRIMARY / CI-FALLBACK EMITIDOS

No se emiten IDs nuevos en CYCLE 020 porque los tres PRIMARY nuevos de CYCLE 019 siguen activos y no procesados. Se preservan exactamente:

### AAA — `NIGHT-AAA-020`
- PRIMARY: SAME #66 race-check + protected integration si exact head/base/evidence siguen válidos.
- CI-FALLBACK: `NONE`.
- Required evidence/STOP: los definidos en `NOCHE - AAA.md`; no scope expansion.

### BBB — `NIGHT-BBB-019`
- PRIMARY: SAME #63, corrective mínimo guiado por el failure real del Windows Import, PASS literal + fresh applicable CI antes de promoción/merge.
- CI-FALLBACK: `NONE`.
- Required evidence/STOP: los definidos en `NOCHE - BBB.md`; PRODUCT_FINDING + STOP si la causa es producto fuera de F4.

### WOZ — `NIGHT-WOZ-019`
- PRIMARY: SAME #67, diagnosticar/corregir restored-state mismatch sin debilitar invariantes, focused tests + fresh Required CI + race-check.
- CI-FALLBACK: `NONE`.
- Required evidence/STOP: los definidos en `NOCHE - WOZ.md`; no 18.x ni bypass recovery.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: governance release/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: merge #66 + residual cold/warm/taxonomy según evidencia; D13–D15 abiertos.
6. F3/17.2: restored-state verification roja en #67; 18–20 abiertos; 16.x physical/deploy tails externos.
7. F4/25.1: Windows Import E2E rojo en #63; otros gaps siguen abiertos; D22/D23 signing/notarization externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; #58/#64 integrados; #66 candidate exact-head verde, no integrado; 12.1/D13–D15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1 integrado; #67 17.2 candidate rojo en Required CI; 18–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 Windows Import rojo; 25.1/25.2 abiertos; D22/D23 externos.

## PLAN SYNC — CYCLE 020

Actualizados por JOBS:
- `!!!PLAN/Plan Maestro.md`;
- `!!!PLAN/Fase 2 - Web y UX.md`;
- `!!!PLAN/Fase 3 - Producción pagos y operación.md`;
- `!!!PLAN/Fase 4 - Desktop y release chain.md`;
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`;
- `!!!PLAN/NOCHE - JOBS.md`.

No se mutaron `NOCHE - AAA.md`, `NOCHE - BBB.md` ni `NOCHE - WOZ.md` porque contienen assignments activos no procesados y sobreescribirlos sería una carrera. F0/F1 no cambiaron materialmente. `Registro de avances.md` ya fue leído en el preflight y no recibe entrada porque no hubo merge/gate nuevo.

JOBS no modificó código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Reread integration HEAD antes de cualquier claim.
2. Procesar resultados reales de AAA-020, BBB-019 y WOZ-019 una sola vez.
3. Si AAA integra #66 y mueve baseline, revalidar #63/#67 contra el nuevo baseline; refresh SAME lineage + fresh applicable exact-head evidence si la combinación cambia materialmente.
4. No crear nuevo Assignment ID solo para reemplazar uno todavía ASSIGNED sin resultado.
5. No abrir F5 hasta que F0–F4 estén realmente en condiciones de gate.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-020
INTEGRATION_HEAD_OBSERVED: ed6aab7e964686cdb5fb1b84eac0198ca67f8892
CONCURRENT_CYCLE_DETECTED: NIGHT-JOBS-019 already completed during preflight
AAA: NIGHT-AAA-020 remains ASSIGNED; no new ID emitted
BBB: NIGHT-BBB-019 remains ASSIGNED; no new ID emitted
WOZ: NIGHT-WOZ-019 remains ASSIGNED; no new ID emitted
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK_PREVENTED: yes — no assignment churn
PLAN_DESYNC_REPAIRED: Plan Maestro + F2 + F3 + F4 + roles
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 020 completado como reconciliación factual/idempotente. El próximo ciclo parte de GitHub vivo y de los resultados de los assignments actualmente activos.
