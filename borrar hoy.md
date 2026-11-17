- **Congelar el estado actual antes de probarlo.** Guardar HEAD, `git diff`, archivos modificados y una huella del working tree. Así esta vez sí tendremos identidad exacta del código probado.
- **Repetir Task 4 con 5 cuentas**, primero la validación funcional/performance corta.
- Si cumple:
    
    - `first_audio_p95 <= 2000 ms`
    - `hot_library_p95 <= 5000 ms`
    - seeks/uploads/metadata/download/persistencia PASS
    
    entonces correr el **soak completo de 30 minutos**.
    
- Si el soak también pasa, Task 4 pasa de `FALLÓ` a **COMPROBADO**, y el fallo anterior queda simplemente como **histórico/superseded por una validación posterior**.
- Después revisamos ese gate residual `0/3` de estabilidad/Reload. Si sigue siendo un requisito real, hacemos las 3 corridas; si ya fue reemplazado por evidencia posterior, lo documentamos como superseded.
- **Sólo entonces Task 7 y cierre final.**