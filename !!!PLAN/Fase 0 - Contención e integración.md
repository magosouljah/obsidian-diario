# Fase 0 — Contención e integración

> Leer primero `Plan Maestro.md`. GitHub/runtime vivo prevalece. No reabrir trabajo técnico cerrado sin invalidación factual.

**Estado CYCLE 104:** `[ 🟡 ]` residual/administrativo. El núcleo técnico necesario para avanzar terminó; 5.1 y 5.2 están `[x]`. 1.2 y 2.2 conservan tails reales, por lo que F0 no se marca `[x]` globalmente.  
**Baseline vivo:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.  
**Release:** 🔴 `NO-GO`.

## Tablero

| Tarea | Estado | Gate resumido |
|---|---|---|
| 0.1 Congelar evidencia | [x] | baseline + NO-GO registrados |
| 0.2 Checkpoint interno | [x] | no equivale a release público |
| 1.1 Negocio | [x] | v1 comercial; mercados/distribución decididos |
| 1.2 Dependencias externas | [ 🟡 ] | governance/provenance + dominio/support/status + signing/reviews/testers |
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

### Release/provenance governance

Nuevo candidate reusable CYCLE 104:
- PR #86 `fix(release): close F0/0.4 provenance and stable/latest governance`;
- OPEN/Ready/mergeable;
- exact base `816f946c09d998ee5a045b3e70b2fe4f3a4160d0`;
- head `200474d061c63406774da8d21bd22460a8bd0312`;
- candidate declara separación alpha/beta/rc/stable, stable-only latest, immutable/no-clobber publication, Draft-before-publish y provenance source/build/target metadata;
- exact-head checks estaban **parcialmente in-progress** al preflight JOBS; no se promueve PASS todavía.

**Owner CYCLE 104: `NIGHT-WOZ-103`.** REUSE #86, review semantics + exact-head applicable CI; solo si exact/race-free/green puede mergear #86. Ese merge, si ocurre, solo cierra la **implementation slice** de governance/provenance; no cierra 1.2 global.

Nuevo candidate observado #87 `F0/0.6: publish security.txt and status surface` @ `d5d129c578355ca2ff6399bd2e6ec752c9f81618`, exact base live. Su body deja DNS/deploy/runtime explícitamente UNVERIFIED. WOZ103 puede inspeccionarlo READ-ONLY únicamente como CI-FALLBACK mientras #86 espera CI; no mutar/mergear #87 en este ciclo.

### Tails aún requeridos para 1.2 `[x]`
- governance/provenance implementation integrada y verificada;
- alphas/betas separadas correctamente del stable/latest real;
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

5.1 y 5.2 permanecen `[x]` con evidencia previamente aceptada: temporary auth/control-side secrets, direct 1.9GB media proof, cross-platform coverage; PostgreSQL authority, PITR RPO ~7m/RTO 3643s, multiversion keyring y observability/on-call. No repetir drills sin invalidación.

**Regla de salida:** F0 no es `[x]` global mientras 1.2/2.2 sigan abiertos. Esto no retrocede F1–F4 ni autoriza release. `Plan Maestro.md` conserva el baseline vivo canónico.
