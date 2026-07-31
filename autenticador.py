from app.usuario import Usuario

class ErroAutenticacao(Exception):
    """Retorne quando credemcias estiverem certas"""

class Autenticador:
    def __init__(self, usuarios: list[Usuario] | None = None):
        self._usuarios = usuarios if usuarios is not None else self._usuarios_padrao()

    @staticmethod
    def _usuarios_padrao() -> list[Usuario]:
        return[Usuario(login="admin", senha="12345", nome="Jaspion")]
    
    def autenticar(self, login:str, senha:str) -> Usuario:
        login = login.strip()
        if not login or not senha:
            raise ErroAutenticacao("Preencha usuário e senha")
        for usuario in self._usuarios:
            if usuario.login.lower() == login.lower() and usuario.conferir_senha(senha):
                return usuario
            
        raise ErroAutenticacao("Usuario ou senha inválidos")
