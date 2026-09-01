# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE117:** `integration-v0.8.0-alpha.1 @ 08e5802d27ad81977b1c2f63ceb0fce398d41e42`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] #92 + #94 INTEGRATED / PUBLIC RUNTIME STILL OPEN`

Evidence factual nueva:
- PR #92 está MERGED como `ada77811059a3319b271dcc98dd5d95efe807dec`.
- PR #94 está MERGED como `08e5802d27ad81977b1c2f63ceb0fce398d41e42`, parents `ada77811059a3319b271dcc98dd5d95efe807dec + b245aea738ab111992b1efd874ae7db25cd91aac`.
- #94 mantiene browser permanent application API ID/hash en cero/vacío y modela la sesión temporal ya bound/initialized para evitar `CONNECTION_API_ID_INVALID`; también corrige el wrapper PowerShell deploy y sus health checks.
- #94 no declara por sí mismo runtime PASS; su propio PR exige production runtime proof posterior.

**12.1 permanece NOT_PASS.** Falta verificar sobre el deployment exacto post-#94:
1. `/web-health` sano y auth-health sano;
2. signed-out startup sin loader falso;
3. authenticated temporary auth + worker initialize/activate/verify;
4. authoritative library index reload o error recuperable explícito;
5. cold/warm startup real cuantificado;
6. cookie/marker/CSRF restore robustness y terminología pública residual aplicable.

Si el owner/runtime access no está disponible, registrar blocker exacto; no fabricar PASS.

### 13.1 — `[ 🟡 ] FROZEN`
#69 Web y #70 Server siguen candidates históricos stale/frozen. REUSE semantics solo bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP / OWNER AAA113`

Review Save/Save All puede avanzar antes de durable completion/failure. `NIGHT-AAA-113` debe aplicar el mínimo corrective con success/close/advance solo tras durable completion; failure/conflict/retry visible; Save All partial per-item; focused Web/no-Tauri tests; bounded candidate; **NO MERGE**.

### 14.1 / 14.2
Playback y queue/browser evidence permanecen secundarios frente a startup/durability/security alpha blockers.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH PRODUCT SEAM`

BBB110 verificó que `SettingsPanel.emptyTrash` hoy limpia estado optimistamente y no tiene strong confirmation ni una recent-reauth seam productiva consumible. Implementar Trash directamente exigiría tocar auth/session core, por lo que hizo STOP correcto.

**Owner CYCLE117: `NIGHT-BBB-112` únicamente para exponer/reusar la seam D8 mínima** de fresh same-provider authorization ligada a user/session, fail-closed y consumible por destructive callers. No Trash UI/purge en ese assignment. Después se reasigna 15.1 para strong confirmation + durable deterministic completion/failure sin false success.

### 15.2 / 15.3
A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; no falsear browser/runtime coverage.
