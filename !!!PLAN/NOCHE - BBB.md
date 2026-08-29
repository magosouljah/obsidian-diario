# NOCHE — BBB

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** BBB — worker nocturno.  
**Área:** F4 — Desktop / packaging / release chain.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-BBB-012`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F4 / 25.1 — integrate SAME PR #60`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 58a6bf61441f08bf68aa63673c0d5f2994b220d9`
- `REUSE_PR: #60 / bbb/task-25.1-functional-matrix`
- `KNOWN_CANDIDATE_HEAD: 945638c8bb650b0ce0bbe569e48a791a93d80e39`
- `JOBS_PRECHECK: exact-head F4 matrix 33265800007 SUCCESS; D6 33265800004 SUCCESS; D7 33265800022 SUCCESS; Test - Desktop Portability 33265800008 SUCCESS; Upgrade 21.2 Staging skipped/no aplicable.`

### Orden JOBS

1. Preflight factual y race-check contra GitHub vivo; REUSE-FIRST exclusivamente SAME #60.
2. Si integration sigue exactamente `58a6bf614...` y head sigue `945638c8...`, consume el CI exact-head ya verde y haz merge protegido con expected-head.
3. Si AAA movió integration antes, refresca la MISMA #60 sobre el nuevo baseline, preserva solo los 3 paths F4 y exige CI nuevo para la combinación material nueva.
4. Tras merge, verifica merge SHA e integration reread. Integrar el artifact no convierte `NOT_COVERED`/`PENDING_EXTERNAL` en PASS funcional.
5. No auto-iniciar 25.2, signing, notarization, release ni fixes F2/F3 en 012.
6. Handoff en este markdown + Issue #41 y STOP.

## RESULTADO DEL TURNO ANTERIOR

`LAST_PROCESSED_ASSIGNMENT: NIGHT-BBB-011`  
`TURN_STATUS: PENDING`  
`RESULT: tras merge #58, SAME #60 fue refrescada sobre 58a6bf614... a head 945638c8bb650b0ce0bbe569e48a791a93d80e39. El turno terminó con CI en curso; GitHub posterior confirma todos los gates aplicables SUCCESS.`  
`EVIDENCE_NEW_BY_JOBS: runs 33265800007/00004/00022/00008 = SUCCESS; #60 OPEN/Ready/mergeable; no merge todavía.`

## HISTORIAL

- `NIGHT-BBB-012`: ASSIGNED — race-check + integración SAME #60 si baseline/head siguen válidos.
- `NIGHT-BBB-011`: PENDING — #60 refreshed a `945638c...`; CI luego verde.
- `NIGHT-BBB-010`: PENDING — #60 repaired/refreshed.
- `NIGHT-BBB-009`: PENDING — candidate con failure/stale base.
- `NIGHT-BBB-008`: DONE — #57 merge `f73c9ee...`; 24.2 closed.
- `NIGHT-BBB-006`: PENDING — #57 candidate.
- `NIGHT-BBB-005`: DONE — PR #55 merge `672e133...`.
- `NIGHT-BBB-003`: DONE — #51 merge `5b05ca845...`.
