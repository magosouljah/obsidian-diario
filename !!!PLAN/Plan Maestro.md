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

## Estado vivo — NIGHT-JOBS-068

- **Release público:** 🔴 `NO-GO`.
- **Integración estable observada:** `integration-v0.8.0-alpha.1 @ 63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.
- **Último merge material verificado:** PR #78 → `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF`; D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real sigue sin prueba literal.
- **F2 / 13.1:** #69 frozen por `STOP_WRITE_SURFACE`; #70 frozen por safe-write + stale baseline.
- **F2 / 14.1:** `NIGHT-AAA-063` no dejó resultado verificable; `NIGHT-AAA-064` queda owner único del slice mínimo streaming/memory safety. No integration mutation.
- **F3 / 17.1 + 17.2 + 18.1:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.2:** #73 reconciliation/exception-queue software slice INTEGRATED; global 18.2 sigue abierto por 3DS/rechazo/pago tardío/renewal/cancel/upgrade/downgrade/refund/grace-period/provider evidence. WOZ067 puede producir solo gap map READ-ONLY si PRIMARY espera operación externa.
- **F3 / 19.2:** #76 OPEN/stale/frozen.
- **F3 / 20.1:** #75 sigue OPEN/non-draft/mergeable, exact head `40e39393247dbdd506ac01edefa84fd0b0add94c`, `base_sha` exactamente `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`. `NIGHT-WOZ-066` no dejó resultado; `NIGHT-WOZ-067` posee la única transacción exact-head autorizada. GitHub CYCLE 068 verifica Required CI y checks aplicables exact-head completos/verdes; Upgrade 21.2 Staging SKIPPED.
- **F3 / 20.2:** PR #78 `[x] HARNESS SOFTWARE INTEGRATED`; target **80 usuarios simultáneos esperados / 160 de validación (2×)** aprobado. `NIGHT-BBB-062` no dejó resultado; `NIGHT-BBB-063` ejecuta evidencia runtime aplicable a 160. Latency/error/queue/recovery, safety margin y durable user waitlist siguen obligatorios.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / windows/auth:** #74/#71 frozen; `NOT_COVERED`.
- **F4 / windows/review:** #72 stale/frozen.
- **F4 / 25.1:** Web/auth y múltiples journeys siguen `NOT_COVERED`.
- **F4 / 25.2:** #79 sigue OPEN/stale, docs-only; queda como CI-FALLBACK independiente de BBB063, refresh + fresh CI, **sin merge**.
- **5.1:** `[x]`. **5.2:** `[x]`.

## RESULTADOS PROCESADOS — CYCLE 068

- `NIGHT-AAA-063`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- `NIGHT-BBB-062`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- `NIGHT-WOZ-066`: `NO_RESULT / NOT_PROCESSED / SUPERSEDED_BY_JOBS`; no merge accepted and integration remains #78.
- El comentario más reciente de Issue #41 antes de este ciclo era CYCLE 067 (`5473761463`); no existía handoff posterior de AAA/BBB/WOZ.
- GitHub verifica #75 exact-base/exact-head/mergeable y todavía no integrado; exact-head Required CI/checks aplicables observados verdes.
- #79 permanece stale contra live integration; no refresh claim.
- Open-PR scan no muestra candidate posterior a #79 ni artifact nuevo atribuible a los assignments sin resultado.
- No se promovió merge/PASS/integration nuevo.

## OWNERS — CYCLE 068

### AAA — `NIGHT-AAA-064` — F2 / 14.1
PRIMARY: live integration only; REUSE-FIRST media streaming/memory slice mínimo; giant-file memory safety + cleanup/cancel; focused tests + fresh exact-head CI; sin Player redesign ni merge.  
CI-FALLBACK: F2/14.2 READ-ONLY player-control gap map solo si PRIMARY queda code-complete esperando CI/review.

### BBB — `NIGHT-BBB-063` — F3 / 20.2
PRIMARY: usar harness #78 ya integrado y objetivo canónico **80/160**; obtener evidencia runtime materialmente aplicable a 160 para latency/error/queue/recovery, safety margin y durable waitlist. No inventar PASS ni generar costo/infra nueva.  
CI-FALLBACK: F4/25.2 SAME #79 narrow history-preserving refresh + fresh exact-head CI únicamente si PRIMARY queda `WAITING_EXTERNAL/WAITING_RUNTIME`; **NO MERGE** y no cerrar 25.2.

### WOZ — `NIGHT-WOZ-067` — F3 / 20.1 / SAME #75
PRIMARY: fresh race-check + exact-head merge transaction de #75; no code workaround; verificar merge SHA/parents si GitHub acepta. Claim máximo software observability integrated; external observability sigue UNVERIFIED.  
CI-FALLBACK: F3/18.2 READ-ONLY payment/provider scenario gap map solo si PRIMARY queda esperando merge acceptance/review/queue equivalente; sin writes/provider calls y sin claim global 18.2.

## Camino crítico global — recalculado desde cero CYCLE 068

1. **F3/20.1 / #75:** shortest material integration step: exact-base, exact-head, mergeable, still unmerged y CI aplicable verde. WOZ067 owns the only integration mutation.
2. **F3/20.2:** target fijo; BBB063 debe demostrar comportamiento runtime aplicable a 160 + safety margin + durable user waitlist.
3. **F2/14.1:** Web media streaming/memory safety es el slice interno independiente de mayor valor.
4. **F4/25.1:** Web/auth y journeys restantes `NOT_COVERED`; #74/#71/#72 siguen frozen por blockers conocidos.
5. **F3/18.2:** software reconciliation integrada; escenarios provider/payment siguen abiertos y solo admiten evidencia real.
6. **F4/25.2 / #79:** fallback preparation only; stale docs candidate must not displace runtime capacity work.
7. **#76 legal / #72 review / #74→#71 auth / #69/#70** frozen hasta cambio factual de blocker.
8. **F2/12.1 + F0/F1/F3/F4 external tails:** runtime/external/RO prerequisites. F5 no abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875caf...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`; #63 → `02a40564...`; #68 → `a9d35a3d...`; #73 → `a306e3b3...`; #78 → `63c9f8c948b1e05c30b12378ab1f31ceb04259c2`.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-064`; 063 está superseded.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-063`; target 80/160 es canónico, no claim.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-067`; SAME #75 exact-head transaction; fallback F3/18.2 solo bajo espera externa real.  
**JOBS:** siguiente ciclo procesa resultados reales; si #75 mergea, todo candidate restante requiere reconciliación al nuevo baseline antes de integración.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 068; GitHub vivo prevalece si cambia después.
