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

## Estado vivo — NIGHT-JOBS-057

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.
- **Último merge material verificado:** PR #73 → `a306e3b3...`. No merge posterior observado durante el preflight CYCLE 057.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1:** #69 frozen por `STOP_WRITE_SURFACE`; #70 frozen por safe-write + stale baseline.
- **F2 / 14.1:** AAA052 no dejó resultado final antes del ciclo y fue superseded; `NIGHT-AAA-053` queda owner único del mismo slice mínimo REUSE-FIRST de streaming/memory safety, seleccionado nuevamente desde cero por valor crítico dependency-safe.
- **F2 / 14.2:** read-only fallback de AAA053 únicamente durante espera externa real del PRIMARY.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** #73 reconciliation/exception-queue software slice INTEGRATED; global 18.2 sigue abierto por escenarios/provider/business-policy reales.
- **F3 / 19.2:** #76 sigue OPEN en `36d218609...`, stale y frozen hasta safe history-preserving refresh.
- **F3 / 20.1:** #75 frozen por corrective/write-flow blocker.
- **F3 / 20.2:** #78 sigue OPEN/mergeable exact-base, head `50aac3f0...`, 2 archivos/+139; exact-head PR workflows observados completos sin failure. WOZ055 no dejó resultado y fue superseded; `NIGHT-WOZ-056` posee la única mutación de integration autorizada del ciclo para race-check + merge. Aun integrado, máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74/#71 frozen; `NOT_COVERED`.
- **F4 / windows/review:** #72 stale/frozen; no historical CI reuse.
- **F4 / 25.2:** PR #79 sigue OPEN/mergeable exact-base, head `c6ec2910...`, docs-only readiness artifact (+84). Permanece `HOLD_GREEN_PENDING_SERIAL_INTEGRATION` para evitar carrera con WOZ/#78; si baseline cambia, refresh + fresh CI antes de merge.
- **F4 / 25.1:** BBB051 no dejó resultado final antes del ciclo y fue superseded; `NIGHT-BBB-052` toma únicamente Web/auth como journey dedicado, recalculado desde cero como mejor slice independiente mientras #79 queda serializado.
- **5.1:** `[x]`. **5.2:** `[x]`.

## RESULTADOS PROCESADOS — CYCLE 057

- `NIGHT-AAA-052`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; no implementation/CI/merge claim.
- `NIGHT-BBB-051`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; no dedicated Web/auth evidence accepted.
- `NIGHT-WOZ-055`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; #78 remains open/mergeable; no merge claim.
- Último resultado material integrado aceptado sigue siendo WOZ048 / #73 `DONE / INTEGRATED` como partial F3/18.2 software slice only.

## OWNERS — CYCLE 057

### AAA — `NIGHT-AAA-053` — F2 / 14.1
PRIMARY: auditar/reutilizar media Web actual y cerrar solo el menor gap literal de progressive/Range-style playback, giant-file memory safety y cleanup/cancel; focused tests + fresh exact-head CI; sin Player redesign.  
CI-FALLBACK: F2/14.2 READ-ONLY player-control gap map solo si PRIMARY queda code-complete esperando CI/review/merge; cero writes; recheck PRIMARY.

### BBB — `NIGHT-BBB-052` — F4 / 25.1 Web/auth
PRIMARY: consumir el residual map BBB049 y producir únicamente evidencia dedicada del journey Web/auth; preferir harness/tests; product fix mínimo solo si el journey alcanza un defecto literal independiente y sin overlap AAA. #79 no se integra en este turno.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-056` — F3 / 20.2
PRIMARY: SAME #78. Recheck exact head/base/two-file delta/CI/mergeability y live integration inmediatamente antes de integrar; merge solo race-clean por flujo WOZ autorizado; verificar SHA + parents post-merge. Máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado desde cero CYCLE 057

1. **F3/20.2 / PR #78:** único merge autorizado del ciclo; exact-base, narrow, mergeable y CI observado sin failure.
2. **F2/14.1:** trabajo Web interno dependency-safe, AAA053.
3. **F4/25.1 Web/auth:** primer journey dedicado desde residual map, BBB052.
4. **F4/25.2 / PR #79:** candidate green preservado; reconciliar/integrar solo después de conocer el baseline resultante de #78.
5. **F3 #76 / legal Settings:** frozen hasta safe history-preserving refresh.
6. **F4 #72 / windows-review:** frozen por refresh blocker.
7. **F4 #74 → #71 windows-auth:** frozen hasta cambio factual de integration/refresh dependency.
8. **F3 #75 / 20.1:** frozen por write-flow blocker.
9. **F2 / 12.1:** real-browser cold/warm runtime evidence.
10. **F2 #69/#70:** write/safe-write blockers.
11. **F2 14.2–15 + remaining F4 25.1 rows:** residual interno posterior.
12. **F0/F1/F3 external tails + F4 D22/D23:** external/RO prerequisites remain. F5 does not open.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875caf...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`; #63 → `02a40564...`; #68 → `a9d35a3d69dd9127029fb851d189f9bd3079d03b`; #73 → `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-053`; 052 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-052`; 051 está superseded y #79 queda hold-green sin merge durante este turno.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-056`; 055 está superseded; SAME #78 únicamente.  
**JOBS:** siguiente ciclo procesa resultados reales; si #78 mueve baseline, reconciliar #79 y cualquier candidate restante antes de confiar en CI previo.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 057; GitHub vivo prevalece si cambia después.
