
# Iniciar servers
### telegram bot
```powershell
$env:TELEGRAM_API_ID="25128267"
$env:TELEGRAM_API_HASH="bf556c65905ac59f5dea067ade959baa"

# Entra a la carpeta del Bot API local
cd D:\BeatGalerBotAPI\telegram-bot-api\build\Release

# Inicia el Bot API local en el puerto 8081 usando tus variables de entorno ya configuradas
.\telegram-bot-api.exe --api-id=$env:TELEGRAM_API_ID --api-hash=$env:TELEGRAM_API_HASH --local --http-port=8081 --verbosity=3
```

### backend
```powershell
# Entra al backend de BeatGaler
cd E:\777\app\beatvault\cloud-server

# Inicia únicamente el backend en el puerto 4000
node server.js
```






```powershell
$env:TELEGRAM_API_ID="25128267"
$env:TELEGRAM_API_HASH="bf556c65905ac59f5dea067ade959baa"
powershell -ExecutionPolicy Bypass -File E:\777\app\beatvault\start-beatgaler-cloud.ps1

# Entrar al proyecto BeatGaler
cd E:\777\app\beatvault

# Ejecutar el launcher completo de BeatGaler
.\start-beatgaler-cloud.ps1

tailscale funnel 4000
```
## version


## borrar cache
```powershell
Remove-Item "$env:TEMP\BeatGaler\cloud-cache" -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item "$env:TEMP\BeatGaler\download-cooking-diagnostic.txt" -Force -ErrorAction SilentlyContinue
```
### check 
```powershell
notepad "$env:TEMP\BeatGaler\download-cooking-diagnostic.txt"
```

## github/version
```powershell
cd E:\777\app\beatvault
# Cambiar versión
npm run version:set -- 0.6.0

# Probar
npm run check

# Guardar versión completa en nueva rama de GitHub
npm run github:save
```

###### cambiar nombre
```powershell
npm run github:save -- --branch performance-v10
```

```POWERSHELL
# Renombra la rama actual
git branch -m galer-atests-beta-v0.6.0

# Borra la rama vieja de GitHub
 git push origin --delete Galer-abctests-beta-v0.6.0

# Sube la rama nueva y la conecta con GitHub
git push -u origin galer-atests-beta-v0.6.0
```

###### DIagnosticos
```
%LOCALAPPDATA%\BeatGaler\diagnostics\telegram-direct-client.txt
```

```
E:\777\app\beatvault\cloud-server\diagnostics\telegram-direct-control.txt
```