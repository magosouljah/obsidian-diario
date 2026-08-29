# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-009`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — matrix/runner dependency-safe REUSE-FIRST`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`
- `PREVIOUS_RESULT: NIGHT-BBB-008 DONE; PR #57 merged as f73c9ee...; 24.2 técnicamente cerrado.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F4 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. 24.2 ya está cerrado. No reabras #57 ni repitas CI aceptado.
3. Usa el audit REUSE-FIRST del turno 008 como input: ya existen harnesses para auth/import/Review/playback/edit/Trash/offline/downloads y updater recovery/static portability; no los reconstruyas.
4. Duplicate-check de PR/rama/candidate existente para 25.1.
5. Construye únicamente un **matrix/runner dependency-safe** que componga evidencia/harnesses existentes y produzca por requisito un estado explícito: `AUTOMATED_PASS`, `PENDING_EXTERNAL`, `PRODUCT_FINDING` o `NOT_COVERED`, con evidencia concreta.
6. El runner/matriz debe cubrir nominalmente Web browsers/iPhone + Windows/macOS y auth/import/Review/playback/edit/Trash/offline/YouTube/updater/billing, pero NO puede inventar PASS donde no haya ejecución real.
7. Añade solo gaps pequeños claramente F4-matrix-only. No cambies lógica de producto F2/F3 para hacer pasar la matriz. Findings de producto vuelven a JOBS.
8. iPhone/hardware/credenciales/signing/notarization se separan como external si no pueden ejecutarse. No crear certificados, no release, no stable/latest, no 25.2.
9. Si hay delta real, usa un único candidate con tests propios + CI exact-head aplicable. Si todo puede resolverse por artefactos existentes, reporta REUSED y evita PR ceremonial.
10. Actualiza solo este markdown con resultado de `NIGHT-BBB-009` y STOP.

### Fuera de scope

D22/D23 signing/notarization reales; F2/F3 product fixes; 25.2 freeze; release público; cualquier `!!!PLAN` salvo este markdown.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-008`  
`TURN_STATUS: DONE`  
`PR: #57 MERGED`  
`MERGE_SHA: f73c9ee8d058df3c780170c8c2a3fabef975c54d`  
`CI: Test - Desktop Portability/Required CI 33255401498 SUCCESS; D6 33255401544 SUCCESS; D7 33255401512 SUCCESS.`  
`AUDIT_25_1: cobertura reutilizable amplia; gaps explícitos en full Web journeys, full cross-OS journeys, iPhone runner, YouTube journey y billing journey.`

## HISTORIAL

- `NIGHT-BBB-009`: ASSIGNED.
- `NIGHT-BBB-008`: DONE — #57 merge `f73c9ee...`; 25.1 audit REUSE-FIRST.
- `NIGHT-BBB-007`: PENDING; luego CI verde.
- `NIGHT-BBB-006`: PENDING — #57 candidate.
- `NIGHT-BBB-005`: DONE — PR #55 merge `672e133...`.
- `NIGHT-BBB-003`: DONE — #51 merge `5b05ca845...`.
