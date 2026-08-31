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

## Estado vivo — NIGHT-JOBS-075

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada al preflight:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.
- **Último merge material verificado:** PR #82 → `957f97771b7a15554cf6e002fe9eb215c71a65cc`, parents `5e117d69...` + `eb817223...`.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 siguen como tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 `PENDING_EXTERNAL_PROOF`; D10.2 requiere decisión RO.
- **F2:** 11.1/11.2/12.2 `[x]`; 12.1 runtime browser real abierto; 13.1 #69/#70 frozen; 13.2 asignado AAA071 READ-ONLY; 14.1 #81 sigue abierto/stale y queda aparcado, no cerrado.
- **F3:** 17.1/17.2/18.1 `[x]`; 18.2 global abierto; 19.x #76 sigue abierto/stale y queda aparcado; 20.1 software observability integrado; 20.2 sigue abierto por 160-runtime + safety margin + durable waitlist. WOZ074 toma únicamente el slice interno durable-waitlist.
- **F4:** 21.1/21.2 y 24.1/24.2 `[x]`; 25.1 incompleto; #79 quedó refrescado a exact head `a3c4d56e8317d7711832154ecc72afe581d2b309` sobre live `957f9777...`, delta docs-only, y JOBS verificó Required CI exact-head `SUCCESS` sin checks in-progress/failure observados. BBB070 posee la transacción final; **todavía no hay merge claim**.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 075

- `NIGHT-AAA-070`: `PENDING / STOP_HISTORY_RECONCILE_UNAVAILABLE`; #81 no cambió. Compare seguía 4 ahead / 13 behind y dos paths materiales; CI previa es stale. Resultado procesado como blocker de superficie, no PASS.
- `NIGHT-BBB-069`: `WAITING_CI`; #79 fue reconciliado history-preservingly a `a3c4d56e...`, behind=0 y exactamente un archivo docs-only. Su fallback F4/25.1 completó mapa read-only; Windows playback quedó como menor journey futuro. Después del handoff, JOBS verificó el exact head y CI ya concluyó verde; no se atribuye merge todavía.
- `NIGHT-WOZ-073`: sin RESULTADO DEL TURNO/handoff nuevo antes del ciclo; superseded por WOZ074 después de recalcular desde cero, no por PASS.
- AAA070 handoff no pudo publicarse por el connector del worker; JOBS lo conserva y lo replica en Issue #41.

## OWNERS — CYCLE 075

### AAA — `NIGHT-AAA-071` — F2 / 13.2 READ-ONLY
PRIMARY: auditoría factual de acciones Web visibles sobre live integration para probar/mapear `Web no llama Tauri/Desktop` y `0 pérdida silenciosa`; sin writes, sin #81/#69/#70.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-070` — F4 / 25.2 / SAME #79
PRIMARY: race-check final de integration/base/head/delta/CI y, solo si todo sigue exacto, merge #79 con expected-head protection; verificar merge SHA + parents. Máximo claim: readiness artifact interno integrado.  
CI-FALLBACK: NONE; el mapa F4/25.1 ya se hizo en BBB069.

### WOZ — `NIGHT-WOZ-074` — F3 / 20.2 durable waitlist
PRIMARY: REUSE-FIRST, implementar solo persistencia/recovery/aislamiento mínimos de user waitlist; tests + fresh exact-head CI; **NO MERGE** y ninguna capacidad runtime claim.  
CI-FALLBACK: F3/18.2 READ-ONLY billing-scenario evidence map únicamente durante genuine WAITING_CI/review; sin provider calls ni writes.

## Camino crítico global — CYCLE 075

1. F4/25.2 #79: exact-head green candidate → transacción final serializada BBB070.
2. F3/20.2: cerrar el gap interno durable-waitlist sin confundirlo con el runtime 160 todavía faltante.
3. F2/13.2: auditoría de boundary/silent-loss para decidir el siguiente slice Web sin reabrir #69/#70 a ciegas.
4. F3/20.2: evidencia runtime aplicable a 160 + latency/error/queue/recovery + safety margin medida.
5. F2/14.1 #81: requiere una superficie capaz de reconciliar historia de forma segura; sigue abierto/aparcado.
6. F2/12.1: cold/warm startup en browser real.
7. F3/19.x #76 y F2/13.1 #69/#70: aparcados hasta cambio factual de blocker/superficie segura.
8. F4/25.1 journeys restantes + signing/notarization/hardware externos.
9. F0/F1 y F3 external/provider/legal tails.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementation details hidden.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud does not relay beat/project payloads.
- Permanent auth/control secrets remain control-side; clients use temporary auth.
- Shared-bot fallback only when no free bot; exclusivity per vault is normal path.
- v1 is not published free-only.
- YouTube exists Desktop/Web; Web does not call Tauri.

## NEXT

**AAA:** execute once `NIGHT-AAA-071`.  
**BBB:** execute once `NIGHT-BBB-070`; only possible integration mutation is #79 and only after fresh final race-check.  
**WOZ:** execute once `NIGHT-WOZ-074`; durable waitlist candidate only, no merge.  
**JOBS:** next cycle starts by re-reading integration; any #79 merge moves baseline and invalidates exact-base assumptions for every other candidate.  
**PLAN_HEALTH:** synced to GitHub observed in CYCLE 075; GitHub live prevails if it changes afterward.
