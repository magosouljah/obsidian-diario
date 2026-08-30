# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-033`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — SAME PR #71 Windows auth failure attribution + corrective mínimo`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 02a40564d85284a119281ff79995c9b9bcb5e833`
- `REUSE_PR: #71 / bbb/night-25.1-windows-auth @ 29656aa0a040043934380c97e0145608c69e8daf`
- `PREDECESSOR: NIGHT-BBB-032 PENDING / WAITING_CI — processed by JOBS; final CI recheck now resolved to FAILURE.`
- `CI-FALLBACK: NONE`

### PRIMARY

1. Preflight live integration + SAME #71 exact head. No replacement PR/branch.
2. Process the completed authoritative run `F4 - 25.1 Windows Auth Journey` `33313675968` on exact head `29656aa0...`: conclusion `FAILURE`. Setup, exact checkout, pinned Node/Rust, locked npm install and embedded-driver preparation all passed; failure occurred in `Run isolated Windows auth assertions`.
3. Attribution-first: inspect the failing assertion/log evidence and classify it as `F4_HARNESS_FINDING` or `PRODUCT_FINDING`. Do not infer product failure from a generic red job.
4. If and only if the failure is in F4 harness/test plumbing, apply the smallest corrective inside #71 F4 test/harness scope. Do not touch product auth logic.
5. If a literal assertion demonstrates a real Desktop auth product defect, record `PRODUCT_FINDING` with exact assertion/evidence and STOP for JOBS reassignment; do not repair product from F4 ownership.
6. `windows/auth` remains `NOT_COVERED`; do not promote the matrix row until literal Windows auth assertions PASS.
7. After a literal PASS, promote only `windows/auth` to `AUTOMATED_PASS`; that creates a new head, so require fresh exact-head Windows Auth + F4 Matrix + D6 + D7 + Desktop Portability/Required CI before race-check/merge.
8. Do not begin other 25.1 rows, 25.2, signing/notarization or external hardware work.
9. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Evidence required:** exact failure/assertion/log, exact head, changed-file scope, literal auth PASS before promotion, then fresh post-promotion applicable gates and race-check.  
**STOP:** product finding; scope escapes F4 harness; external credential/hardware blocker; baseline race; non-attributable CI failure.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback; another matrix row/25.2 would be new scope and may duplicate future ownership.

## RESULTADO PROCESADO — NIGHT-BBB-032

- `STATUS: PENDING / WAITING_CI` at worker close.
- Candidate: #71 @ `29656aa0a040043934380c97e0145608c69e8daf`, base `02a40564...`, exactly 3 F4 harness/workflow files.
- JOBS final CI recheck:
  - F4 Windows Auth `33313675968` — **FAILURE**;
  - failure step: `Run isolated Windows auth assertions`;
  - setup/checkout/toolchains/npm/embedded preparation — SUCCESS;
  - Required CI `33313676131` — SUCCESS;
  - D6 `33313675921` — SUCCESS;
  - D7 `33313675911` — SUCCESS;
  - Windows Import regression `33313676127` — SUCCESS;
  - Upgrade 21.2 — SKIPPED/no aplicable.
- No matrix promotion, no merge. `windows/auth` remains `NOT_COVERED`.
- Issue #41 handoff from worker: `5468908666`.

## HISTORIAL COMPACTO

- `NIGHT-BBB-033`: ASSIGNED — SAME #71 failure attribution/corrective.
- `NIGHT-BBB-032`: PENDING/WAITING_CI; JOBS recheck resolved Windows Auth to FAILURE.
- `NIGHT-BBB-031`: DONE/INTEGRATED — #63 merge `02a40564...`.
- `NIGHT-BBB-030`: matrix corrective, later green.
- `NIGHT-BBB-026`: Windows Import literal PASS before promotion.
- `NIGHT-BBB-012`: #60 matrix integrated.
