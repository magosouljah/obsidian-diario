# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo CYCLE 110:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

Authorization/tenant controls, temp-auth/capabilities, lifecycle/RO decisions, PostgreSQL durability/migrations y restore/recovery permanecen PASS. No factual invalidation observada. D10.1 conserva RPO ~7 min, RTO `3643 s` y off-provider encrypted readback/SHA match. **No repetir PITR/restore/cutover/restart/migrations/rotation.**

## D10.2 — `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`

D10.2 es el mapa de readiness para alpha interna 3–5 cuentas. Los blockers pasan a **1.7**; autorización final = **1.8**; ejecución = **1.9**.

### PROVEN

- D6–D10.1 permanecen cerrados.
- Infra Web pública básica tiene health/TLS previo; no sustituye startup autenticado sobre el nuevo deploy.
- #88 = technical/preparatory Authenticode seam only; production signing sigue externo.
- F0/0.20 OAuth secret rotation está `[x]`: #90 readiness integrado + owner-side credential replacement/deploy + fresh OAuth E2E + old credential removal registrados como verificados, sin exponer secretos.
- #91 Web bootstrap corrective está integrado como `134a293...` con exact-head CI PASS; 12.1 aún necesita deploy público + authenticated startup/cold-warm evidence.

### HARD / EXTERNAL BLOCKERS para alpha

1. **F4/25.1 — Windows packaged auth:** literal run `33449587244` = FAILURE; fresh exact-head PASS requerido.
2. **F2/12.1 runtime externo:** código ya integrado; falta desplegar `134a293...` con owner SSH key y probar startup autenticado + cold/warm.
3. **F0/0.9 security P1:** #89 DNS-rebinding/SSRF corrective sigue stale/no integrado; debe revalidarse antes de 1.8.

### CLOSE OR RO-EXCLUDE antes de 1.8

- **F2/13.2 durable Review:** gap probado de completion/no-silent-loss. Owner CYCLE110 = AAA106 para corrective mínimo.
- **F2/15.1 Empty Trash:** recent-reauth + strong confirmation + durable deterministic purge, o exclusión RO explícita.

### F3 — decisión explícita de aplicabilidad al alpha

- **18.2 provider/payment real scenarios:** `UNVERIFIED_EXTERNAL`; excluir si alpha no cobra.
- **19.2 legal implementation/release backlog:** sigue abierto; decidir superficies obligatorias para cuentas internas.
- **20.2 runtime160/capacity:** no probado; release/scale gate, no representativo de 3–5 cuentas.

### Release-only / external tails

Production signing/notarization, hardware matrix amplia, 12–20 testers, public release governance y demás tails continúan `NO-GO`.

## Salida D10.2 → 1.7

**D10.2 queda cerrado como mapa. Estado resultante: `NOT_READY`.**

Orden mínimo actualizado:
1. obtener PASS literal F4/25.1 Windows packaged auth;
2. cerrar F2/13.2 o preparar exclusión RO;
3. refresh/revalidar #89/F0 security P1;
4. desplegar/probar runtime público autenticado de F2/12.1;
5. cerrar F2/15.1 o preparar exclusión RO;
6. clasificar F3 18.2/19.2/20.2 `IN_ALPHA` / `EXCLUDED_FROM_ALPHA`.

Solo después corresponde **1.8 — decisión RO final**. No crear testers, cobrar o ejecutar alpha desde D10.2.
