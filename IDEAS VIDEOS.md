# problemas



**A. El caos:** tienes cientos de beats con nombres extraños y todo parece desorganizado.

**B. La búsqueda:** recuerdas un beat increíble, pero no sabes cuál de tus archivos es.

**C. El potencial desperdiciado:** produces muchísima música, pero tus beats terminan siendo archivos sin identidad.

**D. Algo diferente:** podemos abandonar estas ideas si encontramos un problema más poderoso.



# hooks/capturar atencion
A. Caos progresivo

B. Caos inmediato

C. Situación reconocible

D. Quiero explorar otros ganchos

# extra
Propuesta de narración:

> “Hundreds of beats. No idea which one's which.”

Mientras la narradora habla, los archivos se acumulan rápidamente y el caos escala.

### **Pregunta 30 — ¿Cómo introducimos la transformación?**

Necesitamos conectar la frustración inicial con la aparición de BeatGaler sin utilizar demasiada narración.

**A. Pregunta provocadora.** “What if your beats were more than filenames?”

**B. Frase directa.** “There's a better way.”

# hacer epsacio
|Componente|Método adecuado|
|---|---|
|Claude VM (10.8 GB)|Revisar alternativa compatible con Cowork; no mover manualmente|
|VS Code|Instalación portátil o rutas configuradas para datos y extensiones|
|Ollama, programa|Reinstalar en D: conservando modelos|
|WSL / PostgreSQL|Migración mediante exportación/importación verificada|
|Otras aplicaciones|Reinstalación en D: o traslado oficial cuando lo permitan|
|Cachés de desarrollo|Limpiar o reubicar después de identificar cuáles se regeneran|

La VM de Claude merece especial cuidado: existen reportes de que **incluso los enlaces NTFS pueden fallar** en algunas versiones de Cowork.

GitHub+1

Para WSL, Microsoft documenta exportación/importación a otra unidad.

Microsoft Learn

**Nunca muevas manualmente** `C:\Windows`, `Program Files`, `pagefile.sys`, `Windows.edb` ni los discos virtuales de Claude o PostgreSQL mientras estén activos.

**Importante:** C: no puede quedar vacío porque contiene Windows. Lo que buscamos es liberar el máximo espacio sin romper las aplicaciones.

**Pásame la salida del primer comando** (espacio libre en C: y D:). Así comprobamos si D: tiene capacidad suficiente antes de mover los componentes grandes.