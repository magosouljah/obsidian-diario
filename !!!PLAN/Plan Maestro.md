# BeatGaler — Plan Maestro para terminar y publicar Web, Windows y macOS

> **ESTE ARCHIVO SE LEE COMPLETO SIEMPRE ANTES DE TRABAJAR EN BEATGALER.**
> Después se lee completa la fase activa indicada en `Estado vivo del plan`. Los demás archivos solo se abren cuando la tarea actual los requiere.

#### ignorar*
```powershell
# Limpia y compacta manualmente la base interna de Git
git gc
```

```powershell
# Baja cambios de GitHub usando rebase
git pull --rebase origin main
```

```powershell
# Sube tus cambios locales a GitHub
git push origin main
```

## REGLAS DE ORO

1. **LEE `Plan Maestro.md` COMPLETO SIEMPRE.**
2. **LEE COMPLETA LA FASE ACTIVA ANTES DE MODIFICAR CÓDIGO.**
3. **SIGUE EL PLAN ESTRICTAMENTE.** No adelantar una tarea saltándose dependencias o gates.
4. **ANTES DE MODIFICAR:** hacer auditoría solo lectura y explicar exactamente qué se cambiará y por qué.
5. **DESPUÉS DE CADA CAMBIO RELEVANTE:** ejecutar las pruebas afectadas y revisar CI antes de seguir.
6. **NO MARCAR `[x]` SIN EVIDENCIA.** `[x]` significa terminado y con gate satisfecho.
7. **NO OLVIDAR ANOTAR CADA AVANCE.** Cada avance relevante actualiza obligatoriamente:
   - este archivo: `Estado vivo del plan`;
   - la tarea/checklist dentro de su archivo de fase;
   - `Registro de avances.md` con evidencia fechada.
8. Si una tarea afecta publicación/go-no-go, leer también `Gates - Publicación y contingencias.md`.
9. No cambiar comportamiento de producto no relacionado para “aprovechar” una tarea.

## Repos

- Plan: https://github.com/magosouljah/obsidian-diario
- BeatGaler: https://github.com/magosouljah/BeatGaler

**Versión del plan:** 1.2  
**Fecha de auditoría base:** 22 de agosto de 2026, `America/Mexico_City`  
**Última reorganización:** 23 de agosto de 2026, `America/Mexico_City`  
**Hito original:** 4 de septiembre de 2026  
**Fecha pública recomendada:** 9 de octubre de 2026, condicionada a todos los gates  
**Ruta conservadora si una persona concentra la ejecución:** 30 de octubre de 2026  
**Alcance:** lanzamiento público directo desde la web, con aplicación Web y descargas firmadas para Windows y macOS.

## Estado vivo del plan

- **Fase actual:** Fase 0 — Contener, decidir y crear una sola línea de release.
- **Día/tarea actual:** Día 5 — **Tarea 5.1 cerrada `[x]`**; **Tarea 5.2 — Aprobar arquitectura de datos está `[ 🟡 ] / EN PROGRESO`**. Tarea 1.2 y 2.2 continúan en paralelo según sus gates.
- **Estado general:** 🔴 `NO-GO` para lanzamiento público. Tareas 4.1, 4.2 y 5.1 quedan cerradas con evidencia; 5.2 sigue abierta porque aún faltan cutover controlado y evidencia real de infraestructura productiva RPO/PITR/KMS. No iniciar tareas posteriores.
- **Último avance:** **Tarea 5.2 ya tiene arquitectura y varias capas técnicas integradas.** PR #29 integró ADR/threat model/rollback; PRs #30–#32 añadieron schema/migrations, envelope encryption, migración legacy idempotente y garbage journal; PR #33 añadió `pg@8.23.0`, bootstrap fail-closed y PostgreSQL 16 real como gate requerido. El primer run live de #33 detectó un race real al crear `schema_migrations`; se corrigió tomando el advisory lock antes del ledger. #33 se integró como `1c5127b30ec7ee11e65d82100bae7fc33a2aeb52` y CI post-merge #254 (`32944403636`) terminó PASS en Web/shared, Supply Chain, PostgreSQL live, Windows, macOS arm64/x86_64 y `Required CI`; probe 5.1 #53 (`32944403720`) PASS. **Ahora está abierto el draft PR #34**, head `103d1e4a1f1a1107935a88362238e5c42f8a64c0`, con operaciones Direct durables, reconciliación forward-only desde el pinned INDEX, detección conservadora de orphans, exporter de rollback desde PG actual y un drill real de dump cifrado + restore a una segunda instancia PostgreSQL. El job PostgreSQL/recovery de CI #255 (`32945413572`, job `98104979741`) ya terminó PASS y produjo artefacto `postgres-recovery-evidence` id `9598064802`, digest `sha256:09622af6bd0d663b328ce28cb2955245db9fd995d93428e9a2fdeeb3a8c07df1`; el CI completo de #34 aún debe terminar antes de mergear. **5.2 no se marca `[x]`.**
- **Próximo paso principal:** terminar CI completo de PR #34; si queda totalmente verde, integrar y verificar CI post-merge. Después implementar el cutover software controlado/default-off y su rollback fail-closed. Solo con proveedor PostgreSQL/KMS real, WAL/PITR/retención configurados, RPO <=15 min/RTO <=2 h demostrados y cutover/rollback real con evidencia podrá cerrarse 5.2. No adelantar tareas posteriores.
- **Trabajo paralelo vigente:** Tarea 1.2 (dominio, Apple Developer, Authenticode, revisión legal/seguridad externa/hardware) y reauditoría diferida de Tarea 2.2.
- **Bloqueos actuales:** historial Git antiguo de información operacional aún pendiente de decisión de purga; dominio, Apple Developer, Authenticode y revisiones externas de 1.2 pendientes; regresión de tiempo de carga inicial de librería registrada para 12.1; gate global de capacidad 2× pendiente de un pico propuesto concreto. Para 5.2 faltan proveedor PostgreSQL/KMS productivo, WAL/PITR y retención reales, prueba RPO/RTO productiva y cutover controlado. Riesgos residuales aceptados en 5.1: shared-bot fallback cross-vault cuando no haya bots libres y cleanup físico cross-bot >48 h como deuda durable de GC con INDEX como autoridad. Además, la auditoría ampliada de `cloud-server` encontró deuda preexistente de supply chain/licencia: `telegram@2.26.22` arrastra `@cryptography/aes@0.1.1` con GPL-3.0-or-later; no se aprobó GPL globalmente y debe resolverse/revisarse antes de release. La revisión independiente externa sigue pendiente como gate global.
- **BeatGaler integración:** rama `integration-v0.8.0-alpha.1`; HEAD integrado `1c5127b30ec7ee11e65d82100bae7fc33a2aeb52`; versión `0.8.0-alpha.1`. PR #34 sigue separado hasta terminar su CI completo.
- **Evidencia 3.2:** PR #8; commit de trabajo `818214889ef3c6f97a262a91046f7df0e4f723fe`; CI PR #64 PASS Windows + macOS arm64 + macOS x86_64; merge `32a38c490a53650a0e9d6435c50cd009ef1b5123`; CI post-merge #65 PASS.
- **Evidencia 4.1:** PR #9; commits de trabajo `e86ab19a7f3eef3a7036a50f8cb083add94c2292`, `a4f58943f222ef8f6a5c85a3e72142353fdf0a72` y `71a559dc4cdcb8e16159c709a7c2d0f64e61e5a0`; CI PR #68 PASS 5/5 incluido `Required CI`; merge `c7894ad3c2b3e296e3d2939d73953b159e48852f`; CI post-merge #70 PASS 5/5 incluido `Required CI`.
- **Evidencia 4.2:** PR #10; head final `902e4edf6f6f5d28f0f98922d5f22cc623c92f3d`; CI PR #100 (`32702389575`) PASS 6/6 incluido `Supply chain gate` y `Required CI`; artefacto `supply-chain-evidence` digest `sha256:d3b38c3be14ec01f0c283522049732a4e300588d8f0a9c588ec30221e0222419`; merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; árbol probado e integrado idéntico `9a7000f3f3a1840ebae0310ac3df6b827561f2c5`.
- **Evidencia 5.1 — CERRADA `[x]`:** PR #11 definió ADR/threat model/rollback; PR #12 retiró permission churn por evidencia de `FLOOD_WAIT`; PRs #13–#18 probaron M0-A/B/C/D, incluido bind split, identidad bot, renovación y **1,992,294,400 bytes** directos con `galer_cloud_file_bytes=0`; PR #23 probó Windows x86_64 + macOS arm64/x86_64; PR #24 probó Chrome + Web Worker real; PR #25 cerró delete reciente y documentó el límite >48 h; PR #26 cerró fair pool/admission max-4 + waitlist; PR #27 probó expiración natural/server-side; PR #28 migró el runtime productivo Web/Desktop y cerró discovery/ID3/CSP/headers/CORS/scopes. Head #28 `5119b3c6616b1a9c725bca1edad8e39036c4b463`; compile probe #32 (`32909324459`) PASS; CI PR #226 (`32909324476`) PASS 6/6; aprobación explícita RO 2026-08-25; merge `d9ae76f42faee3a7207b9232b7421a0bec20b090`; CI integrado #228 (`32912362077`) **PASS 6/6 incluido `Required CI`**. Riesgos residuales shared-bot y cleanup >48 h aceptados; revisión externa independiente continúa como gate global de release.
- **Evidencia 5.2 — EN PROGRESO `[ 🟡 ]`:** arquitectura #29 integrada; schema/migrations/secret envelope/import/garbage journal implementados en #30–#32; #33 integró driver `pg`, bootstrap opt-in fail-closed y test adversarial contra PostgreSQL 16 real. Head #33 `df14472cbb6b25b23d7ab27e9c4315d2b8b52d92`; CI PR #252 (`32943236736`) PASS incluido PostgreSQL live y `Required CI`; probe #52 (`32943236787`) PASS; merge `1c5127b30ec7ee11e65d82100bae7fc33a2aeb52`; CI post-merge #254 (`32944403636`) PASS completo y probe #53 PASS. Draft #34 head `103d1e4a1f1a1107935a88362238e5c42f8a64c0` ya demostró en PostgreSQL real: saga durable/idempotente, reconciliación PG hacia pinned INDEX, orphan debt tras safety window, exporter rollback que conserva una escritura posterior a migración, dump cifrado y restore aislado a segunda instancia con constraints/secretos/estado preservados. Job `98104979741` PASS; artefacto `9598064802`, digest `sha256:09622af6bd0d663b328ce28cb2955245db9fd995d93428e9a2fdeeb3a8c07df1`. **No prueba todavía PITR/WAL/KMS ni RPO/RTO productivos, ni cutover productivo; no hay `[x]`.**
- **Regla GitHub de integración:** PR obligatorio; `Required CI` es el único status check requerido y agrega Web/shared + PostgreSQL live/recovery + supply chain + Windows + macOS arm64/x86_64; la rama debe estar actualizada antes de merge; `Required approvals = 0` porque existe un solo maintainer. Esto **no elimina** los reviewers independientes exigidos más adelante por gates de security/legal/firma/release.

### Estados de seguimiento

- [ ] Pendiente.
- [ 🟡 ] En progreso.
- [ ⚠️ ] Terminado técnicamente, pero falta evidencia o gate.
- [ 🔴 ] Bloqueado.
- [ ⏸️ ] Pausado.
- [x] Terminado y con evidencia/gate satisfecho.

Cuando una tarea cambie de estado, se actualiza aquí y en su checkbox original. Los estados con emoji son marcadores visuales; `[x]` se reserva para trabajo realmente terminado y sustentado por la evidencia exigida por el plan.

## Reglas inmutables de publicación

1. Ningún P0 ni P1 abierto al publicar.
2. Ninguna plataforma se declara soportada sin instalación y flujo crítico en equipo limpio.
3. Ningún pago se acepta sin reconciliación, reembolso y entitlement server-side demostrados.
4. Ninguna evidencia externa se marca como lista sin propietario, fecha y enlace verificable.
5. **BeatGaler v1 nunca se publica como free-only.** Si billing no supera sus gates, v1 se retrasa. Betas y promociones pueden otorgar suscripciones reales sin costo mediante códigos o grants temporales.
6. Web debe funcionar como aplicación Web pura: nunca depender de Tauri, helper local ni BeatGaler Desktop.
7. YouTube es parte del objetivo de producto en **Desktop y Web**. `youtubePublishing: false` en Web describe únicamente el estado actual; solo cambia a `true` cuando el flujo Web real pase sus gates.

## Protocolo de lectura por tarea

1. Leer **este archivo completo**.
2. Abrir el archivo indicado como **fase actual** y leerlo completo.
3. Localizar la tarea exacta, sus dependencias, evidencia y gate de salida.
4. Si la decisión toca release/publicación, abrir `Gates - Publicación y contingencias.md`.
5. Hacer auditoría read-only del código/estado real.
6. Explicar cambio exacto y razón antes de modificar.
7. Ejecutar cambio mínimo.
8. Ejecutar suites afectadas y revisar CI.
9. Solo con evidencia: actualizar fase + este estado vivo + `Registro de avances.md`.

## Mapa de archivos del plan

| Archivo | Cuándo se lee | Contenido |
|---|---|---|
| **`Plan Maestro.md`** | **SIEMPRE, completo** | reglas, estado vivo, orden de trabajo y mapa |
| `00 - Contexto global y criterios.md` | cuando una decisión necesita contexto global/auditoría/diseño/prioridad | veredicto, evidencia, fechas, inventario, diseño, prioridades y roles |
| `Fase 0 - Contención e integración.md` | mientras Fase 0 esté activa | Días 0–5, incluida integración/CI/ADR |
| `Fase 1 - Seguridad cuentas y datos.md` | Fase 1 | Días 6–10 |
| `Fase 2 - Web y UX.md` | Fase 2 | Días 11–15, incluido el plan completo de YouTube Web en Tarea 15.3 |
| `Fase 3 - Producción pagos y operación.md` | Fase 3 | Días 16–20 |
| `Fase 4 - Desktop y release chain.md` | Fase 4 | Días 21–25 |
| `Fase 5 - Betas y RC.md` | Fase 5 | Días 26–30 |
| `Fase 6 - Lanzamiento.md` | Fase 6 | Días 31–35 |
| `Fase 7 - Estabilización.md` | Fase 7 | Días 36–41 |
| `Gates - Publicación y contingencias.md` | gates, go-no-go, riesgos o contingencias | condiciones obligatorias, métricas, RACI, riesgos, contingencias y criterios |
| `Registro de avances.md` | al cerrar/actualizar trabajo | historial cronológico de evidencia |

## Fuente de verdad y precedencia

Si dos textos parecen contradecirse, aplicar este orden:

1. Reglas inmutables y `Estado vivo` de `Plan Maestro.md`.
2. Gate/checklist de la fase activa.
3. `Gates - Publicación y contingencias.md` para condiciones de publicación.
4. `00 - Contexto global y criterios.md` como contexto histórico/estático.

Ningún archivo secundario puede rebajar un gate del principal. Una nueva decisión de producto debe actualizar primero el principal y después los archivos afectados.