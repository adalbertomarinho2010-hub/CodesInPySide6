import sys, os
from PySide6.QtCore import Qt, QRectF
from PySide6.QtGui import QStandardItemModel, QStandardItem, QPixmap, QColor, QPainter
from PySide6.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QTextEdit, 
    QComboBox, QPushButton, QVBoxLayout, QHBoxLayout, 
    QFrame, QFileDialog, QListView,QMainWindow, QButtonGroup, QProgressBar
)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE_DIR)

from Utilitarios.btn_layout import btn_layout

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOGO = os.path.join(BASE, "Imagens", "Embrapa-Logo.png")

class ModeloTelaComite(QMainWindow):
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

        self.btn_home = btn_layout (os.path.join(BASE, "Imagens/Painel-Principal-Icone.png"), "Painel Principal")
        self.btn_empregados = btn_layout (os.path.join(BASE, "Imagens/Empregados-Icone.png"), "Pesquisadores")

        logo_label = QLabel ()
        logo = QPixmap (LOGO)
        logo_certa = logo.scaled (220, 190, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        logo_label.setPixmap (logo_certa)
        logo_label.setAlignment (Qt.AlignLeft)
        
        menu_lateral_layout.addWidget(logo_label)
        menu_lateral_layout.addWidget(self.btn_home)
        menu_lateral_layout.setSpacing(5)
        menu_lateral_layout.addWidget(self.btn_empregados)
            
        self.grupo_botoes = QButtonGroup(self)
        self.grupo_botoes.setExclusive(True)
        self.grupo_botoes.addButton(self.btn_home)
        self.grupo_botoes.addButton(self.btn_empregados)
        
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

        funcao_empregado = QLabel("Comitê", cabecalho)
        funcao_empregado.setGeometry(470, 22, 200, 30)
        funcao_empregado.setStyleSheet("""
            QLabel{
                color: #ffffff;
                font-size: 24px
            }
        """)

        nome_tela = QLabel("Painel Principal", cabecalho)
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
                background-color: #f4f6f9;
                border-top-left-radius: 20px;
                border-top-right-radius: 20px;
            }
        """)

        janela = QWidget(paginaprincipal)
        janela.setObjectName("janela_comite")
        janela.setGeometry(0, 0, 1640, 1010)
        janela.setStyleSheet("background-color: transparent;")

        layout_principal = QVBoxLayout(janela)
        layout_principal.setContentsMargins(40, 30, 40, 30)
        layout_principal.setSpacing(25)

        layout_titulo = QHBoxLayout()
        layout_titulo.addStretch()

        titulo = QLabel("Dashboard")
        titulo.setStyleSheet("font-size: 32px; font-weight: bold; color: #000000;")
        titulo.setAlignment(Qt.AlignCenter)
        layout_titulo.addWidget(titulo)

        layout_titulo.addStretch()

        btn_ano = QComboBox()
        btn_ano.setStyleSheet("""  
            QComboBox {
                background-color: #ffffff; 
                color: #333333;
                font-weight: bold;
                border-radius: 8px;
                padding: 6px 16px;
                border: 1px solid #d0d0d0;
                font-size: 16px;
            } 
        """)
        btn_ano.addItems(["2026", "2025", "2024", "2023"])
        btn_ano.setFixedWidth(130)
        layout_titulo.addWidget(btn_ano)

        layout_principal.addLayout(layout_titulo)

        layout_acoes = QHBoxLayout()
        layout_acoes.setSpacing(20)

        total_acoes = QFrame()
        total_acoes.setFixedHeight(180)
        total_acoes.setStyleSheet("QFrame { background-color: #013171; border-radius: 15px; }")
        layout_total = QVBoxLayout(total_acoes)
        
        titulo_total = QLabel("Total de Ações\nrealizadas:")
        titulo_total.setStyleSheet("color: #ffffff; font-size: 18px; border: none;")
        titulo_total.setAlignment(Qt.AlignCenter)
        
        valor_total = QLabel("220")
        valor_total.setStyleSheet("color: #ffffff; font-size: 42px; border: none;")
        valor_total.setAlignment(Qt.AlignCenter)
        
        layout_total.addWidget(titulo_total)
        layout_total.addWidget(valor_total)

        acoes_aprovadas = QFrame()
        acoes_aprovadas.setFixedHeight(180)
        acoes_aprovadas.setStyleSheet("QFrame { background-color: #058914; border-radius: 15px; }")
        layout_aprovadas = QVBoxLayout(acoes_aprovadas)
        
        titulo_aprovadas = QLabel(" Aprovadas")
        titulo_aprovadas.setStyleSheet("color: #ffffff; font-size: 18px; border: none;")
        titulo_aprovadas.setAlignment(Qt.AlignCenter)
        
        valor_aprovadas = QLabel("110")
        valor_aprovadas.setStyleSheet("color: #ffffff; font-size: 42px; border: none;")
        valor_aprovadas.setAlignment(Qt.AlignCenter)
        
        pct_aprovadas = QLabel("50%")
        pct_aprovadas.setStyleSheet("color: #ffffff; font-size: 16px; border: none;")
        pct_aprovadas.setAlignment(Qt.AlignCenter)

        barra_aprovadas = QProgressBar()
        barra_aprovadas.setFixedHeight(8)
        barra_aprovadas.setTextVisible(False)
        barra_aprovadas.setValue(50)
        barra_aprovadas.setStyleSheet("""
            QProgressBar { background-color: rgba(255, 255, 255, 0.3); border-radius: 4px; border: none; }
            QProgressBar::chunk { background-color: #ffffff; border-radius: 4px; }
        """)
        
        layout_aprovadas.addWidget(titulo_aprovadas)
        layout_aprovadas.addWidget(valor_aprovadas)
        layout_aprovadas.addWidget(pct_aprovadas)
        layout_aprovadas.addWidget(barra_aprovadas)

        acoes_analise = QFrame()
        acoes_analise.setFixedHeight(180)
        acoes_analise.setStyleSheet("QFrame { background-color: #0088FF; border-radius: 15px; }")
        layout_analise = QVBoxLayout(acoes_analise)
        
        titulo_analise = QLabel(" Em análise")
        titulo_analise.setStyleSheet("color: #ffffff; font-size: 18px; border: none;")
        titulo_analise.setAlignment(Qt.AlignCenter)
        
        valor_analise = QLabel("55")
        valor_analise.setStyleSheet("color: #ffffff; font-size: 42px; border: none;")
        valor_analise.setAlignment(Qt.AlignCenter)
        
        pct_analise = QLabel("25%")
        pct_analise.setStyleSheet("color: #ffffff; font-size: 16px; border: none;")
        pct_analise.setAlignment(Qt.AlignCenter)

        barra_analise = QProgressBar()
        barra_analise.setFixedHeight(8)
        barra_analise.setTextVisible(False)
        barra_analise.setValue(25)
        barra_analise.setStyleSheet("""
            QProgressBar { background-color: rgba(255, 255, 255, 0.3); border-radius: 4px; border: none; }
            QProgressBar::chunk { background-color: #ffffff; border-radius: 4px; }
        """)
        
        layout_analise.addWidget(titulo_analise)
        layout_analise.addWidget(valor_analise)
        layout_analise.addWidget(pct_analise)
        layout_analise.addWidget(barra_analise)

        acoes_negadas = QFrame()
        acoes_negadas.setFixedHeight(180)
        acoes_negadas.setStyleSheet("QFrame { background-color: #FD7B01; border-radius: 15px; }")
        layout_negadas = QVBoxLayout(acoes_negadas)
        
        titulo_negadas = QLabel(" Negadas")
        titulo_negadas.setStyleSheet("color: #ffffff; font-size: 18px; border: none;")
        titulo_negadas.setAlignment(Qt.AlignCenter)
        
        valor_negadas = QLabel("55")
        valor_negadas.setStyleSheet("color: #ffffff; font-size: 42px; border: none;")
        valor_negadas.setAlignment(Qt.AlignCenter)
        
        pct_negadas = QLabel("25%")
        pct_negadas.setStyleSheet("color: #ffffff; font-size: 16px; border: none;")
        pct_negadas.setAlignment(Qt.AlignCenter)

        barra_negadas = QProgressBar()
        barra_negadas.setFixedHeight(8)
        barra_negadas.setTextVisible(False)
        barra_negadas.setValue(25)
        barra_negadas.setStyleSheet("""
            QProgressBar { background-color: rgba(255, 255, 255, 0.3); border-radius: 4px; border: none; }
            QProgressBar::chunk { background-color: #ffffff; border-radius: 4px; }
        """)
        
        layout_negadas.addWidget(titulo_negadas)
        layout_negadas.addWidget(valor_negadas)
        layout_negadas.addWidget(pct_negadas)
        layout_negadas.addWidget(barra_negadas)

        layout_acoes.addWidget(total_acoes)
        layout_acoes.addWidget(acoes_aprovadas)
        layout_acoes.addWidget(acoes_analise)
        layout_acoes.addWidget(acoes_negadas)

        layout_principal.addLayout(layout_acoes)

        layout_inferior = QHBoxLayout()
        layout_inferior.setSpacing(20)

        painel_grafico = QFrame()
        painel_grafico.setStyleSheet("QFrame { background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 16px; }")
        layout_painel_grafico = QVBoxLayout(painel_grafico)
        
        titulo_grafico = QLabel("Distribuição das Ações")
        titulo_grafico.setAlignment(Qt.AlignCenter)
        titulo_grafico.setStyleSheet("font-size: 20px; font-weight: bold; color: #000000; border: none;")
        layout_painel_grafico.addWidget(titulo_grafico)

        layout_rosca = QHBoxLayout()
        
        grafico_rosca = DonutChartWidget()
        layout_rosca.addWidget(grafico_rosca)

        layout_legenda = QVBoxLayout()
        layout_legenda.setAlignment(Qt.AlignVCenter)
        
        leg_aprovadas = QLabel("<span style='color:#058914; font-size:20px;'>●</span> <b>Aprovadas</b><br>&nbsp;&nbsp;&nbsp;110 (50%)")
        leg_aprovadas.setStyleSheet("font-size: 14px; color: #333333; font-weight: normal; border: none;")
        
        leg_analise = QLabel("<span style='color:#0088FF; font-size:20px;'>●</span> <b>Em análise</b><br>&nbsp;&nbsp;&nbsp;55 (25%)")
        leg_analise.setStyleSheet("font-size: 14px; color: #333333; font-weight: normal; border: none;")
        
        leg_negadas = QLabel("<span style='color:#FD7B01; font-size:20px;'>●</span> <b>Negadas</b><br>&nbsp;&nbsp;&nbsp;55 (25%)")
        leg_negadas.setStyleSheet("font-size: 14px; color: #333333; font-weight: normal; border: none;")
        
        layout_legenda.addWidget(leg_aprovadas)
        layout_legenda.addWidget(leg_analise)
        layout_legenda.addWidget(leg_negadas)

        layout_rosca.addLayout(layout_legenda)
        layout_painel_grafico.addLayout(layout_rosca)

        painel_resumo = QFrame()
        painel_resumo.setStyleSheet("QFrame { background-color: #ffffff; border: 1px solid #e0e0e0; border-radius: 16px; }")
        layout_painel_resumo = QVBoxLayout(painel_resumo)

        titulo_resumo = QLabel("Resumo rápido")
        titulo_resumo.setAlignment(Qt.AlignCenter)
        titulo_resumo.setStyleSheet("font-size: 20px; font-weight: bold; color: #000000; border: none;")
        layout_painel_resumo.addWidget(titulo_resumo)

        item_maior = QFrame()
        item_maior.setStyleSheet("QFrame { border: 1px solid #e0e0e0; border-radius: 12px; background-color: #ffffff; }")
        layout_maior = QHBoxLayout(item_maior)
        
        icone_maior = QLabel("↑")
        icone_maior.setFixedSize(50, 50)
        icone_maior.setAlignment(Qt.AlignCenter)
        icone_maior.setStyleSheet("background-color: #C8E6C9; color: #2E7D32; font-size: 24px; border-radius: 10px; border: none;")
        
        textos_maior = QVBoxLayout()
        titulo_maior = QLabel("Maior Volume")
        titulo_maior.setStyleSheet("font-size: 15px; font-weight: bold; color: #000000; border: none;")
        sub1_maior = QLabel("Março/2026")
        sub1_maior.setStyleSheet("font-size: 12px; color: #666666; font-weight: normal; border: none;")
        sub2_maior = QLabel("28 Pesquisas")
        sub2_maior.setStyleSheet("font-size: 12px; color: #666666; font-weight: normal; border: none;")
        textos_maior.addWidget(titulo_maior)
        textos_maior.addWidget(sub1_maior)
        textos_maior.addWidget(sub2_maior)
        
        layout_maior.addWidget(icone_maior)
        layout_maior.addLayout(textos_maior)
        layout_maior.addStretch()

        item_menor = QFrame()
        item_menor.setStyleSheet("QFrame { border: 1px solid #e0e0e0; border-radius: 12px; background-color: #ffffff; }")
        layout_menor = QHBoxLayout(item_menor)
        
        icone_menor = QLabel("↓")
        icone_menor.setFixedSize(50, 50)
        icone_menor.setAlignment(Qt.AlignCenter)
        icone_menor.setStyleSheet("background-color: #FFE0B2; color: #E65100; font-size: 24px; border-radius: 10px; border: none;")
        
        textos_menor = QVBoxLayout()
        titulo_menor = QLabel("Menor Volume")
        titulo_menor.setStyleSheet("font-size: 15px; font-weight: bold; color: #000000; border: none;")
        sub1_menor = QLabel("Julho/2026")
        sub1_menor.setStyleSheet("font-size: 12px; color: #666666; font-weight: normal; border: none;")
        sub2_menor = QLabel("12 Pesquisas")
        sub2_menor.setStyleSheet("font-size: 12px; color: #666666; font-weight: normal; border: none;")
        textos_menor.addWidget(titulo_menor)
        textos_menor.addWidget(sub1_menor)
        textos_menor.addWidget(sub2_menor)
        
        layout_menor.addWidget(icone_menor)
        layout_menor.addLayout(textos_menor)
        layout_menor.addStretch()

        item_comp = QFrame()
        item_comp.setStyleSheet("QFrame { border: 1px solid #e0e0e0; border-radius: 12px; background-color: #ffffff; }")
        layout_comp = QHBoxLayout(item_comp)
        
        icone_comp = QLabel("📊")
        icone_comp.setFixedSize(50, 50)
        icone_comp.setAlignment(Qt.AlignCenter)
        icone_comp.setStyleSheet("background-color: #BBDEFB; color: #1565C0; font-size: 24px; border-radius: 10px; border: none;")
        
        textos_comp = QVBoxLayout()
        titulo_comp = QLabel("Comparação")
        titulo_comp.setStyleSheet("font-size: 15px; font-weight: bold; color: #000000; border: none;")
        sub1_comp = QLabel("Aumento de 12% em")
        sub1_comp.setStyleSheet("font-size: 12px; color: #666666; font-weight: normal; border: none;")
        sub2_comp = QLabel("relação ao mês anterior")
        sub2_comp.setStyleSheet("font-size: 12px; color: #666666; font-weight: normal; border: none;")
        textos_comp.addWidget(titulo_comp)
        textos_comp.addWidget(sub1_comp)
        textos_comp.addWidget(sub2_comp)
        
        layout_comp.addWidget(icone_comp)
        layout_comp.addLayout(textos_comp)
        layout_comp.addStretch()

        layout_painel_resumo.addWidget(item_maior)
        layout_painel_resumo.addWidget(item_menor)
        layout_painel_resumo.addWidget(item_comp)

        layout_inferior.addWidget(painel_grafico)
        layout_inferior.addWidget(painel_resumo)

        layout_principal.addLayout(layout_inferior)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ModeloTelaComite()
    window.show()
    sys.exit(app.exec())
