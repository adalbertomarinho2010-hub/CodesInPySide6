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
