# NOCHE — JOBS

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** JOBS — jefe de la noche.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META

Terminar F0–F4 o reducirlas al mínimo número factual de blockers externos. Prioridad: (1) F0–F4, (2) sencillez, (3) limpieza. Evidence-before-claim; REUSE-FIRST; duplicate-check; exact-head; no rebajar gates.

## BASELINE VIVO — CYCLE 010 FINAL

- BeatGaler integración al preflight/cierre JOBS: `integration-v0.8.0-alpha.1 @ be9e58c9edc0bb40742e0b91e3f2ebe771ace502`.
- Release público: 🔴 `NO-GO`.
- F0: técnico habilitado; 1.2 y 2.2 tails externos.
- F1: D6/D7/D8/D9 PASS. D10.1 external-only por off-provider/off-account copy proof real + read/checksum. D10.2 = decisión RO.
- F2: #58 OPEN/Ready/mergeable, head `61e38f8a9c89aaa2e308e1e93bbbf4a7de22f741`, base `be9e58c...`; Test - Desktop Portability `33262586452`, D6 `33262586456`, D7 `33262586450` SUCCESS.
- F3: #61 OPEN/Ready/mergeable, head `d855b3d259626534650c1a78dae6df58f78cdcb9`, base `be9e58c...`; Test - Desktop Portability `33263815780`, D6 `33263815813`, D7 `33263815852`, temp-auth compile `33263815854` SUCCESS. Physical staging/prod sigue externo.
- F4: #60 OPEN/Ready/mergeable, head `f8773d5f3f0a93d5e1a0a338cd3e5db6c1f574c4`, base `be9e58c...`; F4 matrix `33263350498`, Test - Desktop Portability `33263350496`, D6 `33263350489`, D7 `33263350490` SUCCESS. Failure previo 33260592774 quedó diagnosticado/corregido en SAME PR.

## TABLERO AAA / BBB / WOZ

| Worker | Resultado procesado | Asignación nueva | Objetivo |
|---|---|---|---|
| AAA | 010 PENDING; refresh SAME #58 completado y CI terminó verde después del turno | `NIGHT-AAA-011` | race-check + merge SAME #58; luego atomic empty-index únicamente |
| BBB | 010 PENDING; SAME #60 reparado/refrescado y CI terminó verde | `NIGHT-BBB-011` | race-check SAME #60; si AAA mueve baseline, refresh + CI nuevo antes de merge |
| WOZ | 010 PENDING; #61 software candidate creado y CI terminó verde | `NIGHT-WOZ-011` | race-check SAME #61; refresh + CI si baseline cambió; tras merge solo SOFTWARE DONE |

No existe ownership simultáneo: AAA=F2/12.1; BBB=F4/25.1; WOZ=F3/16.2.

## ASIGNACIONES EMITIDAS

### `NIGHT-AAA-011`
- REUSE SAME PR #58 / exact head `61e38f8a...`.
- GitHub precheck: OPEN/Ready/mergeable; portability/D6/D7 SUCCESS sobre base `be9e58c...`.
- Race-check inmediato; merge protegido con expected-head si combinación sigue intacta.
- Si cambia baseline, refresh SAME #58 + CI aplicable.
- Tras merge verificable: atomic empty-index únicamente.
- No pagination/window/memory ni cold/warm residual.

### `NIGHT-BBB-011`
- REUSE SAME PR #60 / exact head `f8773d5...`.
- Candidate está verde sobre `be9e58c...`.
- AAA ejecuta antes: revalidar integration en vivo.
- Si baseline cambió, refresh SAME #60 + CI exact-head; no reutilizar verde anterior.
- Merge protegido solo con todos los gates aplicables verdes.
- Integrar matrix no convierte gaps honestos en PASS.
- No 25.2/signing/notarization/release.

### `NIGHT-WOZ-011`
- REUSE SAME PR #61 / exact head `d855b3d...`.
- Candidate está verde sobre `be9e58c...`.
- AAA/BBB ejecutan antes: revalidar integration y refresh SAME PR + CI si cambió.
- Merge protegido solo con exact-head válido.
- Tras integración: marcar solo 16.2 SOFTWARE DONE / EXTERNAL TAIL.
- No provider resources/costo/deploy real; physical staging/prod y DNS/TLS/rollback reales siguen externos.

## BLOCKERS

1. F0/2.2: GitHub Support server-side cleanup + fresh final verification.
2. F0/1.2: governance/domain/support/status/signing/reviews/test matrix; Apple Developer deferred.
3. F1/D10.1: copia real fuera del primary provider/account failure domain + read/checksum.
4. F1/D10.2: decisión RO sobre alpha final.
5. F2/12.1: #58 todavía no integrado; después atomic empty-index, pagination/window/memory y cold/warm residual.
6. F3/16.1/16.2: runtime software 16.1 integrado y 16.2 candidate verde; physical staging/prod/deploy real externos.
7. F3: 17–20.x sigue siendo el mayor volumen restante; Stripe/DNS/legal/provider incluyen inputs externos.
8. F4/25.1: #60 candidate verde pero no integrado; functional gaps `NOT_COVERED/PENDING_EXTERNAL` siguen abiertos.
9. F4: D22/D23 signing/notarization externos; iPhone/YouTube/billing/cross-platform functional gaps no tienen PASS inventado.

## PROGRESO HACIA F0–F4

- **F0:** solo tails externos/administrativos; no consumir worker técnico en duplicados.
- **F1:** core técnico cerrado; D10.1 external-only + D10.2 RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 tiene candidate exact-head verde listo para transaction de integración.
- **F3:** 16.1 runtime integrado; 16.2 ya tiene candidate software exact-head verde; tails productivos siguen externos.
- **F4:** 24.2 cerrado; 25.1 candidate reparado y exact-head verde; falta integración y luego gaps reales/25.2.

## PLAN SYNC DEL CICLO

Actualizados:
- `!!!PLAN/Plan Maestro.md`
- `!!!PLAN/Equipo multi-IA - Roles y coordinación.md`
- `!!!PLAN/NOCHE - AAA.md`
- `!!!PLAN/NOCHE - BBB.md`
- `!!!PLAN/NOCHE - WOZ.md`
- `!!!PLAN/NOCHE - JOBS.md`

Leídos completos también F0, F1, F2, F3, F4, protocolo y Registro. No se mutaron checkboxes de las fases porque **ningún PR nuevo fue integrado durante este turno JOBS**; el cambio factual fue que los tres candidates pendientes terminaron CI verde. GitHub real e Issue #41 prevalecieron sobre snapshots nocturnos stale.

## SIGUIENTE CICLO

1. Releer integration HEAD y #58/#60/#61 antes de cualquier claim.
2. Procesar resultados 011 en orden factual; no asumir que los tres conservaron base `be9e58c...`.
3. Si #58 integra, sincronizar F2 slice A y avanzar atomic empty-index.
4. Si #60 integra, sincronizar F4/25.1 artifact sin falsear matrix gaps; recalcular 25.2.
5. Si #61 integra, sincronizar F3/16.2 como SOFTWARE DONE + external tail; recalcular siguiente slice F3 de mayor retorno.
6. Mantener D10.1 off-provider, physical staging/prod y signing/notarization como externos hasta evidencia real.
7. No abrir Fase 5 mientras gates reales necesarios sigan abiertos.

## LOG

```text
CYCLE_ID: NIGHT-JOBS-010
INTEGRATION_HEAD: be9e58c9edc0bb40742e0b91e3f2ebe771ace502
AAA: NIGHT-AAA-010 PENDING -> CI finished green on #58 head 61e38f8a -> NIGHT-AAA-011 race-check/merge, then atomic empty-index only
BBB: NIGHT-BBB-010 PENDING -> #60 head f8773d5 matrix/portability/D6/D7 green -> NIGHT-BBB-011 race-check; refresh+CI if prior merge moved baseline
WOZ: NIGHT-WOZ-010 PENDING -> #61 head d855b3d portability/D6/D7/temp-auth green -> NIGHT-WOZ-011 race-check; refresh+CI if prior merge moved baseline
DUPLICATE_WORK: none
CLAIMS_PROMOTED_WITHOUT_EVIDENCE: none
RELEASE: NO-GO
```

**STOP:** ciclo JOBS 010 terminado. La siguiente ejecución debe iniciar desde GitHub vivo, no desde este snapshot si cambió.
