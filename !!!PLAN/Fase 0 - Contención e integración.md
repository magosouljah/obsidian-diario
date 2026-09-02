# Fase 0 — Contención e integración

> Leer primero `Plan Maestro.md`. GitHub/runtime vivo prevalece. No reabrir trabajo técnico cerrado sin invalidación factual.

**Estado CYCLE153:** `[ 🟡 ]` residual/administrativo + security/release tails. 5.1 y 5.2 están `[x]`. 0.8 legal launch review está `[x]` bajo excepción RO-approved AI-assisted; esto cierra la actividad de review, no compliance ni P0/P1 legales. 0.20 OAuth secret rotation está `[x]`.  
**Baseline vivo:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.  
**Release:** 🔴 `NO-GO`.

## Tablero

| Tarea | Estado | Gate resumido |
|---|---|---|
| 0.1 Congelar evidencia | [x] | baseline + NO-GO registrados |
| 0.2 Checkpoint interno | [x] | no equivale a release público |
| 0.8 Legal launch review | [x] | AI-assisted review completed; independent counsel deferred by explicit RO decision |
| 0.20 OAuth secret rotation | [x] | replacement deployed/verified + previous secret removed; no secret values recorded |
| 1.1 Negocio | [x] | v1 comercial; mercados/distribución decididos |
| 1.2 Dependencias externas | [ 🟡 ] | productive signing/security/testers/legal tails |
| 2.1 Contención inmediata | [x] | auth/ownership/límites |
| 2.2 Historial Git | [ 🟡 ] | GitHub Support + fresh inaccessibility verification |
| 3.1 Integración | [x] | `integration-v0.8.0-alpha.1` |
| 3.2 Contrato plataforma | [x] | Web sin Tauri |
| 4.1 Required CI | [x] | required CI policy |
| 4.2 Supply chain | [x] | scans/SBOM/checksums/provenance base |
| 5.1 Trust boundary / Direct | [x] | temporary auth + media directa |
| 5.2 Datos/recovery/secrets | [x] | PostgreSQL + RPO/RTO + rotation + observability |

## 0.8 — `[x]` review administrativo, no compliance

Evidence canónica: `Legal launch review - AI-assisted 2026-08-31.md`. No ocurrió attorney review. Los **12 P0 + 14 P1**, P2/P3 y `UNVERIFIED` del audit siguen abiertos como implementation/release backlog; F3/19.2 permanece abierto.

## 1.2 — `[ 🟡 ]` release dependencies

Software integrado relevante: #86 provenance, #87 public security/status, #88 technical Authenticode/RFC3161, #90 OAuth rotation readiness y #91/#92/#94/#95/#96 Web corrective lineage. PR #98 es un candidate nuevo exact-base para producción Web, todavía OPEN en CYCLE153. Ninguno sustituye productive signing/notarization/tester/legal/security release evidence.

### F0/0.6 — `[x]` public operations

Owner runtime evidence previo mantiene security.txt/status HTTPS/SAN/contactos públicos probados. No equivale a signing/notarization/tester/legal/security release readiness.

### F0/0.7 — `[x]` technical/preparatory Authenticode + RFC3161

#88 integrado. **PRODUCTION SIGNING = NO-GO** hasta provider/certificado/publisher/key custody/CI auth/RFC3161/renewal/outage/rotation y controlled public build con evidencia real.

### F0/0.9 — `[ 🟡 ]` AI-assisted security slice / DNS rebinding

PR #89 sigue OPEN/Ready/mergeable @ `daf87da6ffd604ccac991311036919ae2de9bd7a`, recorded base `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`; stale frente a live `aa445095...`.

**Gate vivo:** F0/0.9 workflow run `33454881387` = `completed/failure` sobre exact head `daf87da6...`. Required CI viejo no sustituye el security gate fallido.

**CYCLE153:** #89 no tiene mutation owner porque WOZ152 fue movido al gate más crítico #98. Mientras #98 esté genuinamente `WAITING_CI/WAITING_EXTERNAL`, WOZ152 puede inspeccionar #89 estrictamente READ-ONLY para duplicate-check, divergence y refresh-readiness. No puede mutarlo, rerunearlo, revisarlo ni mergearlo en ese fallback. Próximo ciclo puede reabrir mutation ownership únicamente si #98 deja de ser la prioridad y JOBS lo asigna explícitamente.

### F0/0.20 — `[x]` OAuth secret rotation

Closed. No repetir ni registrar valores secretos.

### Tails reales restantes

- #89 P1 diagnosis + refresh/revalidation/integration en un ciclo con mutation owner explícito;
- production Authenticode/RFC3161 evidence;
- legal P0/P1 implementation backlog;
- independent security review donde siga siendo gate;
- 12–20 testers + hardware/plataformas/DAWs/fechas;
- F0/2.2 GitHub Support cleanup + fresh inaccessibility verification.

**Regla de salida:** F0 no es `[x]` global mientras 1.2/2.2 sigan abiertos. F5 y release siguen cerrados.
