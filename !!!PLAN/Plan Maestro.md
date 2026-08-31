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

## Estado vivo — NIGHT-JOBS-082

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`, parents `957f97771b7a15554cf6e002fe9eb215c71a65cc` + `a3c4d56e8317d7711832154ecc72afe581d2b309`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 browser runtime abierto; 13.1 frozen. Late AAA074 handoff revalidó sobre live base una brecha concreta: Review Save/Save All puede avanzar/cerrar antes de durable cloud completion. AAA078 corrige únicamente ese action-boundary + focused executable evidence; 13.2 sigue OPEN.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 20.1 software integrated. #83 fue reconciliado history-preserving a live base; head `803b2143e6ea03f6549118e9241fee320dfccdee`; dedicated waitlist run `33388377959` SUCCESS y Required CI exact-head SUCCESS. PR sigue OPEN/DRAFT; WOZ081 owns authorized Ready→expected-head merge transaction. Runtime 160/safety-margin sigue independiente y UNVERIFIED.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #79 readiness artifact integrado; BBB077 mantiene windows/auth #71/#74 current-evidence slice, NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 082

- `NIGHT-WOZ-080`: `WAITING_CI` al cierre; reconciliation de #83 verificada. Post-turn GitHub: exact-head dedicated waitlist + Required CI concluyeron SUCCESS. No Ready/merge claim; runtime capacity sigue UNVERIFIED.
- `NIGHT-AAA-077`: no final result/handoff observado antes del ciclo; not PASS. Late Issue #41 `5478129410` pertenece a `NIGHT-AAA-074`, no a AAA077, pero se acepta como evidencia reusable porque revalidó el finding sobre el baseline vivo actual.
- `NIGHT-BBB-076`: no final result/handoff observado antes del ciclo; not PASS.

## OWNERS — CYCLE 082

### AAA — `NIGHT-AAA-078` — F2 / 13.2
PRIMARY: corregir mínimo Review Save/Save All para esperar durable Web persistence, distinguir `saved/conflict/failed`, exponer retry/no-silent-loss y cubrir touched Web paths con executable Tauri/Desktop call-spies. REUSE #69 lineage solo como helper/input; no revivir #69. Fresh exact-head CI; NO MERGE.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-077` — F4 / 25.1 windows/auth
PRIMARY: REUSE #71/#74; safe history-preserving refresh onto live base si literal y limpio, authoritative Windows auth journey + fresh exact-head CI. STOP with gap map if unsafe. NO MERGE.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-081` — F3 / 20.2 / #83
PRIMARY: recheck live base/head/scope + exact-head green CI, authorized Draft→Ready, then expected-head merge only if exact/race-free; verify merge SHA/parents. Only WOZ/#83 may mutate integration.  
CI-FALLBACK: NONE; #78 already proved local/synthetic-only and cannot satisfy runtime-capacity gate.

## Camino crítico global — CYCLE 082

1. #83 durable waitlist: Ready→exact merge transaction after now-green exact-head CI.
2. F2/13.2 concrete Review Save/Save All durable completion/no-silent-loss correction + executable evidence.
3. F4/25.1 windows/auth current evidence via #71/#74 reuse.
4. F3/20.2 materially applicable 160 runtime + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin.
5. F2/12.1 real-browser cold/warm evidence.
6. F2/14.1 #81 and F3/19.x #76 remain frozen until safe explicit reconciliation.
7. F4 signing/notarization/hardware/tester execution external.
8. F0/F1 provider/legal/operational tails external/RO.

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

AAA executes `NIGHT-AAA-078`; BBB executes `NIGHT-BBB-077`; WOZ executes `NIGHT-WOZ-081`. Next JOBS cycle starts from live integration and processes exact results only. If #83 merges, verify resulting SHA/parents and keep 20.2 OPEN until applicable runtime 160 evidence exists. `PLAN_HEALTH`: synced CYCLE 082; GitHub live prevails if it moves afterward.
