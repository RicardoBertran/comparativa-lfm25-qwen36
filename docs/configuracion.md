# Configuración y alcance de la reproducción

## Evidencia disponible

Los perfiles fuente actuales indican contexto **131072** y una sola secuencia paralela en los dos modelos. No fijan por sí solos cómo se ejecutó cada turno del vídeo. No se ha hecho una nueva generación de los modelos al preparar este paquete ni una prueba que llene 128K tokens.

| Ajuste observado en perfiles actuales | Liquid | Qwen |
|---|---|---|
| Cuantización del modelo principal | Q4_K_M | Q4_K_M |
| Contexto | 131072 | 131072 |
| Temperatura | 0.1 | 0.6 |
| top-k | 50 | 20 |
| top-p | No fijado en el perfil | 0.95 |
| min-p | No fijado en el perfil | 0 |
| repeat-penalty | 1.05 | 1.0 |
| Caché K/V | f16 / f16 | q4_0 / q4_0 |
| Lote / microlote | 512 / 128 | 512 / 128 |
| Paralelismo | 1 | 1 |
| Plantilla Jinja / Flash Attention | activados | activados |
| MTP | No configurado | Borrador Q4_0; draft-mtp, máximo 2, mínimo 0, p mínima 0.5 |

Esto no es una comparación con todos los parámetros iguales. MTP y los ajustes de caché son factores adicionales que se deben declarar. El ejemplo sencillo de arranque de la guía desactiva MTP al no incluir ningún borrador: sirve para repetir las tareas, pero no se presenta como reproducción exacta del rendimiento del vídeo. No hay mediciones nuevas de velocidad.

La extensión encontrada al reunir el paquete es Cline **4.1.24**. La versión histórica exacta de cada tarea, el ejecutable exacto de llama.cpp y las aprobaciones no están fijados en un registro completo. Registra tus versiones y parámetros antes de comenzar; una instalación actual puede cambiar nombres de controles y comportamiento.

## Pesos y recursos

Consulta `modelos.json` para nombres, tamaños y SHA-256 calculados de los dos archivos locales. No se incluyen pesos. La identidad de ambos archivos se ha cotejado con los metadatos remotos. Liquid coincide con LiquidAI; Qwen coincide con la conversión de ggml-org a una revisión fija. El nombre por sí solo no sería suficiente. Consulta las páginas y hashes en `modelos.json`.

Los pesos ocupan aproximadamente 14.5 y 20.4 GB decimales, a lo que se añaden cachés y memoria de ejecución. Tener espacio de disco suficiente no garantiza RAM o VRAM suficiente para 128K. No se ha establecido un mínimo de hardware validado para esta reproducción. La carga parcial en CPU puede ser lenta; si reduces contexto para que arranque, registra el cambio y no lo etiquetes como la prueba a 128K.
