**Estas tareas pueden avanzar sin modificar el funcionamiento de los bots**, en este orden:

- [x] 1. **Cerrar las políticas de Billing V1.**  
    Documentar planes, bienvenida, cancelación, refunds sin borrado, gracia por impago y cambios de plan. Dejar anual y Bulk `limited` pendientes donde corresponda.
    
- [ ] 2. **Definir el catálogo comercial configurable.**  
    Ofertas internas, mensual/anual, moneda y mapping a productos/precios del proveedor. Sin crear productos reales ni tocar transporte.
    
- [ ] 3. **Crear el resolver único de acceso como función pura.**  
    Recibe suscripción, grants y fecha; devuelve plan efectivo, capacidades y cuotas. Inicialmente sin conectarlo al servidor actual.
    
- [ ] 4. **Escribir tests del resolver y las políticas.**  
    Bienvenida que vence, cancelación futura, pago fallido, refund, grants simultáneos y planes ilimitados. No requieren bots ni Telegram.
    
- [ ] 5. **Preparar migraciones exclusivamente de billing.**  
    Clientes, solicitudes de checkout, pagos y ampliaciones de suscripciones/grants. Probarlas en una base aislada. **No aplicarlas a la base usada por la migración de bots ni editar migraciones existentes.**
    
- [ ] 6. **Implementar el adaptador de Polar en sandbox.**  
    Consultar productos, crear checkout, abrir portal y verificar firmas. Fijar versión del SDK y separar credenciales de prueba.
    
- [ ] 7. **Implementar checkout con idempotencia persistente.**  
    Resolver doble-click, retries y timeouts usando PostgreSQL y sandbox. Sin conceder permisos por el redirect.
    
- [ ] 8. **Implementar recepción y procesamiento de webhooks.**  
    Firma, deduplicación, recuperación tras reinicio y actualización de suscripciones. Probarlo en un servidor de pruebas independiente.
    
- [ ] 9. **Implementar el ciclo comercial completo.**  
    Renovación, cancelación, expiración, gracia y refunds. Sólo cambia estado de billing; **no borra archivos ni modifica sesiones de transporte**.
    
- [ ] 10. **Implementar reconciliación y logs de billing.**  
    Comparar proveedor con PostgreSQL, reparar diferencias inequívocas y registrar errores sin secretos.
    
- [ ] 11. **Probar el ciclo completo en sandbox.**  
    Free → pago → Paid → cancelación → expiración, incluyendo refund y pago fallido. Esta prueba valida billing; todavía no valida uploads ni cuotas reales.
    

**Dejaría para después:** conectar el resolver a Auth/Account, retirar la escritura antigua de grants, montar rutas en el arranque actual y modificar Settings. Son trabajos independientes conceptualmente, pero comparten archivos o persistencia con el servidor que está migrándose.

**No tocar todavía:** membership, pool de bots, credenciales Direct, sesiones de transporte, capacidades, uploads, índice de biblioteca, Trash ni helper Desktop.

Para trabajar en paralelo: **rama/worktree separado, base PostgreSQL de pruebas y ningún proceso usando la base o configuración de la migración de bots**. Empieza con las tareas **1–4**; son las de menor riesgo y preparan el resto.