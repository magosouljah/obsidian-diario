# BeatGaler — Plan Maestro para terminar y publicar Web, Windows y macOS

> **ESTE ARCHIVO SE LEE COMPLETO SIEMPRE ANTES DE TRABAJAR EN BEATGALER.**
> Después se lee completa la fase activa indicada en `Estado vivo del plan`. Los demás archivos solo se abren cuando la tarea actual los requiere, salvo ORION, cuyo protocolo especial exige leer todo el `!!!PLAN` operativo vigente.

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
10. **COORDINACIÓN MULTI-CUENTA:** existen cuatro roles: `ORION` (dueño de `!!!PLAN` y coordinador de AAA/BBB), `ATLAS` (jefe técnico e integrador), `AAA` y `BBB` (ayudantes). Leer `Equipo multi-IA - Roles y coordinación.md` cuando se reciba uno de estos roles. **`Eres ORION. Lee !!!PLAN y continúa.` es una invocación completa:** ORION debe leer todo el `!!!PLAN` operativo vigente, auditar su limpieza/coherencia, consultar Issue #41, reasignar automáticamente a AAA/BBB cuando queden libres y entregar a ATLAS el siguiente frente técnico permitido. ORION nunca trabaja en archivos del programa ni infraestructura; sus únicas escrituras de archivos de repositorio son dentro de `!!!PLAN`.

## Repos

- Plan: https://github.com/magosouljah/obsidian-diario
- BeatGaler: https://github.com/magosouljah/BeatGaler

**Versión del plan:** 1.3  
**Fecha de auditoría base:** 22 de agosto de 2026, `America/Mexico_City`  
**Última reorganización:** 27 de agosto de 2026, `America/Mexico_City` — separación ORION/ATLAS y coordinación automática de AAA/BBB  
**Hito original:** 4 de septiembre de 2026  
**Fecha pública recomendada:** 9 de octubre de 2026, condicionada a todos los gates  
**Ruta conservadora si una persona concentra la ejecución:** 30 de octubre de 2026  
**Alcance:** lanzamiento público directo desde la web, con aplicación Web y descargas firmadas para Windows y macOS.

## Estado vivo del plan

- **Fase actual:** Fase 0 — Contener, decidir y crear una sola línea de release.
- **Día/tarea actual:** Día 5 — **Tarea 5.1 cerrada `[x]`**; **Tarea 5.2 — Aprobar arquitectura de datos está `[ 🟡 ] / EN PROGRESO`**. Tarea 1.2 y 2.2 continúan en paralelo según sus gates.
- **Estado general:** 🔴 `NO-GO` para lanzamiento público. Tareas 4.1, 4.2 y 5.1 quedan cerradas con evidencia. En 5.2 ya quedaron integrados el runtime PostgreSQL controlado/default-off, cutover/rollback fail-closed, worker durable de garbage/reconciliación, snapshot sellado/quarantine/final-delta exacto, aislamiento/rotación transaccional de OAuth/MFA, la frontera software para resolver el keyring desde AWS Secrets Manager y el hardening de base64 canónico de PR #42. **El trabajo software-only exigible por 5.2 está cubierto; quedan infraestructura y operación productivas reales**: PostgreSQL/RDS, KMS/Secrets Manager e IAM reales, backup cifrado + WAL/PITR/retención, restore independiente con RPO/RTO y cutover/rollback real. No iniciar tareas posteriores.
- **Último avance técnico:** **PR #42 `fix(data): enforce canonical AWS envelope base64` ya está integrado.** Corrige el finding válido de Issue #41: la validación del keyring productivo ya no confía solo en el decoder base64 tolerante de Node; exige round-trip canónico, conserva la longitud exacta de 32 bytes y añade negativos para caracteres inválidos, padding inválido y trailing data. Head `718efd9073144eb2fd89bfe2459ed2ac8996b079`; merge `a968122127c584b5557b25e70a21eb64f75b3c0e`. El post-merge `Test - Desktop Portability` run `33118368302` terminó PASS en PostgreSQL live/recovery, Web/shared, supply chain, Windows, macOS arm64, macOS x86_64 y `Required CI`. **No cambia el gate productivo:** 5.2 sigue `[ 🟡 ] / NO-GO`.
- **Próximo paso principal para ATLAS:** provisionar la infraestructura real de 5.2 por la ruta más corta compatible con los gates: PostgreSQL/RDS administrado + KMS/Secrets Manager real + IAM mínimo + backups cifrados/PITR/retención + observabilidad; ejecutar el smoke real del provider, restore independiente representativo y demostrar RPO <=15 min/RTO <=2 h; después realizar el maintenance-window cutover/rollback con los bundles y runbook ya implementados. No sustituir estos pasos por flags, mocks o pruebas sintéticas.
- **Trabajo paralelo elegible:** Tarea 1.2 (dominio/DNS, Apple Developer, Authenticode, revisión legal/seguridad externa/hardware/testers) y reauditoría de Tarea 2.2 (historial Git/incidente). ORION mantiene las asignaciones transitorias de AAA/BBB en Issue #41 para no llenar el Plan Maestro con estado efímero de cada oleada.
- **Bloqueos actuales:** historial Git antiguo de información operacional aún pendiente de decisión de purga; dependencias externas de 1.2 aún no completamente demostradas; regresión de tiempo de carga inicial de librería registrada para 12.1; gate global de capacidad 2× pendiente de un pico propuesto concreto. Para 5.2 ya no queda un hueco software-only conocido del ADR: faltan RDS/PostgreSQL y KMS/Secrets Manager/IAM productivos, backups cifrados + WAL/PITR/retención reales, restore independiente representativo, RPO/RTO productivos y cutover/rollback de mantenimiento real. Riesgos residuales aceptados en 5.1: shared-bot fallback cross-vault cuando no haya bots libres y cleanup físico cross-bot >48 h como deuda durable de GC con INDEX como autoridad. Además, la auditoría ampliada de `cloud-server` encontró deuda preexistente de supply chain/licencia: `telegram@2.26.22` arrastra `@cryptography/aes@0.1.1` con GPL-3.0-or-later; no se aprobó GPL globalmente y debe resolverse/revisarse antes de release. La revisión independiente externa sigue pendiente como gate global.
- **BeatGaler integración:** rama `integration-v0.8.0-alpha.1`; HEAD integrado `a968122127c584b5557b25e70a21eb64f75b3c0e`; versión `0.8.0-alpha.1`.
- **Evidencia 3.2:** PR #8; commit de trabajo `818214889ef3c6f97a262a91046f7df0e4f723fe`; CI PR #64 PASS Windows + macOS arm64 + macOS x86_64; merge `32a38c490a53650a0e9d6435c50cd009ef1b5123`; CI post-merge #65 PASS.
- **Evidencia 4.1:** PR #9; commits de trabajo `e86ab19a7f3eef3a7036a50f8cb083add94c2292`, `a4f58943f222ef8f6a5c85a3e72142353fdf0a72` y `71a559dc4cdcb8e16159c709a7c2d0f64e61e5a0`; CI PR #68 PASS 5/5 incluido `Required CI`; merge `c7894ad3c2b3e296e3d2939d73953b159e48852f`; CI post-merge #70 PASS 5/5 incluido `Required CI`.
- **Evidencia 4.2:** PR #10; head final `902e4edf6f6f5d28f0f98922d5f22cc623c92f3d`; CI PR #100 (`32702389575`) PASS 6/6 incluido `Supply chain gate` y `Required CI`; artefacto `supply-chain-evidence` digest `sha256:d3b38c3be14ec01f0c283522049732a4e300588d8f0a9c588ec30221e0222419`; merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; árbol probado e integrado idéntico `9a7000f3f3a1840ebae0310ac3df6b827561f2c5`.
- **Evidencia 5.1 — CERRADA `[x]`:** PR #11 definió ADR/threat model/rollback; PR #12 retiró permission churn por evidencia de `FLOOD_WAIT`; PRs #13–#18 probaron M0-A/B/C/D, incluido bind split, identidad bot, renovación y **1,992,294,400 bytes** directos con `galer_cloud_file_bytes=0`; PR #23 probó Windows x86_64 + macOS arm64/x86_64; PR #24 probó Chrome + Web Worker real; PR #25 cerró delete reciente y documentó el límite >48 h; PR #26 cerró fair pool/admission max-4 + waitlist; PR #27 probó expiración natural/server-side; PR #28 migró el runtime productivo Web/Desktop y cerró discovery/ID3/CSP/headers/CORS/scopes. Head #28 `5119b3c6616b1a9c725bca1edad8e39036c4b463`; compile probe #32 (`32909324459`) PASS; CI PR #226 (`32909324476`) PASS 6/6; aprobación explícita RO 2026-08-25; merge `d9ae76f42faee3a7207b9232b7421a0bec20b090`; CI integrado #228 (`32912362077`) **PASS 6/6 incluido `Required CI`**. Riesgos residuales shared-bot y cleanup >48 h aceptados; revisión externa independiente continúa como gate global de release.
- **Evidencia 5.2 — EN PROGRESO `[ 🟡 ]`:** #29–#36 integraron ADR/schema/migrations/envelope encryption/importador/garbage journal/PostgreSQL 16/sagas/reconciliation/recovery/runtime authority/cutover controlado/rollback y worker durable. #37 añadió migration `0004`, staging durable separado de READY, sealed snapshot bundles, quarantine fail-closed, rechazo de final delta stale, binding a digest externo y commit READY atómico; merge `edad9e324132fa086ef729ef4faec574661578a9`, post-merge #272 (`33008305423`) PASS completo, probe #67 (`33008305463`) PASS y recovery artifact `sha256:8a7eb2ad2010da256a296ce66aa18f33e4d40153fda278a92da8d48fdc680e53`. #38 se cerró sin merge al quedar supersedido por #37. #39 añadió keyring versionado y `rotateStoredControlPlaneSecrets`; el restore aislado demuestra ciphertext-only, wrong/missing-key rejection, v7→v8 con round-trip y rollback atómico de una rotación fallida. Merge #39 `1a5cc387aef431cd5f5115ad537f55e80856fb08`; CI post-merge #274 (`33010599812`) PASS completo; probe #69 (`33010604236`) PASS; recovery artifact id `9622353539`, digest `sha256:0053159a8e21be62e62e72a6996b5ca7baf97ee857db7655d4f827ecd99fc93c`. #40 integró la frontera productiva software del provider de secretos: `@aws-sdk/client-secrets-manager@3.1116.0`, `development|aws-secrets-manager`, `AWSCURRENT`, payload `beatgaler-envelope-keyring-v1`, fail-closed y keyring multiversión; head `517ba593e8db2ee56f295cfbb739a74d7515ec1b`, CI pre-merge #283 (`33016505746`) PASS, merge `f997415c794c74ee1b86ef593476dba3587eeca1`, CI post-merge #285 (`33017201628`) PASS y probe #78 (`33017201608`) PASS. #42 endureció el parsing del keyring a base64 canónico; head `718efd9073144eb2fd89bfe2459ed2ac8996b079`, merge `a968122127c584b5557b25e70a21eb64f75b3c0e`, post-merge run `33118368302` PASS completo incluido `Required CI`. **Pendiente antes de `[x]`: infraestructura RDS/PostgreSQL + KMS/Secrets Manager/IAM real, backup cifrado + WAL/PITR/retención, smoke productivo del provider, restore independiente representativo con RPO/RTO demostrados y cutover/rollback productivo real.**
- **Equipo multi-cuenta:** `ORION` es dueño de `!!!PLAN` y coordinador normal de AAA/BBB; `ATLAS` es jefe técnico e integrador; `AAA` y `BBB` ejecutan paquetes independientes. ORION mantiene limpio el plan, consulta Issue #41, reasigna ayudantes automáticamente cuando queden libres y entrega `ATLAS NEXT`. ATLAS decide e integra lo técnico. BeatGaler Issue #41 conserva asignaciones/handoffs/blockers; `!!!PLAN` solo recibe estado confirmado y no debe duplicar logs/diffs que ya viven en GitHub.
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
2. Si el rol es **ORION**, leer después **todo el `!!!PLAN` operativo vigente completo**: contexto, roles, Fases 0–7, Gates, Registro y cualquier archivo operativo nuevo; excluir de mantenimiento `Plan Maestro 2208 copy DONT TOUCH .md`. Después consultar Issue #41 y GitHub solo en lo necesario para auditar estado/coordinar. Seguir la rutina de ORION definida en `Equipo multi-IA - Roles y coordinación.md`.
3. Si el rol es ATLAS/AAA/BBB, abrir la fase activa o la fase/tarea asignada y leerla completa; leer también `Equipo multi-IA - Roles y coordinación.md`.
4. Localizar la tarea exacta, sus dependencias, evidencia y gate de salida.
5. Si la decisión toca release/publicación, abrir `Gates - Publicación y contingencias.md`.
6. Hacer auditoría read-only del código/estado real cuando el rol y la tarea impliquen estado técnico. ORION no modifica código: audita el plan y consulta evidencia externa solo para sincronizarlo.
7. Explicar cambio exacto y razón antes de modificar.
8. Ejecutar cambio mínimo dentro del scope y autoridad del rol.
9. Ejecutar suites afectadas y revisar CI cuando exista cambio técnico.
10. Solo con evidencia: actualizar fase + este estado vivo + `Registro de avances.md`.

## Mapa de archivos del plan

| Archivo | Cuándo se lee | Contenido |
|---|---|---|
| **`Plan Maestro.md`** | **SIEMPRE, completo** | reglas, estado vivo, orden de trabajo y mapa |
| `Equipo multi-IA - Roles y coordinación.md` | cuando el usuario asigna ORION/ATLAS/AAA/BBB | autoridad por rol, higiene del plan, coordinación automática, asignaciones, handoffs e Issue #41 |
| `00 - Contexto global y criterios.md` | cuando una decisión necesita contexto global; **ORION lo lee siempre** | veredicto, evidencia, fechas, inventario, diseño, prioridades y roles |
| `Fase 0 - Contención e integración.md` | mientras Fase 0 esté activa; **ORION lee todas las fases siempre** | Días 0–5, incluida integración/CI/ADR |
| `Fase 1 - Seguridad cuentas y datos.md` | Fase 1; ORION siempre | Días 6–10 |
| `Fase 2 - Web y UX.md` | Fase 2; ORION siempre | Días 11–15, incluido el plan completo de YouTube Web en Tarea 15.3 |
| `Fase 3 - Producción pagos y operación.md` | Fase 3; ORION siempre | Días 16–20 |
| `Fase 4 - Desktop y release chain.md` | Fase 4; ORION siempre | Días 21–25 |
| `Fase 5 - Betas y RC.md` | Fase 5; ORION siempre | Días 26–30 |
| `Fase 6 - Lanzamiento.md` | Fase 6; ORION siempre | Días 31–35 |
| `Fase 7 - Estabilización.md` | Fase 7; ORION siempre | Días 36–41 |
| `Gates - Publicación y contingencias.md` | gates/go-no-go; **ORION siempre** | condiciones obligatorias, métricas, RACI, riesgos, contingencias y criterios |
| `Registro de avances.md` | al cerrar/actualizar trabajo; **ORION siempre** | historial cronológico de evidencia |
| `Plan Maestro 2208 copy DONT TOUCH .md` | solo comparación histórica explícita | copia protegida; nunca editar |

## Fuente de verdad y precedencia

Si dos textos parecen contradecirse, aplicar este orden:

1. Reglas inmutables y `Estado vivo` de `Plan Maestro.md`.
2. Gate/checklist de la fase activa.
3. `Gates - Publicación y contingencias.md` para condiciones de publicación.
4. `00 - Contexto global y criterios.md` como contexto histórico/estático.

Ningún archivo secundario puede rebajar un gate del principal. Una nueva decisión de producto debe actualizar primero el principal y después los archivos afectados. ORION es responsable de detectar contradicciones, pero no puede resolver por sí mismo una contradicción que requiera una decisión técnica nueva: la eleva a ATLAS y después sincroniza la decisión confirmada.