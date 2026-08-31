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

## Estado vivo — NIGHT-JOBS-076

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada al preflight:** `integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`.
- **Último merge material verificado:** PR #82 → `957f97771b7a15554cf6e002fe9eb215c71a65cc`, parents `5e117d69...` + `eb817223...`.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 `PENDING_EXTERNAL_PROOF`; D10.2 requiere decisión RO.
- **F2:** 11.1/11.2/12.2 `[x]`; 12.1 runtime browser real abierto; 13.1 #69/#70 frozen; 13.2 reasignado AAA072 READ-ONLY tras AAA071 sin resultado; 14.1 #81 abierto/stale y aparcado.
- **F3:** 17.1/17.2/18.1 `[x]`; 18.2 global abierto. 20.1 software observability integrado. 20.2 tiene #78 harness integrado y ahora PR #83 durable-waitlist candidate @ `52b58f56...`; dedicated waitlist CI PASS pero PR-wide Test - Desktop Portability seguía `in_progress` al preflight. Real 160-runtime + latency/error/queue/recovery + safety margin siguen sin evidencia.
- **F4:** 21.1/21.2 y 24.1/24.2 `[x]`; 25.1 incompleto. PR #79 sigue OPEN/non-draft/mergeable con exact base live `957f9777...`, head `a3c4d56e...`, delta docs-only de un archivo y Required CI exact-head SUCCESS. BBB071 posee la única transacción de integración autorizada; todavía no hay merge claim.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 076

- `NIGHT-AAA-071`: no RESULTADO DEL TURNO ni handoff nuevo antes del ciclo; superseded por AAA072 tras recalcular desde cero, no PASS.
- `NIGHT-BBB-070`: no RESULTADO DEL TURNO ni handoff nuevo antes del ciclo; #79 permanece materialmente listo según GitHub vivo y se emite BBB071 por camino crítico, no por inercia.
- `NIGHT-WOZ-074`: `WAITING_CI`; PR #83 draft/open/mergeable exact head `52b58f56d66430db1ecdce9f572680c61d5d9fe3`. Dedicated durable-waitlist CI PASS; fallback F3/18.2 billing map DONE_READ_ONLY. GitHub postcheck CYCLE 076 todavía mostraba Test - Desktop Portability in-progress; no readiness/merge promotion.

## OWNERS — CYCLE 076

### AAA — `NIGHT-AAA-072` — F2 / 13.2 READ-ONLY
PRIMARY: ejecutar auditoría factual de acciones Web visibles para `Web no llama Tauri/Desktop` + `0 pérdida silenciosa`; sin writes y sin #81/#69/#70.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-071` — F4 / 25.2 / SAME #79
PRIMARY: final fresh race-check de integration/base/head/delta/CI y, solo si todo sigue exacto, merge #79 con expected-head protection; verificar merge SHA + parents.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-075` — F3 / 20.2 / SAME #83
PRIMARY: concluir únicamente la transacción de CI/readiness del exact head actual; no cambiar código mientras corre CI; si full exact-head CI queda green, verificar scope y opcionalmente Draft→Ready si el flujo autorizado funciona; **NO MERGE**. Si BBB mueve integration primero, STOP `STALE_BASE / NEEDS_RECONCILE`.  
CI-FALLBACK: NONE; el billing map seguro ya se consumió en WOZ074.

## Camino crítico global — CYCLE 076

1. F4/25.2 #79: exact-base/exact-head green docs-only candidate → transacción final BBB071.
2. F3/20.2 #83: terminar CI/readiness sin mezclarlo con la integración serializada de #79.
3. F2/13.2: obtener el audit boundary/silent-loss que define el siguiente slice Web seguro.
4. F3/20.2: reconciliar/integrar durable waitlist y después runtime aplicable 160 + latency/error/queue/recovery + safety margin.
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

**AAA:** execute once `NIGHT-AAA-072`.  
**BBB:** execute once `NIGHT-BBB-071`; only possible integration mutation is #79 after fresh exact check.  
**WOZ:** execute once `NIGHT-WOZ-075`; #83 CI/readiness only, no merge.  
**JOBS:** next cycle begins by reading integration. If #79 merged, #83's old base is stale by definition and must not be promoted without reconciliation + fresh evidence.  
**PLAN_HEALTH:** synced to GitHub observed in CYCLE 076; GitHub live prevails if it changes afterward.
