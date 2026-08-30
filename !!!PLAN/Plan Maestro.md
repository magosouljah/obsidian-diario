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

## Estado vivo — NIGHT-JOBS-049

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada al preflight:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- **Último merge material observado:** PR #68 → `a9d35a3d...`; no se aceptó claim de merge posterior durante el preflight.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1 Web:** #69 sigue OPEN/Ready/mergeable @ `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`, stale desde `3ad8f55a...`; frozen/unowned por `STOP_WRITE_SURFACE`.
- **F2 / 13.1 server:** #70 frozen por safe-write + stale baseline.
- **F2 / 13.2:** AAA044 no produjo resultado y queda superseded; audit read-only se conserva solo como CI-FALLBACK de AAA045 cuando su PRIMARY esté esperando operación externa.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** #73 sigue OPEN/Ready/mergeable @ `fc831172c4c86d97cadb03801a6777777fd345bb`, base exacta `a9d35a3d...`, exact-head gates verdes; `NIGHT-WOZ-048` es owner único para integración.
- **F3 / 19.2:** apareció #76 OPEN/Ready/mergeable @ `36d218609cf2488997755312fa2dafd0a019d070`, base exacta `a9d35a3d...`; Privacy/Terms v1 + public `/privacy` `/terms` + entry links y CI general verde. Settings todavía contiene copy legal temporal/placeholders/contacto viejo; `NIGHT-AAA-045` es owner único para reuse canónico dentro del SAME #76. No se marca 19.2 `[x]`.
- **F3 / 20.1:** #75 sigue OPEN/Ready/mergeable @ `bb493b37...`; corrective conocido/write blocker; frozen.
- **F3 / 20.2:** WOZ047 no produjo resultado; superseded. Harness parametrizable queda solo como CI-FALLBACK independiente de WOZ048; approved peak + runtime 2× siguen abiertos.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74 sigue OPEN/Ready/mergeable @ `14dfba52...`; merge-flow blocker previo; #71 espera integración real.
- **F4 / windows/review:** #72 sigue OPEN/Ready/mergeable @ `904fbf3c...`, base exacta `a9d35a3d...`; exact-head Windows Review/Matrix/D6/D7/Required CI/Windows Import verdes. `NIGHT-BBB-044` es owner único para integración.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 049

### AAA — `NIGHT-AAA-045` — F3 / 19.2 / SAME #76
PRIMARY: reutilizar documentos legales canónicos de #76 y reemplazar únicamente el copy temporal/placeholders/contacto viejo de las superficies Privacy/Terms ya existentes en `SettingsPanel.tsx`; focused tests + fresh exact-head CI. No segunda UI, no política inventada, no infra/DNS/deploy, no #69/#70.  
CI-FALLBACK: F2/13.2 READ-ONLY gap map solo si PRIMARY queda code-complete y realmente esperando CI/review/merge. Debe entregar matriz/path/symbol/test; cero writes; después recheck PRIMARY.

### BBB — `NIGHT-BBB-044` — F4 / SAME #72
PRIMARY: consumir exact-head SUCCESS, race-check y merge solo si integration/head siguen aplicables. Si baseline mueve, refresh estrecho + fresh applicable CI. No auth/#74/#71 ni legal/#76.  
CI-FALLBACK: F4/25.2 READ-ONLY readiness inventory solo si PRIMARY espera operación externa merge/review/queue; cero writes; después recheck PRIMARY.

### WOZ — `NIGHT-WOZ-048` — F3 / SAME #73
PRIMARY: consumir exact-head SUCCESS, race-check e integrar el software slice de reconciliation/exception queue; si baseline mueve, narrow refresh + fresh applicable CI. No claim de 18.2 completo.  
CI-FALLBACK: F3/20.2 en rama/PR separados, únicamente si PRIMARY espera operación externa; harness parametrizable sin target inventado ni provider/infra load. Resultado máximo `HARNESS_READY`; runtime capacity sigue UNVERIFIED.

## Camino crítico global — recalculado CYCLE 049

1. **#73 / F3 18.2 reconciliation:** exact-base/head green y anterior a 19/20; integración puede reducir un gap factual inmediato.
2. **#72 / F4 windows-review:** exact-base/head green; integración convierte otra journey literal en matrix integrada.
3. **#76 / F3 19.2 legal:** canonical docs/public routes green; falta consistencia in-app mínima antes de integración ideal.
4. **#69 / F2 13.1 Web:** crítico pero bloqueado por write surface; no gastar otro PRIMARY ciego.
5. **F2 / 13.2:** audit mínimo se ejecuta solo como fallback AAA cuando #76 esté esperando.
6. **#74 → #71 / windows-auth:** frozen hasta cambio factual del merge-flow.
7. **#75 / F3 20.1:** frozen por write-flow blocker.
8. **F3 / 20.2:** harness software puede avanzar como fallback; approved peak/runtime 2× siguen separados.
9. **F2 / 12.1:** runtime real-browser cold/warm.
10. **#70 / F2 13.1 server:** safe-write + stale baseline.
11. **F0/F1/F3 external tails + F4 D22/D23 + resto F2/F4 matrix:** externos/RO o aún abiertos. F5 no se abre.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-045`; 044 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-044`; 043 está superseded.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-048`; 047 está superseded.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga reconciliación exact-head antes de integrar candidates restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 049; GitHub vivo prevalece si cambia después.
