# BeatGaler — Fix `stateSnapshot()` sync fs hot path

**Repo:** `magosouljah/BeatGaler`  
**Branch:** `stage1/real-multi-account-e2e`  
**Baseline verificado:** `cf940b9276fc0eb6d2a29f7657ab0d4a7bd5c3d2`  
**Archivo a editar:** `cloud-server/direct-transport-control.js`

## Objetivo

Evitar que una lectura de estado Direct fuerce una escritura durable completa a `transport-pool-state.json`.

Actualmente `stateSnapshot()` llama `writeJsonAtomic()`, que termina haciendo operaciones síncronas como `writeFileSync`, `fsyncSync` y `renameSync`. La corrida real de Stage 1 demostró que esto puede bloquear el event loop durante varios segundos.

`mutateState()` **sí debe seguir persistiendo**. Solo `stateSnapshot()` debe convertirse en lectura real.

## Reemplazo exacto

Busca exactamente este bloque:

```js
function stateSnapshot(pool) {
  return withPoolLock(() => {
    const state = normalizeState(pool);
    writeJsonAtomic(STATE_FILE, state);
    return state;
  });
}
```

Y reemplázalo por:

```js
function stateSnapshot(pool) {
  return withPoolLock(() => normalizeState(pool));
}
```

## No modificar

No cambies ninguna otra función en esta corrección.

En particular, deja `mutateState()` así:

```js
function mutateState(pool, mutator) {
  return withPoolLock(() => {
    const state = normalizeState(pool);
    const result = mutator(state);
    writeJsonAtomic(STATE_FILE, state);
    return result;
  });
}
```

Y **no tocar**:

```text
cloud-server/diagnostics/telegram-direct-control.txt
```

## Validación inmediata

Después de guardar el archivo:

```powershell
cd E:\777\app\beatvault # Entra al checkout correcto.

node --check cloud-server/direct-transport-control.js # Verifica que el archivo siga teniendo sintaxis JavaScript válida.

git diff -- cloud-server/direct-transport-control.js # Confirma que el único cambio sea quitar la escritura de stateSnapshot().
```

El diff esperado debe ser esencialmente:

```diff
 function stateSnapshot(pool) {
-  return withPoolLock(() => {
-    const state = normalizeState(pool);
-    writeJsonAtomic(STATE_FILE, state);
-    return state;
-  });
+  return withPoolLock(() => normalizeState(pool));
 }
```

## Después

Si el diff coincide, vuelve a correr primero la prueba real de **4 cuentas** antes de escalar a 10.

No aumentes timeouts y no reseedees la cohorte.
