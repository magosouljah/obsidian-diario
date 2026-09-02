# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE153:** `integration-v0.8.0-alpha.1 @ aa4450956579de381e82acf06c660b658c703cd1`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- 25.2 readiness docs integrados históricamente; tester execution/signing/notarization/global closure siguen abiertos.
- Issue #97 añade un blocker explícito pre-Beta que requiere validar startup/reveal tanto en Desktop como Web después del cleanup #98.

## windows/auth — `[ 🟡 ] OLD-BASE EXACT-GREEN EVIDENCE / REFRESH REQUIRED`

- BBB105 probó `HARNESS_ONLY_PROVEN`: broad fetch interceptor consumía WDIO/Tauri service plugin IPC.
- PR #93 reconstruyó harness/evidence-only sobre base histórica `134a293985c314eb09c238115e3bcb71e79f1810`, head `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, sin product mutation.
- Exact-head Windows Auth `33468863393` SUCCESS y checks aplicables observados en ese head fueron verdes.
- **GitHub vivo CYCLE153:** #93 sigue OPEN/Ready/mergeable con el mismo stale base/head.

La mergeabilidad mecánica no convierte evidencia vieja en canonical exact-head evidence. #93 queda `PARKED / NO MUTATION OWNER` CYCLE153; no existe fallback autorizado sobre #93 este ciclo.

## windows/review

Durable Review product gap pertenece F2/13.2. AAA114 lo revalidó y paró por write-surface unsafe. CYCLE153 queda `BLOCKED_WRITE_SURFACE / UNASSIGNED`; además #98 ocupa actualmente `src/App.tsx`, por lo que no se abre un owner concurrente.

## Startup/reveal cross-platform — Issue #97

Issue #97 está OPEN y declara `Must be addressed before Beta 1`. Requiere medir first usable cards/full visible library, near-instant startup normal, preservar artwork/playback semantics y validar Desktop + Web. No se implementa concurrentemente con #98 por overlap en App/startup/platform; pasa a next-after-#98.

## Signing Windows / macOS

#88 permanece integrado como technical/preparatory Authenticode + RFC3161 seam. Production signing continúa `NO-GO` hasta inputs/authorization RO y evidencia real; macOS signing/notarization/hardware siguen externos.

## 25.1 — `[ 🟡 ] IN PROGRESS`

Windows Auth conserva candidate evidence histórica pero necesita refresh al live baseline si aplica al alpha. #97 agrega una obligación literal Web+Desktop pre-Beta. Otros journeys aún carecen de evidencia actual completa; iPhone external. No cerrar 25.1 por un solo journey.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`

Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable. #89 todavía contiene el P1 SSRF corrective pendiente; legal audit conserva P0/P1 release blockers; #97 debe resolverse antes de Beta 1. No existe base factual para cerrar 25.2.

**Principio:** exact-head evidence-before-claim; un journey verde no sustituye el resto de 25.1 ni signing/notarization/tester execution.
