# Fase 0 — Contención e integración

> Leer primero `Plan Maestro.md`. GitHub/runtime vivo prevalece. No reabrir trabajo técnico cerrado sin invalidación factual.

**Estado CYCLE 105:** `[ 🟡 ]` residual/administrativo. El núcleo técnico necesario para avanzar terminó; 5.1 y 5.2 están `[x]`. 1.2 y 2.2 conservan tails reales, por lo que F0 no se marca `[x]` globalmente.  
**Baseline vivo:** `integration-v0.8.0-alpha.1 @ b85723e1b3016d24bdb943393e796ccdb744247d`.  
**Release:** 🔴 `NO-GO`.

## Tablero

| Tarea | Estado | Gate resumido |
|---|---|---|
| 0.1 Congelar evidencia | [x] | baseline + NO-GO registrados |
| 0.2 Checkpoint interno | [x] | no equivale a release público |
| 1.1 Negocio | [x] | v1 comercial; mercados/distribución decididos |
| 1.2 Dependencias externas | [ 🟡 ] | governance/provenance software integrated; dominio/support/status + signing/reviews/testers tails |
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

### Release/provenance governance — implementation slice integrated

PR #86 `fix(release): close F0/0.4 provenance and stable/latest governance` fue integrado factual y verificablemente:
- candidate head `200474d061c63406774da8d21bd22460a8bd0312`;
- previous integration `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`;
- merge `b85723e1b3016d24bdb943393e796ccdb744247d`, con esos dos parents;
- implementación preserva alpha/beta/rc como prerelease, stable-only `latest`, no-clobber/immutable publication, Draft-before-publish, provenance source/build/target metadata y kill-switch de publicación.

**Promoción CYCLE 105:** solo la **implementation slice** de release/provenance governance = `PASS / INTEGRATED`. Esto NO cierra 1.2 global, no publica release y no demuestra signing/notarization/tester/legal/security external evidence.

### Public security/status candidate

PR #87 `F0/0.6: publish security.txt and status surface` está OPEN/Ready/mergeable sobre el baseline exacto `b85723e...`, head `ba0d7b689e587da42cc8105b22d0ed0c206bc064`. Workflows observados exact-head: D6 SUCCESS, D7 SUCCESS, Public Operations SUCCESS, Web Production Build SUCCESS, Desktop Portability SUCCESS; Upgrade 21.2 skipped/no aplicable. Runtime/DNS/deploy sigue explícitamente UNVERIFIED.

**Owner CYCLE 105: `NIGHT-WOZ-104`.** REUSE #87; puede mergear únicamente #87 si recheck exact-base/head/scope + applicable CI green + expected-head race-free. Maximum claim: software slice; DNS/TLS/deploy/runtime externos quedan abiertos.

### Tails aún requeridos para 1.2 `[x]`
- dominio/DNS/TLS/support/security-abuse/status con runtime/owners aplicables;
- Windows Authenticode + RFC3161 plan/owner y evidencia cuando corresponda;
- revisión legal independiente;
- revisión de seguridad independiente;
- matriz 12–20 testers + hardware/plataformas/DAWs/fechas.

## 2.2 — `[ 🟡 ]` historial Git

Trabajo técnico de rewrite y Required CI post-rewrite ya completado. Baseline histórico de salida `b9c2317297ff3c0f7a6246ac97517fa978f6caea`; run `33148873459` SUCCESS. Tail restante, no bloqueante para trabajo interno por decisión RO:
- [ ] GitHub Support cleanup server-side aplicable;
- [ ] fresh independent verification de inaccesibilidad posterior.

No repetir rewrite ni borrar evidencia para recrear proof.

## 5.1 / 5.2 — CLOSED

5.1 y 5.2 permanecen `[x]` con evidencia previamente aceptada. No repetir drills sin invalidación.

**Regla de salida:** F0 no es `[x]` global mientras 1.2/2.2 sigan abiertos. Esto no retrocede F1–F4 ni autoriza release. `Plan Maestro.md` conserva el baseline vivo canónico.
