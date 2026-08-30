# BeatGaler — Equipo multi-IA / coordinación

> GitHub + `!!!PLAN` son memoria compartida. Modelo: ROMPECABEZAS CON OWNER FIJO. GitHub/runtime vivo prevalece.

## Roles y ownership actual — CYCLE 049

| Rol | Owner actual | PRIMARY | CI-FALLBACK |
|---|---|---|---|
| JOBS | coordinación | `!!!PLAN`, prioridades, handoffs, gates; no código/infra | n/a |
| AAA | F3 / 19.2 / SAME #76 | `NIGHT-AAA-045`: sincronizar legal canónico en Settings existentes + fresh CI | F2/13.2 read-only gap map solo mientras #76 espera CI/review/merge |
| BBB | F4 / SAME #72 | `NIGHT-BBB-044`: race-check + integración exact-head green | F4/25.2 read-only readiness inventory solo mientras PRIMARY espera merge/review/queue externo |
| WOZ | F3 / SAME #73 | `NIGHT-WOZ-048`: race-check + integración exact-head green de reconciliation | F3/20.2 harness separado solo mientras PRIMARY espera CI/review/merge |

**Baseline canónico CYCLE 049:** `integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`.

## Handoffs/resultados procesados

- AAA044: no RESULTADO DEL TURNO / handoff observable → `NO_RESULT / SUPERSEDED_BY_JOBS`. El audit F2/13.2 se conserva solo como fallback read-only de AAA045.
- BBB043: no RESULTADO DEL TURNO / handoff observable → `NO_RESULT / SUPERSEDED_BY_JOBS`. #72 sigue OPEN/Ready/mergeable exact-base con evidence verde.
- WOZ047: no RESULTADO DEL TURNO / handoff observable → `NO_RESULT / SUPERSEDED_BY_JOBS`. No `HARNESS_READY` aceptado; 20.2 sigue abierto.
- RO/owner produjo PR #76 y handoff en Issue #41: canonical Privacy/Terms v1 + public `/privacy` `/terms`; SettingsPanel viejo debe reutilizar los documentos canónicos, no crear segunda UI.

## Holding / blocked items

- F2/12.1 cold/warm real: runtime navegador.
- F2/13.1 Web #69 @ `b2ab75ae...`: frozen/unowned por write surface.
- F2/13.1 server #70 @ `5a99ebf2...`: frozen por safe-write + stale baseline.
- F2/13.2: fallback read-only de AAA045 únicamente durante espera externa del primary.
- F4/windows-auth #74 @ `14dfba52...`: candidate green/mergeable pero merge-flow blocker previo; frozen. #71 espera integración real + nueva assignment.
- F4/windows-review #72 @ `904fbf3c...`: exact-base/head green; owner BBB044.
- F3/18.2 #73 @ `fc831172...`: exact-base/head green; owner WOZ048.
- F3/19.2 #76 @ `36d21860...`: legal/public candidate exact-base green; owner AAA045 para Settings canonical reuse.
- F3/20.1 #75 @ `bb493b37...`: corrective conocido, previous write-tool blocker; frozen.
- F3/20.2: harness pasa a fallback de WOZ048; runtime/approved peak siguen abiertos.

## Reglas

1. Trabajo cross-phase solo si dependencias reales lo permiten.
2. Una pieza material = un owner.
3. Owner hace preflight → implementation/audit → tests → CI → handoff.
4. Findings no transfieren ownership automáticamente; JOBS lo hace explícitamente.
5. No hopping automático.
6. Bloqueo real → JOBS reasigna explícitamente.
7. `READY_TO_WORK` ≠ `READY_TO_CLOSE` ≠ `READY_TO_RELEASE`.
8. Ningún `[x]` sin evidencia.
9. REUSE-FIRST + duplicate-check obligatorios.
10. Cambio material de baseline/head → refresh + CI aplicable antes de integración.

## PRIMARY / CI-FALLBACK

- PRIMARY siempre primero.
- CI-FALLBACK solo si JOBS lo preautoriza y PRIMARY entra realmente WAITING_CI/WAITING_EXTERNAL/merge-review-queue equivalente.
- Fallback debe ser independiente en archivos/rama/PR/ownership/dependencias; no ampliar scope ni adelantar gate.
- Worker nunca inventa fallback.
- Tras ejecutar fallback autorizado, worker vuelve a comprobar PRIMARY antes de cerrar turno.

## Night Shift Ledger — CYCLE 049

```text
JOBS: integration remains a9d35a3d69dd9127029fb851d189f9bd3079d03b
AAA044: NO_RESULT -> SUPERSEDED_BY_JOBS
AAA045: ASSIGNED SAME #76 canonical legal Settings reuse
AAA045_FALLBACK: F2/13.2 READ_ONLY only while waiting external CI/review/merge
BBB043: NO_RESULT -> SUPERSEDED_BY_JOBS
BBB044: ASSIGNED SAME #72 exact-head integration transaction
BBB044_FALLBACK: F4/25.2 READ_ONLY only while waiting external merge/review/queue
WOZ047: NO_RESULT -> SUPERSEDED_BY_JOBS
WOZ048: ASSIGNED SAME #73 exact-head integration transaction
WOZ048_FALLBACK: F3/20.2 separate parameterized harness only while waiting external operation
DUPLICATE_WORK: prevented by explicit supersede + unique PR/file ownership
RELEASE: NO-GO
```

## Estado vigente

- F0: técnico habilitado; 1.2/2.2 externos.
- F1: D6–D9 PASS; D10.1 external-only; D10.2 RO.
- F2: 12.1 runtime residual; #69/#70 frozen; 13.2 fallback audit queued.
- F3: 17.1/17.2/18.1 integrated; #73 active WOZ048; #76 active AAA045; #75 frozen; 20.2 fallback harness only.
- F4: windows/import integrated; windows/auth #74 holding; windows/review #72 active BBB044; 25.1/25.2 open.
- JOBS: coordinación/plan; no producto/infra.
