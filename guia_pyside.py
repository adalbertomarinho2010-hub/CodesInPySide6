import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, 
    QPushButton, QTableWidget, QHeaderView, QTableWidgetItem, QCheckBox
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

"""
===================================================================
 MAPA VISUAL DO PAINEL ("Gestão de Empregados")
===================================================================

 ┌──────────────────────────────────────────────────────────────┐
 │ LAYOUT PRINCIPAL: QVBoxLayout (Vertical - Cima p/ Baixo)     │
 │                                                              │
 │  [ QLabel: Gestão de Empregados (Centralizado) ]             │
 │                                                              │
 │  ┌────────────────────────────────────────────────────────┐  │
 │  │ QHBoxLayout (Linha de Ações + Mola Flexível)           │  │
 │  │  [ Cadastrar ] [ Baixar ] <--(mola)--> [ Pesquise... ] │  │
 │  └────────────────────────────────────────────────────────┘  │
 │                                                              │
 │  ┌────────────────────────────────────────────────────────┐  │
 │  │ QTableWidget (Topo Arredondado - 5 Colunas)            │  │
 │  │  Nome   │ Email  │ Área    │ Status  │ Status do Func. │  │
 │  │ ────────┼────────┼─────────┼─────────┼─────────────────│  │
 │  │ Fulano. │ silva. │ Pesqui. │ Ativo   │   (  O) [ON]    │  │
 │  │ Fulano. │ arauj. │ Valida. │ Desativ.│   (O  ) [OFF]   │  │
 │  └────────────────────────────────────────────────────────┘  │
 └──────────────────────────────────────────────────────────────┘
===================================================================
"""

app = QApplication(sys.argv)

# 1. JANELA PRINCIPAL
janela = QWidget()
janela.setObjectName("janela_funcionarios")
janela.setWindowTitle("Gestão de Empregados")
janela.resize(1200, 700)
# REVISÃO: Escopado via ID para não forçar o fundo branco em subcomponentes indesejados
janela.setStyleSheet("#janela_funcionarios { background-color: #ffffff; }")

# 2. LAYOUT PRINCIPAL
layout_principal = QVBoxLayout(janela)
layout_principal.setContentsMargins(30, 30, 30, 30)
layout_principal.setSpacing(30)

# --- ELEMENTO 1: TÍTULO ---
titulo = QLabel("Gestão de Empregados")
titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
titulo.setAlignment(Qt.AlignCenter)
layout_principal.addWidget(titulo)

# --- ELEMENTO 2: LINHA DE AÇÕES ---
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
    }
""")

layout_acoes.addWidget(btn_cadastrar)
layout_acoes.addWidget(btn_baixar)
layout_acoes.addStretch()  # Mola invisível
layout_acoes.addWidget(campo_busca)

layout_principal.addLayout(layout_acoes)

# --- ELEMENTO 3: DADOS E TABELA ---
dados_funcionarios = [
  ("Fulano da Silva", "silva@gmail.com", "Pesquisador", "Ativo"),
  ("Fulano Ferreira", "ferreira@gmail.com", "Pesquisador", "Ativo"),
  ("Fulano Araujo", "araujo@gmail.com", "Validador SIPT", "Desativado"),
  ("Fulano Oliveira", "oliveira@gmail.com", "Validador SPAT", "Ativo"),
  ("Fulano Leite", "leite@gmail.com", "Validador NCO", "Ativo"),
  ("Fulano Da Guia", "guia@gmail.com", "Comitê", "Ativo"),
  ("Fulano Jacobina", "jacobina@gmail.com", "Comitê", "Desativado"),
  ("Fulano Nogueira", "nogueira@gmail.com", "Administrador", "Ativo"),
]

tabela = QTableWidget(len(dados_funcionarios), 5)

# CORREÇÃO: Nome ajustado de "Status da Ação" para "Status do Funcionário"
tabela.setHorizontalHeaderLabels(["Nome", "Email", "Área de Atuação", "Status", "Status do Funcionário"])
tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
tabela.verticalHeader().setVisible(False)

# REVISÃO: Desativa a edição de texto das células via duplo clique para comportamento de Dashboard
tabela.setEditTriggers(QTableWidget.NoEditTriggers)

# ESTILIZAÇÃO: Topo Arredondado
tabela.setStyleSheet("""
    QTableWidget {
        background-color: #ffffff;
        gridline-color: #e0e0e0;
        border: 1px solid #d0d0d0;
        border-top-left-radius: 12px;
        border-top-right-radius: 12px;
        border-bottom-left-radius: 0px;
        border-bottom-right-radius: 0px;
    }
    QHeaderView::section {
        background-color: #366896;
        color: white;
        font-weight: bold;
        padding: 10px;
        border: none;
    }
    QHeaderView::section:first {
        border-top-left-radius: 10px;
    }
    QHeaderView::section:last {
        border-top-right-radius: 10px;
    }
""")

# PREENCHIMENTO E MONTAGEM
for linha_id, (nome, email, area, status) in enumerate(dados_funcionarios):
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

    # Botão Switch Centralizado
    container_botao = QWidget()
    layout_celula = QHBoxLayout(container_botao)
    layout_celula.setContentsMargins(0, 0, 0, 0)
    layout_celula.setAlignment(Qt.AlignCenter)

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

    layout_celula.addWidget(btn_switch)
    tabela.setCellWidget(linha_id, 4, container_botao)

layout_principal.addWidget(tabela)

janela.show()
sys.exit(app.exec())
