```powershell
# 1. Estás en main y has hecho cambios
git add .
git commit -m "TESTS"

# 2. Creas un branch que sea el escalón (versión)
git branch Galer beta v0.6.2           # o v1, paso-1, 2026-08-17, como quieras
git push origin Galer beta v0.6.2         # lo subes a GitHub

# 3. Sigues trabajando en main
# Cuando hagas el siguiente cambio importante:
git add .
git commit -m "Siguiente mejora"
git branch v1.1



# Crea una branch nueva llamada galer-beta-v0.6.2 desde tu estado actual
git switch -c galer-beta-v0.6.2

# Sube esa branch a tu repo actual y deja configurado el upstream
git push -u origin galer-beta-v0.6.2


```

Asdsad
versiones
```powershell
# Cambia la versión única de BeatGaler a 0.6.1 y propaga el cambio a package.json, Cargo.toml, tauri.conf.json y demás archivos versionados
node .\scripts\set-version.mjs 0.6.1

# Verifica que todos los archivos importantes quedaron sincronizados con VERSION
npm run test:version
```


```powershell
# Muestra cómo está configurado actualmente el remote origin
git remote -v

# Elimina el origin incorrecto que apunta a "magosouljah/galer.git"
git remote remove origin

# Añade el repositorio nuevo usando una URL completa de GitHub
git remote add origin https://github.com/magosouljah/galer.git

git remote add origin https://github.com/magosouljah/BeatGaler

# Comprueba que origin ahora apunta a la URL correcta
git remote -v


# Renombra tu rama local actual a main
git branch -M galer-beta-v.0.6.1 # cambia por nombre de tu branch

# Comprueba que la rama local ahora se llama main
git branch --show-current




# Muestra si hay archivos pendientes de añadir al nuevo repositorio
git status

# Añade todos los archivos actuales respetando .gitignore
git add -A

# Crea el primer commit del nuevo repositorio con tu estado actual
git commit -m "q cambios?"




# Sube tu BeatGaler actual al repositorio nuevo como rama principal
git push -u origin galer-beta-v.0.6.1
```





git remote add origin https://github.com/magosouljah/galer.git