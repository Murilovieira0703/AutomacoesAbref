from PIL import Image, ImageDraw, ImageFont
from datetime import datetime, timedelta

def gerar_carteirinha_com_foto(nome, nascimento, unidade, foto_path, modelo_path, output_path):
    # Carregar o modelo da carteirinha
    modelo = Image.open(modelo_path)
    draw = ImageDraw.Draw(modelo)

    # Definir a fonte
    fonte = ImageFont.truetype("arial.ttf", 44)
    fonte_unidade = ImageFont.truetype("arial.ttf", 38)

    # Calcular a validade (1 ano a partir da data atual)
    data_criacao = datetime.now()
    validade = data_criacao + timedelta(days=365)
    validade_formatada = validade.strftime("%d/%m/%Y")

    # Adicionar os dados na imagem com efeito de negrito
    for deslocamento in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        draw.text((725 + deslocamento[0], 290 + deslocamento[1]), f"{nome}", fill="black", font=fonte)
        draw.text((725 + deslocamento[0], 436 + deslocamento[1]), f"{nascimento}", fill="black", font=fonte)
        draw.text((725 + deslocamento[0], 570 + deslocamento[1]), f"{validade_formatada}", fill="black", font=fonte)
        draw.text((735 + deslocamento[0], 700 + deslocamento[1]), f"unidade", fill="black", font=fonte_unidade)
        draw.text((710 + deslocamento[0], 750 + deslocamento[1]), f"{unidade}", fill="black", font=fonte)

    # Carregar a foto do atleta
    foto = Image.open(foto_path)

    # Redimensionar a foto mantendo o formato 9:16
    largura_desejada = 477  # Ajuste conforme necessário
    altura_desejada = 713  # Ajuste conforme necessário
    foto = foto.resize((largura_desejada, altura_desejada))

    # Inserir a foto no local correto (ajuste as coordenadas conforme o layout)
    modelo.paste(foto, (106, 208))  # Coordenadas (x, y) para a foto

    # Salvar a imagem gerada
    modelo.save(output_path)
    print(f"Carteirinha gerada e salva em: {output_path}")

def gerar_carteirinha_verso(contato, modelo_path, output_path):
    # Carregar o modelo da carteirinha
    modelo = Image.open(modelo_path)
    draw = ImageDraw.Draw(modelo)

    # Definir a fonte
    fonte = ImageFont.truetype("arial.ttf", 48)

    # Adicionar os dados na imagem
    for deslocamento in [(0, 0), (1, 0), (0, 1), (1, 1)]:
        draw.text((785 + deslocamento[0], 905 + deslocamento[1]), f"{contato}", fill="black", font=fonte)

    # Salvar a imagem gerada
    modelo.save(output_path)
    print(f"Verso da carteirinha gerada e salva em: {output_path}")

gerar_carteirinha_com_foto(
    nome="João Silva",
    nascimento="16/02/2015", 
    unidade="Campinas",  # Unidade do atleta
    foto_path="foto_joao.png",  # Caminho da foto do atleta
    modelo_path="modelo-frente.png",  # Caminho do modelo
    output_path="carteirinha_joao.png"  # Caminho de saída
)

gerar_carteirinha_verso(
    contato="(19) 99999-9999",  # Contato da escola
    modelo_path="modelo-verso.png",  # Caminho do modelo
    output_path="carteirinha_joao_verso.png"  # Caminho de saída
)