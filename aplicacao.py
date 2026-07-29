import sys
from PySide6.QtGui import QColor, QPalette
from PySide6.QtWidgets import QApplication

from app.estilos import ESTILO, Cores
from app.Tela_Login import TelaLogin

class Aplicacao:

    def __init__(self):
        self._app = QApplication(sys.argv)
        self._configurar_tema()

        self.janela = TelaLogin()


    def _configurar_tema(self) -> None:
        self._app.setStyle("Fusion")
        self._app.setStyleSheet(ESTILO)

        paleta = self._app.palette()
        paleta.setColor(QPalette.PlaceholderText,QColor(Cores.PLACEHOLDER))
        self._app.setPalette(paleta)

    def executar(self) -> int:
        self.janela.show()
        return self._app.exec()