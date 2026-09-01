# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 110:** `integration-v0.8.0-alpha.1 @ 78dd55b72142e69ea32ba6c1ba6d43e246ac6843` al preflight JOBS.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- #79 / 25.2 readiness docs integrado históricamente; no demuestra tester execution, signing/notarization ni cierre global 25.2.

## windows/auth — `[ 🟡 ] NOT_PASS`

- #71 conserva fail-before histórico.
- #74 única product-corrective lineage; product mutation no autorizada CYCLE 110.
- #84 única evidence lineage: OPEN/Ready @ `f53d46f39ece94f6de74f2f21a508ce01497ac41`, base vieja `816f946c...`; debe refresh a live head observado por BBB105 antes de fresh evidence si el refresh es clean/safe.
- Generic old-head CI verde no sustituye Windows Auth Journey `33449587244` = **FAILURE**.
- Último resultado verificable de la línea: BBB099 `BLOCKED_STOP / AMBIGUOUS`, Issue #41 `5486566941`.
- Tuple sanitizado reusable: `POST /plugin%3Awdio%7Cget_window_states`, `requestClass=cross-origin`; después tráfico WDIO plugin y `/get_settings`; Tauri service reportó `Failed to get window states`.
- `NIGHT-BBB-104` no dejó final result/handoff verificable al preflight CYCLE 110; `SUPERSEDED / NOT_PASS`.

**Owner CYCLE 110: `NIGHT-BBB-105`.** Demostrar si broad fetch interception del harness está tragando tráfico WDIO/Tauri necesario. Clasificación obligatoria: `HARNESS_ONLY_PROVEN / PRODUCT_SIDE_PROVEN / SERVICE_BOUNDARY_PROVEN / AMBIGUOUS`. Solo HARNESS_ONLY permite corrección mínima de allowlist/mock boundary con assertions literales intactas. Debe usar el live integration head de su turno porque AAA106 puede integrar #91 antes. Required result: session token persistido + AccountGate exited en packaged Windows Auth. **NO PRODUCT MUTATION / NO MERGE. CI-FALLBACK NONE.**

## windows/review

#72 sigue OPEN/stale/frozen. Durable Review product gap pertenece F2/13.2 y no se mezcla con BBB105. AAA106 solo puede inspeccionarlo READ-ONLY como fallback mientras #91 espera CI.

## Signing Windows / macOS

PR #88 quedó **MERGED** como `1dbf60e58ca970c47d387b303e141e30e2b8eef5`, candidate `dcf3e138...`. Exact-candidate evidence relevante fue SUCCESS para portability, F4 controls/matrix, Authenticode seam, D6, D7, Web Build y Windows Import.

**Claim máximo:** technical/preparatory Authenticode + RFC3161 seam integrado. Production signing continúa `NO-GO` hasta inputs/authorization RO y evidencia real; macOS signing/notarization/hardware siguen externos.

## 25.1 — `[ 🟡 ] IN PROGRESS`

Integrated rows conocidas incluyen windows/import, windows/updater y macos/updater automated evidence. windows/auth continúa rojo y otros journeys carecen de evidencia actual completa; iPhone external.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`

#79 docs-only readiness integrado. Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable. #89 conserva P1 software candidate y legal audit conserva P0/P1 release blockers; no existe base factual para cerrar 25.2.

**Principio:** exact-head evidence-before-claim; CI genérico no sustituye journey literal.
