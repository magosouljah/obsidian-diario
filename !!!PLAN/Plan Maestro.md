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

## Estado vivo — NIGHT-JOBS-153

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`; PR #96 sigue siendo el último merge material al preflight de CYCLE153.
- **Nuevo candidato F2/12.1:** PR #98 `fix(web): finalize production MTProto transport` = OPEN/Ready/mergeable, base exacta `aa445095...`, head `00da0ab7716242bbd2c7cb8b8cfdea1ca8b3930c`, 1 commit / 6 files. D6, D7, Web Production Build, Productive Temp Auth Compile y F0 secret scan están SUCCESS; `Test - Desktop Portability` / Required CI run `33575511576` seguía `IN_PROGRESS` al emitir assignments. Production behavior fue reportado como library/artwork/playback funcional, pero deployment-source identity debe clasificarse literalmente antes de cerrar 12.1.
- **Issue #97:** `Pre-Beta 1: make library reveal near-instant across Web/Desktop` está OPEN y dice explícitamente que debe resolverse antes de Beta 1. No se mezcla con #98 porque overlap en `src/App.tsx` y #97 pide arquitectura/performance cross-platform separada tras cleanup.
- **F2/12.1:** sigue `NOT_PASS`; AAA149 posee evidencia runtime/deployment READ-ONLY; WOZ152 posee exclusivamente PR #98 mutation/integration.
- **F2/13.2:** durable Review gap confirmado; `BLOCKED_WRITE_SURFACE / UNASSIGNED`.
- **F2/15.1:** recent-reauth product seam sigue prerequisito; BBB148 posee solo la seam mínima, no Trash UI/purge.
- **F0/0.9:** #89 sigue OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, base registrada `816f946c...` stale; security run `33454881387` sigue FAILURE. CYCLE153 no le da mutation owner: WOZ152 puede inventariarlo READ-ONLY únicamente como fallback mientras #98 espera external CI/review/build.
- **F4/Windows Auth:** #93 sigue OPEN @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base `134a293...` stale; sin mutation owner.
- **F1:** D6–D10.1 PASS; D10.2 map complete / alpha candidate NOT_READY. 1.7 espera facts frescos de #98/runtime, #89, recent-reauth y ahora #97.
- **F3:** provider/payment real, legal implementation y runtime160/capacity siguen abiertos/external o pendientes de clasificación explícita 1.7→1.8.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 global sigue abierto; production signing/notarization/hardware/tester execution externos.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE153

- Issue #41 ya contenía JOBS CYCLE152 (`5502310629`) aunque los markdowns nocturnos del vault seguían en CYCLE151; GitHub/Issue prevaleció y se corrigió la deriva documental.
- `NIGHT-AAA-148`, `NIGHT-BBB-147` y `NIGHT-WOZ-151`: sin matching RESULTADO DEL TURNO/handoff worker posterior a CYCLE152 → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- PR #98 apareció después de CYCLE152 y cambió el camino crítico; no se preservó la asignación WOZ sobre #89 por inercia.
- No se promovió DONE/PASS/integration sin evidencia. `Registro de avances.md` no recibe promoción: #98 aún no está integrado y Required CI estaba en progreso al assignment.

## OWNERS — CYCLE153

### AAA — `NIGHT-AAA-149` — F2 / 12.1 runtime proof
PRIMARY: READ-ONLY exact production evidence around PR #98; bind behavior to immutable deployment/source identity where possible; classify every literal runtime item and keep #97 separate. No deploy/code/PR/infra mutation.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-148` — F1/D8 follow-up seam
PRIMARY: REUSE/expose minimum productive fresh same-provider recent-reauth contract bound to user/session, fail-closed and consumable later by destructive callers; focused tests; bounded candidate; **NO MERGE / no Trash UI / no PR #98 files**.  
CI-FALLBACK: only during genuine external wait after clean candidate, F3/18.2 READ-ONLY evidence inventory; no provider/payment mutation or exclusion decision.

### WOZ — `NIGHT-WOZ-152` — F2/12.1 / PR #98
PRIMARY: exclusive mutation/integration owner of #98. Verify exact six-file scope, exact-head Required CI, review/security requirements and deployment-source evidence; expected-head merge #98 only if exact/green/race-free. Do not absorb #97.  
CI-FALLBACK: only while #98 genuinely waits external CI/review/build, #89 strictly READ-ONLY refresh-readiness inventory. #89 files are disjoint from #98; no mutation/rerun/review/merge.

**Only integration mutation authorized CYCLE153: WOZ152 / PR #98, conditional on exact base/head + applicable Required CI SUCCESS + no required review blocker + race-free expected-head. #89 and #93 have no mutation/merge authorization.**

## Camino crítico global — recalculado desde cero

1. **PR #98 / F2/12.1:** exact-head CI + bounded integration + exact production runtime/source proof.
2. **Issue #97 pre-Beta performance:** after #98 cleanup because it overlaps App/startup surfaces; must close before Beta 1.
3. **F0/0.9 / #89:** P1 DNS-rebinding SSRF corrective still stale with red security gate; refresh/exact-green before integration.
4. **F1/D8→F2/15.1:** product recent-reauth seam, then Trash strong confirmation + durable purge/no-false-success.
5. **F2/13.2:** durable Review product gap; remains blocked by safe write surface.
6. **F1/1.7→1.8:** classify remaining alpha blockers with fresh facts; RO decision only afterward.
7. **F4/25.1 / #93:** refresh/revalidate only if 1.7 keeps Windows Auth canonicalization in alpha.
8. **Parallel external/release tails:** F0 1.2/2.2, production signing/notarization, provider/payment, legal implementation, runtime160/capacity, testers/hardware.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementation internals ocultos.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud no relaya beat/project payloads.
- Permanent auth/control secrets remain control-side; clients use temporary auth.
- Shared-bot fallback only when no bot free; normal exclusivity per vault.
- v1 no se publica free-only; eligibility v1 = **18+**.
- YouTube existe Desktop/Web; Web no llama Tauri.

## NEXT

AAA ejecuta `NIGHT-AAA-149`; BBB `NIGHT-BBB-148`; WOZ `NIGHT-WOZ-152`. #98 es la única integration lane. #89/#93 no tienen mutation owner. #97 queda explícitamente next-after-#98, no mezclado. F2/13.2 continúa `BLOCKED_WRITE_SURFACE / UNASSIGNED`. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE153; GitHub live prevalece si cambia después.
