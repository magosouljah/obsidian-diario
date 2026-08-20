### Regression Shield

Ahora tienes:

npm run test:regressions

Ya verifica automáticamente:

✓ Pinterest URL gana al File virtual

✓ imágenes locales siguen funcionando

✓ imagen local sin MIME sigue funcionando

✓ una URL de página no desplaza un archivo local bueno

✓ i.pinimg.com se reconoce como artwork

✓ App.tsx NO puede volver a meter onDragDropEvent

✓ App.tsx NO puede volver a meter beatgaler-native-drag

✓ BeatCard NO puede volver a crear su propio pipeline de artwork drop

✓ Rust NO puede volver a habilitar native_drop sin romper el test

✓ htmlDropController sigue siendo el dueño global

Y además agregué:

npm run check

regression tests
      ↓
npm run build