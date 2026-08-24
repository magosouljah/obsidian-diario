## upgrades
### arreglar
que la forma en la q ordenamos los beats se guarde 
osea si esta en name o rating se guarde para la proxima session


drop to set as cover funciona con cualquier archivo y no deberia ser asi

drag and drop de archivos mp3/wav para agregarlos como beat no sirve todavia

#### arreglar2
scheduler todavia el dia affecta la hora

*has q  tengan q clickear  continue o clickear en el siguiente de arriba para pasar al siguiente nivel perp q no se puedan saltar los pasos sino 1 por 1*
*pueden regresar pero si regresan y cambian algo otra vez tienen q dar click en continue*
*pero si no cambian nada pueden saltarse todos los pasos*


### Mejorar
mostrar solo los top 5 tags mas usados como sugerencia en el menu de edit meta data

SELECTED
aceptar right click para abrir menu con opciones como edit all o upload to youtube cuando hay varios beats selecionados

mejorar el shift select para q funcione como funciona en los archivos de windows osea q tambien puedes deselecionar si selecionas unos antes de ese nose como explicarlo
pero como funciona ahroa es q se seleccionan y no puedes deseleccionarlo aunq des shift click a unos beats antes de la seleccion y en archivos de windows si se puede


mejor edit all por el caso en el que quiera borrar algunos tags de todos los beats seleccionados
tengo entendido q como esta no puedo hacerlo



### agregar
agregar un boton q sea apply to all para q se ponga el preset en todos los beats

debajo de los beats aparecen los tags pero cuano no hay espacio no aparecen entonces yo lo que quiero es saber si estan los importantes los cuales son de colores entonces lo q podemos hacer es q ademas de los tags se vea un punto de color del tag q no se alcanza a ver

catche para q no se tenga q cargar todo otra vez o sea mas rapído


click derecho en algun tag de arriba y poder cambiar color(eso ya esta) y cambiar nombre
esto igual cambiaria el nombre del tag en todos los beats q lo tengan


# asd
### Tanda 1 — Estado global / velocidad (App.tsx)

**1. Persistir sort order**

- Guardo `sortBy` en localStorage con la misma lógica que `LIBRARY_CACHE_KEY` (otra key, ej `beatvault:sort:v1`).
- Al iniciar, leo ese valor para el `useState` inicial de `sortBy` en vez de arrancar siempre en `"name"`.
- Archivo: `App.tsx`.

**2. Carga más rápida al abrir la app**

- El cache local (`loadCachedBeats`) ya pinta instantáneo, el lag real está en el backend: `load_library` → `sync_library_from_disk` re-lee TODOS los ID3 de TODOS los mp3/wav en cada arranque, aunque nada haya cambiado.
- Plan: guardar en la DB un `mtime` (o hash rápido) por carpeta de beat. Si al escanear el mtime de la carpeta no cambió desde la última vez, uso los datos ya guardados en vez de releer el ID3 del archivo. Solo re-leo cuando la carpeta cambió (se editó, se agregó archivo, etc).
- Archivos: `commands.rs` (columna nueva en tabla `beats`, lógica en `sync_library_from_disk` / `build_from_disk`), `lib.rs` no cambia.

### Tanda 2 — BeatCard.tsx

**3. Drop cover: no resaltar en verde si no es imagen**

- El highlight verde se activa en `onDragOver` solo chequeando que haya "Files", sin mirar el tipo. El tipo real de archivo SÍ está disponible durante dragover vía `e.dataTransfer.items[i].type` (aunque el navegador a veces lo da vacío en algunos SO — lo manejo con fallback: si no puedo saber el tipo, no resalto en verde por las dudas).
- Cambio el chequeo de `imageDragOver` para que solo se active si el/los items son `image/*`.
- Archivo: `BeatCard.tsx`.

**4. Punto de color para tags que no entran**

- Debajo de la artwork se muestran `beat.tags.slice(0,3)`. Para los tags restantes que tengan color asignado (`tagColors`), agrego puntitos de color chiquitos después de los pills, uno por cada tag oculto-con-color (sin texto, solo el dot, con `title` al hover mostrando el nombre).
- Archivo: `BeatCard.tsx` (lee `useTagColors` de `tagColors.ts`, ya existe el hook).

### Tanda 3 — Selección múltiple (App.tsx + BeatCard.tsx)

**5. Right-click con selección múltiple**

- En `BeatCard.tsx`, `handleContextMenu` va a chequear si `selectMode && selected && selectedCount > 1` (necesito pasar `selectedCount` como prop desde `App.tsx`). Si es así, muestro un menú distinto: "Edit all", "Upload to YouTube (bulk)", "Remove all", en vez del menú individual.
- Los handlers de esas acciones ya existen en `App.tsx` (el toolbar de selección los tiene) — los paso como props nuevas a `BeatCard`.
- Archivos: `App.tsx`, `BeatCard.tsx`.

**6. Shift-click estilo Windows**

- Ahora mismo `lastSelectedIdx` se pisa en cada click normal, y el shift-click solo agrega el rango (nunca saca). En Windows, el shift-click recalcula el rango completo desde un "anchor" fijo hasta el ítem clickeado, reemplazando la selección de rango anterior — así si movés el shift-click "hacia atrás" se deseleccionan los que quedaron fuera del nuevo rango.
- Separo el concepto de `anchorIdx` (se fija en click normal, no en shift-click) de la selección actual. En cada shift-click, calculo el rango `[anchor, clickeado]` y seteo la selección a exactamente ese rango (no unión con lo anterior).
- Archivo: `App.tsx` (`handleToggleSelect`).

**7. Edit all: poder quitar tags**

- En `Drawer.tsx`, el modo bulk de tags hoy es "Add tags" / "Replace tags". Agrego un tercer modo "Remove tags": el usuario tipea/selecciona tags a quitar (reusando el mismo `TagEditor`, pero interpretado como "lista negra" en este modo) y al guardar se filtran esos tags de cada beat seleccionado en vez de agregarlos.
- `applyBulkUpdate` en `App.tsx` necesita un tercer caso en `tagsMode: "add" | "replace" | "remove"`.
- Archivos: `Drawer.tsx`, `App.tsx`.

### Tanda 4 — Tags (ui.tsx, Drawer.tsx, App.tsx, backend)

de la tanda 3 tambien necesito q cuando le demos en remove tags cuando editamos varios beats aparescan los tags q tienen en comun esos beats para seleccionarlos y si le damos acpetar se borren

**8. Top 5 tags sugeridos**

- Cambio `.slice(0, 8)` a `.slice(0, 5)` en `TagEditor` (`ui.tsx`). Trivial.

**9. Renombrar tag globalmente (con aviso + reescritura resumable/segura)**  
Esto es lo más pesado del pedido. Plan:

- **Frontend**: en el menú de click derecho sobre un tag (arriba, donde ya está el selector de color — `TagColorMenu` en `App.tsx`), agrego opción "Renombrar". Al confirmar nuevo nombre, muestro un modal de advertencia: "Esto va a reescribir metadata en N archivos, puede tardar. No cierres la app mientras tanto." con botón de confirmar.
- **Backend** (`commands.rs`, nuevo comando `rename_tag_everywhere`):
    - Busco todos los beats en DB cuyos tags (vía re-lectura rápida o cache) incluyan el tag viejo.
    - Antes de tocar nada, creo una carpeta de respaldo temporal (`appdata/.tag-rename-journal/<timestamp>/`) donde copio los mp3/wav originales que voy a modificar (o al menos un journal con la ruta + tag original, más liviano: guardo solo el string de tags original de cada archivo, no todo el archivo — así el rollback es "reescribir el TCON viejo", no restaurar el archivo entero, mucho más rápido y liviano en disco).
    - Proceso archivo por archivo, marco cada uno como "hecho" en el journal a medida que termino.
    - Si la app se cierra/crashea a mitad de camino, al reiniciar (en `lib.rs` setup, similar al auto-purge de trash) reviso si quedó un journal incompleto y hago rollback automático (reescribo el TCON original en los que habían quedado a medio hacer) antes de dejar usar la app normalmente.
    - Si todo termina bien, borro el journal.
    - Emito eventos de progreso (como el patrón de `youtube:started/done/error`) para mostrar una barra de progreso reusando el patrón de `JobStatusBar.tsx`/`jobStore.ts`.
- Archivos: `commands.rs` (comando nuevo + journal + rollback en `lib.rs` setup), `lib.rs` (registrar comando + chequeo de rollback al inicio), `tauri.ts` (wrapper), `App.tsx` (UI del modal de aviso + progreso), posiblemente reuso `jobStore.ts`/`JobStatusBar.tsx` para mostrar el progreso.

### Tanda 5 — UploadModal.tsx / UploadSchedulerNew.tsx

**10. Bug del scheduler + mínimo 30 min + toggle de "sin programar"**

- El bug: `changeField`/`commitTyped` usan `clampToMin(d, minDate)` que, cuando la fecha resultante es inválida, la reemplaza ENTERA por `minDate` (fecha Y hora), perdiendo la hora que el usuario había elegido. Lo correcto: si el día quedó inválido, lo clampeo al mínimo permitido, pero conservo la hora elegida si con ese día ya es válida; solo si sigue siendo inválida ahí sí ajusto la hora al mínimo.
- Cambio `minDate` default: en vez de "ahora", uso "ahora + 30 minutos" como piso real para agendar.
- Agrego un toggle explícito "Programar para después" / "Subir ahora" en el Step3 (arriba del calendario). Si está en "Subir ahora", el calendario se deshabilita/oculta y `scheduled_at` queda `null` sin depender de que el usuario haga click en "Clear".
- Archivos: `UploadSchedulerNew.tsx` (clamp logic + minDate+30min), `UploadModal.tsx` Step3 (el switch nuevo).

**11. Stepper: bloquear saltos si hay cambios sin confirmar**

- Agrego estado `dirty: boolean` y `furthestConfirmedStep: number` en `UploadModal.tsx`.
- Cualquier `updateJob`/`updateActive`/`updateTemplate` (o similar) marca `dirty = true`.
- Mientras `dirty`, el usuario NO puede clickear ningún tab del stepper que esté más adelante que el paso actual — ni siquiera el inmediato siguiente — hasta que:
    - Click en "Continue" (footer) → valida, avanza un paso, `dirty = false`.
    - Click en el tab del paso INMEDIATO siguiente → actúa igual que Continue (avanza y limpia dirty), pero solo si es el siguiente, no más allá.
- Si NO está dirty, puede clickear libremente cualquier tab ya visitado (adelante o atrás) sin restricciones.
- Ir hacia atrás (Back o click en tab anterior) siempre permitido, dirty o no.
- Archivo: `UploadModal.tsx` (componente principal, wiring de `dirty` hacia el stepper y el botón Continue).

**12. Botón "Apply to all" en la sección de presets**

- En el bloque de preset (`presetBlock` dentro de `Step2`), agrego un botón nuevo junto a "Template directory" y "Save": "Apply to all". Al click, fuerza `recomputeJobsFromTemplate(template, "all", ...)` y actualiza `jobPresetMap` para todos los jobs con el preset activo, sin necesidad de tocar el selector de scope.
- Archivo: `UploadModal.tsx` (`Step2`).






