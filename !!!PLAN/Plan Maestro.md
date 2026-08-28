# BeatGaler — Plan Maestro OPERATIVO

> **Objetivo:** terminar y publicar BeatGaler lo más rápido posible **sin rebajar gates reales**.
> Este archivo es el tablero de ejecución. El detalle técnico vive en la fase aplicable y en GitHub; no se duplica aquí.

## Lectura rápida obligatoria

### Para cualquier trabajo
1. Leer **este archivo completo**.
2. Leer **solo la fase activa** y la tarea que se va a ejecutar.
3. Consultar el estado actual necesario en GitHub / Issue #41.
4. Leer `Gates - Publicación y contingencias.md` **solo** cuando la tarea afecte release, seguridad, go/no-go o contingencias.
5. Abrir `00 - Contexto global y criterios.md`, fases futuras o documentación histórica **solo si la tarea lo necesita**.

### JOBS
`Eres JOBS. Lee !!!PLAN y continúa.` ya **NO significa releer Fases 0–7 + todo el Registro + todo Gates** en cada ciclo.

JOBS normalmente lee:
- `Plan Maestro.md`;
- fase activa;
- últimos avances relevantes;
- Issue #41.

JOBS hace auditoría completa de `!!!PLAN` solo al **cambiar de fase**, detectar una **contradicción/desincronización**, aparecer un **gate nuevo real**, o por petición explícita del usuario.

### Archivo protegido
`Plan Maestro 2208 copy DONT TOUCH .md` es histórico. **No modificar ni usar como plan vigente.**

---

## Reglas no negociables

1. No saltar dependencias ni gates reales.
2. No marcar `[x]` sin evidencia verificable.
3. Antes de un cambio técnico: auditoría read-only del estado real.
4. Después de un cambio técnico relevante: pruebas afectadas + CI aplicable.
5. Cada avance que cambie estado actualiza: **Plan Maestro + fase activa + Registro de avances**.
6. No duplicar logs/diffs extensos en `!!!PLAN`; usar PR, Actions e Issue #41 como evidencia detallada.
7. Ningún P0/P1 abierto al publicar.
8. JOBS solo modifica `!!!PLAN`; WOZ decide/ejecuta código, arquitectura e infraestructura.
9. En ejecuciones automáticas/turno nocturno aplica obligatoriamente `Equipo multi-IA - Roles y coordinación.md` → **Modo autónomo / turno nocturno**: preflight factual, idempotencia, evidence-before-claim, STOP conditions, gate transaction y watchdog de 3 ciclos sin progreso.

**Precedencia si hay conflicto:** Estado/reglas de este Plan → gate/checklist de fase activa → Gates → Contexto. GitHub/runtime decide los hechos técnicos actuales.

---

## Estado vivo — AHORA

- **Fase activa:** **Fase 1 — Seguridad, cuentas y datos durables**.
- **Día activo:** **Día 6 — Autorización tenant y abuso**.
- **Release público:** 🔴 `NO-GO`.
- **Modo autónomo nocturno:** **ACTIVO** para los roles configurados por el RO, bajo el protocolo endurecido de `Equipo multi-IA - Roles y coordinación.md`. No altera roadmap, gates ni autoridad de roles.
- **BeatGaler:** `integration-v0.8.0-alpha.1` @ `b9c2317297ff3c0f7a6246ac97517fa978f6caea`, versión `0.8.0-alpha.1`.
- **Required CI post-rewrite:** run **#314** (`33148873459`) = `SUCCESS` sobre `b9c2317297ff3c0f7a6246ac97517fa978f6caea`.
- **Tarea 5.1:** `[x]`.
- **Tarea 5.2:** `[x]` — **CERRADA por síntesis WOZ/RO** en Issue #41 comment `5448976400`. Los 4/4 criterios WAVE 3 quedaron aceptados. No repetir restore/cutover/migrations/durability restart/key rotation para 5.2 salvo evidencia nueva que invalide el resultado.
- **Tarea 2.2:** `[ 🟡 ]` — **tail externo no bloqueante / pendiente de cierre administrativo**. El trabajo técnico necesario para avanzar ya terminó; quedan exclusivamente (1) limpieza server-side por GitHub Support y (2) verificación final de inaccesibilidad de refs/commits históricos. **No marcar `[x]`** hasta tener ambas evidencias. Por decisión explícita del RO, este tail **NO bloquea Fase 1**.
- **Tarea 1.2:** `[ 🟡 ]` **P1 / paralelo externo de release**. Release governance, dominio/DNS/support/status, Authenticode, revisión legal/seguridad independiente y matriz física/testers siguen pendientes. Apple Developer = `PENDING — DEFERRED`. No bloquea la ejecución interna de Fase 1; sí conserva sus gates de release.
- **Fase 0:** trabajo técnico necesario para avanzar concluido; conserva pendientes administrativos/externos sin declararse `[x]` mientras 2.2/1.2 sigan abiertos.
- **Decisión RO vigente:** Fase 1 queda autorizada desde ahora; esto **no** altera el `NO-GO` de publicación.

### Fase 0 — tablero residual

| Tarea | Estado |
|---|---|
| 0.1 Congelar evidencia | [x] |
| 0.2 Checkpoint interno / NO-GO | [x] |
| 1.1 Decisiones de negocio | [x] |
| 1.2 Dependencias externas de release | [ 🟡 ] P1 / externo |
| 2.1 Contención inmediata | [x] |
| 2.2 Historial Git / incidente | [ 🟡 ] tail externo no bloqueante |
| 3.1 Base integrada | [x] |
| 3.2 Contrato plataforma | [x] |
| 4.1 Required CI | [x] |
| 4.2 Supply chain | [x] |
| 5.1 Trust boundary / Direct | [x] |
| 5.2 PostgreSQL + recovery + secrets | [x] |

---

## Fase 1 — orden obligatorio de ejecución

`6.1 ∥ 6.2` → **Gate D6** → `7.1 ∥ 7.2` → **Gate D7** → `8.1 ∥ 8.2` → **Gate D8** → `9.1 ∥ 9.2` → **Gate D9** → `10.1` → `10.2`.

**Regla:** el paralelismo existe únicamente dentro del mismo Día. **No iniciar un Día posterior antes de que WOZ/RO acepte el gate anterior.**

### AHORA — Día 6 / WAVE F1-A

- **WOZ — PRIMARY:** 6.1 — Unificar middleware de autorización; integrar compatibilidad con 6.2 y decidir técnicamente el cierre de Día 6.
- **AAA:** 6.2 — Abuse controls + suite adversarial.
- **BBB:** 6.1 — auditoría/review independiente del authorization boundary, inicialmente **READ ONLY**.
- **JOBS:** coordinar handoffs, mantener `!!!PLAN` y entregar `WOZ NEXT`.

### Gate D6 requerido

- identidad `user / installation / tenant` derivada de sesión validada;
- auth + autorización + límites antes de trabajo costoso;
- ownership por objeto;
- matriz `401 / 403 / 413 / 429`;
- pruebas cross-tenant;
- **cero acceso o mutación cross-tenant** en suite adversarial.

**Hasta D6 PASS:** no iniciar 7.1 ni 7.2.

**Después de D6 PASS:** AAA → 7.2; BBB → review independiente de 7.1; WOZ → 7.1 + integración.

---

## REUSE-FIRST obligatorio para 9.x y 10.x

Antes de ordenar trabajo nuevo, mapear cada requisito contra evidencia válida ya aceptada en Fase 0 / 5.2.

Reutilizar cuando satisfaga **exactamente** el requirement:
- PostgreSQL como autoridad productiva;
- migrations/versionado/constraints;
- importer/idempotencia/rollback;
- durabilidad;
- PITR restore representativo;
- RPO ~7 min;
- RTO `3643 s`;
- keyring multiversión;
- observabilidad/ownership.

**No repetir** restore, cutover, migrations, durability restart ni key rotation únicamente para recrear evidencia ya aceptada. Solo un `GAP` literal genera trabajo nuevo.

---

## Tail de Fase 0 que sigue abierto sin bloquear Fase 1

### 2.2 `[ 🟡 ]` — cierre administrativo externo

Pendiente únicamente:
1. GitHub Support completa limpieza server-side de referencias/caches históricas aplicables.
2. Fresh verification final demuestra inaccesibilidad de refs/commits históricos afectados.
3. Solo entonces JOBS puede sincronizar 2.2 a `[x]` con evidencia.

El post-rewrite baseline `b9c2317297ff3c0f7a6246ac97517fa978f6caea` y Required CI #314 `SUCCESS` son la base técnica vigente de Fase 1.

### 1.2 `[ 🟡 ]` — release externo

Seguir en paralelo sin distraer Día 6:
- corregir governance/provenance del canal público de releases;
- dominio/DNS/support/status;
- Windows Authenticode;
- reservas de revisión legal + seguridad independiente;
- matriz anónima 12–20 testers / hardware físico;
- Apple Developer sigue diferido hasta reactivación explícita.

### Security follow-up antes de release

Rotar el OAuth client secret que fue visible al operador durante troubleshooting de WAVE 3. Su valor **no** debe registrarse en GitHub/`!!!PLAN`.

---

## Evidencia compacta que no se debe reabrir

### 5.1 `[x]`
PRs #11–#28. Temporary auth productiva Web/Desktop; secretos permanentes no llegan al cliente. Transferencia directa probada de **1,992,294,400 bytes** con `galer_cloud_file_bytes=0`. Riesgos residuales shared-bot fallback y cleanup >48 h aceptados/documentados.

### 5.2 `[x]`
PRs #29–#42 + WAVE 3:
- PostgreSQL = autoridad productiva; rollback/durabilidad aceptados independientemente;
- restore PITR representativo: **RPO ~7 min**, **RTO 3643 s**;
- keyring productivo multiversión: activa `2`, versiones `1,2`, lectura de ciphertext v1 verificada;
- alarmas RDS críticas + on-call/rotation/rollback authority aceptados;
- cierre global WOZ/RO: Issue #41 comment `5448976400`.

---

## Bloqueos de release que siguen vivos

No bloquean por sí mismos la ejecución interna de Día 6, pero **sí bloquean publicación cuando aplique**:
- 2.2 hasta cierre administrativo final;
- 1.2 release governance/dependencias externas;
- OAuth secret rotation de seguimiento;
- deuda GPL `telegram@2.26.22` → `@cryptography/aes@0.1.1`;
- regresión de carga inicial asociada a 12.1;
- capacity gate 2×;
- revisión independiente externa;
- firma/notarización y pruebas físicas antes de anunciar soporte público de cada plataforma.

---

## Invariantes de producto/arquitectura

- Telegram es implementación interna oculta; UI habla de **Cloud / Galer Cloud / Storage / Library**.
- Schema visible/interno preferido: **Galer T-Library Schema v2**.
- Web es una app Web pura: **sin Tauri ni Desktop helper**.
- Media viaja **device ↔ provider directo**; Galer Cloud no relaya bytes de beats/proyectos.
- Permanent auth/control secrets permanecen control-side; cliente usa temporary auth.
- Shared-bot es fallback solo cuando no hay bots libres; exclusividad por vault es el camino normal.
- BeatGaler v1 no se publica como free-only; si billing no pasa gates, se retrasa.
- YouTube es objetivo v1 tanto en Desktop como Web y Web no puede resolverlo llamando Tauri.

---

## Roles mínimos

- **JOBS:** dueño de `!!!PLAN`, prioridad, limpieza y coordinación AAA/BBB. No toca producto/infra.
- **WOZ:** jefe técnico e integrador; decide arquitectura, implementación, infraestructura y aceptación técnica.
- **AAA / BBB:** paquetes independientes; no cambian gates ni marcan tareas `[x]` por sí solos.
- **Issue #41:** coordinación/handoffs/blockers. No duplicar allí ni aquí datos secretos.
- **Modo autónomo:** los cuatro roles deben obedecer preflight factual, idempotencia, evidence-before-claim, STOP conditions, gate transaction y watchdog definidos en `Equipo multi-IA - Roles y coordinación.md`.

Detalles solo cuando hagan falta: `Equipo multi-IA - Roles y coordinación.md`.

---

## Estados

`[ ]` pendiente · `[ 🟡 ]` en progreso · `[ ⚠️ ]` técnicamente hecho pero gate/evidencia pendiente · `[ 🔴 ]` bloqueado · `[ ⏸️ ]` pausado · `[x]` cerrado con evidencia.

---

## Mapa de fases

- **Fase 0:** `[ 🟡 ]` residual/administrativa; trabajo técnico necesario para avanzar concluido. 2.2 conserva tail externo no bloqueante y 1.2 conserva dependencias de release.
- **Fase 1:** **ACTIVA — Día 6**.
- **Fases 2–7:** no ejecutar todavía. Se activan una por una después de sus dependencias/gates.

**Principio de velocidad:** si una información no cambia prioridad, dependencia, gate, riesgo aceptado, evidencia o NEXT, no pertenece al camino operativo del Plan Maestro.