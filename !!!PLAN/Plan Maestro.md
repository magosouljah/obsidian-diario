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

## Estado vivo — NIGHT-JOBS-055

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada:** `integration-v0.8.0-alpha.1 @ a306e3b3f6b4a6cf9d678e325b6e529b5344fffe`.
- **Último merge material verificado:** PR #73 → `a306e3b3...`. No merge posterior observado durante el preflight CYCLE 055.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1:** #69 frozen por `STOP_WRITE_SURFACE`; #70 frozen por safe-write + stale baseline.
- **F2 / 14.1:** AAA050 no dejó resultado final antes del ciclo y fue superseded; `NIGHT-AAA-051` queda owner único del mismo slice mínimo REUSE-FIRST de streaming/memory safety.
- **F2 / 14.2:** read-only fallback de AAA051 únicamente durante espera externa real del PRIMARY.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** #73 reconciliation/exception-queue software slice INTEGRATED; global 18.2 sigue abierto por escenarios/provider/business-policy reales.
- **F3 / 19.2:** #76 sigue OPEN en `36d218609...`, stale y frozen hasta safe history-preserving refresh.
- **F3 / 20.1:** #75 frozen por corrective/write-flow blocker.
- **F3 / 20.2:** #78 sigue OPEN exact-base, head `50aac3f0...`, 2 archivos/+139, exact-head Required CI SUCCESS. WOZ053 no dejó resultado y fue superseded; `NIGHT-WOZ-054` posee la única mutación de integration autorizada del ciclo para race-check + merge. Aun integrado, máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74/#71 frozen; `NOT_COVERED`.
- **F4 / windows/review:** #72 stale/frozen; no historical CI reuse.
- **F4 / 25.2:** BBB049 creó PR #79 exact-base, head `c6ec2910...`, un docs-only readiness artifact (+84). JOBS CYCLE 055 verificó exact-head checks completos sin failure/in-progress y `Required CI = SUCCESS`. #79 NO está merged y queda `HOLD_GREEN_PENDING_SERIAL_INTEGRATION` para evitar carrera con WOZ/#78.
- **F4 / 25.1:** residual map BBB049: Web 10/10 NOT_COVERED; Windows import/updater AUTOMATED_PASS y resto NOT_COVERED; macOS updater AUTOMATED_PASS y resto NOT_COVERED; iPhone todo PENDING_EXTERNAL. `NIGHT-BBB-050` toma únicamente Web/auth como journey dedicado.
- **5.1:** `[x]`. **5.2:** `[x]`.

## RESULTADOS PROCESADOS — CYCLE 055

- `NIGHT-AAA-050`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; no implementation/CI/merge claim.
- `NIGHT-BBB-049`: `PENDING / WAITING_CI` al cierre del worker. PR #79 docs-only exact-base. JOBS verificó después exact-head `Required CI = SUCCESS`, sin failures/in-progress; fallback F4/25.1 residual map `DONE / READ_ONLY`. No merge ni full 25.2 PASS.
- `NIGHT-WOZ-053`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; #78 continúa OPEN y verde, sin merge claim.
- Último resultado material integrado aceptado sigue siendo WOZ048 / #73 `DONE / INTEGRATED` como partial F3/18.2 software slice only.

## OWNERS — CYCLE 055

### AAA — `NIGHT-AAA-051` — F2 / 14.1
PRIMARY: auditar/reutilizar media Web actual y cerrar solo el menor gap literal de progressive/Range-style playback, giant-file memory safety y cleanup/cancel; focused tests + fresh exact-head CI; sin Player redesign.  
CI-FALLBACK: F2/14.2 READ-ONLY player-control gap map solo si PRIMARY queda code-complete esperando CI/review/merge; cero writes; recheck PRIMARY.

### BBB — `NIGHT-BBB-050` — F4 / 25.1 Web/auth
PRIMARY: consumir el residual map BBB049 y producir únicamente evidencia dedicada del journey Web/auth; preferir harness/tests; product fix mínimo solo si el journey alcanza un defecto literal independiente y sin overlap AAA. #79 no se integra en este turno.  
CI-FALLBACK: `NONE` para evitar repetir la auditoría 25.1 ya completada.

### WOZ — `NIGHT-WOZ-054` — F3 / 20.2
PRIMARY: SAME #78. Recheck exact head/base/two-file delta/CI/mergeability y live integration inmediatamente antes de integrar; merge solo race-clean por flujo WOZ autorizado; verificar SHA + parents post-merge. Máximo `HARNESS_READY / RUNTIME_CAPACITY_UNVERIFIED`.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado desde cero CYCLE 055

1. **F3/20.2 / PR #78:** único merge autorizado del ciclo; exact-base, narrow, Required CI verde.
2. **F2/14.1:** trabajo Web interno dependency-safe, AAA051.
3. **F4/25.1 Web/auth:** primer journey dedicado desde residual map, BBB050.
4. **F4/25.2 / PR #79:** green candidate preservado; reconciliar/integrar solo después de conocer el baseline resultante de #78.
5. **F3 #76 / legal Settings:** frozen hasta safe history-preserving refresh.
6. **F4 #72 / windows-review:** frozen por refresh blocker.
7. **F4 #74 → #71 windows-auth:** frozen hasta cambio factual de integration/refresh dependency.
8. **F3 #75 / 20.1:** frozen por write-flow blocker.
9. **F2 / 12.1:** real-browser cold/warm runtime evidence.
10. **F2 #69/#70:** write/safe-write blockers.
11. **F2 14.2–15 + remaining F4 25.1 rows:** residual interno posterior.
12. **F0/F1/F3 external tails + F4 D22/D23:** external/RO prerequisites remain. F5 does not open.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-051`; 050 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-050`; #79 queda hold-green sin merge durante este turno.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-054`; SAME #78 únicamente.  
**JOBS:** siguiente ciclo procesa resultados reales; si #78 mueve baseline, reconciliar #79 y cualquier candidate restante antes de confiar en CI previo.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 055; GitHub vivo prevalece si cambia después.
