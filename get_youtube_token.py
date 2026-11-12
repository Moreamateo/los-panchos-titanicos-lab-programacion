"""Paso unico: abre el navegador, autorizas tu canal y guarda token.json."""

from pathlib import Path

from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = ["https://www.googleapis.com/auth/youtube.upload"]
CARPETA = Path(__file__).resolve().parent
CLIENT = CARPETA / "client_secret.json"
TOKEN = CARPETA / "token.json"


def main():
    if not CLIENT.exists():
        raise FileNotFoundError(
            f"No esta {CLIENT}\n"
            "Baja client_secret.json de Google Cloud y ponelo en esta carpeta."
        )

    flow = InstalledAppFlow.from_client_secrets_file(str(CLIENT), SCOPES)
    creds = flow.run_local_server(port=0, access_type="offline", prompt="consent")
    TOKEN.write_text(creds.to_json(), encoding="utf-8")
    print("Listo. Token guardado en:", TOKEN)
    if not creds.refresh_token:
        print("ATENCION: no vino refresh_token. Revoca el acceso y corre esto otra vez.")


if __name__ == "__main__":
    main()
