# Prueba 3 · Organizar archivos por contenido

## Repetir desde cero

1. Lee el [prompt literal](prompt.txt). Es el mismo archivo que había en los dos proyectos originales.
2. Desde la raíz del repositorio ejecuta `python herramientas/preparar.py`. Si `ejecuciones` ya existe, el programa se detiene sin sobrescribirla.
3. En VS Code, **Archivo → Abrir carpeta**, abre `ejecuciones/liquid/03-organizacion`. Debe contener `entrada` con 12 archivos y ningún `resultado`.
4. Selecciona el modelo Liquid en la conexión local de Cline. Crea una tarea nueva y pega todo el contenido de `prompt.txt`. Aprueba las acciones de una en una. No le facilites las soluciones ni el auditor.
5. Cuando termine, conserva la carpeta y exporta por separado la conversación para tu revisión; no publiques datos personales o ajustes de conexión.
6. Cambia a Qwen, abre `ejecuciones/qwen/03-organizacion` e inicia otra tarea nueva con el mismo prompt. No reutilices la conversación.
7. Desde la raíz del repositorio comprueba cada ejecución:

```powershell
python herramientas/auditar_organizacion.py ejecuciones/liquid/03-organizacion
python herramientas/auditar_organizacion.py ejecuciones/qwen/03-organizacion
```

El auditor solo lee archivos. Devuelve error si hay incumplimientos. Antes de ejecutar al agente también puedes comprobar que su entrada tiene los mismos hashes que `inicial/entrada`.

## Entender el resultado

Hay 12 archivos con **10 contenidos únicos**. Los nombres engañan: `factura_pendiente.txt` es un acta y `factura_ideas.log` una nota. Lee su contenido para decidir la categoría.

| Duplicados exactos | Copia equivalente |
|---|---|
| `apuntes_07.txt` | `copia_archivo.log` |
| `documento_09.txt` | `recorte_02.md` |

En `resultado` deben quedar 10 archivos de contenido, además de un CSV con 12 filas. Los dos duplicados descartados deben indicar de qué original son copia. La entrada debe seguir intacta, con 12 archivos; eliminar duplicados solo afecta a `resultado`.

Abre `informe.csv` en VS Code. En una hoja de cálculo, usa **Datos → Desde texto/CSV**, elige coma como separador y la codificación correcta: Liquid usa UTF-16 LE con BOM y Qwen UTF-8 con BOM. No conviertas el archivo original para compararlo por hash.

Consulta [la auditoría por archivo](auditoria.md). Los resultados guardados son evidencia de esas ejecuciones, no archivos para darle al agente al comenzar.
