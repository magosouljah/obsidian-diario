# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 017 FINAL

- BeatGaler integración: `integration-v0.8.0-alpha.1 @ ed6aab7e964686cdb5fb1b84eac0198ca67f8892`.
- Cambio durante race-check final: PR #65 se integró con parents exactos `b114111caf... + e655386405...`; branch reread confirmó `ed6aab7e...`.
- Release público: 🔴 `NO-GO`.
- F0: 1.2 y 2.2 tails externos/administrativos; trabajo técnico interno habilitante ya cerrado.
- F1: D6/D7/D8/D9 PASS; D10.1 external-only por off-provider/off-account copy + read/checksum; D10.2 decisión RO.
- F2: #66 progreso parcial, incompleto y ahora stale frente a `ed6aab7e...`.
- F3: 17.1 SOFTWARE DONE/INTEGRATED por #65; 17.2 queda siguiente slice técnico.
- F4: #63 Windows Import rojo y ahora stale frente a `ed6aab7e...`.

## RESULTADOS PROCESADOS

### AAA / `NIGHT-AAA-017`
- PR #66 @ `c9b5cd95ad5b6b4d8f681265992e44d8c777a76f`: bounded first-load 240 rich Beat objects + `loadWebLibraryPage` + test 10,321 beats.
- Gate incompleto: consumer navigation, refresh/invalidation, no-duplicate/no-omission, rendered bound y proxy CPU/network/memory.
- D6 `33277332289` SUCCESS; D7 `33277332325` SUCCESS; Desktop Portability `33277332334` estaba IN_PROGRESS en preflight inicial.
- Baseline avanzó después a `ed6aab7e...`; cualquier CI anterior deja de autorizar merge. Resultado: `PENDING`, SAME #66 refresh obligatorio.

### BBB / `NIGHT-BBB-016`
- Sin resultado worker nuevo antes del recálculo.
- #63 @ `8768856ff8ea15c7fa164e4b433abccf02852fb1`: F4 Matrix/D6/D7/Desktop Portability verdes; Windows Import `33276125806` FAILURE por EdgeDriver/Tauri Driver/WDIO bootstrap.
- Base antigua `b114111caf...` quedó stale por #65. `windows/import` sigue `NOT_COVERED`.

### WOZ / `NIGHT-WOZ-017`
- Resultado DONE verificable apareció durante el race-check final.
- PR #65 exact head `e65538640581f3f986748968db1f4dfb069c2579`; F3 `33276769749`, Desktop Portability `33276769684`, D6 `33276769695`, D7 `33276769698`, temp-auth `33276769702` SUCCESS.
- Protected expected-head merge → `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`, parents `b114111caf... + e655386405...`.
- Promoción permitida: **17.1 SOFTWARE DONE / INTEGRATED** únicamente. Stripe productivo/credenciales/precios reales siguen UNVERIFIED.

## CAMINO CRÍTICO GLOBAL — RECALCULADO DESDE CERO DESPUÉS DE #65

1. **F2 / 12.1 #66:** mayor blocker interno activo F2; refresh + consumer window/evidence real.
2. **F3 / 17.2:** dependency-ready tras #65; webhook integrity/dedupe/retry software-only, independiente de F2/F4.
3. **F4 / 25.1 #63:** refresh + runner bootstrap + fresh Windows Import literal PASS.
4. **F0/F1:** blockers actuales externos/RO; no repetir drills ni fabricar infraestructura.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | Nueva asignación | Objetivo |
|---|---|---|---|
| AAA | 017 PENDING — #66 parcial, ahora stale | `NIGHT-AAA-018` | SAME #66 refresh sobre `ed6aab7e...` + consumer windowing/bounded evidence + fresh exact-head |
| BBB | 016 sin ejecución; #63 rojo funcional, ahora stale | `NIGHT-BBB-017` | SAME #63 refresh + minimal runner bootstrap + fresh Windows Import/exact-head CI |
| WOZ | 017 DONE — #65 merged `ed6aab7e...` | `NIGHT-WOZ-018` | F3/17.2 webhook raw-body integrity + durable dedupe/idempotency/retry software-only |

Ownership exclusivo: AAA=F2/12.1 #66; BBB=F4/25.1 #63; WOZ=F3/17.2. No overlap material.

## ASIGNACIONES EMITIDAS

### `NIGHT-AAA-018`
SAME #66. Refresh sobre `ed6aab7e...`; completar navigation/windowing, refresh/invalidation, no dup/omission y bounded evidence. Fresh exact-head antes de merge. No D13–D15.

### `NIGHT-BBB-017`
SAME #63. Refresh sobre `ed6aab7e...`; corregir únicamente EdgeDriver/Tauri Driver/WDIO bootstrap; fresh Windows Import exact-head. No 25.2.

### `NIGHT-WOZ-018`
F3/17.2. REUSE-FIRST webhook signature sobre raw body antes de parse/mutate; durable event ID/idempotency; duplicate/out-of-order safety; failure/retry state; tests de firma/body mutation/concurrency/retry. PostgreSQL authority; sin recursos/credenciales Stripe reales, sin 18.x.

## BLOCKERS

1. F0/2.2: GitHub-side cleanup/support + fresh final verification externa.
2. F0/1.2: release governance/domain/support/status/AuthentiCode/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia off-provider/off-account real + read/checksum.
4. F1/D10.2: decisión RO.
5. F2/12.1: #66 completion/refreshed evidence + cold/warm residual; D13–D15 abiertos después.
6. F3: 17.2–20 abiertos; 16.x physical/deploy tails externos; Stripe productivo no probado.
7. F4/25.1: #63 functional red + stale; otros coverage gaps; D22/D23 signing/notarization externos; 25.2 abierto.

## PROGRESO F0–F4

- **F0:** técnico interno cerrado; tails externos solamente.
- **F1:** core técnico cerrado; D10.1 externo + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; #58 + #64 integrados; #66 partial/stale; D13–D15 abiertos.
- **F3:** 16.1/16.2 software integrados con tails externos; **17.1 integrado por #65**; 17.2 asignado; 18–20 abiertos.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; #60 matrix integrada; #63 rojo/stale; 25.1/25.2 abiertos; D22/D23 externos.

## PLAN SYNC

Sincronizados en este ciclo: `Plan Maestro.md`, F2, F3, F4, roles y los cuatro ledgers nocturnos. F0/F1 no cambiaron materialmente. `Registro de avances.md` fue leído completo; el merge #65 queda registrado en Plan/F3/JOBS/WOZ e Issue #41, sin reescribir el ledger histórico voluminoso en esta transacción.

## SIGUIENTE CICLO

1. Reread integration HEAD antes de cualquier claim.
2. Procesar únicamente resultados nuevos `AAA-018`, `BBB-017`, `WOZ-018`.
3. AAA/BBB deben refrescar sus SAME PRs por baseline `ed6aab7e...` antes de merge-authorizing CI.
4. Si WOZ produce candidate 17.2, exigir signature/idempotency/retry exact-head evidence; no inferir Stripe productivo ni 18.x.
5. Mantener F0/F1/signing/physical staging/off-provider como externos hasta evidencia real.
6. No abrir F5 hasta que F0–F4 estén realmente en condiciones de gate.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-017
INTEGRATION_HEAD_FINAL: ed6aab7e964686cdb5fb1b84eac0198ca67f8892
AAA: 017 PENDING -> #66 partial/stale -> NIGHT-AAA-018 SAME #66 refresh/completion
BBB: 016 unexecuted -> #63 Windows Import red/stale -> NIGHT-BBB-017 SAME #63 refresh/bootstrap
WOZ: 017 DONE -> #65 merged ed6aab7e... -> NIGHT-WOZ-018 F3/17.2
DUPLICATE_WORK: none; #62 remains closed/not merged; SAME #66/#63 reused
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
CODE_OR_INFRA_MUTATION_BY_JOBS: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 017 terminado. La siguiente ejecución inicia desde GitHub vivo, no desde este snapshot si cambió.
