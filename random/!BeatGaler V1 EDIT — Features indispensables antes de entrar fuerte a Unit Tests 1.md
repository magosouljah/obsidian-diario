
## 1. Offline / Reconnect
- [x] Detectar offline
- [x] Reproducir cacheado
- [x] Definir comportamiento de no-cacheado
- [x] Guardar operaciones pendientes
- [x] Reanudar al reconectar
- [x] No corromper índice

## 2. Estados internos definitivos
```
sync_state:
  pending_upload
  uploading
  synced
  pending_update
  deleting
  error
  conflict

download_state:
  idle
  downloading
  error

playback_state:
  idle
  playback_preparing
  playing
  error

offline_available:
  true | false
```

Esto es importante porque muchos Unit Tests van a probar exactamente estas transiciones.

## 3. Bulk Import confiable
- [ ] Arreglar beats que quedan con `!` roja
- [ ] Retry individual
- [ ] Error real visible
- [ ] No duplicados
- [ ] Multi-folder confiable

## 4. Review Beat instantáneo
- [ ] Modal visible casi inmediatamente
- [ ] Trabajo pesado en background
- [ ] Multi-beat no debe bloquear la apertura

## 5. Cuentas mínimas de producción
- [ ] Recuperar contraseña
- [ ] Email verification con códigos
- [ ] Sesiones persistentes/revocables
- [ ] Separación segura entre usuarios

No necesitamos terminar fotos, referrals, etc. antes de Unit Tests.

## 6. Arquitectura Client ↔ Telegram
- [ ] Decidir definitivamente cómo Desktop sube/descarga directamente de Telegram
- [ ] Los archivos grandes no pasan por tu PC host
- [ ] No exponer master credentials
- [ ] Backend conserva autorización/control

No necesariamente tiene que estar 100% terminada antes de todos los Unit Tests,
pero sí debemos congelar el diseño porque cambia Upload/Download/Auth.

## 7. Auto-Updater + Schema Versioning mínimo
- [ ] Definir updater
- [ ] Definir versión de schema Telegram
- [ ] Definir versión SQLite
- [ ] Definir estrategia de migraciones

No hace falta perfeccionarlo todavía, pero la arquitectura debe quedar decidida.

## 8. Planes — solo arquitectura
- [ ] Free
- [ ] Paid Entry
- [ ] Highest Paid
- [ ] Entitlements server-side
- [ ] Quotas server-side

No necesitamos decidir precios todavía.

## 9. Web — solo arquitectura antes de los tests profundos
- [ ] Decidir qué backend comparte con Desktop
- [ ] Auth común
- [ ] Entitlements comunes
- [ ] Source of Truth común
- [ ] Cómo accederá Web a archivos sin exponer Telegram secrets

La Web completa puede construirse después de tener bastante testing.

## 10. Seguridad base de arquitectura
- [ ] Toda autorización server-side
- [ ] Tenant isolation
- [ ] Inputs validados backend-side
- [ ] No secrets en frontend
- [ ] Paths/ZIP handling seguro