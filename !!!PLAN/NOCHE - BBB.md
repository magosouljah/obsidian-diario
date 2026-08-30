# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-035`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — windows/review independent journey`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`
- `PREDECESSOR: NIGHT-BBB-034 PENDING / PRODUCT_FINDING — processed by JOBS; #71 stays intact as auth regression proof.`
- `CI-FALLBACK: NONE`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check de cualquier existing Windows Review candidate/evidence.
2. No tocar PR #71, `tests/e2e/auth-flow.e2e.mjs`, auth productivo ni matrix row `windows/auth`.
3. REUSE-FIRST del Desktop/embedded WebDriver harness ya probado por #63/#71.
4. Crear/reusar solo un slice F4 independiente para `windows/review`; preferir workflow/spec nuevos y evitar cambios a shared runner salvo necesidad factual demostrada.
5. La prueba debe alcanzar Review UI/flow real bajo fronteras externas aisladas y hacer assertions literales del journey; green genérico no basta.
6. Si failure es harness, corrective mínimo F4. Si assertion literal demuestra bug de producto: `PRODUCT_FINDING` + STOP para JOBS.
7. No promover `windows/review` hasta PASS literal. Después de promotion, fresh exact-head Windows Review + F4 Matrix + D6 + D7 + Required CI/Desktop Portability antes de race-check/merge.
8. No iniciar otra matrix row, 25.2, signing/notarization ni producto fuera de Review.
9. Escribe RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**STOP:** product finding; external credential/hardware blocker; scope escape; baseline race; CI rojo no atribuible.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback.

## RESULTADO PROCESADO — NIGHT-BBB-034

`STATUS: PENDING / PRODUCT_FINDING`.

- SAME #71 OPEN/Ready/mergeable @ `29656aa0...`, base `02a40564...`, sin cambios.
- Windows Auth run `33313675968` llegó a WebDriver/session real y ejecutó auth spec.
- Assertion literal: Desktop login no persistió `beatgaler:account-session:v1`.
- JOBS acepta el finding como product-auth blocker y reasigna corrective a AAA036.
- `windows/auth` continúa `NOT_COVERED`; #71 queda intacta para revalidation posterior.
- Handoff Issue #41 `5469178213`.

## HISTORIAL COMPACTO

- `NIGHT-BBB-035`: ASSIGNED — independent windows/review journey.
- `NIGHT-BBB-034`: PENDING / PRODUCT_FINDING — Desktop session-token persistence.
- `NIGHT-BBB-031`: DONE/INTEGRATED — #63 merge `02a40564...`.
- `NIGHT-BBB-026`: Windows Import literal PASS before promotion.
