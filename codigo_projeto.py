import sys, os
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QColor
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView, QMainWindow, QButtonGroup, QTableWidget, QHeaderView, QTableWidgetItem, QCheckBox
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")

class ModeloTelaAdministrador(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Criar ação")
        self.setFixedSize(1920, 1080)
        
        self.setStyleSheet("""
            QWidget {
                font-family: 'Verdana';
                font-weight: bold;
                background-color: #356394;
            }
        """)

        menu_lateral = QWidget(self)
        menu_lateral.setGeometry(0, 0, 280, 1080)
        menu_lateral.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        menu_lateral_layout = QVBoxLayout(menu_lateral)
        menu_lateral_layout.setContentsMargins(30, 0, 0, 0)

        self.btn_home = btn_layout(os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_calendario = btn_layout(os.path.join(BASE, "Imagens/Calendario-Icone.png"), "Calendário")
        self.btn_acoes = btn_layout(os.path.join(BASE, "Imagens/Ações-Icone.png"), "Ações")
        self.btn_empregados = btn_layout(os.path.join(BASE, "Imagens/Empregados-Icone.png"), "Empregados")
        self.btn_validadores = btn_layout(os.path.join(BASE, "Imagens/Validadores-Icone.png"), "Validadores")

        logo_label = QLabel()
        logo = QPixmap(LOGO)
        logo_certa = logo.scaled(220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap(logo_certa)
        logo_label.setAlignment(Qt.AlignLeft)
        
        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_calendario)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_acoes)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_empregados)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_validadores)
            
        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_calendario)
        self.grupo_botoes.addButton(self.btn_acoes)
        self.grupo_botoes.addButton(self.btn_empregados)
        self.grupo_botoes.addButton(self.btn_validadores)
        
        menu_lateral_layout.addStretch()

        cabecalho = QWidget(self)
        cabecalho.setGeometry(280, 0, 1640, 70)
        cabecalho.setStyleSheet("""
            QWidget{
                background-color: #356394
            }
        """)

        nome_empregado = QLabel("Fulano da Silva Rodrigues", cabecalho)
        nome_empregado.setGeometry(35, 22, 400, 30)
        nome_empregado.setStyleSheet("""
            QLabel{
                font-size: 24px;
                color: #ffffff;
            }
        """)

        separador = QLabel("|", cabecalho)
        separador.setGeometry(420, 22, 5, 30)
        separador.setStyleSheet("""
            QLabel{
                font-size: 24px;
                color: #ffffff;
            }
        """)

        funcao_empregado = QLabel("Administrador", cabecalho)
        funcao_empregado.setGeometry(470, 22, 200, 30)
        funcao_empregado.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 24px
            }
        """)

        nome_tela = QLabel("Nome da Tela", cabecalho)
        nome_tela.setGeometry(1000, 22, 300, 30)
        nome_tela.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 20px;
                font-weight: lighter
            }
        """)

        botao_logout = QPushButton("Logout", cabecalho)
        botao_logout.setGeometry(1450, 15, 150, 40)
        botao_logout.setStyleSheet("""
            QPushButton{
                background-color: #ffffff;
                color: #08175C;
                font-size: 18px;
                border: 0px solid #ffffff;
                border-radius: 10px;
            }
        """)

        paginaprincipal = QFrame(self)
        paginaprincipal.setGeometry(280, 70, 1640, 1010)
        paginaprincipal.setStyleSheet("""
            QFrame{
                background-color: #ffffff;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px
            }
        """)

        janela = QWidget(paginaprincipal)
        janela.setObjectName("janela_funcionarios")
        janela.setGeometry(0, 0, 1640, 1010)
        janela.setStyleSheet("background-color: transparent;")

        layout_principal = QVBoxLayout(janela)
        layout_principal.setContentsMargins(30, 30, 30, 30)
        layout_principal.setSpacing(30)

        titulo = QLabel("Gestão de Empregados")
        titulo.setStyleSheet("font-size: 24px; font-weight: bold; color: #2c3e50;")
        titulo.setAlignment(Qt.AlignCenter)
        layout_principal.addWidget(titulo)

        layout_acoes = QHBoxLayout()

        btn_cadastrar = QPushButton("Cadastrar Empregado")
        btn_cadastrar.setStyleSheet("""
            QPushButton {
                background-color: #1e7e34;
                color: white;
                font-weight: bold;
                border-radius: 6px;
                padding: 8px 16px;
            }
            QPushButton:hover {
                background-color: #155724;
            }
        """)
        
        btn_baixar = QPushButton("Baixar em Excel")
        btn_baixar.setStyleSheet("""
            QPushButton {
                background-color: #ffffff; 
                color: blue;
                font-weight: bold;
                border-radius: 6px;
                padding: 8px 16px;
                border: 1px solid #d0d0d0;
            }
            QPushButton:hover {
                background-color: #d0d0d0;
            }                        
        """)

        campo_busca = QLineEdit()
        campo_busca.setPlaceholderText("Pesquise...")
        campo_busca.setStyleSheet("""
            QLineEdit {
                border: 1px solid #cccccc;
                border-radius: 4px;
                padding: 6px;
                width: 200px;
                color: #333333;
                background-color: #ffffff;
            }
        """)

        layout_acoes.addWidget(btn_cadastrar)
        layout_acoes.addWidget(btn_baixar)
        layout_acoes.addStretch()
        layout_acoes.addWidget(campo_busca)

        layout_principal.addLayout(layout_acoes)

        dados_funcionarios = [
            ("Fulano da Silva","silva@gmail.com","Pesquisador","Ativo"," "),
            ("Fulano Ferreira", "ferreira@gmail.com", "Pesquisador", "Ativo"," "),
            ("Fulano Araujo", "araujo@gmail.com", "Validador SIPT", "Desativado"," "),
            ("Fulano Oliveira", "oliveira@gmail.com", "Validador SPAT", "Ativo"," "),
            ("Fulano Leite", "leite@gmail.com", "Validador NCO", "Ativo"," "),
            ("Fulano Da Guia", "guia@gmail.com", "Comitê", "Ativo"," "),
            ("Fulano Jacobina", "jacobina@gmail.com", "Comitê", "Desativado"," "),
            ("Fulano Nogueira", "nogueira@gmail.com", "Administrador", "Ativo"," "),
        ]

        tabela = QTableWidget(len(dados_funcionarios),5)
        tabela.setHorizontalHeaderLabels(["Nome","Email","Área de Atuação","Status","Ação"])
        tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        tabela.verticalHeader().setVisible(False)
        tabela.setEditTriggers(QTableWidget.NoEditTriggers)
        tabela.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                gridline-color: #e0e0e0;
                border: 1px solid #d0d0d0;
                border-radius: 8px;
                color: #333333;
            }
            QHeaderView::section {
                background-color: #366896;
                color: white;
                font-weight: bold;
                padding: 10px;
                border: none;
                border-radius: 15px 0px;
            }

            QHeaderView::section:first {
                border-top-left-radius: 10px;
            }
            QHeaderView::section:last {
                border-top-right-radius: 10px;
            }
        """)

        for linha_id, (nome, email, area, status, acao) in enumerate(dados_funcionarios):
            item_nome = QTableWidgetItem(nome)
            item_email = QTableWidgetItem(email)
            item_area = QTableWidgetItem(area)
            item_status = QTableWidgetItem(status)

            item_email.setTextAlignment(Qt.AlignCenter)
            item_area.setTextAlignment(Qt.AlignCenter)
            item_status.setTextAlignment(Qt.AlignCenter)

            if status == "Ativo":
                item_status.setForeground(QColor("green"))
            else:
                item_status.setForeground(QColor("orange"))

            tabela.setItem(linha_id, 0, item_nome)
            tabela.setItem(linha_id, 1, item_email)
            tabela.setItem(linha_id, 2, item_area)
            tabela.setItem(linha_id, 3, item_status)

            conteiner_botao = QWidget()
            layout_botao = QHBoxLayout(conteiner_botao)
            layout_botao.setContentsMargins(0,0,0,0)
            layout_botao.setAlignment(Qt.AlignCenter)

            btn_switch = QCheckBox()
            btn_switch.setChecked(status == "Ativo")
            btn_switch.setCursor(Qt.PointingHandCursor)
            btn_switch.setStyleSheet("""
                    QCheckBox::indicator {
                        width: 38px;
                        height: 20px;
                        border-radius: 10px;
                    }
                    QCheckBox::indicator:unchecked {
                        background-color: #cccccc;
                        border: 1px solid #b0b0b0;
                    }
                    QCheckBox::indicator:checked {
                        background-color: #366896;
                    }
                """)

            layout_botao.addWidget(btn_switch)
            tabela.setCellWidget(linha_id, 4, conteiner_botao)

        layout_principal.addWidget(tabela)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaAdministrador()
    window.show()
    sys.exit(app.exec())
