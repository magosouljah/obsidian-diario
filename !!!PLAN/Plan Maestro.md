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

## Estado vivo — NIGHT-JOBS-047

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- **Último merge material:** PR #68 → `a9d35a3d...`; GitHub vivo no muestra merge posterior.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal. `NIGHT-AAA-043` tiene un CI-FALLBACK read-only para inventariar el runtime si #69 entra en espera CI.
- **F2 / 13.1 Web:** #69 sigue OPEN/mergeable @ `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`, base histórica `3ad8f55a...`; helper Save All/CAS probado, refresh+wiring pendientes. AAA042 no produjo resultado y queda superseded; `NIGHT-AAA-043` es owner único.
- **F2 / 13.1 server:** #70 sigue frozen por safe-write + stale baseline.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** #73 sigue OPEN/Ready/mergeable @ `fc831172...`, base exacta `a9d35a3d...`; no merge verificable y tails provider/business abiertos. Frozen bajo blocker previo.
- **F3 / 20.1:** #75 sigue OPEN/Ready/mergeable @ `bb493b37...`; Required CI conocido falla por floating Action refs y corrective conocido quedó bloqueado por write safety. Frozen.
- **F3 / 20.2:** WOZ045 cerró auditoría, no gate: capacity envelope PARTIAL; approved peak GAP; load harness GAP; 2× proof PENDING_EXTERNAL; latency GAP; error/queue/recovery PARTIAL; admission control/per-bot ceiling EXISTS; safety margin/waitlist GAP. `NIGHT-WOZ-046` implementa solo harness parametrizable, sin inventar peak ni ejecutar carga productiva.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74 sigue OPEN/Ready/mergeable @ `14dfba52...`, exact-head green pero merge-flow previamente bloqueado; frozen. #71 espera integración real de #74.
- **F4 / windows/review:** #72 sigue OPEN/Ready/mergeable @ `904fbf3c0f81e6ff4c22e4ee717f337e5018fa5c`, base exacta `a9d35a3d...`; Windows Review/F4 Matrix/D6/D7/Required CI/Windows Import siguen SUCCESS; Upgrade SKIPPED. BBB041 no produjo resultado y queda superseded; `NIGHT-BBB-042` es owner único para race-check+integración.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 047

### AAA — `NIGHT-AAA-043` — F2 / SAME #69
PRIMARY: refresh mínimo de #69 al baseline vivo + wiring productivo del coordinator `saveAllWebItems`; focused tests + fresh exact-head CI. No #70/auth/F4.  
CI-FALLBACK: F2/12.1 READ-ONLY runtime-prerequisite inventory solo mientras PRIMARY espere CI; sin writes ni benchmark sintético.

### BBB — `NIGHT-BBB-042` — F4 / SAME #72
PRIMARY: consumir exact-head green, race-check e integrar #72 solo si baseline/head siguen aplicables; si baseline mueve, refresh estrecho + fresh applicable CI.  
CI-FALLBACK: F4/25.2 READ-ONLY readiness inventory solo mientras PRIMARY espere operación externa de merge/review/queue; después recheck PRIMARY.

### WOZ — `NIGHT-WOZ-046` — F3 / 20.2
PRIMARY: software slice mínimo para harness parametrizable de capacidad/carga. Debe negarse a afirmar 2× sin target aprobado y solo medir/reportar; no provider/infra/load productivo, no #73/#75.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 047

1. **#72 / windows-review:** candidate interno más listo, exact-head completamente verde; falta transacción de integración del owner.
2. **#69 / F2 13.1 Web:** stale base + wiring productivo; convierte helper probado en flujo real.
3. **F3/20.2:** convertir gap map en harness reusable sin falsear capacidad; target aprobado + runtime 2× quedan separados.
4. **#74 / product-auth prerequisite:** green pero merge-flow blocker previo; frozen hasta cambio factual; después #71.
5. **#75 / F3 20.1:** corrective conocido, write-flow blocker; frozen.
6. **#73 / F3 18.2:** software slice ready, merge-flow blocker previo; frozen.
7. **F2/12.1:** runtime real-browser cold/warm.
8. **#70 / F2 13.1 server:** safe-write + stale baseline.
9. **F0/F1/F3 external tails + F4 D22/D23:** externos/RO.
10. Después: F2 13.2–15, F3 19–20 remainder y F4 remainder 25.1/25.2. **F5 no se abre**.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`; #63 → `02a40564...`; #68 → `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-043`; 042 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-042`; 041 está superseded.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-046`; 045 queda procesado como audit DONE.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga reconciliación exact-head antes de integrar candidates restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 047; GitHub vivo prevalece si cambia después.
