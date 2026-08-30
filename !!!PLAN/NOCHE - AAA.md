# NOCHE — AAA

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** AAA — worker nocturno.  
**Área:** Desktop product-auth corrective.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-AAA-038`
- `ASSIGNMENT_STATUS: WAITING_CI`
- `AREA: F4 blocker / Desktop product-auth — token/session persistence`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b`
- `INPUT_EVIDENCE: PR #71 / BBB034 product finding — Desktop login no persistió beatgaler:account-session:v1`
- `PREDECESSOR: NIGHT-AAA-037 NOT_PROCESSED / SUPERSEDED_BY_JOBS — no resultado/handoff observable al CYCLE 040; no ejecutar 037 después de recibir 038.`

### PRIMARY

1. Preflight GitHub vivo + duplicate-check; integration debe reconciliarse antes de mutar.
2. REUSE-FIRST: tomar el PRODUCT_FINDING de #71 y demostrar causa raíz en código productivo auth/frontend/platform y contrato `AccountGate.storeSession()`.
3. No tocar PR/branch/files de #71; queda como regression proof F4.
4. Solo con causa raíz demostrada, aplicar corrective mínimo en una rama/PR AAA nueva desde baseline vivo. Sin refactor amplio ni cambio de contrato auth/security.
5. Evidencia obligatoria: fail-before/pass-after o equivalente literal; sesión/token persistido tras login Desktop; no regresión Web/AccountGate; fresh applicable exact-head CI.
6. Si integra, handoff para devolver #71 a BBB mediante asignación JOBS posterior; no promover matrix desde AAA.
7. No tocar #69/#70, Review/#72, F3, signing/notarization, infra/provider secrets ni otras filas 25.1.
8. Escribir RESULTADO DEL TURNO aquí + handoff Issue #41 y STOP.

**STOP:** finding no reproducible; causa raíz no demostrable; cambio de contrato/seguridad no autorizado; scope creep; baseline race; CI rojo no atribuible.

### CI-FALLBACK

`NONE`

**Alcance:** N/A.  
**Evidencia requerida:** N/A.  
**STOP:** no inventar fallback.

## RESULTADO DEL TURNO — NIGHT-AAA-038

### PRIMARY

- `STATUS: WAITING_CI`
- `baseline: integration-v0.8.0-alpha.1 @ a9d35a3d69dd9127029fb851d189f9bd3079d03b` — revalidado sin race al cierre.
- `branch/head: aaa/night-25.1-auth-session-corrective @ 92058b42e6e455f641e8a494f5c85ae1f2214834`
- `PR: #74 — fix(auth): preserve Desktop session in packaged Tauri runtime`
- `cambios:` corrective mínimo en `src/platform/index.ts`: detección Desktop mantiene `__TAURI_INTERNALS__` como señal primaria y añade únicamente origins productivos Tauri (`tauri:` / `tauri.localhost`) como fallback cuando los internals todavía no son observables al inicializar frontend. Regresión enfocada nueva en `tests/component-dom/platformRuntime.test.ts`. No se tocaron branch/files/workflow de #71 ni matrix.
- `tests:` fail-before literal reutilizado de #71: Windows Auth run `33313675968`, job `99263095638`, alcanzó WebDriver real y falló `Desktop login did not persist the returned session token.` Pass-after local-equivalent añadido: runtime Tauri por internals, `http://tauri.localhost`, `tauri://localhost`, y no-clasificación Desktop para localhost/web ordinario. Ejecución de esta regresión queda bajo CI exact-head de #74.
- `CI:` recheck único posterior a entrar en espera externa: head exacto `92058b42...`; `Test - Desktop Portability` run `33321752522` QUEUED; `D6 - Cross-Process Authorization` run `33321752555` IN_PROGRESS; `D7 - Direct Capability Authorization` run `33321752537` QUEUED; `Upgrade 21.2 Staging` run `33321752540` SKIPPED. No se afirma PASS.
- `evidencia:` `AccountGate.storeSession()` escribe `beatgaler:account-session:v1` solamente bajo `platform.kind === desktop`; selección de plataforma previa dependía exclusivamente de `window.__TAURI_INTERNALS__`. #71 demostró literalmente ausencia del token dentro de app Tauri/WebView2 real. Tauri v2 usa `http://tauri.localhost` como origin productivo Windows; el corrective usa esa señal estable sin convertir localhost/dev normal en Desktop. PR #74 fue creado sobre base exacta asignada; 2 files, +42/-2 al abrir.
- `UNVERIFIED:` CI final de #74; PASS literal del mismo Windows auth journey después del corrective; integración de #74; promoción `windows/auth`.
- `blockers:` espera externa verificable de CI. Después de integración verde, #71 debe volver a BBB solo mediante nueva asignación JOBS para revalidación literal; AAA no promueve matrix.

### CI-FALLBACK

- `STATUS: NOT_RUN / NONE`
- `branch/head si aplica: N/A`
- `PR si aplica: N/A`
- `cambios: none`
- `tests: none`
- `evidencia: JOBS escribió CI-FALLBACK = NONE para NIGHT-AAA-038.`
- `UNVERIFIED: none adicional`
- `blockers: fallback no autorizado.`
- `STOP alcanzado: sí — no inventar fallback.`

### RECOMENDACIÓN PARA JOBS

Procesar `NIGHT-AAA-038` como `WAITING_CI` sobre PR #74. No reasignar #71 todavía. Cuando #74 tenga fresh exact-head CI verde y sea integrado por autoridad correspondiente, devolver `windows/auth` / SAME #71 a BBB mediante una nueva asignación para ejecutar la prueba literal y promover matrix solo con PASS verificable.

## RESULTADO PROCESADO — NIGHT-AAA-037

- `STATUS: NOT_PROCESSED / SUPERSEDED_BY_JOBS`.
- No RESULTADO DEL TURNO ni handoff observable en ledger/Issue #41 al preflight CYCLE 040.
- La misión sigue siendo críticamente válida por el PRODUCT_FINDING de #71 y se reemite como AAA038 sobre el mismo baseline vivo.

## HOLDING

- F2/12.1 cold/warm real: runtime navegador ejecutable faltante.
- F2/13.1 Web #69: coordinator probado; wiring/refresh pendientes y candidate stale.
- F2/13.1 server #70: frozen por safe-write + stale baseline.

## HISTORIAL COMPACTO

- `NIGHT-AAA-038`: WAITING_CI — #74 product-auth runtime/session corrective @ `92058b42...`; fallback NONE.
- `NIGHT-AAA-037`: NOT_PROCESSED / SUPERSEDED_BY_JOBS.
- `NIGHT-AAA-036`: NOT_PROCESSED / SUPERSEDED_BY_JOBS por baseline movement.
- `NIGHT-AAA-032`: PENDING / STOP_RUNTIME_UNAVAILABLE.
- `NIGHT-AAA-031`: PENDING / STOP_WRITE_SURFACE.
- `NIGHT-AAA-027`: #69 created.
