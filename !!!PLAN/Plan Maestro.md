# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## Reglas de autoridad

- GitHub/runtime vivo prevalece sobre snapshots viejos.
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head son obligatorios.
- Cada pieza material tiene un solo owner.
- JOBS dirige/sincroniza; no modifica código BeatGaler ni infraestructura.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo — NIGHT-JOBS-061

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.
- **Último merge material verificado:** PR #78 → `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF`; D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1:** #69 frozen por `STOP_WRITE_SURFACE`; #70 frozen por safe-write + stale baseline.
- **F2 / 14.1:** AAA056 no dejó resultado verificable; `NIGHT-AAA-057` queda owner único del slice mínimo streaming/memory safety. No integration mutation este ciclo.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** #73 reconciliation/exception-queue software slice INTEGRATED; global 18.2 sigue abierto por provider/payment/business-policy evidence.
- **F3 / 19.2:** #76 OPEN/stale/frozen.
- **F3 / 20.1:** #75 OPEN/non-draft/mergeable @ `40e39393247dbdd506ac01edefa84fd0b0add94c`, exactamente cuatro intended files. Exact-head Required CI y applicable workflows siguen SUCCESS. `NIGHT-WOZ-060` posee la única mutación de integration para race-check + merge exact-head.
- **F3 / 20.2:** PR #78 `[x] HARNESS SOFTWARE INTEGRATED`; approved peak, 2× runtime proof, latency, safety margin y durable user waitlist siguen abiertos.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74/#71 frozen; `NOT_COVERED`.
- **F4 / windows/review:** #72 stale/frozen.
- **F4 / 25.1:** Web/auth sigue `NOT_COVERED`.
- **F4 / 25.2:** #79 sigue OPEN/non-draft/mergeable @ `c6ec2910522370f2506beb71ad5e0fa0317d6a61`, un docs-only artifact sobre baseline histórico. BBB055 no dejó resultado; `NIGHT-BBB-056` lo refresca + CI fresca pero **NO MERGE CYCLE 061** porque WOZ/#75 posee integration.
- **5.1:** `[x]`. **5.2:** `[x]`.

## RESULTADOS PROCESADOS — CYCLE 061

- `NIGHT-AAA-056`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- `NIGHT-BBB-055`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- `NIGHT-WOZ-059`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; #75 permanece OPEN/unmerged.
- No se promovió merge, PASS ni integración nueva; integration permanece en #78.

## OWNERS — CYCLE 061

### AAA — `NIGHT-AAA-057` — F2 / 14.1
PRIMARY: live integration only; REUSE-FIRST sobre media Web y cerrar únicamente el menor gap literal de progressive/Range-style playback, giant-file memory safety y cleanup/cancel; focused tests + fresh exact-head CI; sin Player redesign; NO merge este ciclo.  
CI-FALLBACK: F2/14.2 READ-ONLY player-control gap map solo si PRIMARY queda code-complete esperando CI/review; cero writes; recheck PRIMARY.

### BBB — `NIGHT-BBB-056` — F4 / 25.2 / SAME #79
PRIMARY: reconciliar #79 preservando su único docs-only artifact sobre el live baseline observado; confirmar delta exacto + fresh exact-head CI; **NO MERGE CYCLE 061**. No cerrar 25.2.  
CI-FALLBACK: F4/25.1 Web/auth READ-ONLY evidence map únicamente durante WAITING_CI/review; sin writes; STOP ante overlap/duplicación.

### WOZ — `NIGHT-WOZ-060` — F3 / 20.1 / SAME #75
PRIMARY: race-check exact-head `40e3939...`; confirmar cuatro paths intended + CI exact-head green + live baseline unchanged; merge solo con expected head y verificar merge SHA/parents. Claim máximo: software observability integrated; external observability permanece UNVERIFIED.  
CI-FALLBACK: NONE.

## Camino crítico global — recalculado desde cero CYCLE 061

1. **F3/20.1 / #75:** exact-head green + mergeable sobre live observado; integración es el siguiente paso material más corto.
2. **F4/25.2 / #79:** refresh docs-only + fresh CI en paralelo, serializado detrás de #75.
3. **F2/14.1:** Web media streaming/memory safety dependency-safe.
4. **F4/25.1 Web/auth** y luego demás journeys no cubiertos.
5. **F3/20.2 residual:** approved peak + 2× runtime + latency + safety margin + durable user waitlist.
6. **F3/19.2 #76**, **F4 #72**, **F4 #74→#71**, **F2 #69/#70**: frozen hasta cambio factual de blocker.
7. **F2/12.1**, F0/F1/F3 external tails y F4 D22/D23: external/runtime/RO prerequisites. F5 no abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875caf...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`; #63 → `02a40564...`; #68 → `a9d35a3d...`; #73 → `a306e3b3...`; #78 → `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-057`; 056 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-056`; SAME #79 refresh/CI, sin merge mientras #75 posee integration.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-060`; SAME #75 exact-head race-check + integración.  
**JOBS:** siguiente ciclo procesa resultados reales; si #75 mergea, refrescar cualquier candidate restante contra el nuevo baseline antes de integración.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 061; GitHub vivo prevalece si cambia después.
