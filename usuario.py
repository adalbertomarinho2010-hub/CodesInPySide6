from dataclasses import dataclass

@dataclass(frozen=True)
class Usuario:
    login:str
    senha:str
    nome:str

    @property
    def nome_exibicao(self) -> str:
        return self.nome or self.login
    def conferir_senha(self, senha:str) -> bool:
        return self.senha == senha