# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción/operación software-only.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-032`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.1 — observability / alerts / runbook / kill-switch REUSE-FIRST gap map`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `HOLDING_ITEM_1: F2 / 13.1 / PR #70 frozen exactly @ 5a99ebf2c54a9c0aaae7f20b2262160e55ca6ae7 after NIGHT-WOZ-031 SAFE_WRITE_TOOLING_LIMIT; do NOT touch/retry it.`
- `HOLDING_ITEM_2: F3 / 18.1 / PR #68 remains frozen @ 2a988ec2...; do NOT touch/retry it.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check. No toques #68 ni #70 y no reutilices sus ramas/PRs.
2. Lee F3/20.1 literalmente y aplica REUSE-FIRST sobre evidencia/artefactos ya integrados: 5.2 observabilidad/alarms/on-call, #59 health/readiness, #61 promotion/rollback y cualquier log/metric/alert/runbook/kill-switch existente en el repo.
3. Construye un mapa compacto `requisito -> evidencia exacta -> cobertura -> gap` para: logs/métricas/tracing/error reporting/retention; alerts auth/API/DB/billing/provider/pool/queue/backup/release; on-call/runbook/status/kill switches.
4. No marques un requisito cubierto solo por naming parecido; exige evidencia literal y ejecutable/documentada aplicable.
5. Si el audit demuestra que una parte de 20.1 ya está satisfecha por artefactos existentes, reporta exactamente cuál, con paths/SHAs/tests/CI/runtime aplicable. No cierres 20.1 completo salvo cobertura literal total.
6. Si aparece un **único gap pequeño, independiente, software-only y safely writable**, puedes crear UNA rama/PR nueva exclusivamente para ese gap. Prefiere archivo/harness/test pequeño y aislado; no reemplaces archivos largos truncados ni hagas full-file rewrite inseguro.
7. Si hace falta provider real, dashboards externos, secretos, recursos pagados, DNS/status vendor, infraestructura o decisión RO, registra `PENDING_EXTERNAL` y no lo falsees.
8. Evidencia requerida si hay cambio: branch/head, changed-file scope, focused tests y fresh applicable exact-head CI. Si no hay cambio: paths/SHAs/evidencia REUSE-FIRST y gap map verificable.
9. Publica handoff en Issue #41, actualiza RESULTADO DEL TURNO aquí y STOP.

**STOP:** necesidad de tocar #68/#70/F2/Desktop packaging, full-file destructive write, provider/cost/secret action, scope creep, baseline race o CI rojo no atribuible.

### CI-FALLBACK

`NONE`

Reason: el PRIMARY ya es trabajo independiente y read/audit-first; no se autoriza otro carril.

## RESULTADO PROCESADO — NIGHT-WOZ-031

### PRIMARY
- `Assignment ID: NIGHT-WOZ-031`
- `STATUS: BLOCKED / SAFE_WRITE_TOOLING_LIMIT`
- `baseline: integration-v0.8.0-alpha.1 @ 3ad8f55a9efe907eddbefb7c99d62d0cbdca87af`
- `branch/head: woz/night-13.1-orphan-lifecycle @ 5a99ebf2c54a9c0aaae7f20b2262160e55ca6ae7`
- `PR: #70 OPEN; no merge attempted`
- `cambios: corrective exacto identificado en postgres-live.integration.cjs. El writer disponible reemplaza archivo completo; un intento no seguro produjo commit 588f3895 con contenido truncado y fue revertido inmediatamente moviendo la rama exactamente al head previo 5a99ebf2. Estado final del PR restaurado sin ese cambio.`
- `tests: no fresh tests; no claim PASS`
- `CI: live recheck posterior sobre 5a99ebf2 mantiene Required CI FAILURE y PostgreSQL live/recovery FAILURE; no corrective aplicado.`
- `evidencia: fixture original confirmado: processGarbageBatch para gc-retry-live/orphan_upload carece isObjectStillOrphan; baseline vivo sigue 3ad8f55a...; branch restaurada a 5a99ebf2...`
- `UNVERIFIED: corrective no aplicado; merge no ejecutado`
- `blockers: herramienta de escritura disponible exige reemplazo completo de un archivo largo y no ofrece patch quirúrgico seguro; no repetir escritura destructiva`
- `condición de STOP alcanzada: no existe forma segura disponible en ese turno de aplicar únicamente el fixture autorizado sin riesgo de truncar el archivo`
- `recomendación para JOBS: mantener SAME #70/head frozen hasta disponer de patch/edit seguro.`

### CI-FALLBACK
- `STATUS: NOT_RUN`
- `CI-FALLBACK: NONE`

## HOLDING

- F2/13.1 / #70 @ `5a99ebf2...` — frozen por safe-write tooling; no tocar en 032.
- F3/18.1 / #68 @ `2a988ec2...` — frozen por merge execution blocker; no tocar en 032.

## HISTORIAL COMPACTO

- `NIGHT-WOZ-032`: ASSIGNED — F3/20.1 observability gap map.
- `NIGHT-WOZ-031`: BLOCKED / SAFE_WRITE_TOOLING_LIMIT; #70 restaurado exactamente a 5a99ebf2.
- `NIGHT-WOZ-030`: NO_RESULT / SUPERSEDED_BY_JOBS.
- `NIGHT-WOZ-029`: PENDING / attributed corrective.
- `NIGHT-WOZ-027`: focused F2 SUCCESS; Required CI PG fixture failure.
- `NIGHT-WOZ-025`: #68 exact-head green but merge execution blocked.
- `NIGHT-WOZ-021`: #67 merged `3ad8f55a...`.
