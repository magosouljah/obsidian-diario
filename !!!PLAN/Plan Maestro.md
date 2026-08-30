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

## Estado vivo — NIGHT-JOBS-039

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.
- **Último merge material:** PR #68 → `a9d35a3d...`; F3/18.1 quedó integrado.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real cuantificado sigue bloqueado por runtime navegador ejecutable.
- **F2 / 13.1 Web:** PR #69 OPEN @ `b2ab75ae...`; coordinator Save All/CAS probado, product wiring + refresh siguen pendientes y candidate está stale frente al nuevo baseline. HOLDING.
- **F2 / 13.1 server:** PR #70 OPEN @ `5a99ebf2...`; safe-write blocker + baseline stale. Frozen.
- **F3 / 16.1 + 16.2:** software done con tails externos.
- **F3 / 17.1 + 17.2:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.1:** `[x] SOFTWARE DONE / INTEGRATED`; PR #68 head `68adaad4...` merge `a9d35a3d...`; WOZ037 verificó race-check, CI, merge SHA y parents.
- **F3 / 18.2:** `[ 🟡 ] IN PROGRESS`; WOZ038 toma reconciliation/exception-queue software-only REUSE-FIRST.
- **F3 / 20.1:** gap map audit-only válido; holding.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / 25.1:** `[ 🟡 ]`; `windows/import` integrado. PR #71 Windows Auth demuestra product finding: Desktop login no persistió `beatgaler:account-session:v1`; `windows/auth` sigue `NOT_COVERED`.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 039

### AAA — `NIGHT-AAA-037` — product-auth Desktop finding
PRIMARY: misma misión factual de AAA036, reemitida por baseline movement: root cause + corrective mínimo de token/session persistence desde `a9d35a3d...`; no tocar #71; focused evidence + fresh applicable exact-head CI.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-036` — F4 / 25.1 `windows/review`
PRIMARY: fila independiente Review reemitida contra `a9d35a3d...`; reuse Desktop/embedded harness; no tocar auth/#71; literal Review PASS antes de matrix promotion; PRODUCT_FINDING + STOP si aparece bug producto.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-038` — F3 / 18.2
PRIMARY: REUSE-FIRST de reconciliation Stripe↔BeatGaler + exception queue. Audit-only si ya existe; si hay gap interno, slice software-only mínimo durable/idempotente/fail-closed. Nada de provider/credenciales ni decisiones RO inventadas.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 039

1. **F4 / product-auth finding:** corregir persistencia de sesión Desktop para desbloquear `windows/auth` y reutilizar #71.
2. **F4 / 25.1 windows/review:** fila independiente que BBB puede avanzar sin tocar auth.
3. **F3 / 18.2:** cerrar todo el software verificable de reconciliation/exception handling; separar explícitamente tails provider/business.
4. **F2 / 13.1 / #69:** coordinator probado; wiring + refresh holding hasta liberar AAA.
5. **F2 / 12.1:** requiere runtime navegador real; blocker factual.
6. **F2 #70:** stale + safe-write blocker; frozen.
7. **F3 / 20.1:** gap map listo; holding.
8. **F0/F1/F3 external tails + D22/D23:** externos/RO.
9. Después: F2 13.2–15, F3 19–20 y F4 remainder 25.1/25.2. F5 no se abre.

## Secuencia de integración verificada

#47 → `489d81b...`; #54 → `3560dc844...`; #50 → `39e894c...`; #51 → `5b05ca845...`; #55 → `672e133bc...`; #56 → `f0d65aa...`; #57 → `f73c9ee...`; #59 → `be9e58c...`; #58 → `58a6bf614...`; #60 → `7de7b57a...`; #61 → `55e0d875...`; #64 → `b114111caf...`; #65 → `ed6aab7e...`; #66 → `712b49b...`; #67 → `3ad8f55a...`; #63 → `02a40564...`; #68 → `a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-037`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-036`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-038`.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga race revalidation/fresh applicable exact-head en candidatos restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 039; GitHub vivo prevalece si cambia después.
