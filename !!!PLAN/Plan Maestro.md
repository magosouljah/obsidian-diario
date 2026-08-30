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

## Estado vivo — NIGHT-JOBS-036

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`.
- **Último merge material:** PR #63 exact tested head `7a6b7443fc4821a9b10798e2a3823a9d931bc2df` → merge `02a40564d85284a119281ff79995c9b9bcb5e833`; `windows/import` integrado como `AUTOMATED_PASS`; 25.1 completo sigue abierto.
- **F0:** técnico interno cerrado; 1.2 y 2.2 siguen tails externos/administrativos.
- **F1:** D6–D9 PASS. D10.1 `PENDING_EXTERNAL_PROOF` por copia off-provider/off-account + read/checksum. D10.2 requiere decisión RO.
- **F2 / 11.1, 11.2, 12.2:** `[x]`.
- **F2 / 12.1:** `[ 🟡 ] RUNTIME EVIDENCE`; cold/warm real cuantificado sigue bloqueado por runtime navegador ejecutable.
- **F2 / 13.1 Web:** `[ 🟡 ]`; SAME PR #69 OPEN @ `b2ab75ae...`, Save All coordinator/CAS probado, product wiring App/Review pendiente y candidate stale respecto a `02a40564...`. `NIGHT-AAA-034` owner activo.
- **F2 / 13.1 server:** PR #70 OPEN @ `5a99ebf2...`; corrective conocido, safe-write blocker y baseline stale. Frozen.
- **F3 / 16.1 + 16.2:** software done con tails externos.
- **F3 / 17.1 + 17.2:** `[x] SOFTWARE DONE / INTEGRATED`.
- **F3 / 18.1:** SAME PR #68 OPEN @ `2a988ec2...`; candidate históricamente verde sobre `3ad8f55a...` pero stale frente a `02a40564...`. `NIGHT-WOZ-035` reactiva este candidate con refresh + fresh exact-head CI; no usar evidencia vieja para merge.
- **F3 / 20.1:** gap map audit-only de WOZ033 sigue válido, pero el software slice 20.1 queda en holding este ciclo porque 18.1 es anterior y más crítico.
- **F4 / 21.1+21.2, 24.1, 24.2:** `[x]`.
- **F4 / 25.1:** `[ 🟡 ]`; `windows/import` integrado. SAME PR #71 OPEN @ `29656aa0...` para `windows/auth`. Final exact-head recheck: Windows Auth workflow `33313675968` = **FAILURE** en `Run isolated Windows auth assertions`; setup/checkout/toolchains/npm/embedded preparation pasaron. Required CI/D6/D7/Desktop Portability e Import regression quedaron verdes. `windows/auth` sigue `NOT_COVERED`; `NIGHT-BBB-033` hace attribution-first/corrective mínimo.
- **5.1:** `[x]`. **5.2:** `[x]`.

## OWNERS — CYCLE 036

### AAA — `NIGHT-AAA-034` — F2 / 13.1 SAME #69
PRIMARY: refresh/reconcile SAME #69 contra `02a40564...`; REUSE-FIRST del coordinator existente; cerrar únicamente product wiring App/Review→`saveAllWebItems` si existe superficie segura, preservando saved/conflict/failed + retry semantics. No reemplazar PR ni tocar #70/13.2+/F3/F4.  
CI-FALLBACK: `NONE`.

### BBB — `NIGHT-BBB-033` — F4 / 25.1 SAME #71
PRIMARY: procesar failure exacto `33313675968`; atribuir primero harness vs producto. Si harness, corrective mínimo F4; si assertion demuestra bug de producto, `PRODUCT_FINDING` + STOP. No promover `windows/auth` hasta PASS literal; después fresh post-promotion matrix/D6/D7/Required CI antes de merge.  
CI-FALLBACK: `NONE`.

### WOZ — `NIGHT-WOZ-035` — F3 / 18.1 SAME #68
PRIMARY: refresh/reconcile SAME #68 desde baseline viejo `3ad8f55a...` al vivo `02a40564...`, preservar solo delta 18.1, ejecutar focused tests + fresh applicable exact-head CI y merge únicamente con race-check verde. Si reaparece el blocker de merge execution, registrar error exacto y STOP; no duplicar PR/bypass.  
CI-FALLBACK: `NONE`.

## Camino crítico global — recalculado CYCLE 036

1. **F3 / 18.1 / #68:** es una pieza anterior a 20.1, ya implementada y reutilizable; refresh/fresh CI puede cerrar un gate grande sin arquitectura nueva.
2. **F2 / 13.1 / #69:** coordinator probado; falta product wiring + refresh.
3. **F4 / 25.1 / #71:** Windows Auth llegó a assertions y falló; attribution/corrective es el camino mínimo al siguiente row PASS.
4. **F2 / 12.1:** requiere runtime navegador real; blocker factual.
5. **F2 #70:** stale + safe-write blocker; frozen.
6. **F3 / 20.1:** gap map listo; vuelve después de 18.1 salvo cambio factual.
7. **F0/F1/F3 external tails + D22/D23:** externos/RO.
8. Después: F2 13.2–15, F3 18.2–20 y F4 remainder 25.1/25.2. F5 no se abre.

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

**AAA:** ejecutar una sola vez `NIGHT-AAA-034`.  
**BBB:** ejecutar una sola vez `NIGHT-BBB-033`.  
**WOZ:** ejecutar una sola vez `NIGHT-WOZ-035`.  
**JOBS:** siguiente ciclo procesa resultados reales; cualquier merge que mueva baseline obliga race revalidation/fresh applicable exact-head en candidatos restantes.  
**PLAN_HEALTH:** sincronizado al GitHub observado en CYCLE 036; GitHub vivo prevalece si cambia después.
