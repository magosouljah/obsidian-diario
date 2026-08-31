# Fase 4 — Artefactos desktop confiables y release chain

> GitHub/runtime vivo prevalece. Trabajo F4 puede avanzar en paralelo si respeta dependencias y gates reales.

**Integración estable CYCLE 103:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Estado actual

- 21.1 / 21.2 `[x]`.
- 24.1 / 24.2 `[x]`.
- 25.1 `[ 🟡 ]`.
- #79 / F4 25.2 readiness docs integrado como `816f946c...`; no demuestra tester execution, signing/notarization ni cierre global 25.2.

### windows/auth

- #71 conserva fail-before histórico.
- #74 única product-corrective lineage: `d1593d368e1015abb6a25bf98e5fa8586664ac95`, OPEN/Ready/mergeable, base exact live. No product mutation autorizada en CYCLE 103.
- #84 única evidence lineage: `f53d46f39ece94f6de74f2f21a508ce01497ac41`, OPEN/Ready, base exact live.
- `NIGHT-BBB-097` añadió únicamente diagnóstico sanitizado del primer unexpected request (`{method, pathname/requestClass}`; sin query/body/headers/credentials/token), preservando las assertions literales.
- Exact #84 Windows Auth Journey `33449587244` / job `99676242317` @ `f53d46f...` = **FAILURE** en `Run isolated Windows auth assertions`.
- En el mismo exact head: Windows Import, Desktop Portability, Web Production Build, D6 y D7 = SUCCESS; esos verdes no sustituyen el journey auth literal rojo.
- BBB097 terminó `WAITING_CI`; GitHub posterior resolvió la espera como FAILURE, por lo que F4/25.1 sigue `NOT_PASS`.

**Owner CYCLE 103: `NIGHT-BBB-098`.** Debe recuperar el primer tuple sanitizado del run/job exacto y clasificar `HARNESS_ONLY_PROVEN / PRODUCT_SIDE_PROVEN / SERVICE_BOUNDARY_PROVEN / AMBIGUOUS`. Solo `HARNESS_ONLY_PROVEN` autoriza la mínima corrección de harness #84 + nueva ejecución con assertions intactas. Cualquier product/service/ambiguous ⇒ STOP y nueva autorización JOBS. **NO PRODUCT MUTATION / NO MERGE.** CI-FALLBACK NONE.

### windows/review

#72 sigue OPEN/stale/frozen; no pertenece a BBB098. El durable Review gap F2/13.2 permanece separado y sin owner CYCLE 103 mientras AAA prioriza el public Web startup blocker.

## Día 22 / 23

Signing Windows, SmartScreen/AV/hardware, Apple Developer, certificados/notarization/stapling/hardware siguen externos/abiertos. Owner decidió no pagar Apple Developer/certificados ahora; no describir builds como signed/notarized sin evidencia.

## Día 25

### 25.1 — `[ 🟡 ] IN PROGRESS`

Integrated rows conocidas: `windows/import`, `windows/updater`, `macos/updater` automated evidence. `windows/auth` sigue roja sobre exact #84; múltiples journeys continúan sin evidencia actual completa; iPhone external.

### 25.2 — `[ 🟡 ] READINESS ARTIFACT INTEGRATED / GLOBAL OPEN`

#79 docs-only readiness artifact integrado. Gate real requiere beta/tester execution, 0 P0, ningún P1 core conocido y release-chain evidence aplicable.

**Principio:** exact-head evidence-before-claim; CI genérico no sustituye el journey literal rojo.
