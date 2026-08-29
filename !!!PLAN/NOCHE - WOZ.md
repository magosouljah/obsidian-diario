# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — worker nocturno.  
**Área:** F3 — producción / operación técnica.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## META DE WOZ ESTA NOCHE

Reducir el mayor bloque técnico restante de F0–F4 con REUSE-FIRST y evidencia real, sin inventar infraestructura/costo ni invadir F2/F4. Un turno = una asignación JOBS. WOZ no se autoasigna trabajo.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-008`
- `ASSIGNMENT_STATUS: PENDING_CI`
- `AREA: F3 / 16.1 candidate closure → 16.2 software-only promotion contract`
- `KNOWN_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`
- `REUSE_PR: #59 / woz/night-16.1-runtime-operability`
- `CURRENT_BASE: integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`
- `CURRENT_CANDIDATE_HEAD: 0e0bf188ceb298c5c6846e56576665b50a69e922`

### Orden JOBS

1. Preflight factual completo: Plan Maestro + F3 + Registro + roles + protocolo + este archivo + Issue #41 reciente + GitHub real.
2. REUSE-FIRST: continúa exclusivamente #59 para 16.1; no abras candidate duplicado.
3. Revalida head/base y el workflow Test - Desktop Portability. D6/D7/compile deben corresponder al exact head vigente.
4. Si Desktop Portability/Required CI aplicable termina SUCCESS, #59 sigue Ready/mergeable y no cambió la combinación, realiza race-check final y merge protegido con expected-head. Verifica merge SHA. Si falla, corrige la MISMA PR y vuelve a exigir exact-head.
5. Tras merge, 16.1 **no** se marca completo: el contrato software dependency-safe puede quedar DONE/INTEGRATED, pero la separación física staging/prod (projects, DB, storage, bots, OAuth callbacks, secrets/ownership) permanece PENDING_EXTERNAL hasta evidencia real.
6. Después de integrar #59, inicia 16.2 únicamente en el carril **software-only/dependency-safe** y REUSE-FIRST: audita workflows/deploy assets existentes; define/ajusta el contrato reproducible PR→preview, candidate tag→staging, approval→production; API origin/TLS/headers inyectables y release fail-closed sin Tailscale/local fallback; smoke/rollback scripts o fixtures que no requieran desplegar infraestructura real.
7. No crear RDS/provider projects/buckets/bots/OAuth projects/secret stores ni costo nuevo. No ejecutar deploy productivo ni staging real sin credenciales/RO.
8. Si 16.2 requiere infraestructura para probar el último tramo, separa DONE software-only de blocker externo literal. Un único candidate si hay delta real; si ya existe todo, entrega REUSED con evidencia.
9. No volver a D10.1; no tocar Stripe/DNS/legal/F2/F4. Actualiza solo este markdown + Issue #41 con evidencia y STOP.

### Fuera de scope

F1/D10.1; D10.2; F2; F4; Stripe 17.x; legal/DNS 19.x; capacidad 20.x; recursos/costo nuevos; release público; cualquier `!!!PLAN` salvo este markdown.

## RESULTADO DEL TURNO

`LAST_PROCESSED_ASSIGNMENT: NIGHT-WOZ-008`  
`TURN_STATUS: PENDING_CI`  
`GATE: F3/16.1 software runtime candidate; Required CI exact-head aún no finalizado`  
`BASELINE_AT_PREFLIGHT: integration-v0.8.0-alpha.1 @ f73c9ee8d058df3c780170c8c2a3fabef975c54d`  
`BRANCH_HEAD: woz/night-16.1-runtime-operability @ 0e0bf188ceb298c5c6846e56576665b50a69e922`  
`PR: #59 OPEN / mergeable=true / mergeable_state=blocked por Required CI pendiente`  
`CHANGES: REUSE-FIRST; #59 fue refrescada sobre el baseline vivo f73c9ee mediante merge commit de dos padres, preservando los cuatro archivos 16.1 y los cambios ya integrados de #57; no se abrió candidate duplicado.`  
`TESTS: self-test previo 7/7 PASS reutilizado; sobre exact head 0e0bf188: Web/shared SUCCESS, PostgreSQL live+recovery SUCCESS, Supply chain SUCCESS, Windows portability SUCCESS, macOS arm64 SUCCESS; macOS x86_64 seguía IN_PROGRESS en el último preflight.`  
`CI: productive temp-auth compile SUCCESS; D6 SUCCESS; D7 SUCCESS sobre exact head 0e0bf188. Required CI todavía no existe/termina porque macOS x86_64 sigue ejecutando. Un intento de merge protegido fue rechazado por GitHub con required status check "Required CI" expected; no se forzó ni se bypassó.`  
`EVIDENCIA_REUTILIZADA: #59 original y self-test 7/7; patrones exact-SHA/pinned-actions de workflows existentes; evidencia previa de separación física como blocker externo.`  
`EVIDENCIA_NUEVA: baseline vivo f73c9ee; candidate actualizado 0e0bf188; exact-head CI parcial verde; race-check final de integración confirmó f73c9ee antes del intento de merge; regla de repo confirmó Required CI obligatorio.`  
`UNVERIFIED: Required CI final del exact head 0e0bf188; merge SHA de #59; 16.2 software-only no iniciado porque la orden JOBS exige hacerlo después de integrar #59.`  
`BLOCKERS: CI transitorio: Native macOS smoke (x86_64) / Required CI. BLOCKER_16_1 externo permanente tras eventual merge: separación física staging/prod real (projects, DB, storage, bots, OAuth callbacks, secrets/ownership).`  
`RECOMENDACION_TECNICA_PARA_JOBS: mantener NIGHT-WOZ-008 sobre la misma PR #59; en el siguiente turno reusar esta ejecución, esperar Required CI SUCCESS, repetir race-check y merge expected-head 0e0bf188 si la base no cambia. Solo después iniciar un único candidate 16.2 software-only; no repetir CI ni crear infraestructura real.`  
`STOP: sí.`

## HISTORIAL

- `NIGHT-WOZ-008`: PENDING_CI — #59 refrescada sobre f73c9ee a 0e0bf188; exact-head gates verdes salvo macOS x86_64/Required CI aún en curso; merge correctamente bloqueado por regla Required CI; 16.2 no iniciado antes de integración.
- `NIGHT-WOZ-007`: PENDING_EXTERNAL — PR #59 + self-test 7/7; external physical separation.
- `NIGHT-WOZ-006`: PENDING — PR #56 integrado como `f0d65aa...`; D10.1 external-only.
- `NIGHT-WOZ-005`: PENDING — PR #56 candidate.
- `NIGHT-WOZ-004`: PENDING — D10.1 gaps confirmados.
- `NIGHT-WOZ-003`: superseded unprocessed.
- `NIGHT-WOZ-002`: PENDING — D10.1 audit.
- `NIGHT-WOZ-001`: superseded.
- D9: DONE/PASS — Issue #41 `5460959369`.
