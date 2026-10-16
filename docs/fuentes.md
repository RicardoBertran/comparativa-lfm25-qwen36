# Descargas y documentación

Enlaces consultados el **16 de octubre de 2026**. Los autores oficiales se distinguen de los proveedores de cuantizaciones. Los códigos de respuesta están en `enlaces-verificados.json`. Las páginas de los pesos son páginas descriptivas: al abrirlas no se descarga automáticamente un modelo.

| Fuente | Para qué sirve |
|---|---|
| [Python para Windows](https://www.python.org/downloads/windows/) | Autor oficial; instalación |
| [Visual Studio Code](https://code.visualstudio.com/download) | Microsoft; instalación |
| [Cline en Marketplace](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) | Extensión oficial |
| [Conexión OpenAI Compatible en Cline](https://docs.cline.bot/provider-config/openai-compatible) | Documentación oficial |
| [Publicaciones de llama.cpp](https://github.com/ggml-org/llama.cpp/releases) | Proyecto oficial; paquetes de motor |
| [Servidor de llama.cpp](https://github.com/ggml-org/llama.cpp/blob/master/tools/server/README.md) | Documentación oficial de parámetros y endpoints |
| [Modelo Liquid original](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B) | Autor oficial |
| [Liquid GGUF Q4_K_M fijado por revisión](https://huggingface.co/LiquidAI/LFM2.5-24B-A2B-GGUF/blob/0912d33141f77e10705345a6732bfd83f0252fdc/LFM2.5-24B-A2B-Q4_K_M.gguf) | Autor oficial; hash coincide con el archivo local |
| [Modelo Qwen original](https://huggingface.co/Qwen/Qwen3.6-35B-A3B) | Autor oficial; no es una descarga GGUF |
| [Qwen GGUF Q4_K_M fijado por revisión](https://huggingface.co/ggml-org/Qwen3.6-35B-A3B-GGUF/blob/baec3ebee244827cda0f4557eafa8b28f7545fa6/Qwen3.6-35B-A3B-Q4_K_M.gguf) | ggml-org; tamaño y SHA-256 coinciden con el archivo local |
| [Repositorio Unsloth consultado](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF) | Tercero; ofrece UD-Q4_K_M, que no se presenta como la misma cuantización |
| [jQuery incluido como referencia externa en el HTML](https://code.jquery.com/jquery-3.6.0.min.js) | Solo comprobación de cabecera HTTP; biblioteca no redistribuida |

## Descargar un GGUF desde su página

1. Abre la página del archivo, comprueba el propietario del repositorio y el nombre exacto.
2. Comprueba que termina en `.gguf` y corresponde a Q4_K_M. Lee la licencia en la ficha del modelo.
3. Pulsa el botón de descarga de Hugging Face y elige la carpeta `modelos`. No necesitas descargar todos los archivos del repositorio.
4. Espera a que finalice; después compara su SHA-256 con la fuente y registra la revisión descargada. No uses un archivo parcial.

Liquid: el hash local coincide con el archivo oficial fijado en la tabla. Qwen: el archivo local mide 20 419 565 568 bytes y coincide exactamente en tamaño y SHA-256 con el Q4_K_M de ggml-org a la revisión enlazada. Ya no hace falta sustituirlo por otra cuantización. Unsloth se consultó para contrastar variantes; UD-Q4_K_M no se presenta como idéntica.

No se han descargado pesos nuevos durante la preparación del paquete. Las huellas locales y las de las alternativas consultadas están en `modelos.json`.
