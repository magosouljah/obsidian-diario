# Fase 1 — Seguridad, cuentas y datos durables

> GitHub/runtime vivo prevalece. No repetir drills aceptados sin invalidación factual.

**Baseline vivo CYCLE154:** `integration-v0.8.0-alpha.1 @ c4e203cf5e44cf93c0c017c0120f097473fe91b2`.  
**Estado:** D6 `[x] PASS`; D7 `[x] PASS`; D8 `[x] PASS`; D9 `[x] PASS`; D10.1 `[x] PASS`; D10.2 `[x] MAP COMPLETE / ALPHA CANDIDATE NOT READY`.  
**Release público:** 🔴 `NO-GO`.

## D6–D10.1 — CLOSED

Authorization/tenant controls, temp-auth/capabilities, lifecycle/RO decisions, PostgreSQL durability/migrations y restore/recovery permanecen PASS. D10.1 conserva RPO ~7 min, RTO `3643 s` y off-provider encrypted readback/SHA match. No repetir sin invalidación.

## D10.2 — MAP COMPLETE / NOT READY

### PROVEN / delta vivo

- #92/#94/#95/#96 y ahora **#98** están integrados en la línea F2/12.1. #98 exact candidate head `00da0ab...`; Required CI `33575511576` SUCCESS; integration `c4e203cf...`.
- F2/12.1 todavía exige exact runtime/deployment-source close review; owner READ-ONLY CYCLE154 = AAA150.
- Issue #97 sigue OPEN y `Must be addressed before Beta 1`; #98 ya liberó startup/App surfaces. Owner CYCLE154 = WOZ153.
- #89 sigue stale + security gate FAILURE; sin mutation owner, fallback READ-ONLY de WOZ153 únicamente durante espera externa real de #97.
- F2/13.2 durable Review sigue `BLOCKED_WRITE_SURFACE / UNASSIGNED`.
- D8 recent-reauth decision existe; falta seam productiva consumible por destructive callers. Owner = BBB149.
- #93 conserva old-base Windows Auth evidence; refresh solo si 1.7 lo mantiene IN_ALPHA.

### HARD / ACTIVE BLOCKERS hacia apertura real de F5

1. F2/12.1 exact deployment/runtime close review post-#98.
2. Issue #97 near-instant reveal Web+Desktop.
3. F0/0.9 #89 P1 refresh/exact-green/integration.
4. recent-reauth product seam → F2/15.1 durable Trash.
5. F2/13.2 durable Review safe write surface.
6. #93 Windows Auth canonicalization si sigue IN_ALPHA.

### 1.7 — `[ 🟡 ] REQUEUE AFTER FRESH FACTS`

CYCLE154 no emite 1.7 aún: primero 12.1/#97/#89/recent-reauth deben producir facts frescos. Después clasificar `MUST_CLOSE / RO_EXCLUDE_CANDIDATE / RELEASE_ONLY_EXTERNAL` antes de 1.8.

### F3 — aplicabilidad explícita al alpha

- 18.2 real provider/payment: `UNVERIFIED_EXTERNAL`; exclusión de alpha sin cobros requiere decisión explícita 1.7→1.8. BBB149 puede inventariar READ-ONLY solo como fallback durante espera externa de su PRIMARY.
- 19.2 legal implementation/release backlog abierto.
- 20.2 runtime160/capacity no probado; clasificación explícita requerida.

## Orden mínimo hacia 1.8

1. close review F2/12.1 post-#98;
2. cerrar #97 con Web+Desktop evidence;
3. procesar/integrar #89 P1 exact-green;
4. cerrar recent-reauth y luego F2/15.1 o elevar exclusión RO explícita;
5. cerrar F2/13.2 o elevar exclusión RO sustentada;
6. refresh #93 si permanece IN_ALPHA;
7. reemitir 1.7 + aplicabilidad F3.

Solo después corresponde **1.8 — decisión RO final**.
