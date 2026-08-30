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

## Estado vivo — NIGHT-JOBS-035

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.
- **Último merge material:** PR #63 exact tested head `7a6b7443fc4821a9b10798e2a3823a9d931bc2df` → merge `02a40564d85284a119281ff79995c9b9bcb5e833`; `windows/import` integrado como `AUTOMATED_PASS`; 25.1 completo sigue abierto.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; harness real-browser localizado, pero cold/warm real cuantificado sigue abierto por runtime ejecutable ausente en el turno AAA032.
- **F2 / 13.1 Web:** `[ 🟡 ]`; PR #69 OPEN @ `b2ab75ae...`, Save All coordinator/CAS probado, product wiring App/Review pendiente y candidate stale tras #63. `NIGHT-AAA-033` sigue owner activo; no hay resultado final nuevo observable.
- **F2 / 13.1 server:** PR #70 OPEN @ `5a99ebf2...`; corrective conocido, safe-write blocker y baseline stale. Frozen.
- **F3 / 16.1 + 16.2:** software done con tails externos.
- **F3 / 17.1 + 17.2:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.1:** PR #68 OPEN @ `2a988ec2...`; exact-head green histórico pero stale frente a `02a40564...`, además de blocker previo de merge execution. Frozen.
- **F3 / 20.1:** WOZ033 terminó `DONE / AUDIT_ONLY` y produjo gap map literal; 20.1 sigue abierto. `NIGHT-WOZ-034` toma únicamente el primer software slice: taxonomía canónica de eventos/métricas/alerts. External dashboards/delivery/on-call/status/retention/tracing backend siguen sin probarse.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / 25.1:** `[ 🟡 ]`; `windows/import` integrado. `NIGHT-BBB-032` sigue owner de `windows/auth`; no hay resultado final nuevo observable.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 035

### AAA — `NIGHT-AAA-033` — F2 / 13.1 SAME #69
PRIMARY: refresh/reconcile SAME #69 contra `02a40564...`; REUSE-FIRST del coordinator existente. Cerrar únicamente el product wiring Save All App/Review→`saveAllWebItems` si existe superficie de patch/worktree segura, preservando saved/conflict/failed y retry semantics. No reemplazar PR ni tocar #70/13.2+/F3/F4.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-032` — F4 / 25.1 windows/auth
PRIMARY: REUSE-FIRST sobre `desktop_e2e` + shared auth coverage; demostrar literal Windows auth assertions; solo después promover esa única fila a `AUTOMATED_PASS`; fresh exact-head matrix + D6 + D7 + Required CI/Desktop Portability antes de merge. Product bug => `PRODUCT_FINDING` + STOP.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-034` — F3 / 20.1 software observability contract A
PRIMARY: sobre `02a40564...`, REUSE-FIRST del gap map WOZ033 y superficies integradas. Crear o demostrar una fuente canónica pequeña para taxonomía eventos/métricas/alerts de auth/API/DB/billing/provider/pool/queue/backup/release, reutilizando `backup.failure`/naming existente. Una pieza aditiva pequeña solo si gap literal y safe-write; focused tests + fresh applicable CI si hay código. No provider dashboards/delivery/tracing/status/on-call/retention, no #68/#70/F2/F4. No cerrar 20.1 completo.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 035

1. **F2 / 13.1 / #69:** product wiring sigue siendo el mayor gap interno Web cercano; refresh obligatorio tras #63.
2. **F4 / 25.1 remainder:** `windows/auth` es el siguiente slice F4 automatable y ya tiene owner.
3. **F3 / 20.1:** gap map ya existe; reducir ahora un solo slice software literal sin falsear la mitad externa.
4. **F2 / 12.1:** requiere runtime navegador real; blocker factual.
5. **#70 / #68:** stale + blockers previos; frozen hasta tooling/merge mechanism seguro + revalidación.
6. **F0/F1/F3 external tails + D22/D23:** externos/RO.
7. Después: F2 13.2–15, F3 18.2–20 y F4 remainder 25.1/25.2. F5 no se abre.

## F3 / 20.1 — gap map procesado

- logs: PARTIAL; structured service-wide production logging + retention no demostrados;
- metrics: GAP;
- tracing: GAP;
- error reporting: PARTIAL/GAP;
- retention: PARTIAL/EXTERNAL;
- alerts auth/API/DB/billing/provider/pool/queue/release: GAP como matriz completa; backup alert = PARTIAL SOFTWARE CONTRACT;
- on-call: GAP/PENDING_EXTERNAL;
- runbook: PARTIAL;
- public status: GAP/PENDING_EXTERNAL;
- kill switches: GAP.

Evidencia reutilizada: `cloud-server/runtime-operability.js`, `cloud-server/server.js`, `cloud-server/deployment-promotion-contract.mjs`, `cloud-server/d10-backup-readiness-contract.mjs`. Handoff WOZ033: Issue #41 `5468767913`.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`; #63 → `02a40564d85284a119281ff79995c9b9bcb5e833`.

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

**AAA:** terminar una sola vez `NIGHT-AAA-033`; no duplicar mientras siga ASSIGNED.  
**BBB:** terminar una sola vez `NIGHT-BBB-032`; no duplicar mientras siga ASSIGNED.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-034`.  
**JOBS:** procesar únicamente resultados nuevos; cualquier candidate basado en `3ad8f55a...` requiere refresh/revalidación material antes de merge.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 035; GitHub vivo prevalece si cambia después.
