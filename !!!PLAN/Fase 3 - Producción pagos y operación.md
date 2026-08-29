# Fase 3 — Producción, pagos, legal y operación

> Antes de trabajar aquí: leer completo [`Plan Maestro.md`](./Plan%20Maestro.md).

**Fechas:** 14–18 de septiembre  
**Objetivo:** crear un servicio operable, cobrable y restaurable con verdad legal.

**Estado nocturno actual:** F3 sigue siendo el mayor bloque abierto de F0–F4. JOBS reasignó explícitamente a WOZ desde F1 external-only hacia **16.1** bajo `NIGHT-WOZ-007`. Baseline vivo: `integration-v0.8.0-alpha.1 @ f0d65aa66988e3e1a026e237b65c65a56b098aa9`.

## Owner actual

**WOZ — F3 / 16.1 — `NIGHT-WOZ-007`.**

Primer slice: REUSE-FIRST de assets/runtime existentes; separar lo dependency-safe de lo que realmente requiera recursos/credenciales externos. No crear nueva infraestructura/costo sin autorización RO. Health/readiness/dependency checks, graceful shutdown, timeouts y proxy trust pueden cerrarse técnicamente si existe evidencia aplicable; staging/producción realmente separados no se declararán PASS sin recursos/secretos/callbacks separados verificables.

## Día 16 — 14 de septiembre — Staging y producción reproducibles

**Resultado:** el mismo SHA se despliega de forma aislada y reversible.

### Tarea 16.1 [P0 · OP/BE] — Entornos — `ASSIGNED / IN PROGRESS` — WOZ `NIGHT-WOZ-007`

- [ ] Crear proyectos separados, base de datos, buckets/volúmenes, bots, OAuth callbacks y secretos para staging/producción.
- [ ] Si se mantiene la propuesta del usuario: Cloudflare Pages para Web y Railway para API/PostgreSQL; documentar alternativa y ownership.
- [ 🟡 ] Health, readiness y dependency checks; graceful shutdown, timeouts y proxy trust. **WOZ audita primero lo ya existente y completa solo el delta real dependency-safe.**

**Regla nocturna:** no crear una segunda RDS, nueva infraestructura pagada, cuentas/provider projects, buckets ni recursos con costo sin aprobación explícita RO. Si la separación real staging/prod requiere credenciales/decisión externa, registrar el blocker literal y continuar únicamente el contrato software reproducible.

### Tarea 16.2 [P0 · OP/QA] — Pipeline de promoción

- [ ] PR → preview; tag candidato → staging; aprobación → producción.
- [ ] Inyectar API origin público, TLS y headers; eliminar Tailscale/local fallbacks de release.
- [ ] Smoke post-deploy y rollback al último artefacto/DB compatible.

**Dependencias:** rama integrada y migraciones.  
**Evidencia:** deploy desde cero, smoke y rollback con mismo SHA.  
**Gate de salida:** no existe paso manual irrepetible ni secreto compartido entre entornos.

## Día 17 — 15 de septiembre — Stripe Checkout y webhooks

**Resultado:** compra sandbox crea estado comercial verificable, no un cambio DEV.

### Tarea 17.1 [P0 · BE/LF] — Catálogo y checkout

- [ ] Definir productos/precios/trial/currency/tax y mapearlos a IDs internos estables.
- [ ] Checkout Session server-side; customer linkage y success/cancel URLs sin confiar en query params.
- [ ] Idempotency keys en mutaciones Stripe y sin precios decididos por cliente.

### Tarea 17.2 [P0 · BE/QA] — Webhook seguro

- [ ] Verificar firma sobre raw body, guardar event ID y procesar asíncrono/reintentable.
- [ ] Manejar duplicados, desorden, timeout y eventos desconocidos.
- [ ] Cubrir checkout complete, invoice paid/failed, subscription updated/deleted y dispute/refund relevantes.

**Dependencias:** cuenta/productos Stripe confirmados y entorno staging.  
**Evidencia:** matriz sandbox, replay/duplicate test y ledger consistente.  
**Gate de salida:** la UI nunca concede plan por redirect; solo estado server-side reconciliado. Si falla este gate, v1 se retrasa.

## Día 18 — 16 de septiembre — Entitlements, portal y reconciliación

**Resultado:** planes se aplican atómicamente y el usuario puede gestionar/cancelar.

### Tarea 18.1 [P1 · BE/FE] — Enforcement

- [ ] Aplicar beats/storage/project/device/session/YouTube limits antes de reservar recursos.
- [ ] Transacción o reserva evita carreras; errores incluyen uso, límite y acción posible.
- [ ] Billing Portal/cancelación y estado `active/trialing/past_due/canceled` en Settings.

### Tarea 18.2 [P0 · LF/BE/QA] — Dinero y ledger

- [ ] Job de reconciliación Stripe↔BeatGaler y cola de excepciones con owner.
- [ ] Probar 3DS, rechazo, pago tardío, renewal failed, cancel, upgrade/downgrade y refund.
- [ ] Separar accesos inmediatamente peligrosos de grace periods aprobados.

**Dependencias:** Día 17.  
**Evidencia:** 100% de escenarios de billing esperados reconciliados en sandbox.  
**Gate de salida:** no existe pago sin plan correcto ni plan pagado sin evento/ledger justificable; v1 no tiene fallback free-only.

## Día 19 — 17 de septiembre — Dominio, identidad, legal y soporte

**Resultado:** una persona real sabe quién opera BeatGaler, qué acepta y dónde pedir ayuda.

### Tarea 19.1 [P0/P1 · LF/RO] — Identidad pública

- [ ] Fijar nombre, bundle ID, dominio, API/status/support URLs y sender domains.
- [ ] Configurar DNS/TLS, redirects canónicos y callbacks OAuth exactos.
- [ ] Registrar versión/fecha de Terms/Privacy aceptada en signup.

### Tarea 19.2 [P0/P1 · LF/FE] — Legal y soporte operable

- [ ] Privacy describe Telegram, pagos, providers, retención, export/delete y transferencias reales.
- [ ] Terms/refund/cancelación/renewal y contacto sin placeholders, aprobados por owner legal.
- [ ] Soporte con intake, severidad, SLA propuesto, recuperación, abuso/seguridad, refund y escalación.

**Dependencias:** flujos reales de cuenta/datos/pago ya definidos.  
**Evidencia:** URLs versionadas, aceptación E2E y prueba de ticket/escalación.  
**Gate de salida:** copy y comportamiento coinciden; ningún placeholder o promesa ausente.

## Día 20 — 18 de septiembre — Observabilidad, capacidad y recovery

**Resultado:** fallos se detectan, limitan y recuperan antes de afectar a todos.

### Tarea 20.1 [P1 · OP/BE] — Operación

- [ ] Logs estructurados/redactados, métricas, tracing/error reporting y retention.
- [ ] Dashboards/alerts para auth, API, DB, Stripe, Telegram, lease pool, queue, backup y release.
- [ ] On-call, runbook, status page, severidad y kill switches de registro/pagos/uploads.

### Tarea 20.2 [P1 · OP/QA] — Capacity envelope

- [ ] Definir pico esperado y probar al doble durante 60 minutos como target propuesto.
- [ ] Medir lease/upload/index latency, errores Telegram, queue depth y recuperación.
- [ ] Añadir admission control, per-bot ceiling, 30% de margen propuesto y waitlist; no exigir “80 bots” sin necesidad medida.

**Dependencias:** staging production-shaped.  
**Evidencia:** dashboard, alert delivery, load report y dependency-loss drill.  
**Gate de salida:** alertas accionables y capacidad medida; 0 fuga cross-tenant bajo carga.
