# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 019

- BeatGaler integración: `integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`.
- GitHub vivo confirma que sigue siendo merge PR #65; no existe merge posterior al preflight.
- Release público: 🔴 `NO-GO`.
- F0: trabajo técnico habilitante cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- F1: D6–D9 PASS; D10.1 external-only por copia off-provider/off-account + read/checksum; D10.2 decisión RO.
- F2: #66 implementó navigation bounded productiva; exact-head CI terminó verde; falta transacción race-check/merge y luego quedan residual cold/warm/taxonomía si no demostrados.
- F3: #67 implementó 17.2 software candidate; focal gates verdes pero Required CI está rojo por PostgreSQL recovery verification.
- F4: #63 sigue OPEN; Required CI general verde, pero Windows Import literal falló dentro del E2E harness; `windows/import` sigue NOT_COVERED.

## RESULTADOS PROCESADOS

### AAA / `NIGHT-AAA-019` — PENDING → READY FOR RACE TRANSACTION
- SAME #66 head `86f9659b0341107496332ada546312611e40ddaa`, base `ed6aab7e...`, OPEN/mergeable.
- Production React Previous/Next cursor wiring ya existe sin `Beat[]` global; bounded consumer/10,321-beat continuity permanecen en lineage.
- Exact-head Required CI/Desktop Portability `33278321854`, D6 `33278321859`, D7 `33278321867` = SUCCESS; Upgrade skipped/no aplicable.
- No merge aún. Nueva orden `NIGHT-AAA-020`: race-check + merge SAME #66 si la combinación sigue válida.

### BBB / `NIGHT-BBB-018` — PENDING / FUNCTIONAL FAILURE
- SAME #63 head `ea00d85d7946da8a27fe336bf738afb9a4bd72d0`, base `ed6aab7e...`, OPEN/Ready/mergeable.
- F4 Matrix `33277733635`, D6 `33277733621`, D7 `33277733651`, Desktop Portability/Required CI `33277733647` = SUCCESS.
- Windows Import `33277733650` = FAILURE. Job `99167313710`: setup, exact checkout, dependency install y official Tauri/Edge auto-bootstrap PASS; failure ocurrió en `Run existing Windows import E2E harness`.
- No promoción/no merge. Nueva orden `NIGHT-BBB-019`: SAME #63, log-driven minimal corrective or PRODUCT_FINDING if outside F4.

### WOZ / `NIGHT-WOZ-018` — PENDING_CI / RECOVERY GATE FAILURE
- SAME #67 head `22550152e9960c5dad328711b3a8b150301a8c4f`, base `ed6aab7e...`, OPEN/Ready/mergeable.
- F3 17.2 `33278423859`, D6 `33278423854`, D7 `33278423851`, temp-auth `33278423880` = SUCCESS.
- Required CI `33278423879` = FAILURE. PostgreSQL recovery job `99169258638`: migrations/adversarial persistence PASS; dump/encrypt/restore PASS; `Verify restored constraints, secrets, reconciliation and rollback state` FAILURE; Required CI aggregator FAILURE.
- No merge. Nueva orden `NIGHT-WOZ-019`: SAME #67, root-cause + smallest fix preserving recovery invariants.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO

1. **F2 / 12.1 / #66:** integrar el candidate ya verde; después reducir cold/warm y taxonomy residual honestamente.
2. **F3 / 17.2 / #67:** reparar exact PostgreSQL recovery mismatch sin debilitar D9/D10/recovery invariants; integrar solo con Required CI verde.
3. **F4 / 25.1 / #63:** convertir Windows Import de NOT_COVERED a AUTOMATED_PASS únicamente tras literal functional PASS; integrar SAME lineage.
4. **F0/F1:** mantener blockers externos como externos; no repetir drills técnicos aceptados.
5. Después de estas transacciones, reevaluar D13–D15, F3 18–20 y F4 25.2/dependencias externas; F5 no se abre por calendario.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | PRIMARY emitido | CI-FALLBACK |
|---|---|---|---|
| AAA | 019 PENDING; #66 exact-head CI verde | `NIGHT-AAA-020`: SAME #66 race-check + merge | `NONE` — next F2 work overlaps frontend surfaces o expande scope antes del cierre transaccional |
| BBB | 018 PENDING; Windows Import FAILURE | `NIGHT-BBB-019`: SAME #63 log-driven corrective + literal PASS | `NONE` — 25.2/otros gaps comparten release/test surfaces o adelantan gate |
| WOZ | 018 PENDING_CI; PG recovery gate FAILURE | `NIGHT-WOZ-019`: SAME #67 recovery corrective + fresh Required CI | `NONE` — 18.x comparte billing/PG ownership y depende de 17.2 confiable |

Ownership exclusivo: AAA=#66/F2-12.1; BBB=#63/F4-25.1; WOZ=#67/F3-17.2. No overlap material.

## CI-FALLBACK POLICY APLICADA

- Fallback solo puede ejecutarse cuando PRIMARY entra realmente en `WAITING_CI` o `WAITING_EXTERNAL`.
- Debe usar scope/archivos/rama/PR/ownership independientes y no depender de PRIMARY.
- En este ciclo no existe fallback seguro y útil para ninguno de los tres; por eso los tres quedan explícitamente `NONE` en vez de fabricar paralelismo inseguro.
- Ningún worker puede inventar fallback.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: governance release/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real off-provider/off-account + read/checksum.
4. F1/D10.2: decisión RO sobre alpha.
5. F2/12.1: merge #66 + residual cold/warm/taxonomy según evidencia; D13–D15 abiertos.
6. F3/17.2: PostgreSQL restored-state verification roja en #67; 18–20 abiertos; 16.x physical/deploy tails externos.
7. F4/25.1: Windows Import E2E rojo en #63; otros gaps reales siguen abiertos; D22/D23 signing/notarization externos; 25.2 abierto.

## PROGRESO REAL F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; #58/#64 integrados; #66 listo para race transaction, 12.1 aún no cerrado; D13–D15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; 17.1 integrado; 17.2 candidate existe pero Required CI rojo; 18–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 functional failure pendiente; 25.1/25.2 abiertos; D22/D23 externos.

## ASIGNACIONES EMITIDAS — CYCLE 019

- `NIGHT-AAA-020` — PRIMARY SAME #66 race-check/merge; CI-FALLBACK NONE.
- `NIGHT-BBB-019` — PRIMARY SAME #63 diagnose/fix Windows Import; CI-FALLBACK NONE.
- `NIGHT-WOZ-019` — PRIMARY SAME #67 repair PostgreSQL recovery gate; CI-FALLBACK NONE.

## PLAN SYNC — CYCLE 019

- Actualizados directamente: `NOCHE - AAA.md`, `NOCHE - BBB.md`, `NOCHE - WOZ.md`, `NOCHE - JOBS.md`.
- No se promueve ningún `[x]`, PASS o INTEGRATED nuevo porque este ciclo no produjo merge nuevo.
- Plan Maestro/fases conservan sus gates materiales; GitHub vivo de este ciclo prevalece sobre snapshots CI viejos hasta el siguiente sync documental.
- `Registro de avances.md` leído completo; no se añade entrada porque no hubo cierre/merge/gate nuevo.
- JOBS no modifica código BeatGaler ni infraestructura.

## SIGUIENTE CICLO

1. Reread integration HEAD primero.
2. Procesar AAA-020, BBB-019 y WOZ-019 una sola vez.
3. Si AAA integra #66 y mueve baseline, BBB/WOZ deben refresh SAME lineage + fresh applicable exact-head evidence antes de merge.
4. Si un PRIMARY entra en espera, solo usar CI-FALLBACK si está explícitamente autorizado; en este ciclo todos son NONE.
5. No abrir F5 hasta que F0–F4 estén factual y documentalmente en condiciones reales.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-019
INTEGRATION_HEAD: ed6aab7e964686cdb5fb1b84eac0198ca67f8892
AAA: 019 PENDING + exact-head green -> NIGHT-AAA-020 SAME #66 race/merge
BBB: 018 PENDING + Windows Import FAILURE -> NIGHT-BBB-019 SAME #63 minimal corrective
WOZ: 018 PENDING_CI + PG recovery FAILURE -> NIGHT-WOZ-019 SAME #67 minimal corrective
CI_FALLBACKS: AAA NONE; BBB NONE; WOZ NONE
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 019 procesado. El próximo ciclo parte nuevamente de GitHub vivo.
