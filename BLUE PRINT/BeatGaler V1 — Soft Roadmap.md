Este roadmap da dirección hacia V1 sin convertirse en un plan rígido ni duplicar GitHub.

Los escalones orientan el orden general. El estado real del trabajo vive en GitHub y runtime.

## 0. Entender y preparar

Objetivo: entender cómo está construido BeatGaler, ordenar la base actual y dejar claro qué impide empezar el flujo principal.

### 0.1 Dividir App.tsx

- dividir `App.tsx` en diferentes archivos;
    
- limpiar el código resultante.
    

### 0.2 Mapear las arquitecturas de BeatGaler

Identificar los sistemas que existen, qué responsabilidad tienen, cómo se relacionan y dónde están demasiado mezclados o parecen mal diseñados.

Definir también las arquitecturas lejanas a nivel general, sin diseñarlas todavía.

Ejemplos:

- Library;
    
- startup / lifecycle;
    
- playback;
    
- importing / editing;
    
- Cloud / storage;
    
- sync;
    
- offline / recovery;
    
- sesión / dispositivos;
    
- Web / Desktop;
    
- YouTube;
    
- sharing;
    
- planes / billing;
    
- operación / releases.
    

### 0.3 Entender los flujos críticos

Entender cómo varias arquitecturas trabajan juntas en los flujos importantes.

Ejemplos:

```text
abrir BeatGaler
→ cargar biblioteca
→ reproducir
```

```text
importar
→ Review
→ guardar
→ aparecer en biblioteca
```

```text
editar
→ guardar
→ sync
```

```text
perder conexión
→ seguir funcionando cuando corresponda
→ reconectar
→ recuperar estado correcto
```

### 0.4 Definir y arreglar blockers para empezar fase 1

Revisar los problemas conocidos y corregir únicamente los que impidan comenzar o validar correctamente la fase 1.

Problemas conocidos actuales:

- clickear a lo loco jode el programa;
    
- no se puede reemplazar FLP;
    
- bot se queda dentro aunque salga del programa;
    
- estrellas no se guardan en la metadata;
    
- no se pueden agregar beats.
    

Los problemas que no bloqueen fase 1 se dejan para el escalón donde correspondan.

## 1. Encontrar y usar

```text
abrir BeatGaler
→ ver la biblioteca
→ buscar / ordenar
→ escuchar
→ descargar
```

Objetivo: que este flujo sea rápido, correcto y confiable en las plataformas correspondientes.

## 2. Construir y organizar

```text
subir / importar
→ Review
→ metadata / artwork
→ organizar
→ editar
→ guardar
```

Objetivo: que preparar la biblioteca sea simple y que todo lo hecho aquí mejore directamente el flujo 1.

## 3. Biblioteca confiable

```text
sync
→ multi-device
→ offline
→ Trash / restore
→ recovery
→ fallos de red o Cloud
```

Objetivo: que los dos flujos centrales sobrevivan dispositivos, desconexiones y fallos sin perder ni corromper trabajo.

## 4. Completar V1

Cerrar las features restantes definidas en `V1.md` que no formen parte directa de los dos flujos centrales.

Incluye, cuando corresponda:

- YouTube;
    
- cuenta, sesiones y dispositivos;
    
- planes, límites, suscripciones y pagos;
    
- administración y superficies necesarias alrededor del producto.
    

## 5. Preparar para usuarios reales

Convertir el producto terminado en algo que podamos operar y distribuir con confianza.

Incluye lo que aplique de:

- seguridad final;
    
- deploy y recovery;
    
- Windows/macOS release chain;
    
- signing/notarization/updater;
    
- legal;
    
- soporte/status;
    
- observabilidad;
    
- capacidad y pruebas en hardware real.
    

## 6. Beta → RC → V1

```text
usuarios reales
→ encontrar problemas
→ corregir
→ repetir
→ RC
→ V1
```

Objetivo: validar el producto completo, corregir problemas reales y congelar una V1 confiable.

## Cómo se usa

No se detallan todos los escalones por adelantado.

En cada momento:

```text
escalón actual
→ entender qué toca resolver
→ elegir el problema más importante
→ resolverlo siguiendo SYSTEM.md
→ cerrar limpio
→ elegir el siguiente
```

Normalmente avanzamos dentro del escalón actual, pero no es una línea rígida: un problema de seguridad, integridad de datos o dependencia crítica puede adelantarse si bloquea o pone en riesgo V1.

Se cambia de escalón cuando el anterior ya no contiene el problema más importante que impide llegar a V1.