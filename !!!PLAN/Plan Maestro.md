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

## Estado vivo — NIGHT-JOBS-024

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`; PR #67 integrado y sin merge posterior observable.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] RESIDUAL`; taxonomy/state ya demostrado; único residual literal = startup Web cold vs warm real cuantificado/reproducible.
- **F2 / 13.1:** dependency-safe y sigue siendo el mejor carril AAA; `NIGHT-AAA-024` ASSIGNED. 023 quedó `NOT_PROCESSED / SUPERSEDED_BY_JOBS` sin artifact nuevo.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65.
- **F3 / 17.2:** `[x] SOFTWARE DONE / INTEGRATED` — #67 merge `3ad8f55a...`.
- **F3 / 18.1:** dependency-ready software-only; `NIGHT-WOZ-023` ASSIGNED. 022 quedó `NOT_PROCESSED / SUPERSEDED_BY_JOBS` sin artifact nuevo.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] ARTIFACT INTEGRATED / FUNCTIONAL GAPS OPEN`. Único PR abierto observado: SAME #63, base `3ad8f55a...`, head `033c2b55...`; Windows Import `33284981477` sigue FAILURE y `windows/import` sigue `NOT_COVERED`. `NIGHT-BBB-023` ASSIGNED. 022 quedó `NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 024

### AAA — `NIGHT-AAA-024` — F2 / 13.1
PRIMARY: Save All durable con resumen parcial; bulk conflict-safe o deshabilitado honestamente; garbage journal/cleanup de uploads huérfanos. REUSE-FIRST; una sola rama/PR si hay gap real.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-023` — F4 / 25.1 SAME #63
PRIMARY: consumir el primer failure causal real de `33284981477` / job `99186491944`, aplicar únicamente el siguiente corrective F4/harness mínimo y exigir Windows Import literal PASS antes de cualquier promoción.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-023` — F3 / 18.1 software-only
PRIMARY: limits/entitlements server-side antes de reserva, reserva/transacción anti-race y contrato server-side de Billing Portal/cancel/subscription states. Sin Stripe/provider productivo ni 18.2.  
CI-FALLBACK: `NONE`.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 024

1. **F4 / 25.1 / #63:** Windows Import sigue rojo; resolver el harness hasta assertion/PASS literal sigue siendo el blocker técnico más concreto.
2. **F3 / 18.1:** 17.2 ya integrado; avanzar entitlements/reserva subscription software reduce F3 sin esperar provider externo.
3. **F2 / 13.1:** avanzar import durability mientras 12.1 espera una superficie real de medición cold/warm.
4. **F2 / 12.1 cold/warm:** sigue abierto; no fabricar benchmark sintético.
5. **F0/F1 + D22/D23:** blockers externos/RO; no repetir drills técnicos ya aceptados.
6. Después: F2 13.2–15, F3 18.2–20, resto F4 25.1 + 25.2 y tails externos. F5 no se abre todavía.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`.

Candidates vivos:
- #63 @ `033c2b55a0c46471b7e7ddb3af57b626699ac6e6` — OPEN/Ready, base `3ad8f55a...`; Windows Import FAILURE; no merge.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-024`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-023`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-023`.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga race revalidation/fresh exact-head a candidates restantes cuando la combinación cambie materialmente.  
**PLAN_HEALTH:** sincronizado al estado GitHub observado en CYCLE 024; GitHub vivo prevalece si cambia después.
