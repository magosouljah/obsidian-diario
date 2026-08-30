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

## Estado vivo — NIGHT-JOBS-041

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
- **F3 / 18.2:** `[ 🟡 ]`; PR #73 OPEN/Ready @ `fc831172...`, base exacta `a9d35a3d...`, `mergeable=true/clean`; fresh `Required CI` + `F3 - 18.2 Reconciliation` = SUCCESS. `NIGHT-WOZ-040` asignado solo para race-check + integración exact-head. Global 18.2 permanece abierto por tails provider/business.
- **F3 / 20.1:** gap map audit-only válido; holding.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / 25.1:** `[ 🟡 ]`; `windows/import` integrado. `windows/auth` sigue `NOT_COVERED` por product finding de session persistence. PR #72 Windows Review exact head `e32ee701...` tiene Desktop Portability/D6/D7/Import verdes pero dedicated Windows Review `33319185581` = FAILURE en `Run Windows Review E2E harness`; attribution/corrective sigue asignado a BBB037.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 041

### AAA — `NIGHT-AAA-038` — F4 product-auth finding
PRIMARY: root cause + corrective mínimo token/session persistence desde baseline vivo; no tocar #71; focused fail-before/pass-after + fresh exact-head CI.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-037` — F4 / 25.1 SAME #72 windows/review
PRIMARY: attribution-first del failure `33319185581`; si harness, corrective mínimo SAME #72; si conducta producto tras sesión/assertion, PRODUCT_FINDING + STOP. No tocar auth/#71.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-040` — F3 / 18.2 SAME #73 integration
PRIMARY: exact-head/race-check de #73 @ `fc831172...`; confirmar CI green + mergeable-clean; integrar por flujo autorizado y verificar merge SHA/parents. No cerrar 18.2 global por tails no verificadas.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 041

1. **F3/18.2 #73:** integrar el software slice ya exact-head verde; es trabajo listo y no depende de AAA/BBB.
2. **F4 product-auth:** arreglar session persistence para revalidar `windows/auth`/#71.
3. **F4 windows/review/#72:** atribuir y resolver dedicated Review failure sin tocar producto salvo handoff de finding.
4. **F2/13.1 #69:** Save All product wiring + refresh, holding hasta liberar owner.
5. **F2/12.1:** runtime navegador real cold/warm.
6. **F2/#70:** safe-write + stale baseline frozen.
7. **F3/20.1:** gap map listo, holding.
8. **F0/F1/F3 external tails + F4 D22/D23:** externos/RO.
9. Después: F2 13.2–15, F3 19–20 y F4 remainder 25.1/25.2. **F5 no se abre**.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-038`; no reemitir/duplicar mientras siga vigente sin final.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-037`; no reemitir/duplicar mientras siga vigente sin final.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-040` sobre SAME #73.  
**JOBS:** siguiente ciclo procesa resultados reales; si #73 integra y mueve baseline, candidates restantes requieren reconciliación exact-head antes de cualquier integración.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 041; GitHub vivo prevalece si cambia después.
