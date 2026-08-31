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

## Estado vivo — NIGHT-JOBS-080

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada al preflight:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.
- **Último merge material verificado:** PR #82 → `957f97771b7a15554cf6e002fe9eb215c71a65cc`, parents `5e117d69...` + `eb817223...`.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 `PENDING_EXTERNAL_PROOF`; D10.2 requiere decisión RO.
- **F2:** 11.1/11.2/12.2 `[x]`; 12.1 runtime browser real abierto. 13.1 #69/#70 frozen. 13.2 audit AAA071 consumido; AAA075 no produjo resultado y AAA076 toma únicamente executable Web/Tauri call-spy + Save All partial-failure/conflict/retry evidence/fix mínimo. 14.1 #81 stale/parked.
- **F3:** 17.1/17.2/18.1 `[x]`; 18.2 global abierto. 20.1 software observability integrado. #83 durable-waitlist candidate sigue OPEN/DRAFT exact base `957f9777...`, head `52b58f56...`, exact-head applicable CI verde; WOZ078 quedó `BLOCKED_STOP` por tooling Draft→Ready, no producto/CI. Real 160-runtime + latency/error/queue/recovery + safety margin siguen sin evidencia y pasan a WOZ079 con REUSE #78.
- **F4:** 21.1/21.2 y 24.1/24.2 `[x]`; 25.1 incompleto. #79 sigue OPEN/non-draft/mergeable sobre exact base live `957f9777...`, head `a3c4d56e...`, changed_files=1 docs-only; exact-head applicable workflows concluidos con Test Desktop Portability/D6/D7 SUCCESS. BBB075 posee la única transacción de integración autorizada.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 080

- `NIGHT-AAA-075`: no RESULTADO DEL TURNO ni handoff nuevo antes del ciclo; superseded por AAA076, no PASS. Se conserva REUSE-FIRST de AAA071.
- `NIGHT-BBB-074`: no RESULTADO DEL TURNO ni handoff nuevo; #79 permanece exacto/listo según GitHub vivo y se emite BBB075 por camino crítico, no por inercia.
- `NIGHT-WOZ-078`: `BLOCKED_STOP` factual. #83 quedó exact/scoped + exact-head CI green, pero Draft→Ready falló en el conector por `Repository.fullDatabaseId`; no hubo head/base/integration mutation y el fallback 19.1 no fue elegible.

## OWNERS — CYCLE 080

### AAA — `NIGHT-AAA-076` — F2 / 13.2 executable evidence
PRIMARY: reutilizar AAA071 y convertir el finding en browser/component journey con Tauri/Desktop `invoke`/`listen` call-spies + Save All partial-failure/conflict/retry/no-silent-loss. Solo fix F2 mínimo si el test prueba un gap literal. Nuevo PR solo si cambia archivos; fresh CI; **NO MERGE**.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-075` — F4 / 25.2 / SAME #79
PRIMARY: fresh race-check de integration/base/head/file-delta/CI y, solo si todo sigue exacto, merge #79 con expected-head protection; verificar merge SHA + parents.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-079` — F3 / 20.2 runtime evidence
PRIMARY: REUSE #78 harness ya integrado; obtener evidencia materialmente aplicable a 160 concurrent users para latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin contra 80 expected. No code/infra/provider mutation y no tocar #83.  
CI-FALLBACK: F3/19.1 READ-ONLY evidence map únicamente si PRIMARY entra genuinamente en `WAITING_EXTERNAL_RUNTIME` tras haber iniciado una operación externa verificable.

## Camino crítico global — CYCLE 080

1. F4/25.2 #79: transacción final BBB075.
2. F3/20.2: obtener runtime aplicable 160 + latency/error/queue/recovery + measured safety margin usando #78; #83 sigue parked por tooling Ready.
3. F2/13.2: executable Web/Tauri boundary + Save All no-silent-loss evidence/fix mínimo.
4. #83: después de cualquier movimiento de integration, history-preserving reconcile + fresh exact-head CI y vía Ready verificable antes de integración.
5. F2/14.1 #81: requiere superficie segura de history-preserving reconciliation; aparcado.
6. F2/12.1: cold/warm startup en browser real.
7. F3/19.x #76 y F2/13.1 #69/#70: frozen/aparcados hasta cambio factual.
8. F4/25.1 journeys restantes + signing/notarization/hardware externos.
9. F0/F1 y provider/legal/operational tails externos/RO.

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

**AAA:** execute once `NIGHT-AAA-076`; no repeat audit.  
**BBB:** execute once `NIGHT-BBB-075`; only possible integration mutation is #79 after fresh exact check.  
**WOZ:** execute once `NIGHT-WOZ-079`; runtime evidence only; #83 remains parked/read-only for this assignment.  
**JOBS:** next cycle begins by reading integration. If #79 merged, verify merge SHA/parents and treat #83 base `957f9777...` as stale. Process runtime evidence literally; do not convert local/synthetic evidence into 20.2 PASS if not materially applicable.  
**PLAN_HEALTH:** synced to GitHub observed in CYCLE 080; GitHub live prevails if it changes afterward.
