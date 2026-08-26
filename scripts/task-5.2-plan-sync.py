from pathlib import Path

phase = Path('!!!PLAN/Fase 0 - Contención e integración.md')
text = phase.read_text(encoding='utf-8')
marker = '### Tarea 5.2 [P0 · BE/OP] — Aprobar arquitectura de datos\n'
if marker not in text:
    raise SystemExit('Task 5.2 marker missing')
prefix = text.split(marker, 1)[0]
block = '''### Tarea 5.2 [P0 · BE/OP] — Aprobar arquitectura de datos

- [ 🟡 ] Aprobar una persistencia transaccional durable con migrations, constraints, backup/restore y rollback como requisito de producción. **Arquitectura aprobada; PostgreSQL live, migrations y recovery software ya tienen evidencia real. Falta infraestructura productiva/cutover antes de cerrar.**
- [ 🟡 ] **DECISIÓN APROBADA:** PostgreSQL será la autoridad durable del control-plane para cuentas, sesiones, providers, MFA, entitlements, jobs, auditoría y estado Direct/reconciliación/garbage que deba sobrevivir reinicios. El pinned Galer T-Library Schema v2 INDEX conserva la única autoridad lógica de la biblioteca.
- [ 🟡 ] Cifrado/migraciones/backup/RPO/RTO/rollback: envelope encryption + key version; migración snapshot/dry-run/import idempotente/freeze corto/final delta; rollback post-write exporta primero el estado PG actual. El drill aislado de restore ya funciona, pero **RPO <=15 min / RTO <=2 h productivos todavía requieren proveedor real + WAL/PITR/KMS y evidencia independiente.**
- [ 🟡 ] Reconciliación/garbage: implementación en progreso. El pinned INDEX gana; PG solo observa/repara forward; cleanup es post-commit durable; orphans se detectan tras safety window; `MESSAGE_DELETE_FORBIDDEN` nunca revierte INDEX ni resucita assets.

**Estado/evidencia 5.2 — EN PROGRESO:**
- PR #29 integró ADR, threat model y rollback. Integración tras #29: `6e3b34b6253ffc2686021cf7ac26a61936e5622e`; CI post-merge `32931602282` PASS y probe heredado 5.1 `32931602277` PASS.
- PR #30 añadió el schema PostgreSQL/control-plane y contrato de migrations; head probado `0b7ec35c2c9d1d5d049d01f59fb37b01305115e2`.
- PR #31 añadió migration runner/configuración y secret envelope; head `6cfd7601846ff6d63f1d8724680c1b3b23296409`.
- PR #32 añadió plan/importador legacy idempotente y garbage journal repository; head `1e9ded918895d9a9a6a9850cb3687d697a35fa3a`; baseline integrado posterior `f8e2858a267655d81367e304cd17f850113703a5`; CI post-merge #247 PASS.
- PR #33 `feat(data): run live PostgreSQL control-plane foundation`, head `df14472cbb6b25b23d7ab27e9c4315d2b8b52d92`, añadió `pg@8.23.0`, lock reproducible, bootstrap opt-in fail-closed y PostgreSQL 16 real como gate requerido. El primer run live detectó un race de primer arranque en `schema_migrations`; se corrigió adquiriendo advisory lock antes de crear/verificar ledger. CI PR #252 (`32943236736`) PASS completo y probe #52 (`32943236787`) PASS. Merge integrado `1c5127b30ec7ee11e65d82100bae7fc33a2aeb52`; CI post-merge #254 (`32944403636`) PASS completo y probe #53 (`32944403720`) PASS.
- La ampliación de Supply Chain detectó deuda **preexistente**: `telegram@2.26.22` arrastra `@cryptography/aes@0.1.1` GPL-3.0-or-later. No se aprobó GPL globalmente; el nuevo árbol `pg` tiene gate de licencias propio y el cloud-server completo sigue bajo audit/SBOM. La deuda legacy requiere revisión/resolución antes de release.
- Draft PR #34 `feat(data): prove reconciliation and PostgreSQL recovery drill`, head `103d1e4a1f1a1107935a88362238e5c42f8a64c0`, añade operaciones Direct durables/idempotentes, reconciliación PG forward-only desde pinned INDEX, orphan discovery conservador y exporter PG→legacy para rollback post-write.
- En CI #255 (`32945413572`) el job `PostgreSQL live integration + recovery gate` (`98104979741`) ya terminó PASS: dos PostgreSQL 16 aislados, persistencia adversarial, dump, cifrado temporal, restore en segunda instancia y verificación de constraints/secretos/INDEX observation/garbage debt/escritura post-migración. Artefacto `postgres-recovery-evidence` id `9598064802`, digest `sha256:09622af6bd0d663b328ce28cb2955245db9fd995d93428e9a2fdeeb3a8c07df1`; verifier restaurado reportó 40 ms. Esto prueba el mecanismo CI-scale, **no** RTO/RPO productivos. El CI completo de #34 debe quedar verde antes de merge.
- No hay cutover productivo, dual-write indefinido, autoridad PG sobre beats/trash/deleted, relay de media, cambio UI/Web/Desktop ni token revoke/rotation dentro de este trabajo.
- **Pendiente antes de cerrar 5.2:** CI/merge/post-merge de #34; cutover software default-off + rollback fail-closed; proveedor PostgreSQL/KMS real; backups cifrados + WAL/PITR/retención; prueba RPO <=15 min/RTO <=2 h en infraestructura independiente; cutover/rollback real; revisión de deuda legacy de licencia. No marcar `[x]` todavía.

**Dependencias:** contención terminada.  
**Evidencia:** ADR/threat model/rollback + PRs #29–#34 + migrations/schema/secret envelope/import/garbage + PostgreSQL 16 live + restore aislado.  
**Gate de salida:** arquitectura aprobada y software sensible probado no bastan por sí solos; 5.2 solo se cierra con persistencia/cutover/recovery productivos demostrados y rollback sin pérdida. **Permanece `[ 🟡 ]`.**
'''
phase.write_text(prefix + block, encoding='utf-8')

reg = Path('!!!PLAN/Registro de avances.md')
r = reg.read_text(encoding='utf-8').rstrip() + '\n'
entries = '''
- **2026-08-26 — Tarea 5.2: arquitectura #29 integrada y foundations #30–#32 acumuladas.** PR #29 quedó integrado como `6e3b34b6253ffc2686021cf7ac26a61936e5622e`; CI post-merge `32931602282` PASS y probe heredado `32931602277` PASS. PR #30 estableció schema/constraints/migration contract; #31 añadió runner/configuración y secret envelope; #32 añadió importador legacy idempotente y garbage journal repository. Head #32 `1e9ded918895d9a9a6a9850cb3687d697a35fa3a`; baseline integrado posterior `f8e2858a267655d81367e304cd17f850113703a5`; CI post-merge #247 PASS. El pinned INDEX continúa siendo la autoridad lógica de biblioteca y 5.2 sigue `[ 🟡 ]`.
- **2026-08-26 — Tarea 5.2: PostgreSQL live #33 integrado y race real corregido.** PR #33, head `df14472cbb6b25b23d7ab27e9c4315d2b8b52d92`, añadió `pg@8.23.0`, lock reproducible, bootstrap opt-in fail-closed y PostgreSQL 16 real dentro de `Required CI`. El primer gate live detectó un race al crear `schema_migrations` antes del advisory lock (`pg_type_typname_nsp_index`); se corrigió tomando el lock primero. CI #252 (`32943236736`) PASS completo, probe #52 (`32943236787`) PASS; merge `1c5127b30ec7ee11e65d82100bae7fc33a2aeb52`; CI post-merge #254 (`32944403636`) PASS completo y probe #53 (`32944403720`) PASS. Supply Chain amplió audit/SBOM del cloud-server y detectó deuda preexistente `telegram@2.26.22` → `@cryptography/aes@0.1.1` GPL-3.0-or-later; no se aprobó GPL globalmente y queda deuda legal/supply-chain separada del árbol `pg`.
- **2026-08-26 — Tarea 5.2: PR #34 prueba reconciliación y recovery software en PostgreSQL real.** Draft PR #34, rama `task-5.2-reconcile-recovery-batch`, head `103d1e4a1f1a1107935a88362238e5c42f8a64c0`, añade saga Direct durable/idempotente, reconciliación PG forward-only desde pinned INDEX, orphan detection tras safety window y exporter de rollback desde el estado PG actual. En CI #255 (`32945413572`) el job recovery `98104979741` PASS ejecutó dos PostgreSQL 16 aislados, dump→cifrado temporal→restore, preservó constraints, OAuth/MFA cifrados, INDEX observation, garbage debt y una escritura simulada posterior a migración. Verifier restore: 40 ms; artefacto `postgres-recovery-evidence` id `9598064802`, digest `sha256:09622af6bd0d663b328ce28cb2955245db9fd995d93428e9a2fdeeb3a8c07df1`. Esto no prueba WAL/PITR/KMS ni RPO/RTO productivos; el CI completo/merge de #34 sigue requerido y 5.2 permanece `[ 🟡 ]` / NO-GO.
'''
if 'PR #34 prueba reconciliación y recovery software' not in r:
    r += entries
reg.write_text(r, encoding='utf-8')

Path('.github/workflows/task-5.2-plan-sync.yml').unlink(missing_ok=True)
Path('scripts/task-5.2-plan-sync.py').unlink(missing_ok=True)
