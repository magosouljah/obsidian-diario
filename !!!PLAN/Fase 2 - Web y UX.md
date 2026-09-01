# Fase 2 — Flujos Web completos y rediseño de alto impacto

> GitHub/runtime vivo prevalece. Trabajo cross-phase solo con owner explícito y dependencias reales satisfechas.

**Baseline vivo CYCLE118:** `integration-v0.8.0-alpha.1 @ 43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`.

## Estado actual

11.1, 11.2 y 12.2 están cerrados.

### 12.1 — `[ 🟡 ] #92 + #94 + #95 INTEGRATED / PUBLIC RUNTIME STILL OPEN`

Evidence factual nueva:
- PR #92 MERGED → `ada77811059a3319b271dcc98dd5d95efe807dec`.
- PR #94 MERGED → `08e5802d27ad81977b1c2f63ceb0fce398d41e42`.
- PR #95 MERGED → `43fdf70efe6d12f47f0cd08f6eaaf6440e32f1d3`, parents `08e5802d... + 66f6b18e...`.
- #95 parte de runtime productivo post-#94: API-ID rejection había desaparecido, browser alcanzaba worker connection, pero la remote DC rechazaba el imported temporary auth key con transport 404 porque el bound `tempSessionId` se descartaba y mtcute creaba uno nuevo.
- #95 preserva el exact bound temporary Web session id through the browser-only bridge y lo restaura en primary MAIN antes de abrir socket; conserva el invariant de no enviar permanent application API ID/hash al browser.
- Exact-head observed workflows de #95: Web Production Build, Desktop Portability, D6, D7, productive temp-auth compile y F0/0.20 HEAD Secret Scan = SUCCESS; Upgrade 21.2 Staging = skipped/no aplicable.

**12.1 permanece NOT_PASS.** El propio #95 exige production runtime proof posterior. Falta verificar sobre deployment exacto post-#95:
1. `/web-health` sano y auth-health sano;
2. signed-out startup sin loader falso;
3. authenticated temporary auth + worker initialize/activate/verify usando el bound session id;
4. authoritative library index reload o error recuperable explícito;
5. cold/warm startup real cuantificado;
6. secondary upload/download pool behavior si aplica al gate;
7. cookie/marker/CSRF restore robustness y terminología pública residual aplicable.

Si owner/runtime access no está disponible, registrar blocker exacto; no fabricar PASS.

### 13.1 — `[ 🟡 ] FROZEN`
#69 Web y #70 Server siguen candidates históricos stale/frozen. REUSE semantics solo bajo scope explícito.

### 13.2 — `[ 🟡 ] PROVEN PRODUCT GAP / OWNER AAA114`

Review Save/Save All puede avanzar antes de durable completion/failure. `NIGHT-AAA-114` debe aplicar el mínimo corrective con success/close/advance solo tras durable completion; failure/conflict/retry visible; Save All partial per-item; focused Web/no-Tauri tests; bounded candidate; **NO MERGE**.

### 14.1 / 14.2
Playback y queue/browser evidence permanecen secundarios frente a startup/durability/security alpha blockers.

### 15.1 — `[ 🟡 ] BLOCKED ON RECENT-REAUTH PRODUCT SEAM`

BBB110 verificó que `SettingsPanel.emptyTrash` limpia estado optimistamente y no tiene strong confirmation ni una recent-reauth seam productiva consumible. La decisión D8 existe, pero falta la seam bounded.

**Owner CYCLE118: `NIGHT-BBB-113` únicamente para exponer/reusar la seam D8 mínima** de fresh same-provider authorization ligada a user/session, fail-closed y consumible por destructive callers. No Trash UI/purge en ese assignment. Después se reasigna 15.1 para strong confirmation + durable deterministic completion/failure sin false success.

### 15.2 / 15.3
A11y baseline visual y YouTube Web pure siguen pendientes. Web YouTube nunca depende de Tauri/helper Desktop.

**Principio:** evidence-before-claim; no falsear browser/runtime coverage.
