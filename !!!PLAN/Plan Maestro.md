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

- **Fase actual:** Fase 0 — Contener, decidir y crear una sola línea de release. Sigue abierta por Tareas 2.2 `[ 🟡 ]` y 1.2 `[ 🟡 ]` aunque el frente técnico de datos ya llegó a cierre de evidencia.
- **Día/tarea actual:** Día 5 — **Tarea 5.1 cerrada `[x]`**; **Tarea 5.2 está `[ ⚠️ ]` — 4/4 criterios WAVE 3 satisfechos individualmente, pendiente únicamente de la síntesis global/marked `[x]` por WOZ/RO.** El siguiente P0 de Fase 0 es Tarea 2.2; Tarea 1.2 continúa en paralelo.
- **Estado general:** 🔴 `NO-GO` para lanzamiento público. Para 5.2, WAVE 3 ya produjo evidencia completa en sus cuatro frentes: **(1)** rollback/durabilidad aceptados independientemente; **(2)** restore representativo real con RPO ~7 min y RTO medido **3643 s = 1h 00m 43s**, aceptado independientemente por AAA; **(3)** rotación productiva multiversión aceptada por WOZ con key activa 2, versiones 1/2 retenidas y decrypt de datos v1 bajo keyring v2; **(4)** observabilidad/ownership aceptados por WOZ con alarmas RDS críticas enrutadas y `on-call owner`, `rotation operator` y `rollback/abort authority` definidos. JOBS no añade un quinto criterio: falta solo que WOZ/RO haga la síntesis global del gate y decida el `[x]`.
- **Último avance técnico confirmado:** segundo restore PITR aislado ejecutado exclusivamente para cerrar el RTO formal: `drill_start=2026-08-28 04:21:11 UTC`, `core_smoke_pass=2026-08-28 05:21:54 UTC`, RTO `3643s <=7200s`; AAA re-revisó y marcó criterio 2 `SATISFIED`. WOZ ya había aceptado criterios 3 y 4. No se autoriza repetir cutover, import JSON, migrations, restart de durabilidad, restore adicional ni otra rotación salvo nueva evidencia que invalide lo probado.
- **Próximo paso principal para WOZ:** **hacer únicamente la síntesis global de Tarea 5.2**: aceptar/rechazar el cierre 4/4 y, si no identifica un blocker nuevo real, marcar 5.2 `[x]`. Después, el frente principal permitido de Fase 0 pasa a **Tarea 2.2: decisión/ejecución controlada de purga histórica selectiva**, cuya auditoría AAA ya recomendó `GO`. No ejecutar la purga sin decisión WOZ/RO, write freeze, coordinación de refs/protecciones y limpieza GitHub-side.
- **Trabajo paralelo elegible:** `AAA` y `BBB` no tienen una nueva ejecución productiva WAVE 3 pendiente; quedan `LIBRE/BLOQUEADO POR DEPENDENCIA` hasta la síntesis WOZ/RO. Para 2.2 ya existe handoff read-only suficiente de AAA; no duplicarlo. Para 1.2 ya existe auditoría BBB; avanzar solo compromisos externos reales que el RO active. **Apple Developer = `PENDING — DEFERRED`**.
- **Bloqueos actuales:** **5.2 no tiene evidencia faltante dentro de sus cuatro criterios, pero no se marca `[x]` hasta la síntesis global WOZ/RO.** Tarea 2.2 sigue P0: AAA confirmó metadatos operacionales aún alcanzables en historial público y recomendó **GO para purga histórica selectiva/coordinada**; no hay evidencia de plaintext credential que justifique revoke por sí sola. Tarea 1.2 sigue P1: el repo público de distribución `magosouljah/galer` ya tiene releases alpha publicadas, pero el canal no está release-gate-ready (alphas observadas no prerelease/immutable, `galer:main` sin protección y tag público no ligado directamente al SHA fuente BeatGaler); dominio/DNS/support/status, Authenticode, revisión legal/seguridad independiente y matriz física siguen pendientes; Apple Developer está diferido. **Security follow-up nuevo:** durante troubleshooting de la rotación productiva se expuso un OAuth client secret en salida visible al operador; no se publicó en Issue #41, pero debe rotarse separadamente antes de release. Además siguen la deuda GPL `telegram@2.26.22` → `@cryptography/aes@0.1.1`, la regresión de carga inicial para 12.1, el gate de capacidad 2× y la revisión independiente externa.
- **BeatGaler integración:** rama `integration-v0.8.0-alpha.1`; HEAD integrado `a968122127c584b5557b25e70a21eb64f75b3c0e`; versión `0.8.0-alpha.1`.
- **Evidencia 3.2:** PR #8; commit de trabajo `818214889ef3c6f97a262a91046f7df0e4f723fe`; CI PR #64 PASS Windows + macOS arm64 + macOS x86_64; merge `32a38c490a53650a0e9d6435c50cd009ef1b5123`; CI post-merge #65 PASS.
- **Evidencia 4.1:** PR #9; commits de trabajo `e86ab19a7f3eef3a7036a50f8cb083add94c2292`, `a4f58943f222ef8f6a5c85a3e72142353fdf0a72` y `71a559dc4cdcb8e16159c709a7c2d0f64e61e5a0`; CI PR #68 PASS 5/5 incluido `Required CI`; merge `c7894ad3c2b3e296e3d2939d73953b159e48852f`; CI post-merge #70 PASS 5/5 incluido `Required CI`.
- **Evidencia 4.2:** PR #10; head final `902e4edf6f6f5d28f0f98922d5f22cc623c92f3d`; CI PR #100 (`32702389575`) PASS 6/6 incluido `Supply chain gate` y `Required CI`; artefacto `supply-chain-evidence` digest `sha256:d3b38c3be14ec01f0c283522049732a4e300588d8f0a9c588ec30221e0222419`; merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; árbol probado e integrado idéntico `9a7000f3f3a1840ebae0310ac3df6b827561f2c5`.
- **Evidencia 5.1 — CERRADA `[x]`:** PR #11 definió ADR/threat model/rollback; PR #12 retiró permission churn por evidencia de `FLOOD_WAIT`; PRs #13–#18 probaron M0-A/B/C/D, incluido bind split, identidad bot, renovación y **1,992,294,400 bytes** directos con `galer_cloud_file_bytes=0`; PR #23 probó Windows x86_64 + macOS arm64/x86_64; PR #24 probó Chrome + Web Worker real; PR #25 cerró delete reciente y documentó el límite >48 h; PR #26 cerró fair pool/admission max-4 + waitlist; PR #27 probó expiración natural/server-side; PR #28 migró el runtime productivo Web/Desktop y cerró discovery/ID3/CSP/headers/CORS/scopes. Head #28 `5119b3c6616b1a9c725bca1edad8e39036c4b463`; compile probe #32 (`32909324459`) PASS; CI PR #226 (`32909324476`) PASS 6/6; aprobación explícita RO 2026-08-25; merge `d9ae76f42faee3a7207b9232b7421a0bec20b090`; CI integrado #228 (`32912362077`) **PASS 6/6 incluido `Required CI`**. Riesgos residuales shared-bot y cleanup >48 h aceptados; revisión externa independiente continúa como gate global de release.
- **Evidencia 5.2 — LISTA PARA SÍNTESIS GLOBAL `[ ⚠️ ]`:** PRs #29–#42 integraron ADR/schema/migrations/envelope encryption/importador/garbage journal/PostgreSQL/runtime authority/cutover/rollback fail-closed/worker durable/keyring multiversión/AWS Secrets Manager/base64 canónico con CI integrado verde. WAVE 3 confirmó autoridad PostgreSQL productiva, restart durable y rollback dry-run desde CURRENT PG. **Criterio 1 SATISFECHO** por revisión independiente AAA. **Criterio 2 SATISFECHO**: restore PITR representativo real, RPO ~7 min y segundo restore con RTO `3643s`; AAA lo verificó independientemente. **Criterio 3 PASS/ACEPTADO por WOZ**: key activa 2 con 1/2 disponibles y lectura/decrypt de filas todavía cifradas con v1. **Criterio 4 PASS/ACEPTADO por WOZ**: alarmas críticas RDS enrutadas y ownership/rollback authority definidos. El primer intento de activar key 2 falló cerrado por JSON malformado y se recuperó antes del PASS. **No queda un quinto criterio técnico WAVE 3; WOZ/RO debe hacer la síntesis global y decidir `[x]`.**
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