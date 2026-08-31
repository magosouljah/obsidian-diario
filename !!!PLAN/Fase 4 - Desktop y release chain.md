# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 102:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- #79 / F4 25.2 readiness docs integrado como `816f946c...`; no demuestra tester execution, signing/notarization ni cierre global 25.2.

### windows/auth

- #71 conserva fail-before histórico.
- #74 única product-corrective lineage: `d1593d368e1015abb6a25bf98e5fa8586664ac95`, OPEN/Ready/mergeable, base exact live.
- #84 única evidence lineage: `28c3810c43eefa8bab0ffa2026c371882ead2f2f`, OPEN/Ready/mergeable, base exact live.
- Exact #84 Windows Auth Journey `33439899177` / job `99645269221` = **FAILURE**. D6/D7/Web Production Build/Desktop Portability/Windows Import verdes no sustituyen ese journey literal.
- Reusable trace: repeated `unexpected-request`, `gatePresent=true`, `tokenPresent=false`; literal token-persistence assertion red.
- `NIGHT-BBB-095` terminó `BLOCKED_STOP / HARNESS_SERVICE_BLOCKED`: current harness intercepta fetch y convierte non `/auth/health`/`/auth/login` en synthetic 500, pero la traza no identifica method/path del primer request; por tanto no está probado harness-only ni product-side.
- `NIGHT-BBB-096` no dejó resultado final ni matching Issue #41 handoff al preflight CYCLE 102; `SUPERSEDED / NOT_PASS`. #84 quedó unchanged.

**Owner CYCLE 102: `NIGHT-BBB-097`.** Diagnostic-only: registrar primer unexpected request como `{method, pathname/requestClass}` sanitizado, sin query/body/headers/token/password; fresh packaged Windows journey; solo si la nueva traza prueba harness rejection legítima puede hacerse minimum harness correction. Product-side ⇒ STOP y nueva autorización JOBS. **NO PRODUCT MUTATION / NO MERGE.** CI-FALLBACK NONE.

### windows/review

#72 sigue OPEN/stale/frozen; no pertenece a BBB097 y overlap con AAA098 Review.

## Día 22 / 23

Signing Windows, SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware siguen externos/abiertos. Owner decidió no pagar Apple Developer/certificados ahora; no describir builds como signed/notarized sin evidencia.

## Día 25

### 25.1 — `[ 🟡 ] IN PROGRESS`

Integrated rows conocidas: `windows/import`, `windows/updater`, `macos/updater` automated evidence. `windows/auth` sigue roja sobre exact #84; múltiples journeys continúan sin evidencia actual completa; iPhone external.

### 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`

#79 docs-only readiness artifact integrado. Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable.

**Principio:** exact-head evidence-before-claim; CI genérico no sustituye el journey literal rojo.
