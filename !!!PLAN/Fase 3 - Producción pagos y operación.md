# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 14–18 de septiembre  
**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno CYCLE 007:** F3 sigue siendo el mayor bloque abierto de F0–F4. Baseline al preflight JOBS: `integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`.

## Owner actual

**WOZ — F3 / 16.1 → 16.2 — `NIGHT-WOZ-008`.**

PR #59 `woz/night-16.1-runtime-operability` está OPEN/Ready/mergeable=true, exact head `292a7706bc4f6c21eccc60f2838cda0cd8ed4adc`, base `f0d65aa...`. Self-test 7/7 PASS. D6 `33256145573`, D7 `33256145614`, productive temp-auth compile `33256145521` y Test - Desktop Portability `33256145531` terminaron SUCCESS sobre ese exact head. WOZ debe hacer race-check final y merge protegido si la combinación sigue igual. Esto puede cerrar el **slice software dependency-safe**, no la separación física staging/prod.

Después del merge verificable, `NIGHT-WOZ-008` autoriza avanzar 16.2 solo en el carril software-only/dependency-safe, REUSE-FIRST y sin crear recursos/costo.

## Día 16 — Staging y producción reproducibles

**Resultado:** el mismo SHA se despliega de forma aislada y reversible.

### Tarea 16.1 [P0 · OP/BE] — Entornos — `[ 🟡 ] IN PROGRESS / EXTERNAL TAIL`

- [ ] Crear/probar **entornos físicamente separados** con proyectos/provider ownership, base de datos, storage/buckets/volúmenes, bots, OAuth callbacks y secretos separados para staging/producción. **PENDING_EXTERNAL:** requiere autorización/credenciales/recursos reales; #59 no satisface este literal.
- [ ] Si se mantiene la propuesta del usuario: Cloudflare Pages para Web y Railway para API/PostgreSQL; documentar alternativa y ownership. Sigue sujeto a decisión/provider real donde aplique.
- [ 🟡 ] Health, readiness y dependency checks; graceful shutdown, timeouts y proxy trust. **Candidate #59 exact-head CI verde; integración aún pendiente de owner merge.**

Candidate #59 implementa dependency-safe:
- `/healthz`;
- `/readyz` con PostgreSQL `SELECT 1`, fail-closed si DB requerida falta/no responde;
- draining durante shutdown;
- trust proxy explícito/acotado;
- request/header/keepalive/socket/dependency timeouts;
- graceful SIGINT/SIGTERM drain;
- `BEATGALER_DEPLOYMENT_ENV=staging|production` obligatorio bajo `NODE_ENV=production`;
- knobs documentados en `.env.example`.

**Regla:** no crear una segunda RDS, nueva infraestructura pagada, provider projects, buckets/bots/OAuth projects ni recursos con costo sin aprobación RO. Integrar #59 no convierte 16.1 entero en PASS; physical separation sigue PENDING_EXTERNAL.

### Tarea 16.2 [P0 · OP/QA] — Pipeline de promoción — `NEXT SOFTWARE-ONLY AFTER #59`

- [ ] PR → preview; tag candidato → staging; aprobación → producción.
- [ ] Inyectar API origin público, TLS y headers; eliminar Tailscale/local fallbacks de release.
- [ ] Smoke post-deploy y rollback al último artefacto/DB compatible.

`NIGHT-WOZ-008` puede cerrar únicamente el **contrato software reproducible** de estos puntos si existe delta real y puede probarse sin provider resources: auditar/reutilizar workflows/deploy assets existentes; fail-closed release origins; smoke/rollback scripts/fixtures; un único candidate si hace falta. El deploy real/staging real sigue sin falsearse.

**Dependencias:** rama integrada y migraciones.  
**Evidencia de cierre completo:** deploy desde cero, smoke y rollback con mismo SHA.  
**Gate completo:** no existe paso manual irrepetible ni secreto compartido entre entornos.

## Día 17 — Stripe Checkout y webhooks

### 17.1 [P0 · BE/LF] — Catálogo y checkout
- [ ] Definir productos/precios/trial/currency/tax y mapearlos a IDs internos estables.
- [ ] Checkout Session server-side; customer linkage y success/cancel URLs sin confiar en query params.
- [ ] Idempotency keys en mutaciones Stripe y sin precios decididos por cliente.

### 17.2 [P0 · BE/QA] — Webhook seguro
- [ ] Verificar firma sobre raw body, guardar event ID y procesar asíncrono/reintentable.
- [ ] Manejar duplicados, desorden, timeout y eventos desconocidos.
- [ ] Cubrir checkout complete, invoice paid/failed, subscription updated/deleted y dispute/refund relevantes.

**Dependencias:** cuenta/productos Stripe confirmados y entorno staging.  
**Evidencia:** matriz sandbox, replay/duplicate test y ledger consistente.  
**Gate:** la UI nunca concede plan por redirect; solo estado server-side reconciliado. Si falla, v1 se retrasa.

## Día 18 — Entitlements, portal y reconciliación

### 18.1 [P1 · BE/FE] — Enforcement
- [ ] Aplicar beats/storage/project/device/session/YouTube limits antes de reservar recursos.
- [ ] Transacción o reserva evita carreras; errores incluyen uso, límite y acción posible.
- [ ] Billing Portal/cancelación y estado `active/trialing/past_due/canceled` en Settings.

### 18.2 [P0 · LF/BE/QA] — Dinero y ledger
- [ ] Job de reconciliación Stripe↔BeatGaler y cola de excepciones con owner.
- [ ] Probar 3DS, rechazo, pago tardío, renewal failed, cancel, upgrade/downgrade y refund.
- [ ] Separar accesos inmediatamente peligrosos de grace periods aprobados.

**Dependencias:** Día 17.  
**Evidencia:** 100% de escenarios de billing esperados reconciliados en sandbox.  
**Gate:** no existe pago sin plan correcto ni plan pagado sin evento/ledger justificable; v1 no tiene fallback free-only.

## Día 19 — Dominio, identidad, legal y soporte

### 19.1 [P0/P1 · LF/RO] — Identidad pública
- [ ] Fijar nombre, bundle ID, dominio, API/status/support URLs y sender domains.
- [ ] Configurar DNS/TLS, redirects canónicos y callbacks OAuth exactos.
- [ ] Registrar versión/fecha de Terms/Privacy aceptada en signup.

### 19.2 [P0/P1 · LF/FE] — Legal y soporte operable
- [ ] Privacy describe proveedores reales, pagos, retención, export/delete y transferencias reales.
- [ ] Terms/refund/cancelación/renewal y contacto sin placeholders, aprobados por owner legal.
- [ ] Soporte con intake, severidad, SLA propuesto, recuperación, abuso/seguridad, refund y escalación.

**Dependencias:** flujos reales de cuenta/datos/pago ya definidos.  
**Evidencia:** URLs versionadas, aceptación E2E y prueba de ticket/escalación.  
**Gate:** copy y comportamiento coinciden; ningún placeholder o promesa ausente.

## Día 20 — Observabilidad, capacidad y recovery

### 20.1 [P1 · OP/BE] — Operación
- [ ] Logs estructurados/redactados, métricas, tracing/error reporting y retention.
- [ ] Dashboards/alerts para auth, API, DB, billing/provider, lease pool, queue, backup y release.
- [ ] On-call, runbook, status page, severidad y kill switches de registro/pagos/uploads.

### 20.2 [P1 · OP/QA] — Capacity envelope
- [ ] Definir pico esperado y probar al doble durante 60 minutos como target propuesto.
- [ ] Medir lease/upload/index latency, dependency errors, queue depth y recuperación.
- [ ] Añadir admission control, per-bot ceiling, 30% de margen propuesto y waitlist; no exigir “80 bots” sin necesidad medida.

**Dependencias:** staging production-shaped.  
**Evidencia:** dashboard, alert delivery, load report y dependency-loss drill.  
**Gate:** alertas accionables y capacidad medida; 0 fuga cross-tenant bajo carga.
