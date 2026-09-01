# Fase 0 — Contención e integración

> Leer primero `Plan Maestro.md`. GitHub/runtime vivo prevalece. No reabrir trabajo técnico cerrado sin invalidación factual.

**Estado CYCLE 109:** `[ 🟡 ]` residual/administrativo + security/release tails. 5.1 y 5.2 están `[x]`. 0.8 legal launch review está `[x]` bajo excepción RO-approved AI-assisted; esto cierra la actividad de review, no compliance ni P0/P1 legales.  
**Baseline vivo:** `integration-v0.8.0-alpha.1 @ 78dd55b72142e69ea32ba6c1ba6d43e246ac6843`.  
**Release:** 🔴 `NO-GO`.

## Tablero

| Tarea | Estado | Gate resumido |
|---|---|---|
| 0.1 Congelar evidencia | [x] | baseline + NO-GO registrados |
| 0.2 Checkpoint interno | [x] | no equivale a release público |
| 0.8 Legal launch review | [x] | AI-assisted review completed; independent counsel deferred by explicit RO decision; residual legal risk accepted |
| 0.20 OAuth secret rotation | [ 🟡 ] | readiness software integrated; `READY_FOR_OWNER_ROTATION / NOT DONE`; falta rotación real + verify/revoke |
| 1.1 Negocio | [x] | v1 comercial; mercados/distribución decididos |
| 1.2 Dependencias externas | [ 🟡 ] | governance/provenance + public ops + technical Authenticode seam + OAuth readiness integrated; productive signing/OAuth/security/testers/legal implementation tails |
| 2.1 Contención inmediata | [x] | auth/ownership/límites |
| 2.2 Historial Git | [ 🟡 ] | GitHub Support + fresh inaccessibility verification |
| 3.1 Integración | [x] | `integration-v0.8.0-alpha.1` |
| 3.2 Contrato plataforma | [x] | Web sin Tauri |
| 4.1 Required CI | [x] | required CI policy |
| 4.2 Supply chain | [x] | scans/SBOM/checksums/provenance base |
| 5.1 Trust boundary / Direct | [x] | temporary auth + media directa |
| 5.2 Datos/recovery/secrets | [x] | PostgreSQL + RPO/RTO + rotation + observability |

## 0.8 — `[x]` review administrativo, no compliance

Evidence canónica: `Legal launch review - AI-assisted 2026-08-31.md`. RO reemplazó para F0/0.8 el counsel externo por revisión AI-assisted y aceptó el riesgo residual. No ocurrió attorney review. Los **12 P0 + 14 P1**, P2/P3 y `UNVERIFIED` del audit siguen abiertos como implementation/release backlog; `Gates - Publicación y contingencias.md` sigue exigiendo cero P0/P1 aplicables para publicación y F3/19.2 permanece abierto.

## 1.2 — `[ 🟡 ]` release dependencies

Decisiones fijas: v1 paid/commercial; Web + Windows NSIS + macOS DMG; MX/US/CA/EU/UK; eligibility **18+**. Apple Developer sigue deferred.

Software integrado relevante:
- #86 release/provenance → `b85723e1b3016d24bdb943393e796ccdb744247d`.
- #87 public security/status software → `38517c8065063206fed530028e4e8d20208f3807`.
- #88 F0/0.7 Authenticode + RFC3161 technical/preparatory seam → `1dbf60e58ca970c47d387b303e141e30e2b8eef5`; exact candidate `dcf3e13864d02cd4ffc958dc3a31b7411af6145a`; relevant CI SUCCESS.
- #90 F0/0.20 OAuth secret-rotation readiness + HEAD secret scan → `78dd55b72142e69ea32ba6c1ba6d43e246ac6843`; exact candidate `3f2063cf16fe63913dced6d57dc8a6cb46e12169`; F0/0.20 Secret Scan + Required CI SUCCESS.

### F0/0.6 — `[x]` public operations

Owner runtime evidence del `2026-09-01` mantiene security.txt/status HTTPS/SAN/contactos públicos probados. No equivale a signing/notarization/tester/legal/security release readiness.

### F0/0.7 — `[x]` technical/preparatory Authenticode + RFC3161

#88 quedó integrado el `2026-09-01`. Separa updater signing de Windows Authenticode, exige SHA-256 + RFC3161 y falla cerrado para `release_intent=public` sin inputs. **PRODUCTION SIGNING = NO-GO** hasta provider, certificado, publisher legal, key custody, CI auth, selector/signCommand, HTTPS RFC3161 endpoint, expected subject, renewal/outage/rotation procedures y un controlled public build con evidencia real.

### F0/0.9 — `[ 🟡 ]` AI-assisted security slice / DNS rebinding

PR #89 live: OPEN/Ready, head `daf87da6ffd604ccac991311036919ae2de9bd7a`, base `816f946c...` stale contra `78dd55b...`. Old-head green evidence no autoriza integración. Candidate = AI-assisted audit + DNS-rebinding SSRF hardening; no independent-pentest claim. La afirmación interna de #89 de que #88 no estaba integrado quedó factualmentе stale.

**Owner CYCLE 109: `NIGHT-WOZ-108`.** REUSE #89; reconciliar audit con #88 y #90 ya integrados; history-preserving refresh a `78dd55b...`; fresh exact-head F0/0.9 + Required CI. Solo WOZ108 puede mergear #89 y solo si exact/race-free/green.

### F0/0.20 — `[ 🟡 ]` OAuth rotation readiness

PR #90 quedó integrado el `2026-09-01` como `78dd55b72142e69ea32ba6c1ba6d43e246ac6843` con F0/0.20 Secret Scan y Required CI verdes. La parte software/readiness está integrada, pero el estado funcional permanece **`READY_FOR_OWNER_ROTATION / NOT DONE`**.

Para cerrar 0.20 todavía faltan acciones owner-side con evidencia: crear/reemplazar el credential de Google OAuth, desplegarlo en el secret storage/runtime real de producción, verificar OAuth E2E usando el nuevo credential y deshabilitar/eliminar el secreto anterior. No copiar valores secretos a GitHub, PRs, docs o chat.

### Tails reales restantes

- production Authenticode/RFC3161 evidence;
- actual OAuth secret rotation + verify/revoke;
- legal P0/P1 implementation backlog pese a cierre administrativo 0.8;
- independent security review donde siga siendo gate;
- 12–20 testers + hardware/plataformas/DAWs/fechas;
- F0/2.2 GitHub Support cleanup + fresh inaccessibility verification.

## 5.1 / 5.2 — CLOSED

Permanecen `[x]` con evidencia aceptada. No repetir drills sin invalidación.

**Regla de salida:** F0 no es `[x]` global mientras 1.2/2.2 sigan abiertos. F5 y release siguen cerrados.
