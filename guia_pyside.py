import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QFormLayout, QGridLayout, QLabel, QLineEdit, 
    QPushButton, QCheckBox, QComboBox, QFrame
)
from PySide6.QtCore import Qt

"""
====================================================================
 1. MAPA VISUAL DOS LAYOUTS (Como o PySide enxerga sua tela)
====================================================================

 ┌────────────────────────────────────────────────────────────────┐
 │ LAYOUT PRINCIPAL: QVBoxLayout (Vertical - Cima para Baixo)    │
 │                                                                │
 │  [ QLabel: Título da Tela ]                                    │
 │                                                                │
 │  ┌──────────────────────────────────────────────────────────┐  │
 │  │ QFormLayout (Formulário: Rótulo na Esquerda | Campo)     │  │
 │  │  Nome:  [ QLineEdit.................................. ]  │  │
 │  │  Cargo: [ QComboBox: Selecionar ▼                     ]  │  │
 │  └──────────────────────────────────────────────────────────┘  │
 │                                                                │
 │  ┌──────────────────────────────────────────────────────────┐  │
 │  │ QGridLayout (Grade: Linhas e Colunas)                    │  │
 │  │  Col 0, Linha 0: [X] Checkbox A | Col 1, Linha 0: [ ] B   │  │
 │  └──────────────────────────────────────────────────────────┘  │
 │                                                                │
 │  ~~~~~~~~~~~~~~~~~~ MOLA (addStretch) ~~~~~~~~~~~~~~~~~~~~~~~  │
 │                                                                │
 │  ┌──────────────────────────────────────────────────────────┐  │
 │  │ QHBoxLayout (Horizontal: Lado a Lado + Mola de Espaço)   │  │
 │  │  [ Botão Esquerda ] <--- (mola) ---> [ Cancelar ] [ OK ] │  │
 │  └──────────────────────────────────────────────────────────┘  │
 └────────────────────────────────────────────────────────────────┘
====================================================================
"""

# Inicializa a aplicação (obrigatório para qualquer projeto PySide)
app = QApplication(sys.argv)

# Cria a janela base
janela = QWidget()
janela.setWindowTitle("Guia de Layouts - Cola para VS Code")
janela.resize(500, 450)


# ==================================================================
# 2. LAYOUT PRINCIPAL (QVBoxLayout)
# ==================================================================
# Tudo o que for inserido aqui vai empilhar VERTICALMENTE (de cima para baixo).
layout_principal = QVBoxLayout(janela)

# MARGENS E ESPAÇAMENTO:
layout_principal.setContentsMargins(20, 20, 20, 20)  # Recuo da borda da janela (Esq, Topo, Dir, Baixo)
layout_principal.setSpacing(15)                      # Espaço em pixels ENTRE cada bloco


# --- TÍTULO (Widget simples) ---
titulo = QLabel("Cadastro e Configurações")
titulo.setStyleSheet("font-size: 18px; font-weight: bold; color: #2c3e50;")
titulo.setAlignment(Qt.AlignCenter)  # Alinha o texto no centro do QLabel

layout_principal.addWidget(titulo)   # .addWidget() insere ELEMENTOS no layout


# ==================================================================
# 3. LAYOUT DE FORMULÁRIO (QFormLayout)
# ==================================================================
# Ideal para "Texto na Esquerda" + "Campo na Direita" de forma automática.
layout_formulario = QFormLayout()

campo_nome = QLineEdit()
campo_nome.setPlaceholderText("Digite aqui...")

combo_perfil = QComboBox()
combo_perfil.addItems(["Administrador", "Operador", "Visitante"])

# .addRow("Texto", widget) cria o par na mesma linha
layout_formulario.addRow("Nome do Usuário:", campo_nome)
layout_formulario.addRow("Perfil de Acesso:", combo_perfil)

# Insere a caixa do formulário dentro da caixa principal
layout_principal.addLayout(layout_formulario) # .addLayout() insere OUTRO LAYOUT


# ==================================================================
# 4. LAYOUT EM GRADE (QGridLayout)
# ==================================================================
# Ideal para alinhar itens em formato de Tabela/Planilha (Linha, Coluna).
layout_grade = QGridLayout()

check1 = QCheckBox("Opção A")
check2 = QCheckBox("Opção B")
check3 = QCheckBox("Opção C")
check4 = QCheckBox("Opção D")

# SINTAXE: .addWidget(item, linha, coluna)
layout_grade.addWidget(check1, 0, 0)  # Linha 0, Coluna 0
layout_grade.addWidget(check2, 0, 1)  # Linha 0, Coluna 1
layout_grade.addWidget(check3, 1, 0)  # Linha 1, Coluna 0
layout_grade.addWidget(check4, 1, 1)  # Linha 1, Coluna 1

layout_principal.addLayout(layout_grade)


# ==================================================================
# 5. O TRUQUE DA MOLA FLEXÍVEL (addStretch)
# ==================================================================
# Empurra tudo o que está acima para o TOPO da janela.
layout_principal.addStretch()


# ==================================================================
# 6. LAYOUT HORIZONTAL E ALINHAMENTO (QHBoxLayout)
# ==================================================================
# Coloca elementos LADO A LADO na mesma linha.
layout_rodape = QHBoxLayout()

btn_ajuda = QPushButton("Ajuda")
btn_cancelar = QPushButton("Cancelar")
btn_salvar = QPushButton("Salvar")

# Estilizando um botão com CSS básico (QSS)
btn_salvar.setStyleSheet("background-color: #27ae60; color: white; font-weight: bold;")

# ORDENAÇÃO NA HORIZONTAL:
layout_rodape.addWidget(btn_ajuda)      # 1. Fica na extrema esquerda

layout_rodape.addStretch()              # 2. MOLA INVISÍVEL: Empurra o botão de Ajuda pra esquerda
                                        #    e os botões abaixo para a extrema direita!

layout_rodape.addWidget(btn_cancelar)   # 3. Fica na direita
layout_rodape.addWidget(btn_salvar)     # 4. Fica na direita, ao lado do Cancelar

# Adiciona a linha de botões ao final da janela
layout_principal.addLayout(layout_rodape)


# Execute e exiba a janela
janela.show()
sys.exit(app.exec())







import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, 
    QLabel, QLineEdit, QPushButton, QTableWidget, 
    QTableWidgetItem, QHeaderView
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor

"""
===================================================================
 MAPA VISUAL DO PAINEL ("Gestão de Funcionários")
===================================================================

 ┌──────────────────────────────────────────────────────────────┐
 │ LAYOUT PRINCIPAL: QVBoxLayout (Vertical - Cima p/ Baixo)     │
 │                                                              │
 │  [ QLabel: Gestão de Funcionários (Centralizado) ]           │
 │                                                              │
 │  ┌────────────────────────────────────────────────────────┐  │
 │  │ QHBoxLayout (Linha de Ações + Mola Flexível)           │  │
 │  │  [ Cadastrar funcionário ] <--(mola)--> [ Pesquise...] │  │
 │  └────────────────────────────────────────────────────────┘  │
 │                                                              │
 │  ┌────────────────────────────────────────────────────────┐  │
 │  │ QTableWidget (Tabela de Dados)                         │  │
 │  │  Nome      │ Email            │ Área       │ Status    │  │
 │  │ ───────────┼──────────────────┼────────────┼───────────│  │
 │  │ Fulano...  │ silva@gmail.com  │ Pesquisador│ Ativo     │  │
 │  │ Fulano...  │ araujo@gmail.com │ Validador  │Desativado │  │
 │  └────────────────────────────────────────────────────────┘  │
 └──────────────────────────────────────────────────────────────┘
===================================================================
"""

app = QApplication(sys.argv)

# 1. JANELA BASE (Simulando o painel branco da tela)
janela = QWidget()
janela.setWindowTitle("Gestão de Funcionários")
janela.resize(800, 500)
janela.setStyleSheet("background-color: #ffffff;")  # Fundo branco igual à imagem

# 2. LAYOUT PRINCIPAL (Vertical)
layout_principal = QVBoxLayout(janela)
layout_principal.setContentsMargins(30, 20, 30, 20)
layout_principal.setSpacing(20)


# --- ELEMENTO 1: TÍTULO CENTRALIZADO ---
titulo = QLabel("Gestão de Funcionários")
titulo.setStyleSheet("font-size: 22px; font-weight: bold; color: #000000;")
titulo.setAlignment(Qt.AlignCenter)
layout_principal.addWidget(titulo)


# --- ELEMENTO 2: LINHA DE AÇÕES (Botão na Esquerda + Busca na Direita) ---
layout_acoes = QHBoxLayout()

# Botão verde "Cadastrar funcionário"
btn_cadastrar = QPushButton("Cadastrar funcionário")
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

# Campo de busca
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

# ORDENAÇÃO: Botão -> Mola -> Campo de Busca
layout_acoes.addWidget(btn_cadastrar)
layout_acoes.addStretch()  # MOLA: empurra a busca para a extrema direita
layout_acoes.addWidget(campo_busca)

# Adiciona a linha de ações ao layout principal
layout_principal.addLayout(layout_acoes)


# --- ELEMENTO 3: TABELA DE FUNCIONÁRIOS ---
dados_funcionarios = [
    ("Fulano Da Silva", "silva@gmail.com", "Pesquisador", "Ativo"),
    ("Fulano Ferreira", "ferreira@gmail.com", "Pesquisador", "Ativo"),
    ("Fulano Araujo", "araujo@gmail.com", "Validador SIPT", "Desativado"),
    ("Fulano Oliveira", "oliveira@gmail.com", "Validador SPAT", "Ativo"),
    ("Fulano Leite", "leite@gmail.com", "Validador NCO", "Ativo"),
    ("Fulano Da Guia", "guia@gmail.com", "Comitê", "Ativo"),
    ("Fulano Jacobina", "jabobina@gmail.com", "Comitê", "Desativado"),
    ("Fulano Nogueira", "nogueira@gmail.com", "Administrador", "Ativo"),
]

tabela = QTableWidget(len(dados_funcionarios), 4)
tabela.setHorizontalHeaderLabels(["Nome", "Email", "Área de Atuação", "Status"])

# Redimensiona colunas para ocupar toda a largura disponível
tabela.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
tabela.verticalHeader().setVisible(False)  # Esconde a numeração lateral das linhas

# ESTILIZAÇÃO DA TABELA (Cabeçalho azul e bordas arredondadas igual à foto)
tabela.setStyleSheet("""
    QTableWidget {
        background-color: #ffffff;
        gridline-color: #e0e0e0;
        border: 1px solid #d0d0d0;
        border-radius: 8px;
    }
    QHeaderView::section {
        background-color: #366896;
        color: white;
        font-weight: bold;
        padding: 10px;
        border: none;
    }
""")

# Preenchimento automático dos dados na tabela
for linha_idx, (nome, email, area, status) in enumerate(dados_funcionarios):
    item_nome = QTableWidgetItem(nome)
    item_email = QTableWidgetItem(email)
    item_area = QTableWidgetItem(area)
    item_status = QTableWidgetItem(status)

    # Alinhamentos
    item_email.setTextAlignment(Qt.AlignCenter)
    item_area.setTextAlignment(Qt.AlignCenter)
    item_status.setTextAlignment(Qt.AlignCenter)

    # Define a cor do texto do Status (Verde para Ativo / Laranja para Desativado)
    if status == "Ativo":
        item_status.setForeground(QColor("#28a745"))
    else:
        item_status.setForeground(QColor("#fd7e14"))

    # Insere os itens nas celulas
    tabela.setItem(linha_idx, 0, item_nome)
    tabela.setItem(linha_idx, 1, item_email)
    tabela.setItem(linha_idx, 2, item_area)
    tabela.setItem(linha_idx, 3, item_status)

layout_principal.addWidget(tabela)

# 4. EXIBE A TELA
janela.show()
sys.exit(app.exec())

