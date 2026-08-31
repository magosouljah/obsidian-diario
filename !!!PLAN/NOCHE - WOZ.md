# NOCHE — WOZ

**Sesión:** `NIGHT-2026-08-29`  
**Rol:** WOZ — jefe técnico / integrador nocturno.  
**Protocolo:** `!!!PLAN/NOCHE - Protocolo de orquestación.md`.

## ASIGNACIÓN VIGENTE

- `ASSIGNMENT_ID: NIGHT-WOZ-079`
- `ASSIGNMENT_STATUS: ASSIGNED`
- `AREA: F3 / 20.2 — real 160-concurrent runtime evidence, REUSE #78 harness; READ-ONLY/product-no-write unless literal evidence collection requires no repo mutation`
- `LIVE_BASE_AT_ASSIGNMENT: integration-v0.8.0-alpha.1 @ 957f97771b7a15554cf6e002fe9eb215c71a65cc`
- `PREDECESSOR: NIGHT-WOZ-078 = BLOCKED_STOP. #83 remained exact/scoped + exact-head CI green but Draft→Ready connector path failed with Repository.fullDatabaseId schema error. No integration mutation.`
- `PARKED_PR: #83 @ 52b58f56d66430db1ecdce9f572680c61d5d9fe3 remains OPEN/DRAFT on exact base 957f9777...; do not mutate it in this assignment.`
- `SERIALIZATION: BBB/#79 alone may mutate integration in CYCLE 080. WOZ must not merge or modify #83/#79.`

### PRIMARY

**F3 / 20.2 — obtain the missing materially applicable capacity evidence using the already-integrated #78 harness; do not build another harness.**

1. Fresh preflight integration + Issue #41 + duplicate-check; confirm #78 harness is already integrated and do not recreate it.
2. Execute the existing capacity path only if the available environment is materially applicable to the canonical target: **80 expected simultaneous users / 160 validation users**.
3. Collect verifiable results for: 160 concurrent users reached; latency distribution/target; error rate/types; queue/admission behavior; recovery behavior; unauthorized/cross-tenant behavior; data loss; and measured safety margin relative to 80 expected.
4. Preserve exact runtime/environment identity and commands/config used, but do not expose secrets.
5. If the only available execution is synthetic/local-only in a way that the plan already rejects as closing evidence, record `PENDING_EXTERNAL_RUNTIME` rather than manufacturing PASS.
6. Do not touch #83 durable-waitlist candidate, #79, payment/provider config, infrastructure, DNS, or F2 files. No repo/code changes are authorized by PRIMARY.
7. Maximum claim: `20.2 RUNTIME_EVIDENCE_PASS` only if evidence is materially applicable and all literal runtime criteria pass; otherwise `GAP`/`PENDING_EXTERNAL_RUNTIME`. Even a runtime PASS does not integrate #83 or close 20.2 while durable waitlist remains unintegrated.
8. Write RESULTADO DEL TURNO here + Issue #41 handoff and STOP.

**Required evidence:** exact live baseline; environment/runtime identity; 160 concurrency proof; latency/error/queue/recovery results; safety-margin calculation versus 80; no-data-loss/no-unauthorized-cross-tenant result; explicit limitations/UNVERIFIED.  
**STOP:** applicable runtime requires unavailable credential/provider mutation/infra change; environment is only non-applicable synthetic/local; overlap; #78 harness is missing/broken in a way that requires code changes; integration moves and invalidates applicability materially.

### CI-FALLBACK

**F3 / 19.1 — READ-ONLY deployment/domain evidence map.** Execute only if PRIMARY genuinely enters `WAITING_EXTERNAL_RUNTIME` because an already-triggered external environment/build/verification must complete and there is safe idle time.

- **Scope:** inspect existing public/deployment evidence only for domain/API/status/support URLs, DNS/TLS, redirects/callback exactness and sender-domain evidence. No provider/DNS/resource mutations; no #76 changes.
- **Required evidence:** `PASS / GAP / UNVERIFIED` per 19.1 item with exact observable source and smallest external action for each gap.
- **STOP:** credential/provider action required; unsafe visibility; overlap; PRIMARY external wait resolves, then recheck PRIMARY before closing.
- Fallback cannot close 19.1 and cannot substitute productive provider evidence.

## RESULTADO DEL TURNO MÁS RECIENTE PROCESADO

`NIGHT-WOZ-078`: `BLOCKED_STOP`; #83 exact/scoped, Required CI exact-head success, still Draft because connected Draft→Ready action failed before mutation. Fallback not eligible/not executed.

## RESULTADOS PROCESADOS

- `NIGHT-WOZ-078`: BLOCKED_STOP / #83 exact-head green and scoped, still Draft due connector tooling; no fallback, no integration mutation.
- `NIGHT-WOZ-077`: NO_RESULT before CYCLE 079; superseded, not PASS.
- `NIGHT-WOZ-074`: WAITING_CI / PR #83 candidate created; waitlist workflow PASS; JOBS later verified applicable exact-head CI success.
- `NIGHT-WOZ-070`: DONE / PR #75 integrated; F3/20.1 software observability integrated.
- Older results remain historical in Issue #41 and git history.
