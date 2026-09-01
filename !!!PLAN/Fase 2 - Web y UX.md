# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo:** `integration-v0.8.0-alpha.1 @ 78dd55b72142e69ea32ba6c1ba6d43e246ac6843`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] CODE FIX PROVEN / INTEGRATION + PUBLIC RUNTIME PENDING`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [x] primer bootstrap seam no acotado aislado: `WebTransportWorkerClient.request()` podía quedar pendiente para siempre si el data-plane Worker no respondía ni emitía error;
- [x] corrective mínimo en PR #91 @ `35d44a0dd5ee380f802b3a80b139ca1ca741d5f9`: deadline de 30 s solo para `initialize`, `verify` y `get_index`; Worker silencioso se termina y el siguiente intento obtiene runtime fresco; no se añadió timeout genérico al loader ni se acotaron transfers largos;
- [x] exact-head evidence: Web Production Build PASS; Web + shared gate PASS hasta y incluyendo build Web real, Chrome smoke, typecheck, TypeScript unit contract y DOM component contract con las pruebas enfocadas nuevas;
- [ ] integración autorizada de #91 — el assignment vigente de 12.1 mantiene **NO MERGE**;
- [ ] public Web autenticado desplegado demuestra que sale de `Loading Galer` de forma determinista o cae al estado recuperable existente;
- [ 🟡 ] cold/warm startup Web real cuantificado.

**Resultado 12.1 / NIGHT-AAA-105:** `CODE_FIX_PROVEN / NO_MERGE / PUBLIC_RUNTIME_PENDING`.

El `catch` de startup existente ya convierte un fallo de `reloadAuthoritative()` en la ruta recoverable/offline/poor y descarta el startup loader. El gap probado era que el Worker podía no resolver ni rechazar; #91 convierte ese silencio en rechazo determinista. Esto cierra la ruta de espera infinita a nivel código, pero **12.1 no es PASS todavía**: falta integración autorizada + evidencia runtime pública autenticada sobre el artefacto/deploy que contenga el fix.

### 13.1 — `[ 🟡 ] FROZEN`
#69 Web y #70 Server siguen candidates históricos stale/frozen. REUSE semantics solo bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP`
Gate literal: ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa. Evidence reusable demuestra que Review Save/Save All pueden avanzar/cerrar antes de durable cloud completion/failure. Sigue OPEN y sin owner material mientras 12.1 termina integración/runtime.

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
Playback candidate stale; no priorizar frente a startup/auth/durability.

### 14.2 — `[ ]`
Queue/seek/shuffle/repeat/error recoverable, responsive volume y Safari/Firefox/Chrome/iPhone/degraded-network evidence pendientes.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH SEAM`
Purge lifecycle existe, pero faltan strong confirmation, recent-reauth seam y deterministic durable action boundary; UI puede limpiar optimistamente antes de purge completion. Sigue sin owner y bloquea alpha salvo decisión RO explícita de exclusión.

### 15.2 / 15.3
A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; no falsear browser/runtime coverage.