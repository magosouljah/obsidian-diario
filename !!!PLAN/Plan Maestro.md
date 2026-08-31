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

## Estado vivo — NIGHT-JOBS-083

- **Release público:** 🔴 `NO-GO`.
- **Integración estable verificada:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** PR #79 → `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; docs-only F4/25.2 readiness artifact.
- **F0:** núcleo técnico interno cerrado; 1.2 y 2.2 tails externos/administrativos.
- **F1:** D6–D9 PASS; D10.1 requiere off-provider/off-account proof real; D10.2 decisión RO.
- **F2:** 11.1/11.2/12.2 cerrados; 12.1 browser runtime abierto; 13.1 frozen. 13.2 conserva brecha factual Review Save/Save All durable-completion/no-silent-loss; AAA079 owns minimum corrective candidate. 14.1 #81 parked/stale.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 global abierto; 20.1 software integrated. #83 sigue OPEN/DRAFT, mergeable, exact base `816f946c...`, head `803b2143e6ea03f6549118e9241fee320dfccdee`, exact-head dedicated waitlist + Required CI SUCCESS. WOZ082 owns authorized Draft→Ready→expected-head merge. Runtime 160/safety-margin remains UNVERIFIED.
- **F4:** 21.1/21.2 y 24.1/24.2 cerrados; 25.1 incompleto. #79 readiness artifact integrado. #74 sigue OPEN/Ready but stale/not-mergeable; BBB078 owns safe Windows-auth reconciliation/current evidence, NO MERGE.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 083

- `NIGHT-AAA-078`: `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-BBB-077`: `NO_RESULT / SUPERSEDED / NOT_PASS`.
- `NIGHT-WOZ-081`: `NO_RESULT / SUPERSEDED / NOT_PASS`.
- No claim de integración nuevo; baseline no cambió.

## OWNERS — CYCLE 083

### AAA — `NIGHT-AAA-079` — F2 / 13.2
PRIMARY: corregir mínimo Review Save/Save All para esperar durable Web persistence, distinguir `saved/conflict/failed`, retry/no-silent-loss y focused executable Tauri/Desktop call-spies. Bounded PR/fresh exact-head CI; NO MERGE.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-078` — F4 / 25.1 windows/auth
PRIMARY: REUSE #71/#74; reconcile only intended auth corrective if history-preserving and ownership-safe; authoritative Windows auth journey + fresh exact-head CI. NO MERGE.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-082` — F3 / 20.2 / #83
PRIMARY: exact live recheck; authorized Draft→Ready; expected-head merge only if base/head/scope/CI remain exact and race-free; verify merge SHA/parents. Only WOZ/#83 may mutate integration.  
CI-FALLBACK: NONE.

## Camino crítico global — CYCLE 083

1. #83 durable waitlist Draft→Ready→exact merge transaction.
2. F2/13.2 Review Save/Save All durable completion/no-silent-loss correction + executable evidence.
3. F4/25.1 Windows auth safe current evidence via #71/#74 reuse.
4. F3/20.2 materially applicable 160 runtime + latency/error/queue/recovery/no-loss/no-cross-tenant + measured safety margin.
5. F2/12.1 real-browser cold/warm evidence.
6. F2/14.1 #81, F3/19.x #76, F4/#72 remain frozen until safe explicit reconciliation.
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

AAA executes `NIGHT-AAA-079`; BBB executes `NIGHT-BBB-078`; WOZ executes `NIGHT-WOZ-082`. Next JOBS cycle starts from live integration and processes exact results only. If #83 merges, verify resulting SHA/parents and keep 20.2 OPEN until applicable runtime 160 evidence exists. `PLAN_HEALTH`: synced CYCLE 083; GitHub live prevails if it moves afterward.
