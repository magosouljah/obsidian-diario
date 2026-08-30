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

## Estado vivo — NIGHT-JOBS-042

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- **Último merge material:** PR #68 → `a9d35a3d...`; F3/18.1 integrado.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real cuantificado sigue bloqueado por runtime navegador ejecutable.
- **F2 / 13.1 Web:** PR #69 OPEN @ `b2ab75ae...`; coordinator Save All/CAS probado, product wiring + refresh pendientes; candidate stale/holding.
- **F2 / 13.1 server:** PR #70 OPEN @ `5a99ebf2...`; safe-write blocker + baseline stale; frozen.
- **F3 / 16.1 + 16.2:** software done con tails externos.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** PR #73 OPEN/Ready @ `fc831172...`, base exacta `a9d35a3d...`, mergeable y exact-head CI verde; `NIGHT-WOZ-040` terminó `BLOCKED / MERGE_FLOW_UNAVAILABLE`. El software slice reconciliation/exception queue está integration-ready pero NO integrado; 18.2 global sigue abierto por provider/business tails.
- **F3 / 20.1:** gap map previo válido; `NIGHT-WOZ-041` asignado para cerrar únicamente gaps internos software de observabilidad/alerts/runbook/kill-switch, sin inventar provider/on-call/status externos.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / 25.1:** `[ 🟡 ]`. `windows/import` integrado. `windows/auth` sigue `NOT_COVERED`; PR #74 corrective @ `92058b42...` tiene D6/D7 verdes pero Required CI `33321752522` FAILURE por TypeScript `src/platform/index.ts(10,22): Property '__TAURI_INTERNALS__' does not exist on type '(Window & typeof globalThis) | RuntimeWindow'`. `NIGHT-AAA-039` corrige solo esa causa y revalida. `windows/review` alcanzó literal PASS en PR #72 head `3219996e...` / run `33321799798`; aún no se promueve matrix ni se integra. `NIGHT-BBB-038` hace promoción + fresh exact-head gates + merge si race-clean.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 042

### AAA — `NIGHT-AAA-039` — F4 product-auth / SAME #74
PRIMARY: corregir únicamente el error TypeScript exacto de #74 sin cambiar el contrato de runtime/auth ni tocar #71; focused regression + fresh D6/D7/Required CI; integrar solo por autoridad aplicable cuando todo quede verde.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-038` — F4 / 25.1 SAME #72 windows/review
PRIMARY: consumir literal Review PASS de `33321799798`; promover solo `windows/review = AUTOMATED_PASS`; fresh exact-head Windows Review + F4 Matrix + D6 + D7 + Desktop Portability; race-check + merge solo si todo verde. No auth/#71/#74.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-041` — F3 / 20.1 internal observability slice
PRIMARY: REUSE-FIRST desde gap map WOZ033; cerrar únicamente gaps internos software verificables de logs/métricas/error reporting/alert routing/runbook/kill switches con alcance mínimo. Provider/on-call/status/retention externos quedan explícitamente abiertos. No tocar #73.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 042

1. **F4 product-auth / #74:** resolver compile exacto y obtener candidate verde; después #71 vuelve a BBB mediante nueva asignación para auth literal.
2. **F4 windows/review / #72:** ya tiene PASS literal; promover matrix y cerrar/integrar el slice con fresh exact-head evidence.
3. **F3/20.1:** avanzar gaps internos mientras #73 está bloqueado por merge flow externo.
4. **F3/18.2 #73:** integration-ready, pero bloqueado exclusivamente por merge execution layer; no duplicar/recrear.
5. **F2/13.1 #69:** Save All product wiring + refresh, holding hasta liberar owner.
6. **F2/12.1:** runtime navegador real cold/warm.
7. **F2/#70:** safe-write + stale baseline frozen.
8. **F0/F1/F3 external tails + F4 D22/D23:** externos/RO.
9. Después: F2 13.2–15, F3 19–20 remainder y F4 remainder 25.1/25.2. **F5 no se abre**.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-039`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-038`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-041`.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga reconciliación exact-head antes de integrar candidates restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 042; GitHub vivo prevalece si cambia después.
