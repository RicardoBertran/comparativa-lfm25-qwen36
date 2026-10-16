# Prueba 1 · Aplicación de gastos

## Material recuperado

`resultados/qwen/index.html` es el HTML conservado en el proyecto separado de Qwen. Los dos archivos de `material-recuperado/espacio-compartido` son supervivientes de una carpeta usada primero por Liquid y después por otra tarea de Qwen. Los registros confirman esas sesiones; el HTML tiene una modificación posterior a Liquid y falta `style.css`. No se presentan como el resultado intacto de Liquid ni se ha creado un CSS sustituto. Véase [trazabilidad](../../docs/trazabilidad.md).

El [prompt original literal](prompt.txt) es el mismo utilizado con ambos modelos, facilitado por el autor de la comparativa. Exige expresamente HTML, CSS y JavaScript sin frameworks ni dependencias externas. Se conserva sin reformular ni añadir instrucciones.

## Dependencia externa en Qwen

El HTML contiene exactamente esta solicitud:

```html
<script src="https://code.jquery.com/jquery-3.6.0.min.js"></script>
```

La etiqueta es evidencia de que incluye una carga externa y contradice el requisito literal del prompt de no usar dependencias externas. **No demuestra que jQuery sea necesario para funcionar**: el mismo archivo declara `const $=id=>document.getElementById(id);`. Hay que distinguir una carga externa de una dependencia funcional. No se ha descargado ni redistribuido jQuery.

## Cómo inspeccionar los resultados

1. No uses información financiera real. Los datos de ejemplo están dentro del código.
2. Abre el HTML de Qwen con el navegador. Para comparar entornos, usa perfiles de navegador separados: los datos guardados en el navegador pueden contaminar una segunda prueba.
3. Pulsa F12 y abre **Red / Network**. Recarga. Busca `jquery`: la solicitud externa debe aparecer, aunque falle por falta de conexión.
4. En **Consola / Console**, anota errores. Bloquea esa solicitud en las herramientas del navegador, recarga y comprueba qué funciona. Eso es una nueva comprobación tuya, no un resultado funcional ya validado en este paquete.
5. Anota saldo, ingresos y gastos iniciales. Añade un ingreso ficticio de 100 y un gasto de 30: el saldo debe subir 70 respecto al inicial. Comprueba que las tarjetas, la lista y el gráfico concuerdan.
6. Recarga y comprueba la persistencia en localStorage exigida por el prompt. Prueba campos vacíos e importes no válidos. Registra cada resultado y errores de consola.
7. Los archivos del espacio compartido posterior pueden inspeccionarse, pero su HTML y JavaScript no encajan y falta el CSS. Su aspecto o fallo actual no deben atribuirse al resultado intacto de Liquid.

## Límites

Se han comprobado en navegador la apertura, adición de ingreso y gasto, actualización y persistencia de Qwen, y una vista móvil. Hay desbordamiento horizontal y problemas de texto; no se otorga un aprobado global ni se han cubierto todas las acciones o la accesibilidad. El fallo de la muestra compartida posterior no se puntúa como resultado original de Liquid. Consulta [las capturas y el alcance exacto](revision-navegador.md). Usa el prompt original idéntico en dos tareas nuevas, con carpetas sin código inicial y el mismo procedimiento de aprobación.

## Repetir la tarea con Cline

1. Desde la raíz del repositorio ejecuta `python herramientas/preparar.py`.
2. Abre solo `ejecuciones/liquid/01-gastos` en VS Code. No debe contener código previo; incluye únicamente `prompt.txt`.
3. Conecta Cline al servidor de Liquid, inicia una conversación nueva y pega el contenido completo de `prompt.txt`.
4. Revisa y aprueba las acciones. Abre los archivos que el agente indique, guarda sus resultados y realiza las comprobaciones anteriores.
5. Cambia al servidor de Qwen y abre `ejecuciones/qwen/01-gastos`. Repite en una conversación nueva con exactamente el mismo prompt. Mantén el mismo criterio de aprobaciones.
6. Evalúa cada requisito por separado: aspecto oscuro y acentos verdes, saldo/ingresos/gastos, al menos ocho operaciones, gráfico CSS o SVG, formulario, actualización de las tres vistas, persistencia y adaptación a móvil. Anota además cualquier dependencia externa o función no solicitada. No confundas un buen aspecto con el cumplimiento completo.
