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

## Estado vivo — NIGHT-JOBS-038

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.
- **Último merge material:** PR #63 → `02a40564...`; `windows/import` integrado como `AUTOMATED_PASS`; 25.1 completo sigue abierto.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real cuantificado sigue bloqueado por runtime navegador ejecutable.
- **F2 / 13.1 Web:** SAME PR #69 OPEN @ `b2ab75ae...`, coordinator Save All/CAS probado pero product wiring y refresh siguen pendientes. Queda HOLDING este ciclo para priorizar un P1 product finding de auth.
- **F2 / 13.1 server:** PR #70 OPEN @ `5a99ebf2...`; safe-write blocker + baseline stale. Frozen.
- **F3 / 16.1 + 16.2:** software done con tails externos.
- **F3 / 17.1 + 17.2:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.1:** PR #68 OPEN/Ready/mergeable @ `68adaad4...`, base exacta `02a40564...`, 4 files/+178/-0; fresh exact-head workflows siguen 5 SUCCESS + 1 SKIPPED y cero failure/pending. `NIGHT-WOZ-037` hace únicamente race-check + merge exact-head.
- **F3 / 20.1:** gap map audit-only válido; holding hasta procesar 18.1.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / 25.1:** `[ 🟡 ]`; `windows/import` integrado. PR #71 Windows Auth llegó a WebDriver/session real y falló en assertion literal: Desktop login no persistió `beatgaler:account-session:v1` pese al contrato de `AccountGate.storeSession()`. BBB declaró `PRODUCT_FINDING`; `windows/auth` sigue `NOT_COVERED` y #71 queda intacta como prueba de regresión.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 038

### AAA — `NIGHT-AAA-036` — product-auth Desktop finding
PRIMARY: ownership explícito del finding de #71. Reproducir/diagnosticar por qué el login Desktop no conserva el token de sesión en `AccountGate`; corrective mínimo en frontend/platform auth productivo solo si causa raíz queda demostrada; focused tests + fresh applicable exact-head CI. No tocar PR #71 ni F4 matrix.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-035` — F4 / 25.1 `windows/review`
PRIMARY: dejar #71 intacta y abrir/reutilizar únicamente un slice independiente para Windows Review. Reusar harness Desktop/embedded existente sin modificar auth productivo ni archivos de #71; exigir assertion literal de Review journey antes de cualquier promoción de matrix. Si aparece bug de producto, `PRODUCT_FINDING` + STOP.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-037` — F3 / 18.1 SAME #68
PRIMARY: revalidar integration `02a40564...`, exact head `68adaad4...`, Ready/mergeable y exact-head green evidence; si race-check limpio, merge #68 por flujo autorizado y verificar merge SHA + integration HEAD. No rerun ceremonial ni 18.2/20.1 automático.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 038

1. **F3 / 18.1 / #68:** candidate exact-head verde; solo falta integración autorizada.
2. **F4 / product-auth finding:** corregir persistencia de sesión Desktop para desbloquear `windows/auth` y permitir reutilizar #71.
3. **F4 / 25.1 windows/review:** fila independiente que BBB puede avanzar sin tocar auth.
4. **F2 / 13.1 / #69:** coordinator probado; product wiring + refresh quedan holding hasta liberar AAA.
5. **F2 / 12.1:** requiere runtime navegador real; blocker factual.
6. **F2 #70:** stale + safe-write blocker; frozen.
7. **F3 / 20.1:** gap map listo; vuelve después de 18.1.
8. **F0/F1/F3 external tails + D22/D23:** externos/RO.
9. Después: F2 13.2–15, F3 18.2–20 y F4 remainder 25.1/25.2. F5 no se abre.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-036`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-035`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-037`.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga race revalidation/fresh applicable exact-head en candidatos restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 038; GitHub vivo prevalece si cambia después.
