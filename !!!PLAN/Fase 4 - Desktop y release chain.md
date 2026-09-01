# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 109:** `integration-v0.8.0-alpha.1 @ 1dbf60e58ca970c47d387b303e141e30e2b8eef5`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- #79 / 25.2 readiness docs integrado históricamente; no demuestra tester execution, signing/notarization ni cierre global 25.2.

## windows/auth — `[ 🟡 ] NOT_PASS`

- #71 conserva fail-before histórico.
- #74 única product-corrective lineage; product mutation no autorizada CYCLE 109.
- #84 única evidence lineage: OPEN/Ready/mergeable @ `f53d46f39ece94f6de74f2f21a508ce01497ac41`, `base_sha=816f946c...` stale contra `1dbf60e...`.
- Generic exact-head old evidence incluye Test Desktop Portability/D6/D7/Web Build/Windows Import SUCCESS, pero Windows Auth Journey `33449587244` = **FAILURE**. CI genérico verde no sustituye el journey literal.
- Último resultado verificable de la línea: BBB099 `BLOCKED_STOP / AMBIGUOUS`, Issue #41 `5486566941`.
- Tuple sanitizado reusable: `POST /plugin%3Awdio%7Cget_window_states`, `requestClass=cross-origin`; después tráfico WDIO plugin y `/get_settings`; Tauri service reportó `Failed to get window states`.
- `NIGHT-BBB-103` no dejó final result/handoff verificable al preflight CYCLE 109; `SUPERSEDED / NOT_PASS`.

**Owner CYCLE 109: `NIGHT-BBB-104`.** Demostrar si broad fetch interception del harness está tragando tráfico WDIO/Tauri necesario. Clasificación obligatoria: `HARNESS_ONLY_PROVEN / PRODUCT_SIDE_PROVEN / SERVICE_BOUNDARY_PROVEN / AMBIGUOUS`. Solo HARNESS_ONLY permite corrección mínima de allowlist/mock boundary con assertions literales intactas. Antes de fresh evidence debe history-preserving refresh #84 al baseline `1dbf60e...` si es seguro. Required result: session token persistido + AccountGate exited en packaged Windows Auth. **NO PRODUCT MUTATION / NO MERGE. CI-FALLBACK NONE.**

## windows/review
#72 sigue OPEN/stale/frozen. Durable Review product gap pertenece F2/13.2 y no se mezcla con BBB104.

## Signing Windows / macOS
PR #88 quedó **MERGED** como `1dbf60e58ca970c47d387b303e141e30e2b8eef5`, candidate `dcf3e138...`, parents `38517c...` + `dcf3e138...`. Exact-candidate evidence: Test Desktop Portability `33456692874`, F4 Release Controls `33456692608`, F4 Functional Matrix `33456692456`, Windows Authenticode seam `33456692602`, D6 `33456692675`, D7 `33456692468`, Web Production Build `33456692483` y Windows Import `33456692695` = SUCCESS.

**Claim máximo:** technical/preparatory Authenticode + RFC3161 seam integrado. Production signing continúa `NO-GO` hasta inputs/authorization RO y evidencia real; macOS signing/notarization/hardware siguen externos.

## 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas incluyen windows/import, windows/updater y macos/updater automated evidence. windows/auth continúa rojo y otros journeys carecen de evidencia actual completa; iPhone external.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
#79 docs-only readiness integrado. Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable. #89 conserva P1 software candidate y el legal audit conserva P0/P1 release blockers; no existe base factual para cerrar 25.2.

**Principio:** exact-head evidence-before-claim; CI genérico no sustituye journey literal.
