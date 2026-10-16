# Prueba 2 · Corregir un inventario Python

## Punto de partida

`inicial/inventario.py` contiene el programa defectuoso y cuatro tests. Su huella SHA-256 es `0f293dee3f2be855987ab9cdd63d49bbc817b468bcdb7774275e77e66581426c`, coincidente con la registrada al preparar las dos muestras originales. Se ha recuperado de la copia inicial conservada para la presentación, porque las dos carpetas de los agentes ya contienen las soluciones.

Los tres defectos iniciales son: reponer resta stock, vender permite superar el stock y el valor total suma cantidades y precios en vez de multiplicarlos. Los tests esperan 15 teclados al reponer, rechazar una venta de 20 ratones manteniendo 5, y un valor total de 325. La venta válida ya pasaba.

El [prompt original literal](prompt.txt) es el mismo utilizado con ambos modelos, facilitado por el autor de la comparativa. Se conserva sin reformular. Pide corregir los errores sin modificar los tests, instalar dependencias ni reescribir el programa desde cero.

## Comprobar sin usar ningún modelo

1. Abre la carpeta principal del repositorio en VS Code con **Archivo → Abrir carpeta**.
2. Abre **Terminal → Nuevo terminal**. Copia cada línea por separado:

```powershell
python pruebas/02-inventario/inicial/inventario.py -v
python pruebas/02-inventario/resultados/liquid/inventario.py -v
python pruebas/02-inventario/resultados/qwen/inventario.py -v
```

3. En la primera ejecución deben aparecer cuatro tests, tres `FAIL` y uno `ok`. El proceso termina con error: es el fallo esperado de la muestra inicial.
4. En las otras dos deben aparecer cuatro `ok` y `OK` al final. Aquí ambos obtienen **4/4**.
5. Ejecuta `python herramientas/verificar.py`: compara también la estructura de la clase `TestsInventario` para comprobar que los agentes no cambiaron esos tests. La salida guardada en `docs/verificacion.json` sanea las rutas de los errores.

## Repetir con Cline

Ejecuta el preparador desde la raíz. Abre `ejecuciones/liquid/02-inventario`, inicia una tarea nueva y pega todo el contenido de `prompt.txt`, sin añadir pistas sobre los errores. No abras las soluciones guardadas al agente. Conserva los cuatro tests, ejecuta el archivo final y guarda la salida. Cambia de modelo, abre `ejecuciones/qwen/02-inventario` y repite con el mismo prompt y criterios. No copies la solución del primer agente al segundo.

Los cuatro tests cubren esos ejemplos. No evalúan todos los casos: cantidades negativas, productos inexistentes o entradas de tipos incorrectos requieren otras pruebas, que no se añaden al marcador del vídeo.
