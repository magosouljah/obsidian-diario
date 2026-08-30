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

## Estado vivo — NIGHT-JOBS-050

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada al cierre:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.
- **Último merge material verificado:** PR #73 → `a306e3b3...`, parents `a9d35a3d...` + `fc831172...`.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1 Web:** #69 sigue frozen/unowned por `STOP_WRITE_SURFACE`; stale desde `3ad8f55a...`.
- **F2 / 13.1 server:** #70 frozen por safe-write + stale baseline.
- **F2 / 13.2:** audit read-only queda solo como CI-FALLBACK de AAA046 si su PRIMARY espera operación externa.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** reconciliation/exception-queue software slice de #73 está **INTEGRATED** en `a306e3b3...`; global 18.2 sigue abierto por escenarios/provider/business-policy reales.
- **F3 / 19.2:** #76 sigue OPEN/Ready pero ahora diverged/mergeable=false sobre base histórica `a9d35a3d...`; `NIGHT-AAA-046` es owner único para refresh estrecho + reuse canónico en Settings + fresh exact-head CI.
- **F3 / 20.1:** #75 sigue frozen por corrective/write blocker.
- **F3 / 20.2:** #77 está CLOSED/unmerged; su ejecución prematura no cuenta como evidencia. `NIGHT-WOZ-049` lo reutiliza explícitamente como PRIMARY para refresh/reopen del harness; resultado máximo `HARNESS_READY`, runtime capacity sigue UNVERIFIED.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74 sigue frozen; #71 espera integración real + nueva orden.
- **F4 / windows/review:** #72 sigue OPEN/Ready pero ahora mergeable=false/diverged desde el merge-base `a9d35a3d...`; `NIGHT-BBB-045` es owner único para narrow refresh + fresh CI + integración solo si vuelve a quedar exact-head verde.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 050

### AAA — `NIGHT-AAA-046` — F3 / 19.2 / SAME #76
PRIMARY: refresh estrecho de SAME #76 sobre `a306e3b3...`, reutilizar documentos legales canónicos en Settings existentes, focused tests + fresh exact-head CI; no segunda UI/política/infra.  
CI-FALLBACK: F2/13.2 READ-ONLY gap map solo si PRIMARY queda code-complete y realmente esperando CI/review/merge; cero writes; recheck PRIMARY.

### BBB — `NIGHT-BBB-045` — F4 / SAME #72
PRIMARY: refresh estrecho de SAME #72 sobre `a306e3b3...`; fresh Windows Review/Matrix/Required CI y gates aplicables; integrar solo con exact-head green + race-check.  
CI-FALLBACK: F4/25.2 READ-ONLY readiness inventory solo si PRIMARY espera operación externa; cero writes; recheck PRIMARY.

### WOZ — `NIGHT-WOZ-049` — F3 / 20.2 / REUSE #77
PRIMARY: reutilizar el CLOSED/unmerged #77 ahora explícitamente autorizado, refresh/reopen SAME artifact y validar harness parametrizable sin target inventado ni provider load. Resultado máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 050

1. **#76 / F3 19.2 legal:** candidate útil pero stale tras #73; refresh + in-app canonical consistency puede cerrar el slice software/legal interno.
2. **#72 / F4 windows-review:** candidate probado pero stale tras #73; refresh + fresh CI puede integrar otra journey literal.
3. **F3/20.2 / #77 harness:** ahora existe artifact reusable; convertirlo legítimamente en HARNESS_READY reduce un gap interno sin fingir capacidad real.
4. **F2 / #69 13.1 Web:** crítico pero bloqueado por write surface; no repetir PRIMARY ciego.
5. **F4 #74 → #71 / windows-auth:** frozen hasta cambio factual del merge-flow.
6. **F3 #75 / 20.1:** frozen por write-flow blocker.
7. **F2 / 12.1:** runtime real-browser cold/warm.
8. **F2 #70:** safe-write + stale baseline.
9. **F0/F1/F3 external tails + F4 D22/D23 + resto F2/F4 matrix:** externos/RO o aún abiertos. F5 no se abre.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-046`; 045 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-045`; 044 está superseded.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-049`; 048 ya fue procesado DONE/INTEGRATED.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge adicional obliga reconciliación exact-head de los otros candidates.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 050; GitHub vivo prevalece si cambia después.
