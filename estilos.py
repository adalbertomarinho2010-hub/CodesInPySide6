class Cores:
    FUNDO = "#392850"
    CARTAO = "#8471a8"
    TEXTO = "#000000"
    TEXTO_SECUNDARIO = "#000000"
    PLACEHOLDER = "#8762ec"
    BORDA = "#000000"
    PRIMARIA = "#0709AC"
    PRIMARIA_HOVER = "#0709AC"
    PRIMARIA_PRESSED = "#018547"

ESTILO = f"""
QWidget#Janela {{
    background-color: {Cores.FUNDO};
}}

QFrame#Formulario {{
    background-color: {Cores.CARTAO};
    border-radius: 12px;
}}

QLabel#Titulo {{
    font-size: 26px;
    font-weight: bold;
    color: {Cores.TEXTO};
}}

QLabel#Subtitulo {{
    font-size: 14px;
    color: {Cores.TEXTO_SECUNDARIO};
}}

QLineEdit {{
    background-color: white;
    border: 2px solid {Cores.PLACEHOLDER};
    border-radius: 6px;
    padding: 10px;
    color: {Cores.TEXTO};
    font-size: 14px;
}}

QLineEdit:focus {{
    border: 2px solid {Cores.PRIMARIA}; 
    background-color: #fafdff;
}}

QPushButton#BotaoEntrar {{
    background-color: {Cores.PRIMARIA};
    color: white;
    font-weight: bold;
    border-radius: 6px;
    padding: 12px;
    font-size: 16px;
}}

QPushButton#BotaoEntrar:hover {{
    background-color: {Cores.PRIMARIA_HOVER};
}}

QPushButton#BotaoEntrar:pressed {{
    background-color: {Cores.PRIMARIA_PRESSED};
}}

QPushButton#LinkEsqueci {{
    background-color: transparent;
    color: {Cores.PRIMARIA};
    border: none;
    text-align: right;
}}

QPushButton#LinkEsqueci:hover {{
    text-decoration: underline;
}}
"""
