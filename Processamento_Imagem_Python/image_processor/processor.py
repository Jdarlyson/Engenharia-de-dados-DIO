from PIL import Image

def abrir_imagem(caminho):
    return Image.open(caminho)

def salvar_imagem(imagem, caminho):
    imagem.save(caminho)

def redimensionar_imagem(imagem, nova_largura, nova_altura):
    return imagem.resize((nova_largura, nova_altura))

def main():
    caminho_imagem = '../imagens/python-logo-master.png'  # Caminho relativo da imagem original
    imagem = abrir_imagem(caminho_imagem)
    
    nova_largura = 300  # Defina a largura desejada
    nova_altura = 100   # Defina a altura desejada
    imagem_redimensionada = redimensionar_imagem(imagem, nova_largura, nova_altura)

    # Salvar a imagem redimensionada na pasta 'imagens'
    salvar_imagem(imagem_redimensionada, '../imagens/imagem_redimensionada.png')  # Salve como .png

if __name__ == "__main__":
    main()
