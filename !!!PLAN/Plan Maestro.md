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

## Estado vivo — NIGHT-JOBS-045

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- **Último merge material:** PR #68 → `a9d35a3d...`; GitHub vivo no muestra merge posterior.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real cuantificado sigue bloqueado por runtime navegador ejecutable.
- **F2 / 13.1 Web:** PR #69 OPEN @ `b2ab75ae...`; coordinator Save All/CAS probado, product wiring + refresh pendientes; stale/holding.
- **F2 / 13.1 server:** PR #70 OPEN @ `5a99ebf2...`; safe-write blocker + stale baseline; frozen.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** PR #73 OPEN/Ready @ `fc831172...`, exact-head green y mergeable; `BLOCKED / MERGE_FLOW_UNAVAILABLE`. No integrado; tails provider/business abiertos.
- **F3 / 20.1:** PR #75 OPEN/Ready/mergeable @ `bb493b3755ba1a42b4c5cfe7f3b885edc544c61f`; Required CI `33323457041` sigue FAILURE por floating external Action refs. WOZ043 verificó el corrective exacto de dos pins pero terminó `BLOCKED / WRITE_TOOL_SAFETY`; no hubo write/head/CI/merge nuevo. #75 queda frozen hasta cambio factual del write flow.
- **F3 / 20.2:** abierto. `NIGHT-WOZ-044` hace audit-only REUSE-FIRST de capacity/load readiness; no PASS claim ni load productivo.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #71 sigue regression proof y `NOT_COVERED`. SAME #74 @ `14dfba52775f40f1956e3d1dcb343b07b147ba0c` está OPEN/Ready sobre base exacta `a9d35a3d...`; D6 `33324138675`, D7 `33324138676` y Required CI `33324138689` son SUCCESS. No integrado. AAA040 no produjo resultado y queda superseded; `NIGHT-AAA-041` = race-check + integración exacta.
- **F4 / windows/review:** SAME #72 @ `56dc4adf206cc53f5260c71952f84ae67d994279`; Windows Review `33324512156`, Windows Import `33324512159` y Required CI `33324512153` SUCCESS, pero F4 Matrix `33324512174` FAILURE en `Validate dependency-safe matrix contract`. No integrado. BBB039 sin resultado queda superseded; `NIGHT-BBB-040` = attribution-first + corrective mínimo si corresponde.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 045

### AAA — `NIGHT-AAA-041` — F4 / SAME #74
PRIMARY: consumir exact-head green D6/D7/Required CI; race-check y merge SAME #74 solo si integration sigue compatible; si baseline cambió, refresh + revalidate antes de integración. No tocar #71.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-040` — F4 / SAME #72
PRIMARY: atribuir literalmente el matrix-contract failure post-promotion; corregir solo si es inconsistencia acotada de matriz/workflow/test dentro de #72; fresh exact-head Windows Review + F4 Matrix + D6 + D7 + Required CI; merge solo si todo verde/race-clean. No auth/#71/#74.  
CI-FALLBACK: **F4/25.2 READ-ONLY readiness inventory**, solo si PRIMARY entra realmente `WAITING_CI`; sin rama/PR/commit ni cambios de producto/matrix/docs. Evidencia = artefactos/gaps `EXISTS/PARTIAL/GAP/PENDING_EXTERNAL`; STOP ante cualquier write/overlap/dependencia de #72 y volver a recheck PRIMARY antes de cerrar.

### WOZ — `NIGHT-WOZ-044` — F3 / 20.2
PRIMARY: REUSE-FIRST/read-only audit de capacity envelope, 2× peak evidence, latency/errors/queue/recovery, admission control/per-bot ceiling/margin/waitlist. No inventar expected peak; no load costoso; no branch/PR/commit; no tocar #73/#75.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 045

1. **#74 / product-auth prerequisite:** exact-head green; integración sigue siendo el paso interno más corto. Después #71 requiere nueva prueba literal Windows Auth.
2. **#72 / windows-review:** dedicated journey green pero matrix-contract red; atribuir/corregir antes de merge.
3. **#75 / F3 20.1:** corrective literal conocido, pero write flow está bloqueado; mantener frozen hasta cambio factual, no gastar otro turno repitiendo el mismo intento.
4. **#73 / F3 18.2:** software slice listo pero merge-flow blocked; no duplicar.
5. **F3/20.2:** reducir incertidumbre con audit-only mientras #75/#73 están bloqueados.
6. **#69 / F2 13.1:** product wiring + refresh cuando quede owner libre.
7. **F2/12.1:** runtime navegador real cold/warm.
8. **#70 / F2 13.1 server:** safe-write + stale baseline frozen.
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

**AAA:** ejecutar una sola vez `NIGHT-AAA-041`; `NIGHT-AAA-040` está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-040`; `NIGHT-BBB-039` está superseded.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-044`; #75/#73 quedan frozen bajo blockers conocidos.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga reconciliación exact-head antes de integrar los candidates restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 045; GitHub vivo prevalece si cambia después.
