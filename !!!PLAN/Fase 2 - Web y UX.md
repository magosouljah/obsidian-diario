# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE 111:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810` al preflight JOBS.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] #91 INTEGRATED / #92 ACTIVE CANDIDATE / RUNTIME STILL OPEN`

Evidence ya cerrada:
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [x] silent Worker bootstrap seam acotado por #91: deadline de 30 s solo para `initialize`, `verify`, `get_index`, con fresh Worker on retry;
- [x] #91 exact-head Web/portability/Required CI aplicable PASS e integrado como `134a293985c314eb09c238115e3bcb71e79f1810`.

Nuevo hecho live después de #91:
- [x] deployed signed-out surface mostró `.bg-account-gate` en DOM mientras el static `#beatgaler-startup-loader` seguía encima mostrando `Loading Galer...`;
- [ 🟡 ] PR #92 `F2/12.1: dismiss signed-out Web startup loader` está OPEN/Ready/mergeable, head `9947380ce8095b718a400d1e7781d21e67b29be9`, **exact base `134a293...`**;
- candidate #92 observa `#root` y retira el loader solo cuando el signed-out `.bg-account-gate` realmente aparece; su propia descripción no altera authenticated bootstrap;
- exact-head Web/shared y otros checks se observaron SUCCESS, pero WOZ110 debe verificar el conjunto requerido completo antes de merge.

**Owner CYCLE111 para #92: `NIGHT-WOZ-110`.** Única integration mutation lane del ciclo, condicionada a exact-base/head + all applicable required CI SUCCESS + race-free expected-head.

**12.1 permanece NOT_PASS.** Después de cualquier integración de #92 todavía falta probar el deployment del resulting canonical baseline con evidencia aplicable:
1. `/web-health` sano;
2. auth-health sano;
3. signed-out startup no queda tapado por loader;
4. authenticated startup sale de `Loading Galer` o cae a estado recuperable explícito;
5. cold/warm startup real cuantificado.

No inferir authenticated PASS desde el hallazgo signed-out de #92.

### 13.1 — `[ 🟡 ] FROZEN`
#69 Web y #70 Server siguen candidates históricos stale/frozen. REUSE semantics solo bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP / OWNER AAA107`

Gate literal: ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa. Evidence reusable demuestra que Review Save/Save All pueden avanzar/cerrar antes de durable cloud completion/failure.

**Owner CYCLE111: `NIGHT-AAA-107`.** Minimum corrective: visible success/close/advance solo después de durable completion; failure/retry visible; Save All partial/failure semantics; focused Web/no-Tauri tests; bounded candidate; **NO MERGE**.

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
Playback candidate stale; no priorizar frente a startup/auth/durability.

### 14.2 — `[ ]`
Queue/seek/shuffle/repeat/error recoverable, responsive volume y Safari/Firefox/Chrome/iPhone/degraded-network evidence pendientes.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH SEAM`
Purge lifecycle existe, pero faltan strong confirmation, recent-reauth seam y deterministic durable action boundary; UI puede limpiar optimistamente antes de purge completion. Bloquea alpha salvo decisión RO explícita de exclusión.

### 15.2 / 15.3
A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; no falsear browser/runtime coverage.
