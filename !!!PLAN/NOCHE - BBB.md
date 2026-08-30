# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-032`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — windows/auth functional journey`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`
- `PREDECESSOR: NIGHT-BBB-031 DONE / INTEGRATED — #63 merged; do not rerun.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check.
2. REUSE-FIRST sobre `desktop_e2e`, shared auth tests y cualquier existing Windows harness. No copies #63 blindly and no second general matrix.
3. Scope exacto: demostrar el journey `windows/auth` en Windows mediante el camino mínimo F4/harness/workflow. Preferir wiring de evidencia sobre cambios de producto.
4. Debe alcanzar assertions funcionales reales de auth; un launcher/session green sin auth assertion no basta.
5. Si un assertion revela bug de producto, registrar `PRODUCT_FINDING` con evidencia y STOP; no reparar producto desde F4 sin reasignación.
6. Solo después de literal PASS puede cambiar únicamente `windows/auth` de `NOT_COVERED` a `AUTOMATED_PASS` con referencia exact-head verificable.
7. Cualquier promotion cambia head: exigir fresh Windows auth journey + F4 matrix contract + D6 + D7 + Required CI/Desktop Portability aplicables antes de merge.
8. Race-check final contra integration; merge solo si la combinación sigue compatible. Verificar merge SHA + integration HEAD.
9. No 25.2, signing/notarization, iPhone, YouTube/billing ni otras filas.
10. Reportar RESULTADO DEL TURNO + Issue #41 y STOP.

**Required evidence:** exact base/head, changed-file scope, auth assertions literal PASS, matrix contract, fresh applicable exact-head CI, merge evidence si aplica.  
**STOP:** product bug, runner/hardware/credential external, scope creep, baseline race no reconciliable, CI rojo no atribuible.

### CI-FALLBACK

`NONE`

Reason: otro matrix slice sería nuevo scope/ownership; no existe fallback independiente preautorizable sin ampliar 25.1.

## RESULTADO PROCESADO — NIGHT-BBB-031

- `STATUS: DONE / INTEGRATED`.
- SAME #63 exact head `7a6b7443fc4821a9b10798e2a3823a9d931bc2df`.
- Windows Import `33308327283` SUCCESS; F4 Matrix `33308327295` SUCCESS; D6 `33308327262` SUCCESS; D7 `33308327271` SUCCESS; Desktop Portability `33308327289` SUCCESS.
- Merge SHA / integration HEAD: `02a40564d85284a119281ff79995c9b9bcb5e833`.
- Scope integrated: exactly 3 F4 files; `windows/import` only.
- Issue #41 handoff `5468611912`.

## HISTORIAL COMPACTO

- `NIGHT-BBB-032`: ASSIGNED — windows/auth journey.
- `NIGHT-BBB-031`: DONE/INTEGRATED — #63 merge `02a40564...`.
- `NIGHT-BBB-030`: matrix corrective, later green.
- `NIGHT-BBB-026`: Windows Import literal PASS before promotion.
- `NIGHT-BBB-012`: #60 matrix integrated.
