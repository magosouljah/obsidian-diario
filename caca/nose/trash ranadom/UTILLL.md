$env:TELEGRAM_API_ID="25128267"
$env:TELEGRAM_API_HASH="bf556c65905ac59f5dea067ade959baa"


cd E:\777\app\beatvault
	powershell -ExecutionPolicy Bypass -File .\start-beatgaler-cloud.ps1
	
	
	
	
	
	
	
	
$env:TELEGRAM_API_ID="25128267"
$env:TELEGRAM_API_HASH="bf556c65905ac59f5dea067ade959baa"
cd D:\BeatGalerBotAPI\telegram-bot-api\build\Release .\telegram-bot-api.exe --local --http-port=8081



$env:TELEGRAM_API_ID="25128267"
$env:TELEGRAM_API_HASH="bf556c65905ac59f5dea067ade959baa"
cd E:\777\app\beatvault\cloud-server
node setup-master-account.js






$env:TELEGRAM_API_ID="25128267"
$env:TELEGRAM_API_HASH="bf556c65905ac59f5dea067ade959baa"
powershell -ExecutionPolicy Bypass -File E:\777\app\beatvault\start-beatgaler-cloud.ps1
tailscale funnel 4000