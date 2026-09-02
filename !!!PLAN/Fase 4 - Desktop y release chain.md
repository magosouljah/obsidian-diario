# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE155:** `integration-v0.8.0-alpha.1 @ c2766fb23de5bb837a7fef4080a6aa7a6716f15e`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- 25.2 readiness docs integrados; tester execution/signing/notarization/global closure abiertos.
- Issue #97 es blocker literal pre-Beta y exige validación startup/reveal Desktop + Web; owner CYCLE155 = WOZ154.

## windows/auth — `[ 🟡 ] OLD-BASE EXACT-GREEN EVIDENCE / REFRESH REQUIRED IF IN_ALPHA`

PR #93 sigue OPEN @ `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, base histórica `134a293985c314eb09c238115e3bcb71e79f1810`; harness/evidence-only, sin product mutation. Windows Auth histórica fue exact-green para ese baseline, no canónica para live `c2766fb...`.

CYCLE155: #93 = `PARKED / NO MUTATION OWNER`; refresh/revalidation solo si F1/1.7 lo mantiene `IN_ALPHA`.

## windows/review

Durable Review pertenece F2/13.2. AAA114 probó el gap y paró por write-surface unsafe. CYCLE155 sigue `BLOCKED_WRITE_SURFACE / UNASSIGNED`; no abrir owner concurrente mientras #97 ocupe App/startup surfaces.

## Startup/reveal cross-platform — Issue #97

#97 sigue OPEN, cero comments, y `Must be addressed before Beta 1`. WOZ154 posee #97 exclusivamente: medir first usable cards/full visible library, mínimo correction shared/cross-platform, preservar artwork/playback semantics y validar Desktop + Web. Conditional merge solo con exact-green/race-free evidence.

## Signing Windows / macOS

#88 sigue integrado como technical/preparatory Authenticode + RFC3161 seam. Production signing = `NO-GO` hasta inputs/authorization RO + evidencia real; macOS signing/notarization/hardware externos.

## 25.1 — `[ 🟡 ] IN PROGRESS`

Windows Auth necesita refresh si aplica al alpha. #97 añade obligación Web+Desktop pre-Beta. Otros journeys carecen de evidencia actual completa; iPhone external. No cerrar 25.1 por un journey verde.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`

Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence. #89 conserva P1 corrective pendiente bajo AAA151; legal audit conserva P0/P1 release blockers; #97 debe resolverse antes de Beta 1. #99 mejora provenance Web pero no sustituye signing/notarization/testers.

**Principio:** exact-head evidence-before-claim; un journey verde no sustituye el resto de 25.1 ni signing/notarization/tester execution.
