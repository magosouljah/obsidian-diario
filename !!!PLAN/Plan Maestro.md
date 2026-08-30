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

## Estado vivo — NIGHT-JOBS-034

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.
- **Cambio material:** PR #63 fue MERGED con exact tested head `7a6b7443fc4821a9b10798e2a3823a9d931bc2df`; merge SHA `02a40564d85284a119281ff79995c9b9bcb5e833`. Windows/import queda integrado como `AUTOMATED_PASS`; 25.1 completo sigue abierto.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`. AAA032 encontró harness real-browser (`test:web:smoke`) pero no pudo ejecutar checkout/npm/Chrome en su runtime; cold/warm real cuantificado sigue abierto.
- **F2 / 13.1 Web:** `[ 🟡 ]`. PR #69 sigue OPEN @ `b2ab75ae...`; Save All coordinator/CAS está probado pero product wiring App/Review falta. El merge #63 movió integration, así que cualquier integración futura de #69 exige refresh/revalidación. `NIGHT-AAA-033` owner.
- **F2 / 13.1 server:** PR #70 sigue OPEN @ `5a99ebf2...`, con corrective conocido pero bloqueado por safe-write tooling; ahora además quedó sobre baseline anterior. Frozen hasta patch seguro + refresh.
- **F3 / 16.1 + 16.2:** software done con tails externos.
- **F3 / 17.1 + 17.2:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.1:** PR #68 sigue OPEN @ `2a988ec2...`; exact-head green histórico pero no mergeado. Tras #63, candidate queda stale frente a `02a40564...` y requiere refresh/fresh applicable CI antes de cualquier merge. Frozen; no reintentos ceremoniales.
- **F3 / 20.1:** `NIGHT-WOZ-033` continúa auditoría REUSE-FIRST sobre baseline vivo nuevo; 032 queda superseded por baseline move antes de resultado observable.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / 25.1:** `[ 🟡 ]`. Windows/import está integrado por #63. Persisten otros gaps honestos. `NIGHT-BBB-032` toma únicamente `windows/auth`, el siguiente slice automatable respaldado por harness existente.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 034

### AAA — `NIGHT-AAA-033` — F2 / 13.1 SAME #69
PRIMARY: refresh/reconcile SAME #69 contra `02a40564...`; REUSE-FIRST del coordinator existente. Cerrar únicamente el product wiring Save All App/Review→`saveAllWebItems` si existe superficie de patch/worktree segura, con resumen saved/conflict/failed y retry semantics. No reemplazar PR ni tocar #70/13.2+/F3/F4. Si no existe patch seguro, STOP explícito sin mutación destructiva.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-032` — F4 / 25.1 windows/auth
PRIMARY: REUSE-FIRST sobre `desktop_e2e` + shared auth coverage; crear solo la evidencia/harness F4 mínima para demostrar el journey `windows/auth` en Windows. Promover esa única fila a `AUTOMATED_PASS` solo después de literal PASS + fresh exact-head applicable CI; merge si race-check limpio. Si aparece bug de producto, `PRODUCT_FINDING` + STOP.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-033` — F3 / 20.1 observability gap map
PRIMARY: sobre `02a40564...`, REUSE-FIRST de observabilidad/alerts/runbook/status/kill-switch existentes. Mapear requisito→evidencia→gap. Solo una pieza software-only mínima si existe gap literal pequeño, independiente y safely writable. No #68/#70/F2/F4/provider resources/costs/secrets.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 034

1. **F2 / 13.1 / #69:** product wiring sigue siendo el mayor gap interno Web cercano; refresh obligatorio tras #63.
2. **F4 / 25.1 remainder:** windows/import ya integrado; windows/auth es el siguiente slice F4 automatable sin depender de signing/hardware externo.
3. **F3 / 20.1:** cerrar/reducir observability software por REUSE-FIRST mientras #68 está stale/frozen.
4. **F2 / 12.1:** requiere runtime navegador real; blocker factual, no fabricar benchmark.
5. **#70 / #68:** stale + blockers previos; no tocar hasta resolver tooling/merge mechanism y revalidar baseline.
6. **F0/F1/F3 external tails + D22/D23:** externos/RO.
7. Después: F2 13.2–15, F3 18.2–20 y F4 remainder 25.1/25.2. F5 no se abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`; #63 → `02a40564d85284a119281ff79995c9b9bcb5e833`.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-033`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-032`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-033`.  
**JOBS:** procesar resultados reales; cualquier candidate basado en `3ad8f55a...` requiere refresh/revalidación material antes de merge.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 034; GitHub vivo prevalece si cambia después.
