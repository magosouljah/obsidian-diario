# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 108:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- #79 / 25.2 readiness docs integrado históricamente; no demuestra tester execution, signing/notarization ni cierre global 25.2.

## windows/auth — `[ 🟡 ] NOT_PASS`

- #71 conserva fail-before histórico.
- #74 única product-corrective lineage, OPEN/Ready; product mutation no autorizada CYCLE 108.
- #84 única evidence lineage: OPEN/Ready @ `f53d46f39ece94f6de74f2f21a508ce01497ac41`, `base_sha=816f946c...` stale contra `38517c...`.
- Required CI en ese old head = SUCCESS, pero Exact Windows Auth Journey `33449587244` / job `99676242317` = **FAILURE**. CI genérico verde no sustituye el journey literal.
- Último resultado verificable de la línea: BBB099 `BLOCKED_STOP / AMBIGUOUS`, Issue #41 `5486566941`.
- Tuple sanitizado reusable: `POST /plugin%3Awdio%7Cget_window_states`, `requestClass=cross-origin`; después aparece tráfico WDIO plugin y `/get_settings`, y Tauri service reporta `Failed to get window states`.
- `NIGHT-BBB-102` no dejó final result/handoff verificable al preflight CYCLE 108; `SUPERSEDED / NOT_PASS`.

**Owner CYCLE 108: `NIGHT-BBB-103`.** Debe demostrar si broad fetch interception del harness está tragando tráfico WDIO/Tauri necesario. Clasificación obligatoria: `HARNESS_ONLY_PROVEN / PRODUCT_SIDE_PROVEN / SERVICE_BOUNDARY_PROVEN / AMBIGUOUS`. Solo HARNESS_ONLY permite corrección mínima de allowlist/mock boundary con assertions literales intactas. Antes de fresh evidence debe refresh history-preserving #84 al baseline `38517c...` si es seguro. Required result: session token persistido + AccountGate exited en packaged Windows Auth. **NO PRODUCT MUTATION / NO MERGE. CI-FALLBACK NONE.**

## windows/review
#72 sigue OPEN/stale/frozen. Durable Review product gap pertenece F2/13.2 y no se mezcla con BBB103.

## Signing Windows / macOS
PR #88 está ahora sobre base exacta `38517c...` y prepara seam fail-closed Authenticode + RFC3161, pero production signing continúa `NO-GO` hasta inputs/authorization RO y evidencia real. SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware siguen externos/abiertos. Exact-base no implica autorización de merge ni release.

## 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas incluyen windows/import, windows/updater y macos/updater automated evidence. windows/auth continúa rojo y otros journeys carecen de evidencia actual completa; iPhone external.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
#79 docs-only readiness artifact integrado. Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable. #89 registra P1 software DNS-rebinding candidate corrective y #88 mantiene signing P1 externo; no existe base factual para cerrar 25.2.

**Principio:** exact-head evidence-before-claim; CI genérico no sustituye journey literal.
