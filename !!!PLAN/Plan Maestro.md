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

## Estado vivo — NIGHT-JOBS-048

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- **Último merge material:** PR #68 → `a9d35a3d...`; GitHub vivo no muestra merge posterior.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1 Web:** #69 sigue OPEN/Ready/mergeable @ `b2ab75ae1dbde4e3aba389da844f466920a5d6eb`, stale desde `3ad8f55a...`. AAA043 terminó `PENDING / STOP_WRITE_SURFACE`; #69 queda frozen/unowned hasta superficie patch-capable.
- **F2 / 13.1 server:** #70 frozen por safe-write + stale baseline.
- **F2 / 13.2:** `NIGHT-AAA-044` hace gap map read-only para definir slices mínimos sin tocar #69/#70.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** #73 sigue OPEN/Ready/mergeable @ `fc831172...`, no merge verificable; frozen.
- **F3 / 20.1:** #75 sigue OPEN/Ready/mergeable @ `bb493b37...`; corrective conocido/write blocker; frozen.
- **F3 / 20.2:** audit gap map retenido. WOZ046 no produjo resultado; superseded. `NIGHT-WOZ-047` conserva únicamente harness parametrizable, sin claim 2×.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74 sigue OPEN/Ready/mergeable @ `14dfba52...`; merge-flow blocker previo; #71 espera integración real.
- **F4 / windows/review:** #72 sigue OPEN, draft=false, merged_at=null, head `904fbf3c...`, base exacta `a9d35a3d...`; exact-head gates conocidos verdes. BBB042 no produjo resultado y queda superseded; `NIGHT-BBB-043` es owner único.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 048

### AAA — `NIGHT-AAA-044` — F2 / 13.2
PRIMARY: read-only code-grounded gap map de ReviewShell Import/Edit/Bulk, progreso N/N, errores/retry/skip/cancel/confirmación y cobertura E2E; producir slices mínimos y dependencias exactas. No writes, no #69/#70.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-043` — F4 / SAME #72
PRIMARY: race-check + integrar #72 solo si base/head/evidencia siguen aplicables; si baseline mueve, refresh estrecho + fresh applicable CI.  
CI-FALLBACK: F4/25.2 READ-ONLY readiness inventory solo mientras PRIMARY espere merge/review/queue externo; luego recheck PRIMARY.

### WOZ — `NIGHT-WOZ-047` — F3 / 20.2
PRIMARY: software slice mínimo para harness parametrizable de capacidad/carga. Debe exigir target explícito, negarse a claim 2× sin target aprobado y medir/reportar; no provider/infra/load productivo, no #73/#75.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 048

1. **#72 / windows-review:** candidate interno más listo; exact-head verde conocido; falta integración real.
2. **#69 / F2 13.1 Web:** sigue crítico pero actualmente bloqueado por write surface; no gastar otro ciclo ciego.
3. **F3/20.2:** cerrar gap de harness software; target aprobado + runtime 2× siguen separados.
4. **F2/13.2:** convertir requisitos abiertos en slices exactos y dependency-safe para ejecución posterior.
5. **#74 → #71 / windows-auth:** frozen hasta cambio factual del merge-flow.
6. **#75 / F3 20.1:** frozen por write-flow blocker.
7. **#73 / F3 18.2:** frozen por merge-flow blocker.
8. **F2/12.1:** runtime real-browser cold/warm.
9. **#70 / F2 13.1 server:** safe-write + stale baseline.
10. **F0/F1/F3 external tails + F4 D22/D23:** externos/RO. F5 no se abre.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-044`; #69 queda frozen hasta patch-capable surface.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-043`; 042 está superseded.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-047`; 046 está superseded.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga reconciliación exact-head antes de integrar candidates restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 048; GitHub vivo prevalece si cambia después.
