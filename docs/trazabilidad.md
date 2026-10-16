# Qué se ha podido acreditar de las ejecuciones

Se han contrastado los registros locales de Cline del 15 de octubre de 2026, las fechas de los archivos conservados y la identidad de los GGUF. Esta tabla resume hechos relevantes para interpretar el vídeo, sin distribuir conversaciones, órdenes privadas ni registros completos. Las horas son de España peninsular (CEST).

| Hora del 15 de octubre | Hecho observado |
|---|---|
| 11:26:27 | Cline inicia gastos con LFM2.5 24B A2B en el espacio compartido |
| 11:28:57 y después | La sesión de Liquid recibe seguimientos de verificación; no es una única respuesta al prompt inicial |
| 12:01:02 | Se inicia otra tarea de gastos con Qwen 3.6 35B en el mismo espacio compartido |
| 12:02:02 | Última modificación del HTML compartido conservado, posterior al comienzo de Qwen |
| 12:02:40 y 12:03:01 | La sesión de Qwen registra órdenes de eliminación de `style.css`; el archivo no está disponible ahora |
| 12:05:54 | Qwen inicia gastos en su proyecto separado, del que se conserva el HTML distribuido |
| 12:44:35 | Cline inicia inventario en la carpeta de Qwen con Qwen 3.6 35B |
| 12:47:08 | Cline inicia inventario en la carpeta de Liquid con LFM2.5 24B A2B |
| 12:52:39 | Cline inicia organización en la carpeta de Liquid con LFM2.5 24B A2B |
| 12:55:41 | Cline inicia organización en la carpeta de Qwen con Qwen 3.6 35B |

La fecha de creación del HTML compartido es 11:27:04; su modificación final, 12:02:02. El JavaScript conservado se creó a las 11:27:44 y se modificó a las 11:37:14, dentro de la sesión de Liquid. Es evidencia de procedencia temporal, no una copia archivada por hash al final de cada turno. No se puede presentar la pareja actual como resultado intacto de Liquid.

Los registros muestran aprobación automática de algunas acciones. La guía propone aprobación manual para una nueva repetición; esa diferencia debe declararse y no atribuirse retroactivamente a la grabación. Tampoco se ha reconstruido cada intervención humana ni cada valor de muestreo.

La búsqueda cubrió proyectos de pruebas, espacio de Cline, sesiones y registros de Cline/VS Code, historial local del editor, copias y proyectos relacionados de octubre y la guía anterior de Qwen. No apareció el CSS ni una copia anterior del HTML compartido en esas ubicaciones. Esto no demuestra que no exista otra copia externa o en una grabación. No se ha intentado recuperación forense de archivos borrados ni se ha usado una regeneración de IA como sustituto.

Los perfiles actuales acreditan 131072 configurado, con diferencias de caché, muestreo y MTP. No se ha encontrado un registro completo de arranque y generación a ese contexto para cada tarea. Se mantiene ese límite. El origen de los pesos principales sí está resuelto por SHA-256 y revisión remota en `modelos.json`.
