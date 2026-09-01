# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 107:** `integration-v0.8.0-alpha.1 @ 38517c8065063206fed530028e4e8d20208f3807`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- #79 / 25.2 readiness docs integrado históricamente; no demuestra tester execution, signing/notarization ni cierre global 25.2.

## windows/auth — `[ 🟡 ] NOT_PASS`

- #71 conserva fail-before histórico.
- #74 única product-corrective lineage, OPEN/Ready; product mutation no autorizada CYCLE 107.
- #84 única evidence lineage: OPEN/Ready @ `f53d46f39ece94f6de74f2f21a508ce01497ac41`, pero su `base_sha=816f946c...` está stale contra integración `38517c...`.
- Exact Windows Auth Journey `33449587244` / job `99676242317` = **FAILURE** en isolated auth assertions. Otros checks verdes no sustituyen el journey literal.
- Último resultado verificable BBB099: `BLOCKED_STOP / AMBIGUOUS`, Issue #41 `5486566941`.
- JOBS recuperó del failed job el primer tuple sanitizado: `POST /plugin%3Awdio%7Cget_window_states`, `requestClass=cross-origin`; después aparece tráfico WDIO plugin y `/get_settings`, y el Tauri service reporta `Failed to get window states`.
- `NIGHT-BBB-101` no dejó final result/handoff al preflight CYCLE 107; `SUPERSEDED / NOT_PASS`.

**Owner CYCLE 107: `NIGHT-BBB-102`.** Debe demostrar si el broad fetch interception del harness está tragando tráfico WDIO/Tauri necesario. Clasificación obligatoria: `HARNESS_ONLY_PROVEN / PRODUCT_SIDE_PROVEN / SERVICE_BOUNDARY_PROVEN / AMBIGUOUS`. Solo HARNESS_ONLY permite corrección mínima de allowlist/mock boundary, assertions literales intactas. Antes de fresh evidence debe refresh history-preserving #84 al baseline `38517c...` si es seguro. Required result sigue: session token persistido + AccountGate exited en packaged Windows Auth. **NO PRODUCT MUTATION / NO MERGE.** CI-FALLBACK NONE.

## windows/review
#72 sigue OPEN/stale/frozen. Durable Review product gap pertenece F2/13.2 y no se mezcla con BBB102.

## Signing Windows / macOS
PR #88 prepara seam fail-closed Authenticode + RFC3161, pero production signing continúa `NO-GO` hasta inputs/authorization RO y evidencia real. SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware siguen externos/abiertos. No describir builds como signed/notarized sin evidencia.

## 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas incluyen windows/import, windows/updater y macos/updater automated evidence. windows/auth continúa rojo y otros journeys carecen de evidencia actual completa; iPhone external.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
#79 docs-only readiness artifact integrado. Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable. #89 actualmente registra un P1 software DNS-rebinding en candidate corrective y #88 mantiene el signing P1 separado; por tanto no existe base factual para cerrar 25.2.

**Principio:** exact-head evidence-before-claim; CI genérico no sustituye journey literal.
