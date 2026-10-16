# Material disponible y pendiente

| Material | Estado |
|---|---|
| Prompt de gastos, idéntico para ambos | Incluido literalmente en `pruebas/01-gastos/prompt.txt`; texto original facilitado por el autor de la comparativa |
| Resultado Qwen de gastos | `index.html` conservado byte a byte |
| Resultado Liquid de gastos | Ejecución identificada en registros; resultado final intacto no recuperado. HTML modificado después durante otra tarea de Qwen; CSS ausente. Supervivientes separados como material recuperado |
| Prompt de inventario, idéntico para ambos | Incluido literalmente en `pruebas/02-inventario/prompt.txt`; texto original facilitado por el autor de la comparativa |
| Inicio de inventario | Copia de la muestra de presentación; SHA-256 coincide con la huella de la preparación original |
| Dos inventarios corregidos | Conservados; 4/4 cada uno al volver a ejecutar sus tests |
| Tests de inventario | Clase de tests idéntica por estructura Python en los tres archivos |
| Organización | Prompt literal idéntico en ambos proyectos, 12 originales ficticios y dos resultados completos |
| Entrada de Liquid tras la prueba 3 | Vacía en el proyecto original al preparar el paquete; documentada como observación, no se infiere si movió o borró archivos |
| Imágenes | Tres capturas nuevas de la revisión del 16 de octubre, con alcance indicado; no son capturas del vídeo. Esquemas identificados como tales |
| Ejecuciones históricas y parámetros | Modelo y tarea identificados en registros, con seguimientos y algunas aprobaciones automáticas. Sigue faltando una captura completa de parámetros/versiones de cada ejecución |
| Pesos Qwen y procedencia de su cuantización | Confirmados: GGUF de ggml-org a revisión fija, con mismo tamaño y SHA-256 que el archivo local; descarga documentada |

Los archivos fuente de las pruebas no se han editado. `procedencia.json` enumera las copias, sus tamaños y hashes sin rutas personales. No se distribuyen conversaciones, ajustes privados, credenciales, bases de datos de Cline ni historiales de trabajo.
