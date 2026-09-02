# Fase 0 — Contención e integración

> Leer primero `Plan Maestro.md`. GitHub/runtime vivo prevalece. No reabrir trabajo técnico cerrado sin invalidación factual.

**Estado CYCLE156:** `[ 🟡 ]` residual/administrativo + security/release tails. 5.1 y 5.2 `[x]`; 0.8 review administrativo `[x]` bajo excepción RO-approved AI-assisted; 0.20 OAuth secret rotation `[x]`.  
**Baseline vivo:** `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.  
**Release:** 🔴 `NO-GO`.

## Tablero

| Tarea | Estado | Gate resumido |
|---|---|---|
| 0.1 Congelar evidencia | [x] | baseline + NO-GO |
| 0.2 Checkpoint interno | [x] | no release público |
| 0.8 Legal launch review | [x] | AI-assisted review complete; substantive legal backlog remains |
| 0.20 OAuth secret rotation | [x] | replacement verified; old removed; no values recorded |
| 1.1 Negocio | [x] | v1 comercial |
| 1.2 Dependencias externas | [ 🟡 ] | productive signing/security/testers/legal tails |
| 2.1 Contención inmediata | [x] | auth/ownership/límites |
| 2.2 Historial Git | [ 🟡 ] | GitHub Support + fresh inaccessibility verification |
| 3.1 Integración | [x] | `integration-v0.8.0-alpha.1` |
| 3.2 Contrato plataforma | [x] | Web sin Tauri |
| 4.1 Required CI | [x] | policy vigente |
| 4.2 Supply chain | [x] | scans/SBOM/checksums/provenance base |
| 5.1 Trust boundary / Direct | [x] | temporary auth + media directa |
| 5.2 Datos/recovery/secrets | [x] | PostgreSQL + RPO/RTO + rotation + observability |

## 1.2 — release dependencies

Software integrado relevante incluye #86 provenance, #87 public ops, #88 Authenticode/RFC3161 seam, #90 OAuth readiness, #91/#92/#94/#95/#96/#98 Web corrective lineage y #99 Web runtime source binding, merge/current integration `c2766fb...`. Nada sustituye productive signing/notarization/tester/legal/security release evidence.

### F0/0.9 — `[ 🟡 ]` AI-assisted security slice / DNS rebinding

PR #89 sigue OPEN @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`, stale frente a `c2766fb...`.

**Gate vivo:** run `33454881387` = `completed/failure` sobre exact head `daf87da6...`; no hay evidencia nueva que permita rebajarlo.

**CYCLE156:** `NIGHT-AAA-152` es owner exclusivo de #89: REUSE/history-preserving refresh, mínimo gate-precondition correction, exact-head revalidation y conditional expected-head merge solo si exact/green/race-free. No duplicate PR. WOZ155 no toca #89.

### Tails reales restantes

- #89 P1 refresh/revalidation/integration;
- production Authenticode/RFC3161 evidence;
- legal P0/P1 implementation backlog;
- independent security review donde sea gate;
- 12–20 testers + hardware/plataformas/DAWs/fechas;
- F0/2.2 GitHub Support cleanup + fresh inaccessibility verification.

**Regla de salida:** F0 no es `[x]` global mientras 1.2/2.2 sigan abiertos. F5 y release siguen cerrados.
