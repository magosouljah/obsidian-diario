# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## DECISIÓN RO — ROMPECABEZAS CON OWNER FIJO

Desde 2026-08-28 el trabajo se desbloquea por dependencia real, incluso cross-phase, pero cada agente conserva ownership estable de su pieza hasta cerrarla o hasta una reasignación explícita de JOBS/RO.

Reglas:
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- GitHub real prevalece sobre snapshots viejos del plan.
- Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head son obligatorios.
- Un gate controla cierre/promoción/release; no bloquea trabajo independiente de otra fase.
- JOBS dirige/sincroniza; no toca código BeatGaler ni infraestructura.
- RO conserva alcance de producto, riesgo aceptado y go/no-go público.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo — NIGHT-JOBS-033

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`; GitHub vivo sigue sin merge posterior a #67.
- **F0:** trabajo técnico interno cerrado; 1.2 y 2.2 conservan tails externos/administrativos.
- **F1:** D6/D7/D8/D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia real off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1:** `[x]` #47. **11.2:** `[x]` #54. **12.2:** `[x]` #50.
- **F2 / 12.1:** `[ 🟡 ] RESIDUAL / RUNTIME EVIDENCE`; queda comparación cold/warm Web real cuantificada/reproducible. `NIGHT-AAA-032` sigue ASSIGNED y no tiene resultado observable todavía; no se supersede.
- **F2 / 13.1 Web:** `[ 🟡 ] HOLDING / WRITE-SURFACE BLOCKER`. PR #69 `aaa/night-13.1-web-save-all @ b2ab75ae...` sigue OPEN/Ready/mergeable; helper/unit + CI previo green, pero product wiring App/Review sigue faltando. #69 permanece frozen.
- **F2 / 13.1 server:** `[ 🟡 ] BLOCKED / SAFE_WRITE_TOOLING_LIMIT`. PR #70 `woz/night-13.1-orphan-lifecycle @ 5a99ebf2...` sigue OPEN/Ready/mergeable. WOZ031 identificó el corrective exacto pero un writer full-file no permitió patch quirúrgico seguro; un intento truncado fue revertido y la rama quedó restaurada exactamente a `5a99ebf2...`. Fresh live recheck: Required CI y PostgreSQL live/recovery siguen FAILURE sobre ese mismo head; no PASS ni merge.
- **F3 / 16.1:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`.
- **F3 / 16.2:** `[ 🟡 ] SOFTWARE DONE + EXTERNAL TAIL`.
- **F3 / 17.1:** `[x] SOFTWARE DONE / INTEGRATED` — #65.
- **F3 / 17.2:** `[x] SOFTWARE DONE / INTEGRATED` — #67 merge `3ad8f55a...`.
- **F3 / 18.1:** `[ 🟡 ] EXACT-HEAD GREEN / BLOCKED_EXTERNAL_MERGE_EXECUTION`. PR #68 sigue OPEN/Ready/mergeable @ `2a988ec2...`; no existe merge SHA aceptado. Candidate frozen.
- **F3 / 20.1:** `NIGHT-WOZ-032` abre únicamente una auditoría REUSE-FIRST software-only para localizar evidencia/artefactos existentes de observabilidad/alerts/runbook/kill-switch y producir un gap map accionable; solo puede crear un artifact pequeño y aislado si el gap literal lo exige y la superficie de escritura es segura. No toca #68/#70 ni infraestructura.
- **F4 / 21.1+21.2:** `[x]` #51. **24.1:** `[x]` #55. **24.2:** `[x]` #57.
- **F4 / 25.1:** `[ 🟡 ] WINDOWS IMPORT SLICE EXACT-HEAD GREEN / MERGE PENDING`. SAME #63 @ `7a6b7443...` sigue OPEN/Ready/mergeable sobre base `3ad8f55a...`; live recheck mantiene 14 checks sin failure y Required CI SUCCESS. `NIGHT-BBB-031` sigue ASSIGNED para final race-check + merge SAME #63; no se supersede. 25.1 completo permanece abierto por otros gaps.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **2.2:** `[ 🟡 ]` tail externo. **1.2:** `[ 🟡 ]` release externo; Apple Developer `PENDING — DEFERRED`.

## OWNERS — CYCLE 033

### AAA — `NIGHT-AAA-032` — F2 / 12.1 runtime — ACTIVE / UNCHANGED
PRIMARY: REUSE-FIRST sobre instrumentación #58/#66; producir cold/warm Web real reproducible mediante harness aislado pequeño, sin reescribir App.tsx ni tocar #69. Si demuestra el requisito literal, recomendar cierre solo de 12.1.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-031` — F4 / 25.1 SAME #63 — ACTIVE / UNCHANGED
PRIMARY: no más corrective. Verificar exact head `7a6b7443...`, changed-file scope, fresh green set y race-check contra integration `3ad8f55a...`; integrar SAME #63 solo si todo permanece compatible, y verificar merge SHA + integration HEAD.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-032` — F3 / 20.1 observability gap map
PRIMARY: salir del blocker de escritura de #70 sin duplicarlo. Hacer auditoría REUSE-FIRST de observabilidad software existente para auth/API/DB/billing/provider/pool/queue/backup/release + runbook/kill-switch. Entregar mapa requisito→evidencia→gap. Solo si aparece un gap literal pequeño, independiente y safely writable, implementar una única pieza software-only en rama/PR nuevo con tests/CI aplicables. No provider resources, costos, secrets, #68, #70, F2 ni Desktop packaging.  
CI-FALLBACK: `NONE`.

### JOBS
Mantiene prioridades, `!!!PLAN`, handoffs y gates. No modifica código BeatGaler ni infraestructura.

## Camino crítico global — recalculado CYCLE 033

1. **F4 / 25.1 / #63:** exact-head sigue green y mergeable; final race-check/merge continúa siendo la transacción más corta de avance real.
2. **F2 / 12.1:** AAA032 sigue activo para cerrar cold/warm runtime real; no se emite ID nuevo mientras no haya resultado.
3. **F2 / 13.1 server / #70:** corrective está atribuido pero bloqueado por tooling de patch seguro. Candidate queda frozen en `5a99ebf2...`; no repetir escritura destructiva.
4. **F3 / 20.1:** WOZ032 busca REUSE-FIRST/gaps software independientes mientras #70 está tooling-blocked y #68 merge-blocked.
5. **F2 / 13.1 Web / #69:** frozen hasta disponer de patch/worktree seguro para App.tsx; no duplicar PR.
6. **F3 / 18.1 / #68:** exact-head green pero merge execution blocked; conservar frozen porque reintentos ceremoniales no añaden evidencia.
7. **F0/F1/F3 external tails + D22/D23:** externos/RO; no repetir drills aceptados.
8. Después: F2 13.2–15, F3 18.2–20 y F4 25.1 remainder/25.2. F5 no se abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`.

Candidates vivos:
- #63 @ `7a6b7443...` — fresh exact-head green; final merge transaction pending.
- #70 @ `5a99ebf2...` — focused PASS histórico; fresh Required CI/PostgreSQL live FAILURE; corrective bloqueado por safe-write tooling.
- #69 @ `b2ab75ae...` — product wiring pending, frozen by write-surface blocker.
- #68 @ `2a988ec2...` — exact-head green; merge execution blocked/frozen.

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

**AAA:** ejecutar una sola vez la ya vigente `NIGHT-AAA-032`; no superseder hasta resultado.  
**BBB:** ejecutar una sola vez la ya vigente `NIGHT-BBB-031`; no superseder hasta resultado.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-032`.  
**JOBS:** siguiente ciclo procesa resultados reales; si BBB/#63 mueve integration, cualquier candidate restante debe revalidar combinación material antes de merge.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 033; GitHub vivo prevalece si cambia después.
