# Auditoría de los resultados conservados

Comprobación repetida sobre las copias distribuidas el 16 de octubre de 2026. La referencia son los 12 archivos ficticios de la entrada intacta de Qwen, con 10 contenidos únicos. La categoría se determina leyendo el contenido; los hashes permiten comprobar que no cambió.

| Originales del mismo contenido | Categoría esperada | Destino Liquid | Correcto | Destino Qwen | Correcto |
|---|---|---|---|---|---|
| apuntes_07.txt / copia_archivo.log | facturas | notas/apuntes_07.txt | No | facturas/apuntes_07.txt | Sí |
| borrador_12.md | documentos | documentos/borrador_12.md | Sí | documentos/borrador_12.md | Sí |
| datos_04.json | documentos | documentos/datos_04.json | Sí | documentos/datos_04.json | Sí |
| documento_09.txt / recorte_02.md | notas | documentos/documento_09.txt | No | notas/documento_09.txt | Sí |
| factura_ideas.log | notas | facturas/factura_ideas.log | No | notas/factura_ideas.log | Sí |
| factura_pendiente.txt | documentos | facturas/factura_pendiente.txt | No | documentos/factura_pendiente.txt | Sí |
| lista_11.csv | notas | documentos/lista_11.csv | No | notas/lista_11.csv | Sí |
| nota_final.log | documentos | notas/nota_final.log | No | documentos/nota_final.log | Sí |
| registro_B.md | facturas | documentos/registro_B.md | No | facturas/registro_B.md | Sí |
| resumen_azul.csv | facturas | documentos/resumen_azul.csv | No | facturas/resumen_azul.csv | Sí |

## Clasificación y conservación

Liquid: **2/10** contenidos únicos bien clasificados. Qwen: **10/10**. En ambos resultados hay diez archivos de contenido, con los mismos diez hashes únicos que la muestra inicial: las dos copias redundantes no aparecen como archivos adicionales.

La entrada del proyecto de Liquid estaba vacía al recopilar los materiales; la de Qwen conserva los doce originales con nombres y bytes idénticos. La carpeta vacía no se representa como un archivo ficticio ni se rellena con las muestras originales. Git no conserva carpetas vacías: su ausencia en la copia es coherente con ese estado observado, sin demostrar cómo ocurrió.

## CSV

Ambos tienen las cinco columnas solicitadas y doce filas. Eso no basta para dar por cumplida la tarea:

- Liquid identifica dos filas como descartadas, pero `duplicado_de` contiene una marca de sí mal codificada, en lugar del nombre del original. También declara destinos que no existen para esos descartes. Su CSV se conserva sin convertir: UTF-16 LE con BOM.
- Qwen identifica los originales equivalentes en `duplicado_de`, deja vacío el destino de los dos descartados y conserva las doce entradas. CSV UTF-8 con BOM.

El informe completo, con errores concretos del CSV y clasificación, está en `docs/verificacion.json`, desde la raíz del repositorio. Puedes repetirlo con `python herramientas/verificar.py`. La auditoría no vuelve a ejecutar agentes ni altera los CSV.
