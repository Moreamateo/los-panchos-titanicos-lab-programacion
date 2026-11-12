"""
Sube todos los videos que existan en output/ a YouTube.
- Uno por día
- A las 21:00 hora Argentina
- En modo público
"""

from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

from videos import VIDEOS

# ==================== CONFIGURACIÓN ====================
SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
ART = ZoneInfo("America/Argentina/Buenos_Aires")

CARPETA = Path(__file__).resolve().parent
TOKEN = CARPETA / "token.json"
CARPETA_VIDEOS = CARPETA / "output"

# Hora de publicación todos los días
HORA_PUBLICACION = 21   # 21:00
MINUTO_PUBLICACION = 0
# =======================================================


def client():
    if not TOKEN.exists():
        raise FileNotFoundError(
            "Falta token.json. Corré primero: python get_youtube_token.py"
        )

    creds = Credentials.from_authorized_user_file(str(TOKEN), SCOPES)
    if not creds.valid:
        if creds.refresh_token:
            creds.refresh(Request())
            TOKEN.write_text(creds.to_json(), encoding="utf-8")
        else:
            raise RuntimeError(
                "El token expiró y no tiene refresh_token. "
                "Corré otra vez: python get_youtube_token.py"
            )
    return build("youtube", "v3", credentials=creds)


def siguiente_fecha_publicacion(dias_adelante: int) -> str:
    """
    Devuelve la fecha de publicación en formato ISO.
    Empieza siempre desde MAÑANA a las 21:00, sin importar la hora de ejecución.
    """
    now = datetime.now(ART)
    # Empezamos desde mañana
    target = now.replace(
        hour=HORA_PUBLICACION,
        minute=MINUTO_PUBLICACION,
        second=0,
        microsecond=0
    ) + timedelta(days=1 + dias_adelante)

    return target.isoformat()


def videos_existentes():
    """
    Devuelve solo los videos de la lista VIDEOS cuyo archivo .mp4 existe.
    Ordenados por id.
    """
    existentes = []
    for video in VIDEOS:
        ruta = CARPETA_VIDEOS / f"video_{video['id']}.mp4"
        if ruta.exists():
            existentes.append((video, ruta))
        else:
            print(f"  ⚠ No se encontró: {ruta.name} → se saltea")
    return existentes


def subir_video(youtube, video: dict, ruta: Path, publish_at: str):
    title = video["titulo"][:100]
    description = video["descripcion"]
    tags = video.get("tags", [])

    body = {
        "snippet": {
            "title": title,
            "description": description,
            "tags": tags,
            "categoryId": "27",  # Educación
        },
        "status": {
            "privacyStatus": "private",   # Se sube como privado
            "publishAt": publish_at,      # YouTube lo hace público a esa hora
            "selfDeclaredMadeForKids": False,
        },
    }

    media = MediaFileUpload(
        str(ruta),
        mimetype="video/mp4",
        resumable=True,
        chunksize=8 * 1024 * 1024,
    )

    request = youtube.videos().insert(
        part="snippet,status",
        body=body,
        media_body=media,
    )

    print(f"\nSubiendo: {ruta.name}")
    print(f"  Título   : {title}")
    print(f"  Publica  : {publish_at}")

    response = None
    while response is None:
        status, response = request.next_chunk()
        if status:
            print(f"  Progreso : {int(status.progress() * 100)}%")

    video_id = response["id"]
    print(f"  ✓ Listo  : https://studio.youtube.com/video/{video_id}/edit")
    return video_id


def main():
    if not CARPETA_VIDEOS.exists():
        raise FileNotFoundError(f"No existe la carpeta: {CARPETA_VIDEOS}")

    print("Buscando videos generados...")
    lista = videos_existentes()

    if not lista:
        print("No se encontró ningún video_XX.mp4 en output/")
        return

    print(f"\nSe van a subir {len(lista)} videos (uno por día a las 21:00 ART)\n")

    youtube = client()

    resultados = []
    for i, (video, ruta) in enumerate(lista):
        publish_at = siguiente_fecha_publicacion(i)
        video_id = subir_video(youtube, video, ruta, publish_at)
        resultados.append((video["id"], video["titulo"], publish_at, video_id))

    print("\n" + "=" * 70)
    print("RESUMEN DE SUBIDAS")
    print("=" * 70)
    for vid_id, titulo, fecha, yt_id in resultados:
        print(f"  {vid_id} | {fecha[:16]} | {titulo[:50]}")
        print(f"         → https://youtu.be/{yt_id}")
    print(f"\nTotal subidos: {len(resultados)}")
    print("Todos quedan PRIVATE hasta la hora programada. YouTube los publica solo.")


if __name__ == "__main__":
    main()
