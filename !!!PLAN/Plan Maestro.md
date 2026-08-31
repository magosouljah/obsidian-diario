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

## Estado vivo — NIGHT-JOBS-062

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.
- **Último merge material verificado:** PR #78 → `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF`; D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1:** #69 frozen por `STOP_WRITE_SURFACE`; #70 frozen por safe-write + stale baseline.
- **F2 / 14.1:** AAA057 no dejó resultado verificable; `NIGHT-AAA-058` queda owner único del slice mínimo streaming/memory safety. No integration mutation.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** #73 reconciliation/exception-queue software slice INTEGRATED; global 18.2 sigue abierto por provider/payment/business-policy evidence.
- **F3 / 19.2:** #76 OPEN/stale/frozen.
- **F3 / 20.1:** WOZ060 verificó #75 exact-head `40e39393247dbdd506ac01edefa84fd0b0add94c`, cuatro intended files y CI aplicable verde, pero el merge fue bloqueado por `MERGE_FLOW_UNAVAILABLE` antes de aceptación GitHub. #75 sigue OPEN/unmerged. `NIGHT-WOZ-061` reintenta únicamente la transacción exact-head.
- **F3 / 20.2:** PR #78 `[x] HARNESS SOFTWARE INTEGRATED`; decisión RO nueva fija **80 usuarios simultáneos esperados / 160 usuarios simultáneos de validación (2×)**. Esa decisión no es PASS. `NIGHT-BBB-057` ejecuta evidencia runtime aplicable a 160; latency/error/queue/recovery, safety margin y durable user waitlist siguen obligatorios.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74/#71 frozen; `NOT_COVERED`.
- **F4 / windows/review:** #72 stale/frozen.
- **F4 / 25.1:** Web/auth sigue `NOT_COVERED`.
- **F4 / 25.2:** #79 sigue OPEN/stale, un docs-only artifact. BBB056 no dejó resultado; #79 queda como CI-FALLBACK independiente de BBB057, refresh + fresh CI, **sin merge**.
- **5.1:** `[x]`. **5.2:** `[x]`.

## RESULTADOS PROCESADOS — CYCLE 062

- `NIGHT-AAA-057`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- `NIGHT-BBB-056`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- `NIGHT-WOZ-060`: `BLOCKED / MERGE_FLOW_UNAVAILABLE`; #75 exact-head/four-file/CI evidence remains valid at observed baseline, but no merge was accepted.
- RO/OWNER Issue #41 `5472774681`: capacity target approved = **80 expected / 160 validation**; no runtime PASS promoted.
- No merge/PASS/integration new; integration remains #78.

## OWNERS — CYCLE 062

### AAA — `NIGHT-AAA-058` — F2 / 14.1
PRIMARY: live integration only; REUSE-FIRST media streaming/memory slice mínimo; giant-file memory safety + cleanup/cancel; focused tests + fresh exact-head CI; sin Player redesign ni merge.  
CI-FALLBACK: F2/14.2 READ-ONLY player-control gap map solo si PRIMARY queda code-complete esperando CI/review.

### BBB — `NIGHT-BBB-057` — F3 / 20.2
PRIMARY: usar harness #78 ya integrado y objetivo canónico **80/160**; obtener evidencia runtime materialmente aplicable a 160 para latency/error/queue/recovery, safety margin y durable waitlist. No inventar PASS ni generar costo/infra nueva.  
CI-FALLBACK: F4/25.2 SAME #79 narrow history-preserving refresh + fresh exact-head CI únicamente si PRIMARY queda `WAITING_EXTERNAL/WAITING_RUNTIME`; **NO MERGE** y no cerrar 25.2.

### WOZ — `NIGHT-WOZ-061` — F3 / 20.1 / SAME #75
PRIMARY: fresh race-check + retry exact-head merge transaction de #75; no code workaround; verificar merge SHA/parents si GitHub acepta. Claim máximo software observability integrated; external observability sigue UNVERIFIED.  
CI-FALLBACK: NONE.

## Camino crítico global — recalculado desde cero CYCLE 062

1. **F3/20.1 / #75:** candidate exact-head green; único blocker actual es merge-flow transaction. WOZ061 posee la única mutación de integration.
2. **F3/20.2:** decisión RO eliminó el blocker de target; BBB057 debe probar 160 concurrentes en runtime aplicable y medir requisitos literales.
3. **F2/14.1:** Web media streaming/memory safety, independiente y dependency-safe.
4. **F4/25.2 / #79:** fallback/preparación únicamente; no desplaza la evidencia de capacidad recién habilitada.
5. **F4/25.1 Web/auth** y demás journeys `NOT_COVERED`.
6. **#76 legal / #72 review / #74→#71 auth / #69/#70** frozen hasta cambio factual.
7. **F2/12.1 + F0/F1/F3/F4 external tails:** runtime/external/RO prerequisites. F5 no abre.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-058`; 057 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-057`; target 80/160 es canónico, no claim.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-061`; SAME #75 exact-head merge retry.  
**JOBS:** siguiente ciclo procesa resultados reales; si #75 mergea, todo candidate restante requiere reconciliación al nuevo baseline antes de integración.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 062; GitHub vivo prevalece si cambia después.
