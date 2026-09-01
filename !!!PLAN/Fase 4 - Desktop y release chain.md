# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 111:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810` al preflight JOBS.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- #79 / 25.2 readiness docs integrado históricamente; no demuestra tester execution, signing/notarization ni cierre global 25.2.

## windows/auth — `[ 🟡 ] NOT_PASS / HARNESS_CAUSE_PROVEN`

- #71 conserva fail-before histórico.
- #74 es la product-corrective lineage histórica; **product mutation no está autorizada** en CYCLE111.
- #84 evidence lineage sigue OPEN/Ready @ `f53d46f39ece94f6de74f2f21a508ce01497ac41`, recorded base `816f946c...`, stale contra live `134a293...`.
- Literal old-head Windows Auth `33449587244` permanece **FAILURE**; generic CI no lo sustituye.
- `NIGHT-BBB-105` terminó `BLOCKED_STOP / HARNESS_ONLY_PROVEN_REFRESH_UNSAFE`.
- Causal evidence reusable: `POST /plugin%3Awdio%7Cget_window_states`, `requestClass=cross-origin`, pertenece al tráfico WDIO/Tauri service; el broad fetch interceptor del harness es la frontera que lo consume. Esto eleva causalidad de AMBIGUOUS a **HARNESS_ONLY_PROVEN**, pero no es PASS del journey.
- BBB105 no modificó nada ni lanzó fresh test porque su autoridad previa exigía STOP ante refresh/reconstruction inseguro.

**Owner CYCLE111: `NIGHT-BBB-106`.** Authority bounded para reconstruir un clean successor/evidence candidate desde live baseline preservando solo el delta harness/evidence autorizado y la exact intended #74 lineage bajo prueba. Puede aplicar únicamente el mínimo IPC bypass/allowlist en harness/service boundary; debe conservar `/auth/health` + `/auth/login` stubs y assertions literales. **NO PRODUCT MUTATION / NO MERGE.**

PASS literal requiere, en el mismo exact head:
1. returned session token persisted;
2. AccountGate exited;
3. packaged Windows Auth SUCCESS;
4. applicable exact-head CI SUCCESS.

Si la reconstrucción exige product-auth/session mutation, BBB106 debe STOP `PRODUCT_SIDE_REQUIRED`.

## windows/review

#72 sigue OPEN/stale/frozen. Durable Review product gap pertenece F2/13.2 y es owner AAA107; no mezclar con BBB106.

## Signing Windows / macOS

PR #88 quedó MERGED como `1dbf60e58ca970c47d387b303e141e30e2b8eef5`, candidate `dcf3e138...`. Claim máximo: technical/preparatory Authenticode + RFC3161 seam integrado. Production signing continúa `NO-GO` hasta inputs/authorization RO y evidencia real; macOS signing/notarization/hardware siguen externos.

## 25.1 — `[ 🟡 ] IN PROGRESS`

Integrated rows conocidas incluyen windows/import, windows/updater y macos/updater automated evidence. windows/auth continúa rojo y otros journeys carecen de evidencia actual completa; iPhone external.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`

#79 docs-only readiness integrado. Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable. #89 conserva P1 software candidate y legal audit conserva P0/P1 release blockers; no existe base factual para cerrar 25.2.

**Principio:** exact-head evidence-before-claim; causal proof del harness no sustituye journey literal.
