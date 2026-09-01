# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo:** `integration-v0.8.0-alpha.1 @ 134a293985c314eb09c238115e3bcb71e79f1810`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] INTEGRATED / PUBLIC DEPLOY + AUTH RUNTIME PENDING`
- [x] índice vacío atómico — #64;
- [x] empty/no-results/offline/auth/cloud-failure separados — #58 + AAA022;
- [x] lazy artwork + pagination/window/memory — #58/#66;
- [x] primer bootstrap seam no acotado aislado: `WebTransportWorkerClient.request()` podía quedar pendiente para siempre si el data-plane Worker no respondía ni emitía error;
- [x] corrective mínimo en PR #91 @ `35d44a0dd5ee380f802b3a80b139ca1ca741d5f9`: deadline de 30 s solo para `initialize`, `verify` y `get_index`; Worker silencioso se termina y el siguiente intento obtiene runtime fresco; no se añadió timeout genérico al loader ni se acotaron transfers largos;
- [x] exact-head evidence de #91: Web Production Build PASS; `Test - Desktop Portability` run `33464096509` terminó con Web/shared, PostgreSQL, supply-chain, Windows, macOS arm64 y macOS x86_64 en PASS; `Required CI` job `99722252533` PASS;
- [x] PR #91 integrado con autorización RO del turno como merge commit `134a293985c314eb09c238115e3bcb71e79f1810`; integración race-clean desde base `78dd55b72142e69ea32ba6c1ba6d43e246ac6843`;
- [ ] desplegar el nuevo baseline público en `https://beatgaler.com`;
- [ ] public Web autenticado demuestra que sale de `Loading Galer` de forma determinista o cae al estado recuperable existente;
- [ 🟡 ] cold/warm startup Web real cuantificado.

**Resultado 12.1 / NIGHT-AAA-105:** `INTEGRATED / PUBLIC_DEPLOY_AND_AUTH_RUNTIME_PENDING`.

El `catch` de startup existente ya convierte un fallo de `reloadAuthoritative()` en la ruta recoverable/offline/poor y descarta el startup loader. El gap probado era que el Worker podía no resolver ni rechazar; #91 convierte ese silencio en rechazo determinista y ya está en la rama canónica.

El cierre literal de 12.1 requiere ahora evidencia sobre el deployment que contenga `134a293...`. El mecanismo productivo vigente no es un workflow remoto: `scripts/deploy-web-production.ps1` construye `dist`, empaqueta y copia por `scp/ssh` al EC2, y exige `-KeyPath` hacia la llave SSH del owner. Desde este entorno no existe acceso a esa llave/máquina ni conector AWS/SSH; por tanto no se inventa runtime PASS.

Comando owner-machine para desplegar el baseline integrado desde un checkout actualizado:

```powershell
powershell -NoProfile -ExecutionPolicy Bypass -File .\scripts\deploy-web-production.ps1 -KeyPath "<RUTA-A-LA-LLAVE-EC2.pem>"
# Construye Web y despliega el contenido actual a beatgaler.com usando la llave SSH del EC2.
```

Después del deploy, evidence mínima para cerrar 12.1:
1. `https://beatgaler.com/web-health` responde `ok`;
2. `https://beatgaler.com/beatgaler-api/auth/health` permanece sano;
3. entrar con una cuenta real de prueba y confirmar que el startup deja `Loading Galer` de forma determinista, mostrando biblioteca/estado vacío válido o un estado recuperable explícito;
4. registrar cold/warm startup real aplicable.

### 13.1 — `[ 🟡 ] FROZEN`
#69 Web y #70 Server siguen candidates históricos stale/frozen. REUSE semantics solo bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP`
Gate literal: ninguna acción Web visible llama Tauri/Desktop; 0 pérdida silenciosa. Evidence reusable demuestra que Review Save/Save All pueden avanzar/cerrar antes de durable cloud completion/failure. Sigue OPEN y sin owner material mientras 12.1 termina runtime público.

### 14.1 — `[ 🟡 ] PARKED / #81 STALE`
Playback candidate stale; no priorizar frente a startup/auth/durability.

### 14.2 — `[ ]`
Queue/seek/shuffle/repeat/error recoverable, responsive volume y Safari/Firefox/Chrome/iPhone/degraded-network evidence pendientes.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH SEAM`
Purge lifecycle existe, pero faltan strong confirmation, recent-reauth seam y deterministic durable action boundary; UI puede limpiar optimistamente antes de purge completion. Sigue sin owner y bloquea alpha salvo decisión RO explícita de exclusión.

### 15.2 / 15.3
A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; no falsear browser/runtime coverage.