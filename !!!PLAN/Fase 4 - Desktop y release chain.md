# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE137:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- 25.2 readiness docs integrados históricamente; tester execution/signing/notarization/global closure siguen abiertos.

## windows/auth — `[ 🟡 ] OLD-BASE EXACT-GREEN EVIDENCE / REFRESH REQUIRED`

- BBB105 probó `HARNESS_ONLY_PROVEN`: broad fetch interceptor consumía WDIO/Tauri service plugin IPC.
- PR #93 reconstruyó harness/evidence-only sobre base histórica `134a293985c314eb09c238115e3bcb71e79f1810`, head `b2c4eb441280343c4b9c39d57851c6d3da33abaa`, 3 files, sin product mutation.
- Exact-head Windows Auth `33468863393` SUCCESS y checks aplicables observados en ese head fueron verdes.
- **GitHub vivo CYCLE137:** #93 sigue OPEN/Ready/mergeable, pero recorded base `134a293...` continúa stale contra integration `43fdf70e...` después de #92/#94/#95.

La mergeabilidad mecánica no convierte evidencia vieja en exact-head canonical evidence. #93 queda `PARKED / NO MUTATION OWNER` CYCLE137. WOZ136 puede hacer únicamente inventario READ-ONLY de aplicabilidad como CI-FALLBACK mientras #89 esté genuinamente esperando CI después de clean refresh; no puede mutar #93 ni promover 25.1.

## windows/review

Durable Review product gap pertenece F2/13.2. AAA114 lo revalidó y paró por write-surface unsafe; CYCLE137 queda `BLOCKED_WRITE_SURFACE / UNASSIGNED`, sin mezclarlo con F4.

## Signing Windows / macOS

#88 permanece integrado como technical/preparatory Authenticode + RFC3161 seam. Production signing continúa `NO-GO` hasta inputs/authorization RO y evidencia real; macOS signing/notarization/hardware siguen externos.

## 25.1 — `[ 🟡 ] IN PROGRESS`

Windows Auth conserva candidate evidence histórica pero necesita refresh al live baseline si aplica al alpha. Otros journeys aún carecen de evidencia actual completa; iPhone external. No cerrar 25.1 por un solo journey.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`

Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable. #89 todavía contiene el P1 SSRF corrective pendiente; legal audit conserva P0/P1 release blockers. No existe base factual para cerrar 25.2.

**Principio:** exact-head evidence-before-claim; un journey verde no sustituye el resto de 25.1 ni signing/notarization/tester execution.
