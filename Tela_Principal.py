from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QFrame, QLabel, QBoxLayout, QWidget, QVBoxLayout

from app import IMAGEM_PERFIL
from app.usuario import Usuario

LARGURA = 520
ALTURA = 620
LARGURA_FOTO = 380

class TelaPrincipal(QWidget):
    def __init__(self, usuario: Usuario | None = None):
        super().__init__()
        self.usuario = usuario

        self.setObjectName("janela_inicial")
        self.setWindowTitle("Contato")
        self.setFixedSize(LARGURA, ALTURA)

        self.painel_imagem = PainelImagemPrincipal()

        layout = QVBoxLayout(self)
        layout.setContentsMargins(30,30,30,30)
        layout.setSpacing(0)

        email = QLabel("Email: adalbertomarinho2010@gmail.com")
        email.setObjectName("Email")

        telefone = QLabel("Telefone: (67 993334663)")
        telefone.setObjectName("Telefone")



        layout.addWidget(self.painel_imagem)
        layout.addWidget(email)
        layout.addWidget(telefone)

class PainelImagemPrincipal(QLabel):
    def __init__(self, caminho_imagem = IMAGEM_PERFIL, parent: QWidget | None = None):
        super().__init__(parent)
        self.setObjectName("Imagem_perfil")
        self.setAlignment(Qt.AlignCenter)
        self._carregar(caminho_imagem)

    def _carregar(self, caminho) -> None:
        pixmap = QPixmap(str(caminho))
        if pixmap.isNull():
            self.setText((f"Imagem não encontrada:\n{caminho.name}"))
            return
        
        self.setPixmap(
            pixmap.scaled(
                LARGURA,
                ALTURA,
                Qt.KeepAspectRatioByExpanding,
                Qt.SmoothTransformation
            )
        )
