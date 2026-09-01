# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 104:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- #79 / 25.2 readiness docs integrado como `816f946c...`; no demuestra tester execution, signing/notarization ni cierre global 25.2.

## windows/auth — `[ 🟡 ] NOT_PASS`

- #71 conserva fail-before histórico.
- #74 única product-corrective lineage, OPEN/Ready/mergeable, exact live base. Product mutation no autorizada CYCLE 104.
- #84 única evidence lineage: OPEN/Ready/mergeable @ `f53d46f39ece94f6de74f2f21a508ce01497ac41`, exact live base.
- Exact Windows Auth Journey `33449587244` / job `99676242317` = **FAILURE** en isolated auth assertions. Otros exact-head checks verdes no sustituyen el journey literal.
- `NIGHT-BBB-098` no dejó final result/handoff al preflight CYCLE 104; `SUPERSEDED / NOT_PASS`.

**Owner CYCLE 104: `NIGHT-BBB-099`.** Debe obtener el primer tuple sanitizado `{method, pathname/requestClass}`. Si el output exacto no lo contiene, se permite una sola modificación diagnostic-only mínima en #84 que emita únicamente ese tuple y rerun, preservando assertions. Clasificar `HARNESS_ONLY_PROVEN / PRODUCT_SIDE_PROVEN / SERVICE_BOUNDARY_PROVEN / AMBIGUOUS`. Solo HARNESS_ONLY autoriza mínimo harness correction; product/service/ambiguous => STOP. **NO PRODUCT MUTATION / NO MERGE.** CI-FALLBACK NONE.

## windows/review
#72 sigue OPEN/stale/frozen. Durable Review product gap pertenece F2/13.2 y no se mezcla con BBB099.

## Día 22 / 23
Signing Windows, SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware siguen externos/abiertos. No describir builds como signed/notarized sin evidencia.

## 25.1 — `[ 🟡 ] IN PROGRESS`
Integrated rows conocidas incluyen windows/import, windows/updater y macos/updater automated evidence. windows/auth continúa rojo y otros journeys carecen de evidencia actual completa; iPhone external.

## 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`
#79 docs-only readiness artifact integrado. Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable.

**Principio:** exact-head evidence-before-claim; CI genérico no sustituye journey literal.
