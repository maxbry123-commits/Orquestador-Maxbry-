# Método

Canónico: https://github.com/maxbry123-commits/agentes/blob/main/PIPELINE/56_METODO_COPY_MOVE_REUSE_INDEX.md

COPY-FIRST. EXTRACT_LITERAL. No reescribir.

## Procedimiento ZIP → nueva raíz

1. Auditar destino y localizar el ZIP por nombre, ruta, SHA y tamaño.
2. Descargarlo como binario; no interpretarlo como UTF-8.
3. Extraer todos los archivos y directorios a un área temporal.
4. Auditar el contenido extraído y detectar una carpeta envolvente del ZIP.
5. Crear una sola raíz nueva con el nombre solicitado.
6. Colocar TODO el contenido extraído dentro de esa raíz, quitando solo la carpeta envolvente si existe.
7. Mantener nombres, rutas internas y contenido sin modificaciones.
8. Comparar inventario ZIP ↔ raíz: archivos, directorios, tamaños y SHA/contenido cuando sea posible.
9. Crear tree/commit conservando el resto del repositorio y actualizar la rama destino.
10. Verificar en GitHub que la nueva raíz contiene todo lo esperado.

## Reglas

- ZIP original intacto salvo instrucción expresa.
- No clasificar, mover, borrar ni reescribir otros documentos durante esta tarea.
- GitHub = verdad.
- TERMINADA solo después de verificación cruzada.

Flujo: `localizar ZIP → descargar binario → extraer → inventariar → crear raíz → desplegar → comparar → commit → push → verificar`.