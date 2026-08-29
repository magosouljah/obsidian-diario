# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Reducir el mayor bloque técnico restante de F0–F4 con REUSE-FIRST y evidencia real, sin inventar infraestructura/costo ni invadir F2/F4. Un turno = una asignación JOBS. WOZ no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-007`
- `ASSIGNMENT_STATUS: PENDING_EXTERNAL`
- `AREA: F3 / 16.1 — entornos / runtime-operability dependency-safe slice`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`
- `CONTEXT: NIGHT-WOZ-006 integró PR #56. D10.1 quedó exclusivamente PENDING_EXTERNAL_PROOF por copia real fuera del primary provider/account failure domain; no queda trabajo técnico interno útil en ese lane hasta acción externa RO. JOBS reasigna WOZ explícitamente a F3/16.1.`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F3 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. REUSE-FIRST: audita primero los assets/runtime/deploy/config existentes para prod/staging, health/readiness/dependency checks, graceful shutdown, timeouts y proxy trust. No asumas que F3 parte de cero.
3. Ejecuta únicamente el slice dependency-safe de 16.1 que pueda demostrarse sin nuevas credenciales/costo:
   - separar/validar contractualmente staging vs producción donde ya exista soporte;
   - health/readiness/dependency checks fail-closed;
   - graceful shutdown, timeouts y proxy trust seguros/reproducibles;
   - documentar el gap exacto de recursos/secretos/callbacks separados si requiere acción externa.
4. No crees una segunda RDS, nueva infraestructura pagada, cuentas/provider projects, buckets o recursos con costo sin autorización RO explícita. No cambies DNS/Stripe/legal.
5. Duplicate-check antes de rama/PR. Si código/config necesita cambio, usa un único candidate mínimo y CI exact-head. Si todo lo dependency-safe ya existe, entrega evidencia REUSED en vez de reimplementarlo.
6. Si staging real separado requiere credenciales/decisión externa, reduce el blocker a una acción literal y no lo declares PASS. La ausencia de staging productivo no impide cerrar subrequisitos puramente software si están demostrados.
7. No volver a D10.1 ni repetir restore/cutover/restart/migrations/rotation. No tocar F2/F4.
8. Actualiza solo este markdown + Issue #41 con evidencia y STOP.

### Fuera de scope

F1/D10.1 off-provider copy; D10.2; F2; F4; Stripe 17.x; legal/DNS 19.x; capacidad 20.2 salvo inspección de dependencias; nueva infraestructura/costo; release público; cualquier `!!!PLAN` salvo este markdown.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-007`  
`TURN_STATUS: PENDING_EXTERNAL`  
`GATE: F3 / 16.1 — dependency-safe runtime slice READY_FOR_REVIEW; physical environment separation PENDING_EXTERNAL.`  
`BASE_BEFORE: integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`  
`BRANCH_HEAD: woz/night-16.1-runtime-operability @ 292a7706bc4f6c21eccc60f2838cda0cd8ed4adc`  
`PR: #59 OPEN / mergeable; base exact f0d65aa66988e3e1a026e237b65c65a56b098aa9; 4 changed files.`  
`CHANGES: añadido contrato dependency-safe F3/16.1: /healthz; /readyz con PostgreSQL SELECT 1 y fail-closed si DB requerida falta/no responde; estado draining; trust proxy explícito y acotado; request/header/keepalive/socket/dependency timeouts; graceful SIGINT/SIGTERM HTTP drain; BEATGALER_DEPLOYMENT_ENV obligatorio como staging|production cuando NODE_ENV=production; knobs documentados en .env.example. Se reutiliza bootstrap/shutdown PostgreSQL y el patrón existente de installers Express; no se toca server-core monolítico ni se crean recursos/provider/costo.`  
`TESTS: PASS_LOCAL_UNIT — node:test 7/7 para contrato de entorno, proxy trust, readiness missing/SELECT 1, timeouts, graceful drain e integración del patch Express. Intento de clone/full-repo self-test no ejecutable por DNS del runtime; no se falsea evidencia.`  
`CI: UNVERIFIED/NO_RUN para head 292a7706bc4f6c21eccc60f2838cda0cd8ed4adc — GitHub reportó workflow_runs=[] y combined statuses=[] al cierre; no se lanzó CI costoso artificialmente.`  
`EVIDENCE_REUSED: /auth/health existente; timeouts puntuales de dependencias; postgres-bootstrap con pool+migrations y cierre pool en SIGINT/SIGTERM; patrón Express prototype installers ya integrado; baseline estable f0d65aa66988e3e1a026e237b65c65a56b098aa9.`  
`EVIDENCE_NEW: PR #59; head exact 292a7706bc4f6c21eccc60f2838cda0cd8ed4adc; self-test 7/7; PR mergeable=true contra baseline exact.`  
`UNVERIFIED: ejecución full-repo del candidate; CI exact-head inexistente al cierre; staging/prod físicos separados; proyectos/provider, DB, buckets/volumes, bots, OAuth callbacks, secrets y ownership reales separados.`  
`BLOCKERS: EXTERNAL — para completar literalmente 16.1, RO/provider owner debe definir/autorizar topología y credenciales de staging/prod separados (proyectos + DB + storage + bots + OAuth callbacks + secret stores/ownership). WOZ no puede crear esos recursos/costos sin autorización explícita.`  
`RECOMMENDATION_TO_JOBS: revisar PR #59 y, si acepta el contrato software, integrarlo con protección exact-head. Mantener 16.1 PENDING exclusivamente por separación física externa y CI/full-repo aún no observado; no reasignar WOZ dentro de este turno.`  
`TURN_FINISHED_AT: 2026-08-29T07:53:18-06:00`  
`STOP: sí.`

## HISTORIAL

- `NIGHT-WOZ-007`: PENDING_EXTERNAL — PR #59 runtime-operability candidate; self-test 7/7; separación física staging/prod requiere RO/provider action; CI exact-head no observado al cierre.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrado como f0d65aa66988e3e1a026e237b65c65a56b098aa9; D10.1 external-only por off-provider proof.
- `NIGHT-WOZ-005`: PENDING — PR #56 candidate; self-test PASS; único blocker off-provider; CI luego verificado SUCCESS por JOBS.
- `NIGHT-WOZ-004`: PENDING — tres gaps literales confirmados.
- `NIGHT-WOZ-003`: superseded unprocessed.
- `NIGHT-WOZ-002`: PENDING — D10.1 REUSE-FIRST audit.
- `NIGHT-WOZ-001`: superseded.
- D9: DONE/PASS — Issue #41 `5460959369`.
