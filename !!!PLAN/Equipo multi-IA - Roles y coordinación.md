# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 102

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, priorities, handoffs, gates; no BeatGaler code/infra | n/a |
| AAA | F2 / 13.2 | `NIGHT-AAA-098`: durable Review Save/Save All boundary + no-silent-loss/Web-no-Tauri evidence; NO MERGE | NONE |
| BBB | F4 / 25.1 | `NIGHT-BBB-097`: #84 first unexpected-request sanitized causal localization; no product mutation; NO MERGE | NONE |
| WOZ | F1 / D10.2 | `NIGHT-WOZ-101`: alpha-readiness decision map READ-ONLY; no alpha/provider/infra mutation | NONE |

**Baseline canónico:** `integration-v0.8.0-alpha.1 @ 816f946c09d998ee5a045b3e70b2fe4f3a4160d0`.

## Handoffs/resultados procesados — CYCLE 102

- AAA097: no final result/handoff/candidate → `NO_RESULT / SUPERSEDED / NOT_PASS`.
- BBB096: no final result/handoff → `NO_RESULT / SUPERSEDED / NOT_PASS`; #84 unchanged and literal Windows Auth remains red.
- WOZ100: `BLOCKED_STOP / PREFLIGHT_COMPLETE / NO_MUTATION`; Issue #41 `5485787222`. #76 remains stale because supported write surface lacks history-preserving branch refresh.
- PR #85 appeared externally owner-owned at exact live base: `owner/web-deploy-powershell-fix @ 5225fae856ac8e5e094bc76f4a70383296fa224b`; one-file deploy-script corrective. Night workers must not claim or mutate it while external ownership is active.
- #83 remains exact OPEN/DRAFT/mergeable with Ready tooling blocker unchanged.
- #79 remains latest material integration merge.

## Serialización

**No worker is authorized to mutate integration in CYCLE 102.** #74/#84 remain BBB auth lineages without merge authority. #76 parked until a supported refresh-capable surface exists. #83 remains PARKED. #85 is external/owner-owned. AAA owns no auth/session/Trash/legal/deploy files.

## Holding / blocked items

- F0 1.2/2.2 external/admin.
- F1 D10.1 CLOSED; D10.2 = WOZ101 READ-ONLY map, RO decision remains authoritative.
- F2/12.1 real-browser runtime needs executable browser surface.
- F2/13.1 #69/#70 frozen except helper-level reuse explicit in AAA098.
- F2/13.2 = AAA098.
- F2/14.1 #81 stale/parked.
- F2/15.1 strong confirmation + recent-reauth + deterministic purge gaps; paused while BBB097 owns auth boundary.
- F3/18.2 provider/payment live/staging proof external.
- F3/19.1 owner-owned #85 may reduce deployment blocker; workers do not collide with it.
- F3/19.2 #76 blocked on refresh-capable execution surface; external legal review/deployment separate.
- F3/20.2 #83 Ready process blocked; runtime 160 required after integration.
- F4/25.1 #74/#84 = BBB097 diagnostic-only; no product corrective without subsequent JOBS authorization.
- F4 signing/notarization/hardware/tester execution external.

## Reglas

1. One material piece = one owner.
2. REUSE-FIRST + duplicate-check mandatory.
3. Evidence-before-claim; no `[x]` without literal evidence.
4. Material base/head change => history-preserving refresh + exact-head CI before integration.
5. PRIMARY first; CI-FALLBACK only if explicitly preauthorized and PRIMARY genuinely waits externally.
6. Worker never invents fallback/next task.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.

## Night Shift Ledger — CYCLE 102

```text
JOBS: baseline-start 816f946c09d998ee5a045b3e70b2fe4f3a4160d0
AAA097: NO_RESULT -> SUPERSEDED / NOT_PASS
AAA098: ASSIGNED F2/13.2 durable Review boundary; FALLBACK NONE
BBB096: NO_RESULT -> SUPERSEDED / NOT_PASS
BBB097: ASSIGNED #84 sanitized first-request diagnostic; FALLBACK NONE
WOZ100: BLOCKED_STOP / NO_MUTATION / #76 refresh tooling unavailable
WOZ101: ASSIGNED F1/D10.2 READ-ONLY decision map; FALLBACK NONE
PR85: EXTERNAL_OWNER_ACTIVE / DO_NOT_COLLIDE
INTEGRATION_MUTATION: NONE
RELEASE: NO-GO
F5: CLOSED
```
