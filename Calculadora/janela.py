import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget
)
from soma import Soma
from subtracao import Subtracao
from multiplicacao import Multiplicacao
from divisao import Divisao

OPERACOES = {
    "+": Soma,
    "-": Subtracao,
    "*": Multiplicacao,
    "/": Divisao
}

ESTILO = """
QWidget {
    background-color: #f2f2f2;
    font-family: Segoe UI, Arial;
}
QLabel#visor {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 28px;
    padding: 12px;
}
QLabel#conta {
    color: #777777;
    font-size: 13px;
    padding-left: 4px;
}
QPushButton {
    background-color: #ffffff;
    border: 1px solid #cccccc;
    color: #222222;
    font-size: 18px;
    min-width: 56px;
    min-height: 48px;
}
QPushButton:hover {
    background-color: #e8e8e8;
}
QPushButton:pressed {
    background-color: #dcdcdc;
}
"""

class Calculadora(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculadora")

        self.digitado = "0"
        self.primeiro = None
        self.classe = None
        self.zerar = False

        self.conta = QLabel("")
        self.conta.setObjectName("conta")
        self.conta.setAlignment(Qt.AlignRight)

        self.visor = QLabel(self.digitado)
        self.visor.setObjectName("visor")
        self.visor.setAlignment(Qt.AlignRight)
        grade = QGridLayout()
        botoes = [
            ("c", 0, 0), ("<", 0, 1), ("+/-", 0, 2), ("/", 0, 3),
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("*", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("-", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("+", 3, 3),
            ("0", 4, 0), (",", 4, 1), ("=", 4, 2), 
        ]
        for texto, linha, coluna in botoes:
            botao = QPushButton(texto)
            largura = 2 if texto == "=" else 1
            grade.addWidget(botao, linha, coluna, 1, largura)
            botao.clicked.connect(self.criar_acao(texto))
        
        layout = QVBoxLayout()
        layout.addWidget(self.conta)
        layout.addWidget(self.visor)
        layout.addLayout(grade)

        self.setLayout(layout)

    def criar_acao(self, texto):
        return lambda: self.clicar(texto)
    
    def clicar(self, texto):
        if texto in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", ","]:
            self.digitar(texto)
        elif texto in ["+", "-", "*", "/"]:
            self.escolher_operacao(texto)
        elif texto == "=":
            self.calcular()
        elif texto == "c":
            self.limpar()
        elif texto == "<":
            self.apagar()
        elif texto == "+/-":
            self.inverter_sinal()

    def digitar(self, tecla):
        if tecla == ",":
            tecla = "."

        if self.digitado == "0" and tecla != ".":
            self.digitado = tecla
        else:
            if self.zerar == True:
                if tecla == ".":
                    self.digitado = "0."
                else:
                    self.digitado = tecla
                self.zerar = False
            else:
                self.digitado += tecla

        self.visor.setText(self.digitado)

    def valor_do_visor(self):
        texto = self.visor.text()
        texto = texto.replace(",", ".")
        if "." in texto:
            return float(texto)
        else:
            return int(texto)
        
    def mostrar(self, numero):
        self.digitado = f"{numero:g}"
        self.visor.setText(self.digitado)
    
    def escolher_operacao(self, simbolo):
        self.primeiro = self.valor_do_visor()
        self.operacao_simbolo = simbolo
        self.zerar = True

        self.conta.setText(f"{self.primeiro} {simbolo}")

    def calcular(self):
        if self.primeiro is not None:
            segundo = self.valor_do_visor()
            try:
                operacao_escolhida = OPERACOES[self.operacao_simbolo]
                instancia_operacao = operacao_escolhida(self.primeiro, segundo)
                try:
                    resultado = instancia_operacao.calcular()
                except TypeError:
                    resultado = instancia_operacao.calcular(segundo)
                    
                self.mostrar(resultado)

            except ZeroDivisionError:
                self.visor.setText("Erro")
                self.digitado = "0"

            self.primeiro = None
            self.zerar = True
            self.conta.setText("")

    def limpar(self):
        self.digitado = "0"
        self.primeiro = None
        self.classe = None
        self.zerar = False
        self.visor.setText("0")
        self.conta.setText("")

    def apagar(self):
        if len(self.digitado) > 1:
            self.digitado = self.digitado[:-1]
        else:
            self.digitado = "0"
        self.visor.setText(self.digitado)

    def inverter_sinal(self):
        numero = self.valor_do_visor() * -1
        self.mostrar(numero)

    

def main():
    app = QApplication(sys.argv)
    app.setStyleSheet(ESTILO)
    janela = Calculadora()
    janela.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()