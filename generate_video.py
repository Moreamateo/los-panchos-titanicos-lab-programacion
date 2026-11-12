"""
Genera TODOS los videos de la lista (videos.py).
Cada video se guarda como: output/video_01.mp4, output/video_02.mp4, etc.
"""

from pathlib import Path

from moviepy import ColorClip, CompositeVideoClip, TextClip, concatenate_videoclips

from videos import VIDEOS

# ==================== CONFIGURACIÓN ====================
ANCHO = 1280
ALTO = 720
FPS = 24
SEGUNDOS_POR_SLIDE = 18          # 18 slides × 18 s ≈ 5 min 24 s por video

# Fuente (funciona en Linux y también podés cambiarla en Windows)
FUENTE = Path(r"C:\Windows\Fonts\arial.ttf")
FUENTE_BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")

# Si estás en Windows, descomentá estas dos líneas y comentá las de arriba:
# FUENTE = Path(r"C:\Windows\Fonts\arial.ttf")
# FUENTE_BOLD = Path(r"C:\Windows\Fonts\arialbd.ttf")

CARPETA = Path(__file__).resolve().parent
CARPETA_SALIDA = CARPETA / "output"
# =======================================================


def slide(titulo: str, cuerpo: str, segundos: float) -> CompositeVideoClip:
    """Crea un slide con fondo oscuro + título + texto."""
    fondo = ColorClip(size=(ANCHO, ALTO), color=(12, 18, 32)).with_duration(segundos)

    t_titulo = (
        TextClip(
            font=str(FUENTE_BOLD if FUENTE_BOLD.exists() else FUENTE),
            text=titulo,
            font_size=58,
            color="white",
            method="caption",
            size=(ANCHO - 160, None),
            text_align="center",
        )
        .with_duration(segundos)
        .with_position(("center", 140))
    )

    t_cuerpo = (
        TextClip(
            font=str(FUENTE),
            text=cuerpo,
            font_size=34,
            color="#d0d7e2",
            method="caption",
            size=(ANCHO - 200, None),
            text_align="center",
        )
        .with_duration(segundos)
        .with_position(("center", 340))
    )

    return CompositeVideoClip([fondo, t_titulo, t_cuerpo])


def generar_un_video(video: dict) -> Path:
    """Genera un solo MP4 a partir de un dict de la lista VIDEOS."""
    video_id = video["id"]
    slides = video["slides"]
    salida = CARPETA_SALIDA / f"video_{video_id}.mp4"

    print(f"\n{'='*60}")
    print(f"Generando video {video_id}: {video['titulo']}")
    print(f"{'='*60}")

    clips = [
        slide(titulo, cuerpo, SEGUNDOS_POR_SLIDE)
        for titulo, cuerpo in slides
    ]

    final = concatenate_videoclips(clips, method="compose")
    print(f"Duración total: {final.duration:.1f} segundos ({final.duration/60:.1f} min)")

    final.write_videofile(
        str(salida),
        fps=FPS,
        codec="libx264",
        audio=False,
        preset="ultrafast",   # más rápido (podés cambiar a "medium" para mejor calidad)
        threads=4,
        logger="bar",
    )

    print(f"✓ Guardado: {salida}")
    return salida


def main():
    if not FUENTE.exists():
        raise FileNotFoundError(
            f"No encontré la fuente: {FUENTE}\n"
            "En Windows cambiá FUENTE y FUENTE_BOLD al principio del archivo."
        )

    CARPETA_SALIDA.mkdir(exist_ok=True)

    print(f"Se van a generar {len(VIDEOS)} videos.")
    print(f"Carpeta de salida: {CARPETA_SALIDA}")
    print("Esto puede tardar bastante (varios minutos por video)...\n")

    generados = []
    for video in VIDEOS:
        ruta = generar_un_video(video)
        generados.append(ruta)

    print("\n" + "="*60)
    print("¡TODOS LOS VIDEOS GENERADOS!")
    print("="*60)
    for r in generados:
        print(f"  → {r.name}")
    print(f"\nTotal: {len(generados)} videos en {CARPETA_SALIDA}")


if __name__ == "__main__":
    main()
