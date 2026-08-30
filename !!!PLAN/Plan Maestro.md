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

## Estado vivo — NIGHT-JOBS-054

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.
- **Último merge material verificado:** PR #73 → `a306e3b3...`, parents `a9d35a3d...` + `fc831172...`. No merge posterior observado durante el preflight CYCLE 054.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1:** #69 frozen por `STOP_WRITE_SURFACE`; #70 frozen por safe-write + stale baseline.
- **F2 / 14.1:** `NIGHT-AAA-049` no produjo resultado final y fue superseded; `NIGHT-AAA-050` queda owner único para un slice mínimo REUSE-FIRST de streaming/memory safety sobre live integration.
- **F2 / 14.2:** read-only fallback de AAA050 únicamente durante espera externa real del PRIMARY.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** #73 reconciliation/exception-queue software slice INTEGRATED; global 18.2 sigue abierto por escenarios/provider/business-policy reales.
- **F3 / 19.2:** #76 sigue OPEN en `36d218609...`, stale contra live integration y frozen hasta safe history-preserving refresh. Canonical legal docs/routes existen; Settings canonical sync sigue pendiente.
- **F3 / 20.1:** #75 frozen por corrective/write-flow blocker.
- **F3 / 20.2:** WOZ052 abrió replacement PR #78 exact-base, head `50aac3f0...`, 2 archivos/+139. En CYCLE 054 el exact-head CI ya materializó 13 check-runs sin failure/pending/null y `Required CI = SUCCESS`; #78 sigue OPEN/non-draft/mergeable=true. `NIGHT-WOZ-053` queda owner único para race-check + integración. Aun integrado, máximo claim `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74/#71 frozen por refresh/integration dependency; `NOT_COVERED`.
- **F4 / windows/review:** #72 sigue stale/frozen; no safe history-preserving refresh disponible y no se reutiliza CI histórico.
- **F4 / 25.2:** BBB048 no produjo resultado final y fue superseded; `NIGHT-BBB-049` queda owner único para materializar solo P2/P3 beta backlog + beta script/form/entry-exit criteria faltantes.
- **5.1:** `[x]`. **5.2:** `[x]`.

## RESULTADOS PROCESADOS — CYCLE 054

- `NIGHT-AAA-049`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; no implementation/CI/merge claim.
- `NIGHT-BBB-048`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; no implementation/CI/merge claim.
- `NIGHT-WOZ-052`: `PENDING / WAITING_CI`; abrió exactamente una replacement PR #78 desde el artifact existente, exact-base `a306e3b3...`, head `50aac3f0...`, dos archivos/+139. El worker cerró antes de que Actions apareciera; JOBS verificó después que fresh exact-head CI sí existe y que `Required CI` terminó SUCCESS. No merge ni runtime-capacity PASS se promueven todavía.
- Último resultado material integrado aceptado: WOZ048 / #73 `DONE / INTEGRATED` como partial F3/18.2 software slice only.

## OWNERS — CYCLE 054

### AAA — `NIGHT-AAA-050` — F2 / 14.1
PRIMARY: auditar/reutilizar media Web actual y cerrar solo el menor gap literal de progressive/Range-style playback, giant-file memory safety y cleanup/cancel; focused tests + fresh exact-head CI; sin Player redesign.  
CI-FALLBACK: F2/14.2 READ-ONLY player-control gap map solo si PRIMARY queda code-complete esperando CI/review/merge; cero writes; recheck PRIMARY.

### BBB — `NIGHT-BBB-049` — F4 / 25.2
PRIMARY: reutilizar inventario BBB047 y evidencia existente; materializar únicamente P2/P3 beta backlog + beta test script/form/entry-exit criteria faltantes; fresh exact-head CI para cambios de repo; sin release público/signing/notarization/product mutation.  
CI-FALLBACK: F4/25.1 READ-ONLY residual journey map solo mientras PRIMARY espera operación externa; cero writes; recheck PRIMARY.

### WOZ — `NIGHT-WOZ-053` — F3 / 20.2
PRIMARY: SAME #78. Recheck exact head/base/two-file delta/CI/mergeability y live integration inmediatamente antes de integrar; merge solo race-clean por flujo WOZ autorizado; verificar SHA + parents post-merge. Máximo claim `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado desde cero CYCLE 054

1. **F3/20.2 / PR #78:** candidate exact-base, narrow y exact-head CI verde; el siguiente avance útil es integración race-clean por WOZ, sin declarar capacity PASS.
2. **F2/14.1:** trabajo Web interno dependency-safe no bloqueado por #69/#70/#76.
3. **F4/25.2:** gaps internos concretos ya auditados; materializarlos reduce residual mientras #72/#74 están bloqueados.
4. **F3 #76 / legal Settings:** frozen hasta safe history-preserving refresh.
5. **F4 #72 / windows-review:** frozen por el mismo blocker de refresh; no historical CI reuse.
6. **F4 #74 → #71 windows-auth:** frozen hasta cambio factual de integration/refresh dependency.
7. **F3 #75 / 20.1:** frozen por write-flow blocker.
8. **F2 / 12.1:** real-browser cold/warm runtime evidence.
9. **F2 #69/#70:** write/safe-write blockers.
10. **F2 14.2–15 + remaining F4 25.1 rows:** residual interno posterior.
11. **F0/F1/F3 external tails + F4 D22/D23:** external/RO prerequisites remain. F5 does not open.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`; #63 → `02a40564...`; #68 → `a9d35a3d69dd9127029fb851d189f9bd3079d03b`; #73 → `a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-050`; 049 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-049`; 048 está superseded.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-053`; SAME #78 únicamente.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga reconciliación exact-head de candidates restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 054; GitHub vivo prevalece si cambia después.
