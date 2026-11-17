# BeatGaler V1 — siguientes pasos (versión simple)

Actualizado: 10 de octubre de 2026, noche CDMX.

## Estado actual

- Fase 2: cerrada.
- Fase 3: STEP 0–13 PASS.
- STEP 14: PARTIAL.
- STEP 15: todavía no se ejecuta; su preparación está guardada aparte.
- Rama activa: `integration-v0.9.0-alpha.4`.
- HEAD actual: `3146cf9159bc672d0728180962960ae05bd0fecb`.
- Preparación STEP 15: `prep/phase3-step15-e2e` @ `78fc437ad806045e236ab0bfe1683c303ca65358`.
- Preparación Fase 4: `prep/phase4-public-launch` @ `02d0cbd1cb939e0f6219803d9ce9bbf55aa59c72`.

## Mañana — 11 de octubre

### 18:30 CDMX

Prender/confirmar:

- PC despierta.
- WSL abierto.
- Internet estable.
- Abrir el chat que está manejando STEP 14.
- Pedirle que compruebe que TODOS los receivers/relays necesarios siguen vivos antes de los eventos. Los procesos 4011/4013 estaban activos; si siguen vivos, NO reiniciarlos por gusto.

No levantar procesos a mano siguiendo comandos viejos. Que el agente lea el estado actual y decida qué necesita estar vivo.

### Antes de 19:03 CDMX

STEP 14 debe estar mirando Polar + webhook + Access + reconciliación.

### ~19:03 CDMX

Esperar/capturar el cambio natural **Highest → Entry pagado**.

Queremos evidencia real de:

`Polar payment/order → webhook firmado → lifecycle → Access → reconciliación`.

### ~19:24 CDMX

Esperar/capturar la **expiración natural de la suscripción cancelada**.

No simular fechas ni fabricar webhooks.

### Después

Todavía falta **otra transición Entry → Highest con recepción real de `order.paid`**. El agente de STEP 14 debe decidir, leyendo el estado real, cómo y cuándo prepararla. No adivinar horarios ni reutilizar evidencia falsa.

Cuando esos gates reales estén completos:

**STEP 14 = PASS.**

## En paralelo mientras esperamos STEP 14

Trabajar únicamente en la rama aislada:

`prep/phase3-step15-e2e`

Se puede adelantar preparación, harnesses, auditoría, fixtures y pruebas locales de STEP 15.

NO:

- integrar STEP 15 a la rama activa;
- tocar los runs/procesos de STEP 14;
- usar sus DB, usuarios, vaults o evidencia como fixtures mutables;
- declarar STEP 15 PASS;
- empezar Fase 4.

## Cuando STEP 14 dé PASS

1. Congelar el SHA final de STEP 14.
2. Hacer el checkpoint arquitectónico obligatorio sobre ESE SHA.
3. Rebasar/integrar con cuidado la preparación `prep/phase3-step15-e2e`.
4. Ejecutar STEP 15 E2E final con entorno aislado.
5. Probar Browser + Cloud + PostgreSQL + Telegram real + Polar Sandbox real.
6. Probar planes, cuotas, PROJECT, Trash/purge, downgrade, checkout y estado comercial.
7. Si todo pasa: **STEP 15 PASS → Fase 3 CLOSED.**

## Después de Fase 3: Fase 4

Tomar como preparación:

`prep/phase4-public-launch`

Antes de abrir V1 a usuarios con dinero real hay que cerrar, en simple:

1. **Producción real:** Polar Live, productos/precios Live, webhook Live y portal/cancelación.
2. **Datos seguros:** PostgreSQL productivo, backups/PITR, restore medido, KMS/secrets y rollback.
3. **PROJECT grande:** trayecto multipart/S3/Telegram/proxy probado realmente hasta el contrato de 1.9 GB.
4. **Deploy seguro:** publicar un SHA exacto y probar rollback real.
5. **Operación:** alertas, monitoreo y alguien responsable si algo falla.
6. **Legal/soporte:** quitar placeholders de Privacy/Terms y tener cancelación/soporte reales.
7. **Prueba final con dinero real controlado.**
8. Abrir gradualmente a usuarios.

## Qué significa “V1 terminada”

**STEP 14 PASS → STEP 15 PASS/Fase 3 CLOSED → Fase 4 GO → deploy de producción → compra real controlada → abrir usuarios.**

YouTube/Bulk y plan anual NO son requisito de la V1 Web actual.
