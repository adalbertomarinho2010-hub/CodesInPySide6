from pathlib import Path

BASE_D18 = Path(__file__).resolve().parent.parent
IMAGEM_LOGIN = BASE_D18 / "Login.png"
IMAGEM_PERFIL = BASE_D18 / "Image.png"

__all__ = ["BASE_D18", "IMAGEM_LOGIN", "IMAGEM_PERFIL"]
