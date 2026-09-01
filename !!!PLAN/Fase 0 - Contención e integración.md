# Fase 0 — Contención e integración

> Leer primero `Plan Maestro.md`. GitHub/runtime vivo prevalece. No reabrir trabajo técnico cerrado sin invalidación factual.

**Estado CYCLE 108:** `[ 🟡 ]` residual/administrativo + security/release tails. El núcleo técnico necesario para avanzar terminó; 5.1 y 5.2 están `[x]`. **0.8 legal launch review está `[x]` bajo la excepción RO-approved AI-assisted; esto cierra la tarea de review, no compliance.** 1.2 y 2.2 conservan tails reales.  
**Baseline vivo:** `integration-v0.8.0-alpha.1 @ 1dbf60e58ca970c47d387b303e141e30e2b8eef5`.  
**Release:** 🔴 `NO-GO`.

## Tablero

| Tarea | Estado | Gate resumido |
|---|---|---|
| 0.1 Congelar evidencia | [x] | baseline + NO-GO registrados |
| 0.2 Checkpoint interno | [x] | no equivale a release público |
| 0.8 Legal launch review | [x] | AI-assisted review completed; independent counsel deferred by explicit RO decision; residual legal risk accepted by RO |
| 1.1 Negocio | [x] | v1 comercial; mercados/distribución decididos |
| 1.2 Dependencias externas | [ 🟡 ] | governance/provenance + public operations runtime + Authenticode seam integrated; production signing/provider/security-review/testers tails; legal implementation backlog remains |
| 2.1 Contención inmediata | [x] | auth/ownership/límites |
| 2.2 Historial Git | [ 🟡 ] tail externo | GitHub Support + fresh inaccessibility verification |
| 3.1 Integración | [x] | integration-v0.8.0-alpha.1 |
| 3.2 Contrato plataforma | [x] | Web sin Tauri |
| 4.1 Required CI | [x] | required CI policy |
| 4.2 Supply chain | [x] | scans/SBOM/checksums/provenance base |
| 5.1 Trust boundary / Direct | [x] | temporary auth + media directa |
| 5.2 Datos/recovery/secrets | [x] | PostgreSQL + RPO/RTO + rotation + observability |

## 0.8 — `[x]` Legal launch review — AI-assisted administrative closure

`0.8 Legal launch review — AI-assisted review completed; independent counsel deferred by explicit RO decision; residual legal risk accepted by RO.`

**Evidence:** [`Legal launch review - AI-assisted 2026-08-31.md`](./Legal%20launch%20review%20-%20AI-assisted%202026-08-31.md).

**RO decision:** for F0/0.8 only, the originally required independent external legal review is replaced by the AI-assisted launch-readiness review completed on **2026-08-31**. RO expressly accepts the residual legal risk of deferring independent counsel at this stage. No attorney review occurred or is implied.

**Meaning of `[x]`:** the **review activity** is complete under the new governance policy. It does **not** mean BeatGaler is legally compliant, does not close substantive legal implementation work, and does not authorize public release.

The audit's **12 P0 + 14 P1** remain open implementation/release gates. P2/P3 and all `UNVERIFIED` items remain in the legal risk/backlog record. `Gates - Publicación y contingencias.md` still requires zero applicable P0/P1 for public release, and F3/19.2 remains open for product/legal implementation.

## 1.2 — `[ 🟡 ]` release dependencies

Decisiones fijas: v1 paid/commercial; Web + Windows NSIS + macOS DMG; MX/US/CA/EU/UK; eligibility **18+**. Apple Developer sigue deferred y no puede describirse macOS como public-signed/notarized sin evidencia.

### Software ya integrado

- PR #86 release/provenance governance integrado como `b85723e1b3016d24bdb943393e796ccdb744247d`.
- PR #87 public security/status software slice integrado como `38517c8065063206fed530028e4e8d20208f3807`; exact parents `b85723e...` + `ba0d7b...` y applicable exact-head CI SUCCESS.
- PR #88 F0/0.7 Authenticode + RFC3161 technical/preparatory seam integrado como `1dbf60e58ca970c47d387b303e141e30e2b8eef5`; candidate `dcf3e138...` sobre baseline exacto `38517c...`, Authenticode seam SUCCESS y Required CI SUCCESS.

### F0/0.6 — `[x]` public operations

Cerrado con evidencia runtime pública el `2026-09-01`:
- `https://beatgaler.com/.well-known/security.txt` → HTTP 200, `Content-Type: text/plain; charset=utf-8`, contactos Security/Abuse, idiomas `en, es`, canonical correcto y `Expires: 2027-02-28T23:59:59Z`;
- `https://status.beatgaler.com/` → HTTP 200 sobre HTTPS y superficie pública de estado para Web, API, Authentication y Galer Cloud / Storage;
- certificado servido por Nginx cubre `beatgaler.com`, `www.beatgaler.com` y `status.beatgaler.com`;
- soporte/security/abuse permanecen como contactos públicos operativos.

F0/0.6 no es ya un tail de 1.2. Esta evidencia no prueba signing/notarization/tester/legal/security restantes ni autoriza release.

### F0/0.7 — `[x]` Authenticode / RFC3161 technical-preparatory seam

PR #88 quedó integrado el `2026-09-01` como `1dbf60e58ca970c47d387b303e141e30e2b8eef5` tras exact-head CI verde. El seam separa Tauri updater signing de Windows Authenticode, exige SHA-256 + RFC3161, verifica installer/app y mantiene fail-closed la intención `public` mientras falten inputs production.

**F0/0.7 queda DONE únicamente para la parte técnica/preparatoria.** Owner = RO; provider permanece `PENDING_OWNER_PROVIDER`; **PRODUCTION SIGNING = NO-GO**. Siguen pendientes como release-chain externo: provider, certificado, publisher legal, key custody, CI auth, selector/config o `signCommand`, endpoint HTTPS RFC3161, expected subject, renovación/expiración, outage procedure, rotation/emergency disable y un controlled `release_intent=public` con evidencia real.

### F0/0.9 — security audit + P1 DNS-rebinding

PR #89 continúa OPEN/Ready al preflight CYCLE 108, head `daf87da6ffd604ccac991311036919ae2de9bd7a`, base_sha `816f946c...` stale contra `1dbf60e...`. Sus checks old-head, incluido Required CI, están verdes, pero esa evidencia no autoriza integración contra el baseline actual.

El candidate declara audit AI-assisted, no independent pentest. P1 software observado: DNS-rebinding SSRF hardening; Authenticode queda separado en #88.

**Owner CYCLE 108: `NIGHT-WOZ-107`.** REUSE #89; review + refresh history-preserving al baseline vivo + fresh exact-head CI. Puede mergear únicamente #89 si queda exact-base/head, applicable CI green y race-free. No external-pentest claim.

### OAuth secret rotation readiness

PR #90 es readiness software/documental; rotar/desplegar/verificar/revocar la credencial sigue siendo acción owner externa. `NIGHT-WOZ-107` puede inspeccionarlo READ-ONLY solo si #89 espera CI.

### Tails aún requeridos para 1.2 `[x]`
- Windows Authenticode + RFC3161 productivo y evidencia cuando corresponda;
- rotación real del OAuth secret afectado y verificación/revocación owner-side;
- **F0/0.8 review está cerrado por excepción AI-assisted RO-approved; los P0/P1 legales sustantivos permanecen abiertos bajo F3/19.2 + gate canónico**;
- revisión de seguridad independiente donde siga siendo gate real;
- matriz 12–20 testers + hardware/plataformas/DAWs/fechas.

## 2.2 — `[ 🟡 ]` historial Git

Trabajo técnico de rewrite y Required CI post-rewrite ya completado. Baseline histórico de salida `b9c2317297ff3c0f7a6246ac97517fa978f6caea`; run `33148873459` SUCCESS. Tail restante:
- [ ] GitHub Support cleanup server-side aplicable;
- [ ] fresh independent verification de inaccesibilidad posterior.

No repetir rewrite ni borrar evidencia para recrear proof.

## 5.1 / 5.2 — CLOSED

5.1 y 5.2 permanecen `[x]` con evidencia previamente aceptada. No repetir drills sin invalidación.

**Regla de salida:** F0 no es `[x]` global mientras 1.2/2.2 sigan abiertos. Cerrar administrativamente 0.8 no cambia esa regla, no retrocede F1–F4 y no autoriza release.
