# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 113:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810` al preflight JOBS.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- #79 / 25.2 readiness docs integrado históricamente; no demuestra tester execution, signing/notarization ni cierre global 25.2.

## windows/auth — `[ 🟡 ] EXACT-GREEN CANDIDATE / GLOBAL 25.1 STILL OPEN`

- #71 conserva fail-before histórico.
- #74 es la product-corrective lineage histórica; CYCLE113 no autoriza product mutation.
- #84 queda como evidence lineage histórica stale @ `f53d46f...`; no usar su old-head failure como estado actual después de la evidencia #93.
- BBB105 probó `HARNESS_ONLY_PROVEN`: el broad fetch interceptor consumía tráfico WDIO/Tauri service como `POST /plugin%3Awdio%7Cget_window_states`.
- `NIGHT-BBB-107` reconstruyó un successor limpio directamente sobre live baseline y abrió PR #93 `bbb/night-25.1-auth-live-rebuild @ b2c4eb441280343c4b9c39d57851c6d3da33abaa`, exact base `134a293...`.
- #93 cambia únicamente tres archivos de harness/evidence: `.github/workflows/f4-25.1-windows-auth.yml`, `scripts/run-auth-e2e.mjs`, `tests/e2e/auth-flow.e2e.mjs`; no product files.
- Corrección bounded: el auth mock delega `/plugin%3Awdio%7C...` a native fetch; `/auth/health` y `/auth/login` siguen stubbed; assertions literales token persistence + AccountGate exit permanecen.
- Exact-head Windows Auth run `33468863393` = **SUCCESS**; job `99734302105` = **SUCCESS**, incluyendo `Run isolated Windows auth assertions`.
- Exact-head D6, D7, Desktop Portability, Windows Import y F0/0.20 secret scan = SUCCESS; Upgrade 21.2 Staging skipped/no aplicable.

**Resultado procesado CYCLE113:** `F4/25.1 WINDOWS_AUTH_CANDIDATE_EXACT_GREEN / NO_MERGE`. Esto sustituye factual y operacionalmente el antiguo estado “Windows Auth literal rojo” para este candidate, pero **no cierra global 25.1** y no convierte el baseline canónico en evidence-integrated hasta que el owner autorizado procese #93.

**Owner CYCLE113: `NIGHT-WOZ-112`.** Puede revisar/mergear **#93 solamente** si base/head siguen exactos, checks aplicables siguen SUCCESS y no hay race. Maximum claim post-merge: `WINDOWS_PACKAGED_AUTH_LITERAL_PASS_EVIDENCE_INTEGRATED`; no cerrar 25.1 sin el resto de journeys.

## windows/review

#72 sigue OPEN/stale/frozen. Durable Review product gap pertenece F2/13.2 y es owner AAA109; no mezclar con WOZ112.

## Signing Windows / macOS

PR #88 quedó MERGED como `1dbf60e58ca970c47d387b303e141e30e2b8eef5`, candidate `dcf3e138...`. Claim máximo: technical/preparatory Authenticode + RFC3161 seam integrado. Production signing continúa `NO-GO` hasta inputs/authorization RO y evidencia real; macOS signing/notarization/hardware siguen externos.

## 25.1 — `[ 🟡 ] IN PROGRESS`

Integrated rows conocidas incluyen windows/import, windows/updater y macos/updater automated evidence. Windows Auth ahora tiene candidate exact-green #93 pendiente de integration review. Otros journeys aún carecen de evidencia actual completa; iPhone external. Por eso 25.1 global permanece abierto.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`

#79 docs-only readiness integrado. Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable. #89 conserva P1 software candidate y legal audit conserva P0/P1 release blockers; no existe base factual para cerrar 25.2.

**Principio:** exact-head evidence-before-claim; un journey verde no sustituye el resto de 25.1 ni signing/notarization/tester execution.
