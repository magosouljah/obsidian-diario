# BeatGaler — Plan Maestro para terminar y publicar Web, Windows y macOS

> **ESTE ARCHIVO SE LEE COMPLETO SIEMPRE ANTES DE TRABAJAR EN BEATGALER.**
> Después se lee completa la fase activa indicada en `Estado vivo del plan`. Los demás archivos solo se abren cuando la tarea actual los requiere, salvo JOBS, cuyo protocolo especial exige leer todo el `!!!PLAN` operativo vigente.

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
10. **COORDINACIÓN MULTI-CUENTA:** existen cuatro roles: `JOBS` (dueño de `!!!PLAN` y coordinador de AAA/BBB), `WOZ` (jefe técnico e integrador), `AAA` y `BBB` (ayudantes). Leer `Equipo multi-IA - Roles y coordinación.md` cuando se reciba uno de estos roles. **`Eres JOBS. Lee !!!PLAN y continúa.` es una invocación completa:** JOBS debe leer todo el `!!!PLAN` operativo vigente, auditar su limpieza/coherencia, consultar Issue #41, reasignar automáticamente a AAA/BBB cuando queden libres y entregar a WOZ el siguiente frente técnico permitido. JOBS nunca trabaja en archivos del programa ni infraestructura; sus únicas escrituras de archivos de repositorio son dentro de `!!!PLAN`. **`Eres WOZ. Lee !!!PLAN y continúa.` activa el liderazgo técnico.** Las personalidades de JOBS y WOZ están definidas en el archivo de roles y sirven al trabajo: foco/simplicidad/calidad para JOBS; curiosidad técnica/elegancia/prueba real para WOZ.

## Repos

- Plan: https://github.com/magosouljah/obsidian-diario
- BeatGaler: https://github.com/magosouljah/BeatGaler

**Versión del plan:** 1.4  
**Fecha de auditoría base:** 22 de agosto de 2026, `America/Mexico_City`  
**Última reorganización:** 27 de agosto de 2026, `America/Mexico_City` — roles JOBS/WOZ y coordinación automática de AAA/BBB  
**Hito original:** 4 de septiembre de 2026  
**Fecha pública recomendada:** 9 de octubre de 2026, condicionada a todos los gates  
**Ruta conservadora si una persona concentra la ejecución:** 30 de octubre de 2026  
**Alcance:** lanzamiento público directo desde la web, con aplicación Web y descargas firmadas para Windows y macOS.

## Estado vivo del plan

- **Fase actual:** Fase 0 — Contener, decidir y crear una sola línea de release.
- **Día/tarea actual:** Día 5 — **Tarea 5.1 cerrada `[x]`**; **Tarea 5.2 — Aprobar arquitectura de datos está `[ 🟡 ] / EN PROGRESO`**. Tarea 1.2 y 2.2 continúan en paralelo según sus gates.
- **Estado general:** 🔴 `NO-GO` para lanzamiento público. Tareas 4.1, 4.2 y 5.1 quedan cerradas con evidencia. En 5.2 el trabajo software-only exigible por el ADR está cubierto y el estado productivo ya avanzó: **PostgreSQL es la autoridad productiva del control-plane**, su durabilidad sobrevivió un reinicio controlado y existe un rollback dry-run construido desde el estado PostgreSQL actual. Esto no cierra 5.2: permanecen exactamente cuatro criterios de salida productivos/independientes definidos por WAVE 3. No iniciar tareas posteriores.
- **Último avance técnico confirmado:** **WAVE 3 de Issue #41 congeló el cierre de 5.2** sobre `integration-v0.8.0-alpha.1@a968122127c584b5557b25e70a21eb64f75b3c0e`. WOZ verificó que el control-plane productivo sigue en PostgreSQL tras terminación/restart controlado y que el proceso reiniciado vuelve a pasar el barrier fail-closed antes de servir. También ejecutó un rollback dry-run de solo lectura desde el estado PostgreSQL actual: reconstruyó y validó el snapshot de rollback sin escribir JSON, cambiar el marker de PostgreSQL ni imprimir secretos. **Ese dry-run aún requiere aceptación independiente y no equivale a un rollback productivo comprometido. 5.2 sigue `[ 🟡 ] / NO-GO`.**
- **Próximo paso principal para WOZ:** ejecutar el **restore independiente representativo** y medir evidencia real de **RPO <=15 min / RTO <=2 h**. Después, realizar solo las acciones productivas que queden justificadas por los handoffs WAVE 3. **No repetir cutover, import JSON, migrations ni la prueba de restart ya demostrada.**
- **Trabajo paralelo elegible:** WAVE 3 vive operativamente en BeatGaler Issue #41: `AAA` revisa de forma independiente la evidencia de durabilidad + rollback actual; `BBB` define/verifica readiness de observabilidad + rotación multiversión; `WOZ` conserva el lane activo de restore/RPO-RTO. Tareas 1.2 y 2.2 siguen siendo paralelos permitidos, pero no amplían los cuatro criterios de cierre de 5.2. **Apple Developer = `PENDING — DEFERRED`** hasta retomar su gate de firma/notarización. Las futuras asignaciones transitorias siguen viviendo en Issue #41 para no llenar el Plan Maestro con estado efímero.
- **Bloqueos actuales:** para **5.2** quedan **solo cuatro criterios de salida**: **(1)** aceptación independiente de la evidencia actual de rollback; **(2)** restore independiente representativo con RPO <=15 min y RTO <=2 h medidos; **(3)** evidencia productiva de rotación multiversión; **(4)** observabilidad, alertas, on-call y rollback authority asignados/probados. Fuera de 5.2 siguen pendientes la decisión de purga del historial Git de 2.2, dependencias externas de 1.2 —con Apple Developer diferido—, la regresión de tiempo de carga inicial registrada para 12.1 y el gate global de capacidad 2× con pico propuesto concreto. Riesgos residuales aceptados en 5.1: shared-bot fallback cross-vault cuando no haya bots libres y cleanup físico cross-bot >48 h como deuda durable de GC con INDEX como autoridad. Además, la auditoría ampliada de `cloud-server` encontró deuda preexistente de supply chain/licencia: `telegram@2.26.22` arrastra `@cryptography/aes@0.1.1` con GPL-3.0-or-later; no se aprobó GPL globalmente y debe resolverse/revisarse antes de release. La revisión independiente externa sigue pendiente como gate global.
- **BeatGaler integración:** rama `integration-v0.8.0-alpha.1`; HEAD integrado `a968122127c584b5557b25e70a21eb64f75b3c0e`; versión `0.8.0-alpha.1`.
- **Evidencia 3.2:** PR #8; commit de trabajo `818214889ef3c6f97a262a91046f7df0e4f723fe`; CI PR #64 PASS Windows + macOS arm64 + macOS x86_64; merge `32a38c490a53650a0e9d6435c50cd009ef1b5123`; CI post-merge #65 PASS.
- **Evidencia 4.1:** PR #9; commits de trabajo `e86ab19a7f3eef3a7036a50f8cb083add94c2292`, `a4f58943f222ef8f6a5c85a3e72142353fdf0a72` y `71a559dc4cdcb8e16159c709a7c2d0f64e61e5a0`; CI PR #68 PASS 5/5 incluido `Required CI`; merge `c7894ad3c2b3e296e3d2939d73953b159e48852f`; CI post-merge #70 PASS 5/5 incluido `Required CI`.
- **Evidencia 4.2:** PR #10; head final `902e4edf6f6f5d28f0f98922d5f22cc623c92f3d`; CI PR #100 (`32702389575`) PASS 6/6 incluido `Supply chain gate` y `Required CI`; artefacto `supply-chain-evidence` digest `sha256:d3b38c3be14ec01f0c283522049732a4e300588d8f0a9c588ec30221e0222419`; merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; árbol probado e integrado idéntico `9a7000f3f3a1840ebae0310ac3df6b827561f2c5`.
- **Evidencia 5.1 — CERRADA `[x]`:** PR #11 definió ADR/threat model/rollback; PR #12 retiró permission churn por evidencia de `FLOOD_WAIT`; PRs #13–#18 probaron M0-A/B/C/D, incluido bind split, identidad bot, renovación y **1,992,294,400 bytes** directos con `galer_cloud_file_bytes=0`; PR #23 probó Windows x86_64 + macOS arm64/x86_64; PR #24 probó Chrome + Web Worker real; PR #25 cerró delete reciente y documentó el límite >48 h; PR #26 cerró fair pool/admission max-4 + waitlist; PR #27 probó expiración natural/server-side; PR #28 migró el runtime productivo Web/Desktop y cerró discovery/ID3/CSP/headers/CORS/scopes. Head #28 `5119b3c6616b1a9c725bca1edad8e39036c4b463`; compile probe #32 (`32909324459`) PASS; CI PR #226 (`32909324476`) PASS 6/6; aprobación explícita RO 2026-08-25; merge `d9ae76f42faee3a7207b9232b7421a0bec20b090`; CI integrado #228 (`32912362077`) **PASS 6/6 incluido `Required CI`**. Riesgos residuales shared-bot y cleanup >48 h aceptados; revisión externa independiente continúa como gate global de release.
- **Evidencia 5.2 — EN PROGRESO `[ 🟡 ]`:** #29–#36 integraron ADR/schema/migrations/envelope encryption/importador/garbage journal/PostgreSQL 16/sagas/reconciliation/recovery/runtime authority/cutover controlado/rollback y worker durable. #37 añadió migration `0004`, staging durable separado de READY, sealed snapshot bundles, quarantine fail-closed, rechazo de final delta stale, binding a digest externo y commit READY atómico; merge `edad9e324132fa086ef729ef4faec574661578a9`, post-merge #272 (`33008305423`) PASS completo, probe #67 (`33008305463`) PASS y recovery artifact `sha256:8a7eb2ad2010da256a296ce66aa18f33e4d40153fda278a92da8d48fdc680e53`. #38 se cerró sin merge al quedar supersedido por #37. #39 añadió keyring versionado y `rotateStoredControlPlaneSecrets`; el restore aislado demuestra ciphertext-only, wrong/missing-key rejection, v7→v8 con round-trip y rollback atómico de una rotación fallida. Merge #39 `1a5cc387aef431cd5f5115ad537f55e80856fb08`; CI post-merge #274 (`33010599812`) PASS completo; probe #69 (`33010604236`) PASS; recovery artifact id `9622353539`, digest `sha256:0053159a8e21be62e62e72a6996b5ca7baf97ee857db7655d4f827ecd99fc93c`. #40 integró la frontera productiva software del provider de secretos: `@aws-sdk/client-secrets-manager@3.1116.0`, `development|aws-secrets-manager`, `AWSCURRENT`, payload `beatgaler-envelope-keyring-v1`, fail-closed y keyring multiversión; head `517ba593e8db2ee56f295cfbb739a74d7515ec1b`, CI pre-merge #283 (`33016505746`) PASS, merge `f997415c794c74ee1b86ef593476dba3587eeca1`, CI post-merge #285 (`33017201628`) PASS y probe #78 (`33017201608`) PASS. #42 endureció el parsing del keyring a base64 canónico; head `718efd9073144eb2fd89bfe2459ed2ac8996b079`, merge `a968122127c584b5557b25e70a21eb64f75b3c0e`, post-merge run `33118368302` PASS completo incluido `Required CI`. **WAVE 3 añade evidencia productiva confirmada sin nuevo cambio de código:** PostgreSQL ya opera como autoridad; el estado productivo sobrevivió un restart controlado manteniendo marker/fingerprints; y el rollback dry-run desde el estado PostgreSQL actual reconstruyó/validó un snapshot sin escribir JSON ni cambiar el marker. **Pendiente antes de `[x]`, y solo esto:** (1) aceptación independiente de rollback; (2) restore independiente representativo con RPO/RTO medidos; (3) rotación productiva multiversión; (4) observabilidad/alertas/on-call/rollback authority. No repetir cutover/import/migrations/restart.
- **Equipo multi-cuenta:** `JOBS` es dueño de `!!!PLAN` y coordinador normal de AAA/BBB; `WOZ` es jefe técnico e integrador; `AAA` y `BBB` ejecutan paquetes independientes. JOBS mantiene limpio el plan, consulta Issue #41, reasigna ayudantes automáticamente cuando queden libres y entrega `WOZ NEXT`. WOZ decide e integra lo técnico. BeatGaler Issue #41 conserva asignaciones/handoffs/blockers; `!!!PLAN` solo recibe estado confirmado y no debe duplicar logs/diffs que ya viven en GitHub.
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
2. Si el rol es **JOBS**, leer después **todo el `!!!PLAN` operativo vigente completo**: contexto, roles, Fases 0–7, Gates, Registro y cualquier archivo operativo nuevo; excluir de mantenimiento `Plan Maestro 2208 copy DONT TOUCH .md`. Después consultar Issue #41 y GitHub solo en lo necesario para auditar estado/coordinar. Seguir la rutina de JOBS definida en `Equipo multi-IA - Roles y coordinación.md`.
3. Si el rol es WOZ/AAA/BBB, abrir la fase activa o la fase/tarea asignada y leerla completa; leer también `Equipo multi-IA - Roles y coordinación.md`.
4. Localizar la tarea exacta, sus dependencias, evidencia y gate de salida.
5. Si la decisión toca release/publicación, abrir `Gates - Publicación y contingencias.md`.
6. Hacer auditoría read-only del código/estado real cuando el rol y la tarea impliquen estado técnico. JOBS no modifica código: audita el plan y consulta evidencia externa solo para sincronizarlo.
7. Explicar cambio exacto y razón antes de modificar.
8. Ejecutar cambio mínimo dentro del scope y autoridad del rol.
9. Ejecutar suites afectadas y revisar CI cuando exista cambio técnico.
10. Solo con evidencia: actualizar fase + este estado vivo + `Registro de avances.md`.

## Mapa de archivos del plan

| Archivo | Cuándo se lee | Contenido |
|---|---|---|
| **`Plan Maestro.md`** | **SIEMPRE, completo** | reglas, estado vivo, orden de trabajo y mapa |
| `Equipo multi-IA - Roles y coordinación.md` | cuando el usuario asigna JOBS/WOZ/AAA/BBB | autoridad por rol, personalidad operativa, higiene del plan, coordinación automática, asignaciones, handoffs e Issue #41 |
| `00 - Contexto global y criterios.md` | cuando una decisión necesita contexto global; **JOBS lo lee siempre** | veredicto, evidencia, fechas, inventario, diseño, prioridades y roles |
| `Fase 0 - Contención e integración.md` | mientras Fase 0 esté activa; **JOBS lee todas las fases siempre** | Días 0–5, incluida integración/CI/ADR |
| `Fase 1 - Seguridad cuentas y datos.md` | Fase 1; JOBS siempre | Días 6–10 |
| `Fase 2 - Web y UX.md` | Fase 2; JOBS siempre | Días 11–15, incluido el plan completo de YouTube Web en Tarea 15.3 |
| `Fase 3 - Producción pagos y operación.md` | Fase 3; JOBS siempre | Días 16–20 |
| `Fase 4 - Desktop y release chain.md` | Fase 4; JOBS siempre | Días 21–25 |
| `Fase 5 - Betas y RC.md` | Fase 5; JOBS siempre | Días 26–30 |
| `Fase 6 - Lanzamiento.md` | Fase 6; JOBS siempre | Días 31–35 |
| `Fase 7 - Estabilización.md` | Fase 7; JOBS siempre | Días 36–41 |
| `Gates - Publicación y contingencias.md` | gates/go-no-go; **JOBS siempre** | condiciones obligatorias, métricas, RACI, riesgos, contingencias y criterios |
| `Registro de avances.md` | al cerrar/actualizar trabajo; **JOBS siempre** | historial cronológico de evidencia |
| `Plan Maestro 2208 copy DONT TOUCH .md` | solo comparación histórica explícita | copia protegida; nunca editar |

## Fuente de verdad y precedencia

Si dos textos parecen contradecirse, aplicar este orden:

1. Reglas inmutables y `Estado vivo` de `Plan Maestro.md`.
2. Gate/checklist de la fase activa.
3. `Gates - Publicación y contingencias.md` para condiciones de publicación.
4. `00 - Contexto global y criterios.md` como contexto histórico/estático.
Ningún archivo secundario puede rebajar un gate del principal. Una nueva decisión de producto debe actualizar primero el principal y después los archivos afectados. JOBS es responsable de detectar contradicciones, pero no puede resolver por sí mismo una contradicción que requiera una decisión técnica nueva: la eleva a WOZ y después sincroniza la decisión confirmada.