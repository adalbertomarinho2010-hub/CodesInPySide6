from PySide6.QtCore import Qt, Signal
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
QCheckBox,
QFrame,
QHBoxLayout,
QLabel,
QLineEdit,
QMessageBox,
QVBoxLayout,
QWidget,
QPushButton
)

from app import IMAGEM_LOGIN
from app.autenticador import Autenticador, ErroAutenticacao
from app.usuario import Usuario

LARGURA = 760
ALTURA = 420

class PainelImagem(QLabel):
    def __init__(self, caminho_imagem = IMAGEM_LOGIN, parent: QWidget | None = None):
        super().__init__(parent)
        self.setObjectName("Imagem")
        self.setAlignment(Qt.AlignCenter)
        self._carregar(caminho_imagem)

    def _carregar(self, caminho) -> None:
        pixmap = QPixmap(str(caminho))
        if pixmap.isNull():
            self.setText((f"Imagem não encontrada:\n{caminho.name}"))
            return
        
        self.setPixmap(
            pixmap.scaled(
                LARGURA // 2,
                ALTURA,
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
        )

class FormularioLogin(QFrame):
    login_solicitado = Signal(str, str)
    senha_esquecida = Signal()

    def __init__(self,parent: QWidget | None = None):
        super().__init__(parent)
        self.setObjectName("Formulario")
        self._montar_interface()

    def _montar_interface(self) -> None:
        layout = QVBoxLayout(self)
        layout.setContentsMargins(40, 40, 40, 40)
        layout.setSpacing(10)

        titulo = QLabel("Bem vindo!")
        titulo.setObjectName("Titulo")

        subtitulo = QLabel("Entre com a sua conta para continuar")
        subtitulo.setObjectName("Subtitulo")

        self.campo_usuario = QLineEdit()
        self.campo_usuario.setPlaceholderText("Usuário")
     
        self.campo_senha = QLineEdit()
        self.campo_senha.setPlaceholderText("Senha")
        self.campo_senha.setEchoMode(QLineEdit.Password)

        self.mostrar_senha = QCheckBox("Mostrar senha")
        self.mostrar_senha.toggled.connect(self._alterar_senha)

        self.botao_entrar = QPushButton("Entrar")
        self.botao_entrar.setObjectName("BotaoEntrar")
        self.botao_entrar.setCursor(Qt.PointingHandCursor)
        self.botao_entrar.clicked.connect(self._emitir_login)

        self.link_esqueci = QPushButton("Esqueci minha senha")
        self.link_esqueci.setObjectName("LinkEsqueci")
        self.link_esqueci.setCursor(Qt.PointingHandCursor)

        self.campo_usuario.returnPressed.connect(self._emitir_login)
        self.campo_senha.returnPressed.connect(self._emitir_login)

    
        layout.addStretch()
        layout.addWidget(titulo)
        layout.addWidget(self.campo_usuario)
        layout.addSpacing(18)

        layout.addWidget(subtitulo)
        layout.addWidget(self.campo_senha)
        layout.addSpacing(8)

        layout.addWidget(self.mostrar_senha)
        layout.addWidget(self.botao_entrar)
        layout.addSpacing(8)

        layout.addWidget(self.link_esqueci)

    def _alterar_senha(self, marcado: bool) -> None:
        self.campo_senha.setEchoMode(
            QLineEdit.Normal if marcado else QLineEdit.Password
        )

    def _emitir_login(self) -> None:
        self.login_solicitado.emit(self.campo_usuario.text(), self.campo_senha.text())

    def limpa_senha(self) -> None:
        self.campo_senha.clear()
        self.campo_senha.setFocus()

class TelaLogin(QWidget):
    autenticado = Signal(Usuario)
    def __init__(self, autenticador: Autenticador | None = None):
        super().__init__()
        self.autenticador = autenticador or Autenticador()

        self.setObjectName("Janela")
        self.setWindowTitle("Login")
        self.setFixedSize(LARGURA, ALTURA)

        self.painel_imagem = PainelImagem()
        self.formulario = FormularioLogin()

        layout = QHBoxLayout(self)
        layout.setContentsMargins(0,0,0,0)
        layout.setSpacing(0)
        layout.addWidget(self.painel_imagem, 1)
        layout.addWidget(self.formulario, 1)

        self.formulario.login_solicitado.connect(self._tentar_login)
        self.formulario.senha_esquecida.connect(self._Mostrar_ajuda_senha)

    def _tentar_login(self, login:str, senha:str) -> None:
        try:
            usuario = self.autenticador.autenticar(login,senha)
        except ErroAutenticacao as erro:
            QMessageBox.warning(self, "Falha no Login", str(erro))
            self.formulario.limpa_senha()
            return
        
        QMessageBox.information(
            self, "Sucesso", f"Bem vindo,{usuario.nome_exibicao}!"
            )
        
        self.autenticado.emit(Usuario)

    def _Mostrar_ajuda_senha(self) -> None:
        QMessageBox.information(
            self,"Recuperar senha","Entre em contato com o Administrador"
        )
