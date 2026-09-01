# Fase 0 — Contención e integración

> Leer primero `Plan Maestro.md`. GitHub/runtime vivo prevalece. No reabrir trabajo técnico cerrado sin invalidación factual.

**Estado CYCLE 108:** `[ 🟡 ]` residual/administrativo + security/release tails. El núcleo técnico necesario para avanzar terminó; 5.1 y 5.2 están `[x]`. 1.2 y 2.2 conservan tails reales.  
**Baseline vivo:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.  
**Release:** 🔴 `NO-GO`.

## Tablero

| Tarea | Estado | Gate resumido |
|---|---|---|
| 0.1 Congelar evidencia | [x] | baseline + NO-GO registrados |
| 0.2 Checkpoint interno | [x] | no equivale a release público |
| 1.1 Negocio | [x] | v1 comercial; mercados/distribución decididos |
| 1.2 Dependencias externas | [ 🟡 ] | governance/provenance + security/status software integrated; signing/provider/runtime/reviews/testers tails |
| 2.1 Contención inmediata | [x] | auth/ownership/límites |
| 2.2 Historial Git | [ 🟡 ] tail externo | GitHub Support + fresh inaccessibility verification |
| 3.1 Integración | [x] | integration-v0.8.0-alpha.1 |
| 3.2 Contrato plataforma | [x] | Web sin Tauri |
| 4.1 Required CI | [x] | required CI policy |
| 4.2 Supply chain | [x] | scans/SBOM/checksums/provenance base |
| 5.1 Trust boundary / Direct | [x] | temporary auth + media directa |
| 5.2 Datos/recovery/secrets | [x] | PostgreSQL + RPO/RTO + rotation + observability |

## 1.2 — `[ 🟡 ]` release dependencies

Decisiones fijas: v1 paid/commercial; Web + Windows NSIS + macOS DMG; MX/US/CA/EU/UK; eligibility **18+**. Apple Developer sigue deferred y no puede describirse macOS como public-signed/notarized sin evidencia.

### Software ya integrado

- PR #86 release/provenance governance integrado como `b85723e1b3016d24bdb943393e796ccdb744247d`.
- PR #87 public security/status software slice integrado como `38517c8065063206fed530028e4e8d20208f3807`; exact parents `b85723e...` + `ba0d7b...` y applicable exact-head CI SUCCESS.

Estas promociones no prueban signing/notarization/tester/legal/security external evidence ni status DNS/public runtime.

### F0/0.9 — security audit + P1 DNS-rebinding

PR #89 continúa OPEN/Ready al preflight CYCLE 108, head `daf87da6ffd604ccac991311036919ae2de9bd7a`, base_sha `816f946c...` stale contra `38517c...`. Sus checks old-head, incluido Required CI, están verdes, pero esa evidencia no autoriza integración contra el baseline actual.

El candidate declara audit AI-assisted, no independent pentest. P1 software observado: DNS-rebinding SSRF hardening; Authenticode queda separado en #88.

**Owner CYCLE 108: `NIGHT-WOZ-107`.** REUSE #89; review + refresh history-preserving al baseline vivo + fresh exact-head CI. Puede mergear únicamente #89 si queda exact-base/head, applicable CI green y race-free. No external-pentest claim.

### Authenticode / RFC3161 — external owner inputs

PR #88 ahora está sobre base exacta `38517c...`, pero su contrato mantiene **PRODUCTION SIGNING = NO-GO** y exige autorización/inputs RO: provider, certificado, publisher legal, custody, CI auth, selector/config, RFC3161 endpoint, renewal/outage/rotation y controlled public build. Exact base no elimina ese gate. No nocturnal merge authorization.

### OAuth secret rotation readiness

PR #90 es readiness software/documental; rotar/desplegar/verificar/revocar la credencial sigue siendo acción owner externa. `NIGHT-WOZ-107` puede inspeccionarlo READ-ONLY solo si #89 espera CI.

### Tails aún requeridos para 1.2 `[x]`
- dominio/DNS/TLS/support/security-abuse/status con runtime/owners aplicables;
- Windows Authenticode + RFC3161 productivo y evidencia cuando corresponda;
- rotación real del OAuth secret afectado y verificación/revocación owner-side;
- revisión legal/seguridad independiente donde siga siendo gate real;
- matriz 12–20 testers + hardware/plataformas/DAWs/fechas.

## 2.2 — `[ 🟡 ]` historial Git

Trabajo técnico de rewrite y Required CI post-rewrite ya completado. Baseline histórico de salida `b9c2317297ff3c0f7a6246ac97517fa978f6caea`; run `33148873459` SUCCESS. Tail restante:
- [ ] GitHub Support cleanup server-side aplicable;
- [ ] fresh independent verification de inaccesibilidad posterior.

No repetir rewrite ni borrar evidencia para recrear proof.

## 5.1 / 5.2 — CLOSED

5.1 y 5.2 permanecen `[x]` con evidencia previamente aceptada. No repetir drills sin invalidación.

**Regla de salida:** F0 no es `[x]` global mientras 1.2/2.2 sigan abiertos. Esto no retrocede F1–F4 ni autoriza release.
