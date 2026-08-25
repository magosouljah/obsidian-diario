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
# Sube tus cambios locales
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
- **Día/tarea actual:** Día 5 — Tarea 5.1 — Aprobar límites de confianza; Tarea 1.2 y 2.2 continúan en paralelo según sus gates.
- **Estado general:** 🔴 `NO-GO` para lanzamiento público. Tareas 4.1 y 4.2 quedan cerradas con pipeline obligatorio reproducible y supply chain conocida cubierta por gates automáticos; siguen abiertos P0/P1 posteriores y dependencias externas.
- **Último avance:** M0-H de expiración natural/server-side de temporary auth queda probado en el draft PR BeatGaler #27, rama `task-5.1-temp-auth-natural-expiry-probe`, head `4ddd6052f0fee7e2b6c82e3f2ebb86610b4c1f3e`. Temp A con TTL de 60 s funcionó antes de `expires_at`; sin reset local, revoke ni rotation, la misma A fue rechazada dos veces después de su expiración natural con `400:TIMEOUT`; una Temp B fresca volvió a funcionar con la misma identidad bot. Workflow dedicado `32895996417`, job `97958708150`, PASS y artefacto `natural-expiry-evidence` digest `sha256:39d0159d6c8cc44a6d06219080aa1b9afc2883033ebd6cf92e553165856cc4a2`. CI normal #193 (`32896306047`) terminó **PASS 6/6**, incluido `Required CI`, Web/shared, supply chain, Windows, macOS arm64 y macOS x86_64. No se tocó runtime productivo, vaults/datos reales ni token rotation/revoke. Esta evidencia retira la expiración natural como incógnita técnica, pero no cierra 5.1 ni cambia el `NO-GO`.
- **Próximo paso principal:** migrar el runtime productivo Web/Desktop al modelo temporary-auth sin credenciales permanentes compartidas; después cerrar discovery/hardening restante y revisión independiente. **No iniciar Tarea 5.2 todavía.**
- **Trabajo paralelo vigente:** Tarea 1.2 (dominio, Apple Developer, Authenticode, revisiones/hardware) y reauditoría diferida de Tarea 2.2.
- **Bloqueos actuales:** historial Git antiguo de información operacional aún pendiente de decisión de purga; dominio, Apple Developer, Authenticode y revisiones externas de 1.2 pendientes; regresión de tiempo de carga inicial de librería registrada para 12.1; 5.1 no puede aprobarse hasta completar migración productiva sin credencial compartida, discovery/hardening restante y revisión independiente. La expiración natural/server-side ya quedó probada por M0-H y deja de ser bloqueo pendiente. El gate global de capacidad 2× continúa siendo un gate de release separado y requiere un pico propuesto concreto. El shared-bot fallback queda registrado como riesgo residual aceptado por el RO y debe permanecer excepcional/observable; no se tratará como aislamiento cross-vault demostrado. El cleanup físico cross-bot >48 h queda registrado como limitación/deuda de GC futura, no como blocker funcional de 5.1, porque el INDEX es la autoridad y 5.2 ya exige reconciliación + garbage journal.
- **BeatGaler integración:** rama `integration-v0.8.0-alpha.1`; merge 4.2 `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; versión `0.8.0-alpha.1`.
- **Evidencia 3.2:** PR #8; commit de trabajo `818214889ef3c6f97a262a91046f7df0e4f723fe`; CI PR #64 PASS Windows + macOS arm64 + macOS x86_64; merge `32a38c490a53650a0e9d6435c50cd009ef1b5123`; CI post-merge #65 PASS.
- **Evidencia 4.1:** PR #9; commits de trabajo `e86ab19a7f3eef3a7036a50f8cb083add94c2292`, `a4f58943f222ef8f6a5c85a3e72142353fdf0a72` y `71a559dc4cdcb8e16159c709a7c2d0f64e61e5a0`; CI PR #68 PASS 5/5 incluido `Required CI`; merge `c7894ad3c2b3e296e3d2939d73953b159e48852f`; CI post-merge #70 PASS 5/5 incluido `Required CI`.
- **Evidencia 4.2:** PR #10; head final `902e4edf6f6f5d28f0f98922d5f22cc623c92f3d`; CI PR #100 (`32702389575`) PASS 6/6 incluido `Supply chain gate` y `Required CI`; artefacto `supply-chain-evidence` digest `sha256:d3b38c3be14ec01f0c283522049732a4e300588d8f0a9c588ec30221e0222419`; merge `f6d1f998bd63589ec2ddad7ee4d5818e9b85f016`; árbol probado e integrado idéntico `9a7000f3f3a1840ebae0310ac3df6b827561f2c5`.
- **Evidencia 5.1 (en progreso):** PR #11 `security: define Task 5.1 trust boundaries`; head inicial `5cdcfcecccea63a31adc5eaf66416929c0fbb95a`; CI #103 PASS 6/6. Head documental corregido `bb162c01c80e21a264c4022c9c682a90c14fbb98`; CI #108 PASS 6/6 incluido `Required CI`. PR #12 `test(security): probe Telegram admin-rights churn`, head `2b8904880dfeaa57b970674a79abcb181161af0a`, CI #105 PASS 6/6; prueba riesgo de churn, no una cifra universal. PR #13 `test(security): prove M0 temp-auth binding boundary`, draft, head `96af35e85481ff85d856dc22949bfb314ebedc3e`; CI #109 PASS 6/6 incluido `Required CI`. PR #14 `test(security): audit mtcute seam for M0-B`, head `9bd8bee1eda87cbeab051a3937ef95f6c4884ec4`; CI #111 PASS 6/6. PR #15 `test(security): prove M0-B1 split temp-auth bind`, head `2b942deea108fc4818bbb1c088db2f144f3c42c0`; live PASS y CI #117 PASS 6/6. PR #16 `test(security): prove M0-B2 bot temp-auth identity`, head `5ff0d70edd6c4ac11ff54bbd52a68246342130ac`; workflow `32789070730` PASS y CI #130 PASS 6/6. PR #17 `test(security): prove M0-C temp-auth renewal`, head `64308f3297304907972e777200db04b38119c7c0`; workflow `32791160563` PASS y CI #132 PASS 6/6. PR #18 `test(security): prove M0-D direct 1.9GB data plane`, head `ca4c312784242c6d7bc98bc5c55b458823d2de23`; workflow `32796833343` PASS con 1,992,294,400 bytes y CI #136 PASS 6/6. PR #23 `test(security): prove temp auth across Windows and macOS`, head `8ea250cf7b71dda6d09fd408deb473a9151e7d2e`; workflow #173 (`32827228117`) PASS live en Windows x86_64, macOS arm64 y macOS x86_64. PR #24 `test(security): prove M0-E2 Web temp auth in browser worker`, head `d69248492a8be4d37f376440d28e03e47e5b0d68`; workflow `32829804778` PASS en Chrome/Web Worker real y CI normal #176 (`32829804659`) terminó PASS incluido `Required CI`. PR #25 `test(security): probe M0-F delete permission boundary`, rama `task-5.1-delete-permission-probe`: negativo live PASS (`own_delete_without_admin_proven=true`, `cross_bot_delete_without_admin_denied=true`); CI #180 (`32831177470`) PASS. Rerun live final del workflow M0-F, run `32877055196`, job `97900929779`, PASS: sesión MTProto antes de membership, vault privado aprendido por la misma sesión y delete cross-bot reciente ejecutado sin MASTER por archivo. El probe >48 h en run `32880457856`, job `97908382881`, llegó a `channels.deleteMessages` y falló con `MESSAGE_DELETE_FORBIDDEN`; se registra como límite real/deuda futura de GC y no como requisito de cierre de 5.1. Decisión RO 2026-08-25: exclusividad por vault es preferida pero no obligatoria; shared-bot queda permitido únicamente como fallback cuando el pool no tenga bots libres, conservando reparto justo por carga y aceptando explícitamente el riesgo residual cross-vault de una identidad temporal no scoped por vault. M0-G / draft PR #26, head `f39578ab0afe40448566087edfdbb62a2c80967a`: caracterización `32891545205` PASS; implementación/admission workflow final `32891823812` PASS; máximo 4 vaults/bot, waitlist bounded, recuperación y observabilidad probadas sin Telegram real ni datos reales; CI normal #192 (`32891830172`) PASS 6/6 incluido `Required CI`. M0-H / draft PR #27, head `4ddd6052f0fee7e2b6c82e3f2ebb86610b4c1f3e`: Temp A TTL 60 s funcionó antes de expiry, fue rechazada dos veces tras expiry natural sin reset/revoke/rotation y Temp B fresca restauró la misma identidad; workflow `32895996417` PASS, artefacto `natural-expiry-evidence` digest `sha256:39d0159d6c8cc44a6d06219080aa1b9afc2883033ebd6cf92e553165856cc4a2`; CI normal #193 (`32896306047`) PASS 6/6 incluido `Required CI`. Ningún checkbox 5.1 queda cerrado todavía.
- **Regla GitHub de integración:** PR obligatorio; `Required CI` es el único status check requerido y agrega Web/shared + supply chain + Windows + macOS arm64/x86_64; la rama debe estar actualizada antes de merge; `Required approvals = 0` porque existe un solo maintainer. Esto **no elimina** los reviewers independientes exigidos más adelante por gates de security/legal/firma/release.

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