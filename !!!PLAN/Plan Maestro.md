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

## Estado vivo — NIGHT-JOBS-052

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.
- **Último merge material verificado:** PR #73 → `a306e3b3...`, parents `a9d35a3d...` + `fc831172...`. No merge posterior observado en CYCLE 052.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1 Web:** #69 frozen/unowned por `STOP_WRITE_SURFACE`.
- **F2 / 13.1 server:** #70 frozen por safe-write + stale baseline.
- **F2 / 13.2:** audit read-only solo como CI-FALLBACK de AAA048 si PRIMARY espera operación externa.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** reconciliation/exception-queue software slice de #73 está INTEGRATED; global 18.2 sigue abierto por escenarios/provider/business-policy reales.
- **F3 / 19.2:** #76 sigue OPEN/Ready/mergeable en `36d218609...`, base_sha `a9d35a3d...`, stale contra live integration. `NIGHT-AAA-048` es owner único para refresh estrecho + canonical Settings reuse + fresh exact-head CI.
- **F3 / 20.1:** #75 sigue frozen por corrective/write blocker.
- **F3 / 20.2:** #77 sigue CLOSED/unmerged y no puede reabrirse. WOZ050 refrescó SAME branch a `50aac3f0c700a88e1f058372c23ee1d96ecf247a`; compare contra live integration = ahead 2 / behind 0 / merge-base exacto `a306e3b3...`, dos archivos harness/test. `NIGHT-WOZ-051` autoriza una sola replacement PR desde ese branch; resultado máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74 sigue frozen; #71 espera integración real + nueva orden.
- **F4 / windows/review:** #72 sigue OPEN/Ready/mergeable en `904fbf3c...`, base_sha `a9d35a3d...`, stale contra live integration. `NIGHT-BBB-047` es owner único para narrow refresh + fresh CI + integración solo si exact-head verde/race-clean.
- **5.1:** `[x]`. **5.2:** `[x]`.

## RESULTADOS PROCESADOS — CYCLE 052

- `NIGHT-AAA-047`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; #76 head unchanged; no implementation/CI/merge claim.
- `NIGHT-BBB-046`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; #72 head unchanged; no refresh/CI/merge claim.
- `NIGHT-WOZ-050`: `BLOCKED / REOPEN_UNAVAILABLE`; #77 cannot reopen (GitHub 422), but source branch was refreshed cleanly onto live integration as `50aac3f0...`; no tests/CI/merge and no capacity PASS claim.
- Último resultado material integrado aceptado: WOZ048 / #73 `DONE / INTEGRATED` as partial F3/18.2 software slice only.

## OWNERS — CYCLE 052

### AAA — `NIGHT-AAA-048` — F3 / 19.2 / SAME #76
PRIMARY: refresh estrecho de SAME #76 sobre `a306e3b3...`, reutilizar documentos legales canónicos en Settings existentes, focused tests + fresh exact-head CI; no segunda UI/política/infra.  
CI-FALLBACK: F2/13.2 READ-ONLY gap map solo si PRIMARY queda code-complete y realmente esperando CI/review/merge; cero writes; recheck PRIMARY.

### BBB — `NIGHT-BBB-047` — F4 / SAME #72
PRIMARY: refresh estrecho de SAME #72 sobre `a306e3b3...`; fresh Windows Review/Matrix/Required CI y gates aplicables; integrar solo con exact-head green + race-check.  
CI-FALLBACK: F4/25.2 READ-ONLY readiness inventory solo si PRIMARY espera operación externa; cero writes; recheck PRIMARY.

### WOZ — `NIGHT-WOZ-051` — F3 / 20.2 / replacement continuation
PRIMARY: desde branch refrescado `50aac3f0...`, verificar delta exacto 2 archivos y crear una sola replacement PR autorizada porque #77 no puede reabrirse; focused deterministic tests + fresh exact-head CI; máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado desde cero CYCLE 052

1. **#76 / F3 19.2 legal:** nearest clean internal closure candidate; canonical docs exist, but refresh + in-app canonical consistency + fresh CI remain.
2. **#72 / F4 windows-review:** existing useful harness candidate; refresh + fresh exact-head CI can integrate another literal Windows journey.
3. **F3/20.2 replacement continuation:** refreshed source branch is exact-base and narrow; authorized one replacement PR can reduce internal capacity gap to HARNESS_READY without fabricating runtime proof.
4. **F2 / #69 13.1 Web:** critical but blocked by write surface; no blind retry.
5. **F4 #74 → #71 / windows-auth:** frozen until merge-flow blocker changes factually.
6. **F3 #75 / 20.1:** frozen by write-flow blocker.
7. **F2 / 12.1:** real-browser cold/warm runtime evidence.
8. **F2 #70:** safe-write + stale baseline.
9. **F2 14–15 + remaining F4 25.x rows:** internal work still open after candidates above.
10. **F0/F1/F3 external tails + F4 D22/D23:** external/RO blockers remain prerequisites to factual F0–F4 closure. F5 does not open.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-048`; 047 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-047`; 046 está superseded.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-051`; 050 está procesado/BLOCKED.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge adicional obliga reconciliación exact-head de los otros candidates.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 052; GitHub vivo prevalece si cambia después.
