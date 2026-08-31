# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar BeatGaler lo más rápido posible sin rebajar gates reales.

## Reglas de autoridad

- GitHub/runtime vivo prevalece sobre snapshots viejos.
- `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
- Evidence-before-claim, REUSE-FIRST, duplicate-check y exact-head son obligatorios.
- Cada pieza material tiene un solo owner.
- JOBS dirige/sincroniza; no modifica código BeatGaler ni infraestructura.
- No se marca `[x]` sin evidencia verificable.
- `Plan Maestro 2208 copy DONT TOUCH .md` permanece protegido.

## Estado vivo — NIGHT-JOBS-103

- **Release público:** 🔴 `NO-GO`.
- **Integración estable:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.
- **Último merge material:** #79 → `816f946c...`.
- **F0:** núcleo técnico interno cerrado; 1.2/2.2 conservan tails externos/administrativos. Eligibility v1 canónica: **18+**.
- **F1:** D6–D10.1 PASS. D10.2 sigue `[ 🟡 ] RO / ALPHA DECISION`; `NIGHT-WOZ-102` refresca mapa READ-ONLY con blockers vivos.
- **F2:** 11.1/11.2/12.2 cerrados. Nuevo blocker productivo: owner Issue #41 `5485984669` demuestra infra Web pública funcional pero apex detenido en `Loading Galer`; `NIGHT-AAA-099` toma el bootstrap/runtime Web. 13.1 frozen; 13.2 durable Review gap sigue abierto pero sin owner CYCLE 103; 14.1 parked; 15.1 recent-reauth/confirmation/action boundary abierto.
- **F3:** 17.1/17.2/18.1 cerrados; 18.2 provider/payment external. 19.1 public infrastructure principal ahora probada por owner runtime; legal/public-route/support/OAuth tails siguen parciales. PR #85 externo/owner-owned permanece OPEN. #76 stale/13+ sigue bloqueado por refresh-capable surface. #83 OPEN/DRAFT/tooling-blocked; runtime 160 UNVERIFIED.
- **F4:** 21.1/21.2/24.1/24.2 cerrados; 25.1 incompleto. #84 avanzó a exact `f53d46f...`; Windows Auth run `33449587244` / job `99676242317` terminó FAILURE. `NIGHT-BBB-098` consume el tuple sanitizado y solo corrige harness si causalmente probado.
- **5.1:** `[x]`. **5.2:** `[x]`.
- **F5:** `NO ABRIR`.

## RESULTADOS PROCESADOS — CYCLE 103

- `NIGHT-AAA-098`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no final result, matching Issue #41 handoff ni candidate material.
- `NIGHT-BBB-097`: Issue #41 `5486012736` cerró turno `WAITING_CI` en #84 `f53d46f...`. GitHub post-turn resolvió la espera: exact Windows Auth `33449587244` / `99676242317` = FAILURE. Otros checks exact-head verdes no sustituyen auth literal. Resultado procesado = `NOT_PASS`.
- `NIGHT-WOZ-101`: `NO_RESULT / SUPERSEDED / NOT_PASS`; no matching final handoff observado.
- Owner Issue #41 `5485984669`: web-health ok, auth-health reachable, www→apex y TLS reissued; deployment/public infra no se reabre por el nuevo `Loading Galer`.
- PR #85 live head verificado `ab25e89570de66189612c7a4677161a73bbe5d5d`, OPEN/Ready, exact live base, external owner. No worker lo toca.
- No BeatGaler merge ni integration mutation en este ciclo.

## OWNERS — CYCLE 103

### AAA — `NIGHT-AAA-099` — F2 / 12.1
PRIMARY: reproducir `Loading Galer`, aislar primer bootstrap phase no resuelto y hacer mínimo corrective Web-only con termination semantics, focused tests, Web/no-Tauri proof y exact-head CI; **NO MERGE**. Shared auth/session/backend/provider/deploy ⇒ STOP.  
CI-FALLBACK: NONE.

### BBB — `NIGHT-BBB-098` — F4 / 25.1
PRIMARY: consumir exact failed #84 diagnostic, recuperar primer tuple sanitizado `{method, pathname/requestClass}`, clasificar causa; mínimo harness fix solo si `HARNESS_ONLY_PROVEN`, literal assertions intactas + fresh packaged auth; product/service/ambiguous ⇒ STOP. **NO PRODUCT MUTATION / NO MERGE**.  
CI-FALLBACK: NONE.

### WOZ — `NIGHT-WOZ-102` — F1 / D10.2
PRIMARY: mapa READ-ONLY de readiness alpha interna 3–5 cuentas actualizado con `Loading Galer` y Windows Auth rojo; no lanzar alpha ni mutar infra/provider.  
CI-FALLBACK: NONE.

**Integration mutation authorization CYCLE 103: NONE.**

## Camino crítico global — recalculado CYCLE 103

1. **F2/12.1 public Web startup:** `Loading Galer` debe terminar correctamente; hoy bloquea uso normal de testers y la evidencia browser real.
2. **F4/25.1 windows/auth:** consumir sanitized tuple → causalidad harness/service/product → literal packaged PASS requerido.
3. **F2/13.2 Review:** durable Save/Save All completion/no-silent-loss + executable Web/no-Tauri evidence.
4. **F3/19.2 legal/public:** #76 requiere history-preserving refresh surface → 18+ + canonical Settings/public copy → exact-head evidence; public legal routes/fallback aún necesarios.
5. **F2/15.1 Empty Trash:** recent-reauth seam + strong confirmation + deterministic purge.
6. **F3/20.2:** #83 supported Ready tooling debe cambiar materialmente; luego runtime 160 + latency/error/queue/recovery/no-loss/no-cross-tenant + safety margin.
7. **F3/18.2:** provider/staging/payment scenarios reales.
8. **F1/D10.2:** readiness map + RO decision solo cuando technical prerequisites aplicables estén verdes.
9. **F0/F3/F4 external tails:** GitHub historical support/admin, support/mail/OAuth/legal review, signing/notarization/hardware/tester execution.

## Invariantes

- UI: Cloud / Galer Cloud / Storage / Library; implementation internals ocultos.
- Schema: **Galer T-Library Schema v2**.
- Web pure: no Tauri/Desktop helper.
- Media: device ↔ provider direct; Galer Cloud no relaya beat/project payloads.
- Permanent auth/control secrets permanecen control-side; clients usan temporary auth.
- Shared-bot fallback solo cuando no hay bot libre; exclusivity per vault normal.
- v1 no se publica free-only; eligibility v1 = **18+**.
- YouTube existe Desktop/Web; Web no llama Tauri.

## NEXT

AAA ejecuta `NIGHT-AAA-099`; BBB `NIGHT-BBB-098`; WOZ `NIGHT-WOZ-102`. Nadie puede mutar integration. No tocar PR #85 mientras siga owner-owned activo. No retry #76 con la misma superficie incapaz de refresh. No retry #83 sin material supported-tooling change. F5 sigue CLOSED / NO-GO. `PLAN_HEALTH`: synced CYCLE 103; GitHub live prevalece si cambia después.
