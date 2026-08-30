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

## Estado vivo — NIGHT-JOBS-046

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- **Último merge material:** PR #68 → `a9d35a3d...`; GitHub vivo no muestra merge posterior.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real cuantificado sigue bloqueado por runtime navegador ejecutable.
- **F2 / 13.1 Web:** PR #69 OPEN/mergeable @ `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`, base vieja `3ad8f55a...`; coordinator Save All/CAS probado, product wiring + refresh pendientes. `NIGHT-AAA-042` es owner activo para SAME #69.
- **F2 / 13.1 server:** PR #70 OPEN/mergeable @ `5a99ebf2...`; safe-write blocker + stale baseline; frozen.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** PR #73 OPEN/Ready/mergeable @ `fc831172...`, exact-head green; `MERGE_FLOW_UNAVAILABLE`. No integrado; tails provider/business abiertos.
- **F3 / 20.1:** PR #75 OPEN/Ready/mergeable @ `bb493b3755ba1a42b4c5cfe7f3b885edc544c61f`; Required CI conocido falla por floating Action refs. Corrective exacto conocido pero write bloqueado por `WRITE_TOOL_SAFETY`; frozen.
- **F3 / 20.2:** abierto. WOZ044 no produjo resultado y queda superseded; `NIGHT-WOZ-045` reemite audit-only REUSE-FIRST. No PASS claim.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #71 sigue regression proof y `NOT_COVERED`. #74 @ `14dfba52775f40f1956e3d1dcb343b07b147ba0c` está OPEN/Ready/mergeable y exact-head green, pero AAA041 terminó `STOP_MERGE_FLOW_BLOCKED`; #74 queda frozen. #71 no se revalida hasta integración real de #74.
- **F4 / windows/review:** SAME #72 @ `904fbf3c0f81e6ff4c22e4ee717f337e5018fa5c` está OPEN/Ready/mergeable. Fresh exact-head Windows Review `33327407530`, F4 Matrix `33327407521`, D6 `33327407516`, D7 `33327407519`, Required CI `33327407533` y Windows Import `33327407514` son SUCCESS; Upgrade `33327407526` SKIPPED/no aplicable. `NIGHT-BBB-041` = race-check + integración exacta.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 046

### AAA — `NIGHT-AAA-042` — F2 / SAME #69
PRIMARY: refresh mínimo de #69 desde base `3ad8f55a...` a baseline vivo, preservar coordinator/CAS ya probado y conectar `saveAllWebItems` al flujo Web productivo Save All/Review/Import/Bulk sin reimplementar single-item commit ni server garbage journal. Fresh focused tests + CI exact-head. No #74/#71/#72/#70.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-041` — F4 / SAME #72
PRIMARY: consumir exact-head green completo, race-check y merge SAME #72 solo si integration sigue compatible. Si baseline movió, refresh estrecho + fresh applicable CI antes de integrar. No auth/#74/#71.  
CI-FALLBACK: **F4/25.2 READ-ONLY readiness inventory** solo si PRIMARY queda realmente esperando operación externa de merge/review/queue; sin rama/PR/commit/write, sin tocar #72/producto/matrix/docs. Evidencia = paths/artefactos + `EXISTS/PARTIAL/GAP/PENDING_EXTERNAL`; recheck PRIMARY antes de cerrar.

### WOZ — `NIGHT-WOZ-045` — F3 / 20.2
PRIMARY: REUSE-FIRST/read-only audit de capacity envelope, 2× peak evidence, latency/errors/queue/recovery, admission control/per-bot ceiling/margin/waitlist. No inventar expected peak; no load costoso; no branch/PR/commit; no tocar #73/#75.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 046

1. **#72 / windows-review:** todos los gates exact-head están verdes; integración es el candidato interno más listo.
2. **#74 / product-auth prerequisite:** exact-head green pero merge-flow bloqueado; frozen hasta cambio factual. Solo después #71 puede revalidar Windows Auth.
3. **#69 / F2 13.1 Web:** refresh + product wiring ahora asignados a AAA para convertir helper probado en flujo real.
4. **F3/20.2:** gap map audit-only con WOZ para reducir incertidumbre sin tocar blockers #73/#75.
5. **#75 / F3 20.1:** pin corrective conocido, pero write flow bloqueado; mantener frozen.
6. **#73 / F3 18.2:** software slice listo pero merge-flow blocked; no duplicar.
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

**AAA:** ejecutar una sola vez `NIGHT-AAA-042`; #74 queda frozen bajo merge-flow blocker.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-041`; integrar #72 solo con race-check exacto.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-045`; `NIGHT-WOZ-044` está superseded; #75/#73 siguen frozen.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga reconciliación exact-head antes de integrar candidates restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 046; GitHub vivo prevalece si cambia después.
