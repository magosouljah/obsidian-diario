# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## DECISIÓN RO — ROMPECABEZAS CON OWNER FIJO

Desde 2026-08-28 el trabajo se desbloquea por dependencia real, incluso cross-phase, pero cada agente conserva ownership estable de su pieza hasta cerrarla o hasta una reasignación explícita de JOBS/RO.

Reglas:
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- GitHub real prevalece sobre snapshots viejos del plan.
- Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head son obligatorios.
- Un gate controla cierre/promoción/release; no bloquea trabajo independiente de otra fase.
- JOBS dirige/sincroniza; no toca código BeatGaler ni infraestructura.
- RO conserva alcance de producto, riesgo aceptado y go/no-go público.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo — NIGHT-JOBS-023

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`; merge verificado de PR #67.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] RESIDUAL`. #58/#64/#66 integrados. `NIGHT-AAA-022` verificó literalmente taxonomy/state `empty / no-results / offline / auth-failure / cloud-failure`; ese subrequisito queda demostrado sin cambio ceremonial. Único residual literal: comparación startup Web cold vs warm real, mismo escenario, cache/session cold vs preservados y métricas cuantificadas/reproducibles. No se marca 12.1 `[x]` hasta esa evidencia.
- **F2 / D13–D15:** abiertos. AAA se mueve explícitamente a D13.1 dependency-safe bajo `NIGHT-AAA-023`; el residual cold/warm queda abierto y no se falsea ni bloquea trabajo independiente.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #59 integrado; separación física staging/prod externa.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL` — #61 integrado; deploy/staging/rollback reales externos.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65.
- **F3 / 17.2:** `[x] SOFTWARE DONE / INTEGRATED` — PR #67 exact tested head `27c2f30007a687a144be289a64ab986451f05c99`; F3 17.2 `33283532676`, D6 `33283532664`, D7 `33283532679`, temp-auth `33283532723` y Desktop Portability `33283532696` SUCCESS; merge `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`. No prueba Stripe productivo ni infraestructura externa.
- **F3 / 18.1:** dependency-ready software-only. `NIGHT-WOZ-022` ASSIGNED para limits/entitlements server-side, reserva anti-race y estado/portal subscription dentro de contrato software; sin Stripe productivo ni decisiones comerciales inventadas.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. SAME PR #63 sigue OPEN/Ready sobre base `3ad8f55a...`, head `033c2b55a0c46471b7e7ddb3af57b626699ac6e6`. Windows Import run `33284981477` terminó **FAILURE**: setup/checkout/Node/Rust/npm y `Prepare isolated embedded Tauri WebDriver` pasaron; `Run existing Windows import E2E harness` falló. No existe PASS literal, `windows/import` sigue `NOT_COVERED`, no merge ni promoción. `NIGHT-BBB-022` ASSIGNED para consumir el log de ese fallo y aplicar únicamente el siguiente corrective F4 mínimo en SAME #63.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 023

### AAA — `NIGHT-AAA-023` — F2 / 13.1
PRIMARY: implementar/auditar solo Save All durable con resumen parcial, bulk conflict-safe o deshabilitado honestamente y garbage journal para uploads huérfanos; REUSE-FIRST; una sola rama/PR si hace falta. No 13.2, D14/D15, billing, desktop ni infra.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-022` — F4 / 25.1 SAME #63
PRIMARY: consumir la evidencia exacta del run fallido `33284981477` / job `99186491944`; identificar el primer failure causal del harness y aplicar únicamente corrective F4 mínimo sobre SAME #63. Exigir Windows Import literal PASS antes de promover matrix; cualquier head nuevo requiere fresh applicable exact-head gates antes de merge.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-022` — F3 / 18.1 software-only
PRIMARY: REUSE-FIRST después de #65/#67; implementar/validar limits server-side antes de reservar recursos, transacción/reserva anti-carreras y contrato de Billing Portal/cancelación/estados subscription. Sin Stripe productivo, provider resources, credenciales, 18.2 ni decisiones de grace period.  
CI-FALLBACK: `NONE`.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 023

1. **F4 / 25.1 / #63:** Windows Import sigue rojo; resolver el harness hasta assertion/PASS literal es el blocker técnico más concreto del estado actual.
2. **F3 / 18.1:** 17.2 ya está integrado; avanzar entitlements/reserva subscription software reduce camino crítico de F3 sin esperar infraestructura externa.
3. **F2 / D13.1:** 12.1 quedó bloqueado solo por medición runtime cold/warm; avanzar D13.1 independiente evita tiempo muerto sin fingir cierre de 12.1.
4. **F2 / 12.1 cold/warm:** requiere superficie/harness que ejecute dos startups Web reales comparables; queda abierto hasta evidencia reproducible.
5. **F0/F1 y D22/D23:** blockers externos/RO; no repetir drills técnicos ya aceptados.
6. Después: F2 13.2–15, F3 18.2–20, F4 resto de 25.1 + 25.2 y tails externos. F5 no se abre todavía.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e964686cdb5fb1b84eac0198ca67f8892`; #66 → `712b49b6689a31a47902dbe95e98622d001dab40`; #67 → `3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`.

Candidates vivos:
- #63 @ `033c2b55a0c46471b7e7ddb3af57b626699ac6e6` — OPEN/Ready, base `3ad8f55a...`; Windows Import `33284981477` FAILURE; no merge.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementación interna oculta.
- Schema: **Galer T-Library Schema v2**.
- Web pura: sin Tauri ni Desktop helper.
- Media: device ↔ provider directo; Galer Cloud no relaya beats/proyectos.
- Permanent auth/control secrets quedan control-side; cliente usa temporary auth.
- Shared-bot fallback solo cuando no hay bots libres; exclusividad por vault es camino normal.
- v1 no se publica free-only.
- YouTube existe en Desktop/Web; Web no llama Tauri.

## NEXT

**AAA:** ejecutar una sola vez `NIGHT-AAA-023`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-022`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-022`.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga race revalidation/fresh exact-head a candidates restantes cuando la combinación cambie materialmente.  
**PLAN_HEALTH:** sincronizado al estado GitHub observado en CYCLE 023; GitHub vivo prevalece si cambia después.
