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

## Estado vivo — NIGHT-JOBS-078

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada al preflight:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.
- **Último merge material verificado:** PR #82 → `957f97771b7a15554cf6e002fe9eb215c71a65cc`, parents `5e117d69...` + `eb817223...`.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 `PENDING_EXTERNAL_PROOF`; D10.2 requiere decisión RO.
- **F2:** 11.1/11.2/12.2 `[x]`; 12.1 runtime browser real abierto; 13.1 #69/#70 frozen; 13.2 sigue sin resultado aceptable y queda reasignado AAA074 READ-ONLY; 14.1 #81 abierto/stale y aparcado.
- **F3:** 17.1/17.2/18.1 `[x]`; 18.2 global abierto. 20.1 software observability integrado. 20.2 tiene #78 harness integrado y PR #83 durable-waitlist candidate @ `52b58f56...`; #83 sigue draft/open sobre exact base `957f9777...`. Real 160-runtime + latency/error/queue/recovery + safety margin siguen sin evidencia.
- **F4:** 21.1/21.2 y 24.1/24.2 `[x]`; 25.1 incompleto. PR #79 sigue OPEN/non-draft sobre exact base live `957f9777...`, head `a3c4d56e...`, docs-only; BBB073 posee la única transacción de integración autorizada.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 078

- `NIGHT-AAA-073`: no RESULTADO DEL TURNO ni handoff nuevo antes del ciclo; superseded por AAA074 tras recalcular desde cero, no PASS.
- `NIGHT-BBB-072`: no RESULTADO DEL TURNO ni handoff nuevo antes del ciclo; #79 permanece materialmente exacto/listo según GitHub vivo y se emite BBB073 por camino crítico, no por inercia.
- `NIGHT-WOZ-076`: no RESULTADO DEL TURNO ni handoff nuevo antes del ciclo; #83 permanece draft/open sobre el mismo baseline y se emite WOZ077 para SAME #83 sin merge.

## OWNERS — CYCLE 078

### AAA — `NIGHT-AAA-074` — F2 / 13.2 READ-ONLY
PRIMARY: ejecutar auditoría factual de acciones Web visibles para `Web no llama Tauri/Desktop` + `0 pérdida silenciosa`; sin writes y sin #81/#69/#70.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-073` — F4 / 25.2 / SAME #79
PRIMARY: fresh race-check de integration/base/head/delta/CI y, solo si todo sigue exacto, merge #79 con expected-head protection; verificar merge SHA + parents.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-077` — F3 / 20.2 / SAME #83
PRIMARY: si integration sigue `957f9777...`, verificar #83 y promover Draft→Ready sin mover head/base; si BBB ya movió integration, reconciliar history-preserving SAME #83 sobre nuevo live baseline + fresh exact-head CI; **NO MERGE**.  
CI-FALLBACK: F3/19.1 READ-ONLY deployment/domain evidence map solo durante `WAITING_CI`, sin provider/DNS mutations ni #76.

## Camino crítico global — CYCLE 078

1. F4/25.2 #79: transacción final BBB073.
2. F3/20.2 #83: preservar/promover o reconciliar inmediatamente después de cualquier movimiento de #79, sin merge concurrente.
3. F2/13.2: audit boundary/silent-loss para definir el siguiente slice Web seguro.
4. F3/20.2: integrar durable waitlist en ciclo posterior autorizado y obtener runtime aplicable 160 + latency/error/queue/recovery + safety margin.
5. F2/14.1 #81: requiere superficie segura de history-preserving reconciliation; sigue aparcado.
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

**AAA:** execute once `NIGHT-AAA-074`.  
**BBB:** execute once `NIGHT-BBB-073`; only possible integration mutation is #79 after fresh exact check.  
**WOZ:** execute once `NIGHT-WOZ-077`; SAME #83 readiness/reconcile only, no merge; fallback 19.1 read-only only while waiting fresh CI.  
**JOBS:** next cycle begins by reading integration. If #79 merged, verify merge SHA/parents and treat unreconciled #83 base `957f9777...` as stale.  
**PLAN_HEALTH:** synced to GitHub observed in CYCLE 078; GitHub live prevails if it changes afterward.
