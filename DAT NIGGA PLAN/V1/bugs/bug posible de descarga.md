Es una **inconsistencia entre lo que la UI considera descargable y lo que el downloader Web realmente puede descargar**.

Actualmente `CloudFilesModal.tsx` decide si habilitar cada botón así:

```
const hasMp3 =
  Boolean(beat.assets?.master) ||
  Boolean(beat.telegram_file_id) ||
  Boolean(beat.offline_available && beat.mp3_path);

const hasWav =
  Boolean(beat.assets?.wav) ||
  Boolean(beat.offline_available && beat.wav_path) ||
  files.some(file => file.file_type === "WAV");

const hasProject =
  Boolean(beat.assets?.project) ||
  Boolean(beat.offline_available && (beat.flp_path || beat.als_path)) ||
  files.some(file => file.file_type === "PROJECT");
```

Es decir, el modal acepta **varias fuentes de evidencia** para decir “sí, este archivo existe”.

Pero Web usa otro criterio.

`WebDownloadsManager` crea los archivos descargables exclusivamente desde:

```
beat.assets?.master
beat.assets?.wav
beat.assets?.artwork
beat.assets?.project
```

más `beat.image_base64` para artwork. Después filtra y conserva solamente refs cuyo `object_id` tenga exactamente el formato:

```
direct:<message_id>
```

Por ejemplo:

```
direct:12345
```

Si no existe ese `direct:<id>`, ese asset desaparece de la lista que puede descargar Web.

### MP3

El modal dice que MP3 existe si encuentra **cualquiera** de estas tres cosas:

```
beat.assets.master
telegram_file_id
offline_available + mp3_path
```

Pero el downloader Web solamente sabe usar:

```
beat.assets.master → direct:<message_id>
```

Así que un beat viejo podría tener:

```
telegram_file_id = "..."
assets.master = null
```

La UI mostraría:

**MP3 — Download**

pero al hacer clic `WebDownloadsManager` no encontraría ningún MP3 válido y terminaría con:

```
MP3 is not available for this beat.
```

Lo mismo puede ocurrir si solamente existe `mp3_path`.

### WAV

El modal acepta:

```
assets.wav
offline_available + wav_path
CloudFileRecord WAV
```

Pero en Web ocurre además algo importante: `useBeatDownloads()` hace explícitamente esto:

```
const files = platform.kind === "web"
  ? []
  : await listCloudFilesForBeat(beat.id);
```

Por lo tanto **Web nunca recibe esos `CloudFileRecord[]`**. Ese mecanismo actualmente es Desktop.

Así que en Web realmente podríamos tener:

```
offline_available = true
wav_path = "..."
assets.wav = null
```

El modal:

```
WAV → disponible
```

Downloader Web:

```
assets.wav → null
```

Resultado: botón permitido, descarga imposible.

### PROJECT

Exactamente el mismo patrón.

El modal acepta:

```
assets.project
offline_available + flp_path
offline_available + als_path
CloudFileRecord PROJECT
```

Pero el Web downloader quiere:

```
assets.project.object_id = "direct:<message_id>"
```

Un `.flp` o `.als` local no le dice al navegador cómo descargar el ZIP Cloud.

### Download Everything

Aquí el efecto se puede hacer más confuso.

El modal calcula:

```
const availableCount =
  Number(hasMp3) +
  Number(hasWav) +
  Number(hasProject);
```

y activa **Download Everything** si:

```
availableCount > 0
```

Pero cuando Web realmente inicia `ALL`, `WebDownloadsManager` vuelve a calcular qué existe usando solamente sus `assets` resolubles.

Entonces la UI podría decir:

```
Download Everything
3 available assets
```

mientras el downloader quizá solo pueda resolver 1, 2 o incluso 0 mediante referencias Cloud actuales.

## Por qué existe

Parece venir de la convivencia de **dos modelos históricos**.

El modal todavía intenta ser compatible con información del mundo Desktop/offline:

```
telegram_file_id
mp3_path
wav_path
flp_path
als_path
CloudFileRecord[]
offline_available
```

Mientras el nuevo downloader Web fue diseñado alrededor del modelo actual:

```
Beat
  └── assets
       ├── master
       ├── wav
       ├── artwork
       └── project
              ↓
         direct:<message_id>
```

De hecho el propio `useBeatDownloads` ya establece la separación: Web usa las referencias autoritativas que vienen dentro del Beat; Desktop conserva el inventario nativo/offline.

## Qué tan grave es

Para **beats actuales correctamente sincronizados que tengan `beat.assets.*` con refs `direct:<id>`**, no veo aquí un problema. Es justamente el camino que acabamos de probar y arreglar.

El riesgo está principalmente en beats:

- antiguos;
- migrados desde esquemas previos;
- que tengan `offline_available`;
- que conserven paths locales de Desktop;
- que tengan `telegram_file_id` pero todavía no el nuevo `assets.master`;
- o que tengan datos parciales/inconsistentes.

No tengo evidencia todavía de que **tus beats actuales** estén en uno de esos estados.

## Lo que yo haría

Para V1 Web, la solución más Stupid Simple sería que **la disponibilidad Web se calcule con exactamente la misma fuente que utiliza `WebDownloadsManager`**.

En Web:

```
MP3 disponible     = assets.master resoluble
WAV disponible     = assets.wav resoluble
PROJECT disponible = assets.project resoluble
```

Desktop puede seguir considerando:

```
offline paths
CloudFileRecord
etc.
```

Eso evita intentar “enseñarle” al navegador a interpretar paths locales de Desktop y mantiene un único contrato:

```
Web UI dice que puede descargar
            ↓
Web downloader realmente puede descargar
```