# BeatGaler — YouTube Web

**Estado:** TARGET obligatorio para v1.  
**Regla de producto:** YouTube debe existir tanto en Desktop como en Web. Que `youtubePublishing` sea `false` hoy en Web describe únicamente el estado actual; **no es una exclusión permanente de la plataforma Web**.

## Estado actual

- Desktop: YouTube implementado mediante Tauri/Rust y debe conservarse sin regresiones.
- Web: YouTube todavía no está implementado.
- Web nunca debe depender de Tauri, un helper local ni de que BeatGaler Desktop esté instalado.
- La UI de YouTube ya forma parte del alcance de producto; la implementación Web debe reutilizar el flujo compartido cuando sea posible sin copiar la dependencia nativa.

## Arquitectura objetivo

1. Crear un contrato compartido de publicación YouTube para que la UI no llame directamente a `src/lib/tauri.ts`.
2. Mantener un adaptador Desktop que conserve la implementación Tauri/Rust actual.
3. Crear un adaptador Web puro respaldado por el backend/control plane de BeatGaler.
4. Mantener OAuth, refresh tokens, client secrets y demás secretos únicamente server-side; el navegador recibe solo estado/capabilities y credenciales efímeras cuando sean estrictamente necesarias.
5. Implementar en Web el ciclo completo: conectar canal, leer estado del canal, configurar metadata/visual/visibilidad/schedule, iniciar upload, progreso, retry, cancelación, resultado y desconexión.
6. Reutilizar el stepper/UI compartido de YouTube y adaptar únicamente las operaciones que dependen de plataforma.
7. No cambiar `WEB_FOUNDATION_CAPABILITIES.youtubePublishing` a `true` hasta que el flujo Web real esté implementado y probado.

## Tarea propuesta para Plan Maestro

### Tarea 15.3 [P1 · FE/BE/QA] — Portar YouTube a Web sin Tauri

- [ ] Extraer un contrato compartido de YouTube; Desktop conserva Tauri/Rust detrás de su adaptador.
- [ ] Implementar el backend Web para OAuth/estado/upload/schedule/progreso/retry/cancel/disconnect con secretos server-side.
- [ ] Implementar el adaptador Web sin Tauri, sin helper local y sin dependencia de BeatGaler Desktop.
- [ ] Reutilizar la UI compartida de selección, visual, metadata/presets, visibilidad/schedule, conexión y job/progreso.
- [ ] Añadir pruebas DOM/integration/backend/E2E que demuestren que YouTube Web funciona y nunca invoca Tauri.
- [ ] Mantener regresiones Desktop verdes para Direct, Offline y YouTube durante toda la migración.
- [ ] Cambiar `WEB_FOUNDATION_CAPABILITIES.youtubePublishing` a `true` solo después de que el flujo Web pase sus gates.

**Dependencias:** auth/OAuth Web seguro, backend durable, upload/job infrastructure y contrato de plataforma compartido.  
**Evidencia:** tests Web + backend + E2E, OAuth real de staging, upload real controlado, progreso/cancel/retry y CI cross-platform verde.  
**Gate de salida:** Web puede completar el flujo YouTube de principio a fin sin Tauri ni Desktop helper, mientras Desktop conserva Direct/Offline/YouTube sin regresiones.

## Relación con Tarea 3.2

La Tarea 3.2 solo congela el contrato actual y evita regresiones durante la convergencia. No declara YouTube como Desktop-only para el producto final.

Evidencia técnica preparada para 3.2 el 23 de agosto de 2026:
- PR BeatGaler #8: `test(platform): enforce 3.2 Web/Desktop contract`.
- Commit: `818214889ef3c6f97a262a91046f7df0e4f723fe`.
- CI `Test - Desktop Portability` run #64: PASS en Windows, macOS arm64 y macOS x86_64.
- El test de capacidades ahora se ejecuta realmente dentro de la suite TS.
- Nuevo guard DOM: cualquier invocación Tauri desde los flujos del adaptador Web hace fallar la prueba.
- Desktop queda protegido explícitamente para Direct, Offline y YouTube.

**Cierre 3.2:** pendiente de integrar PR #8 en `integration-v0.8.0-alpha.1`. GitHub exige una aprobación de un reviewer con permiso de escritura y no permite que el autor apruebe su propio PR. No marcar 3.2 `[x]` en `Plan Maestro.md` hasta que el PR esté integrado y el CI final de la rama protegida quede verde.
