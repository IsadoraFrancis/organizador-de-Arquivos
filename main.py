import os
from tkinter.filedialog import askdirectory

# Seleciona a pasta
caminho = askdirectory(title="Selecione uma pasta")

# Só executa se uma pasta for selecionada
if caminho:
    lista_arquivos = os.listdir(caminho)

    # Define as extensões e os nomes das subpastas
    locais = {
        "imagens": [".png", ".jpg", ".jpeg"],
        "planilhas": [".xlsx"],
        "pdfs": [".pdf"],
        "csv": [".csv"],
    }

    for arquivo in lista_arquivos:
        nome, extensao = os.path.splitext(arquivo)
        extensao = extensao.lower()  # padroniza a extensão para evitar problemas com .JPG e .jpg

        for pasta, extensoes in locais.items():
            if extensao in extensoes:
                # Caminho da subpasta
                pasta_destino = os.path.join(caminho, pasta)

                # Cria a subpasta se ela não existir
                if not os.path.exists(pasta_destino):
                    os.mkdir(pasta_destino)

                # Caminho completo do arquivo de origem e destino
                origem = os.path.join(caminho, arquivo)
                destino = os.path.join(pasta_destino, arquivo)

                # Garante que o arquivo existe antes de mover
                if os.path.exists(origem):
                    os.rename(origem, destino)