# LOS PANCHOS TITÁNICOS

Proyecto de **Laboratorio de Programación, 6to 3ra**.

**Integrantes:** Morea, Coronel, Barrales y Valencia.

Generador local de una colección de videos educativos y scripts para autenticación OAuth y subida programada a YouTube.

## Funcionamiento actual

`videos.py` contiene 20 videos, cada uno con identificador, título, descripción, etiquetas y 18 diapositivas. `generate_video.py` compone fondo y texto con MoviePy: 18 segundos por diapositiva, **324 segundos (5:24)** por video, 1280×720, 24 fps, H.264 (`libx264`, preset `ultrafast`, 4 threads), sin audio. Guarda `output/video_01.mp4` hasta `output/video_20.mp4`.

`get_youtube_token.py` realiza OAuth con un cliente Desktop y alcance `youtube.upload`; guarda el token local. `upload_youtube.py` toma los archivos existentes siguiendo el orden de `VIDEOS`, renueva el token cuando corresponde y solicita la subida privada con `publishAt`, uno por día **a las 21:00 de Argentina**, empezando siempre mañana. YouTube administra la publicación programada. No hay un servicio local que espere hasta esa hora.

Al 12/11/2026 existen **19 videos completos (01–19)**; falta el 20. No se reinició la generación ni se ejecutó ninguna subida. Ver [estado verificado](docs/ESTADO_VIDEOS.md).

## Archivos

- `videos.py`: contenidos de la colección.
- `generate_video.py`: composición y exportación.
- `get_youtube_token.py`: autorización inicial.
- `upload_youtube.py`: subida y fechas de publicación.
- `requirements.txt`: dependencias del entorno.
- `output/`: videos locales excluidos; Git conserva solo `.gitkeep`.
- `docs/`: estado, antecedentes y proceso de incorporación.

## Preparación en Windows (PowerShell)

Desde la carpeta del proyecto, usar Python 3.11 y un entorno virtual. Si `.venv` ya existe, reutilizarlo:

```powershell
# Solo en una instalación nueva:
python -m venv .venv
# Instalar las dependencias en ese entorno:
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
ffmpeg -version
ffprobe -version
.\.venv\Scripts\python.exe -c "from zoneinfo import ZoneInfo; print(ZoneInfo('America/Argentina/Buenos_Aires'))"
```

Para instalar FFmpeg y ffprobe si faltan: `winget install Gyan.FFmpeg`; reabrir la terminal después. El generador utiliza las fuentes `C:\Windows\Fonts\arial.ttf` y `arialbd.ttf`. En otro sistema hay que adaptar estas rutas. Se preservan dependencias heredadas como OpenCV, edge-tts y pydub; el generador actual no utiliza narración ni mezcla de audio.

## Generación: conservar los archivos existentes

`python generate_video.py` procesa **todos** los videos y puede sobrescribirlos. Usarlo solo en una salida nueva/vacía. No ejecutarlo para continuar esta copia.

Para generar únicamente el video 20 en una sesión futura, comprobar primero que no haya otro generador activo. Desde la raíz del proyecto, este comando rechaza un destino existente y llama a la función de generación solo para ese identificador:

```powershell
.\.venv\Scripts\python.exe -c "from generate_video import CARPETA_SALIDA, generar_un_video; from videos import VIDEOS; v = next(v for v in VIDEOS if v['id'] == '20'); destino = CARPETA_SALIDA / 'video_20.mp4'; CARPETA_SALIDA.mkdir(exist_ok=True); destino.exists() and exit('Cancelado: el archivo ya existe'); generar_un_video(v)"
```

Este comando no se ejecutó en la revisión. La comprobación no reemplaza un bloqueo contra procesos concurrentes. Si existe un archivo incompleto, preservarlo e investigar antes de regenerar.

## Autenticación y subida (acciones manuales)

Habilitar YouTube Data API v3 en el proyecto de Google Cloud, preparar un cliente OAuth Desktop y autorizar la cuenta del canal según la configuración de la aplicación. Guardar el archivo descargado como `client_secret.json` en la raíz. Estos archivos nunca deben agregarse a Git.

```powershell
# Solo cuando sea necesario autorizar el canal:
.\.venv\Scripts\python.exe get_youtube_token.py
# Solo cuando se quiera subir y programar los videos existentes:
.\.venv\Scripts\python.exe upload_youtube.py
```

La subida modifica el canal: confirmar primero el estado de los MP4, las cuotas disponibles y las publicaciones ya hechas. El script no detecta duplicados, no valida la duración ni reanuda un lote entre ejecuciones. Si falla a mitad, revisar YouTube Studio antes de repetir. Las fechas se calculan para cada video desde el momento de ejecución; una corrida que atraviese medianoche podría desplazar días. No se confirmó ninguna subida real durante esta revisión.

## Guía anterior y alcance

La guía `Guia_Video_Python_YouTube 2.pdf` describe un único archivo `output/video.mp4`, 20 diapositivas de 18 segundos (6 minutos), 2 threads y publicación a las 21:00. Esta copia trabaja con una lista de 20 videos, 18 diapositivas cada uno, nombres numerados y 4 threads. La programación actual comienza siempre mañana; no decide entre hoy y mañana según la hora.

El PDF menciona GitHub Actions como pendiente. Esta copia tampoco incluye automatización en Actions. Subir el código a GitHub no activa renders ni publicaciones. Los antecedentes de OAuth y tzdata se distinguen de los hallazgos actuales en [errores y soluciones](docs/ERRORES_Y_SOLUCIONES.md).

## Git y seguridad

Los commits iniciales incorporan trabajo ya existente por partes coherentes; no reconstruyen ni simulan el desarrollo histórico. Se usa la identidad Git previamente configurada, sin atribuir commits ficticios a los integrantes. Se excluyen entorno virtual, cachés, credenciales, videos y temporales. Ver [proceso de incorporación](docs/PROCESO.md).
