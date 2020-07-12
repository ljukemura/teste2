from PIL import Image
import pytesseract
from datetime import datetime
from os import  listdir
import pygame

diretorio = listdir('D:\experimentos\pasta de imagens')
diretorio.remove("Arquivos gerados")

print ('Diretório de imagens:')
for index, item in enumerate(diretorio):
    print (index, "-", item)

escolha_usuario = int(input("Coloque o nº do arquivo que deseja: "))
nome_arq_ent = (diretorio[escolha_usuario])
im = Image.open('D:\experimentos\pasta de imagens\\' + diretorio[escolha_usuario])


text = pytesseract.image_to_string(im, lang = 'por')
print("\n","-"*10,"Texto extraído","-"*10,"\n")
print(str(text.strip()))
print("\n","-"*10,"Texto extraído","-"*10,"\n")

dc1 = str.upper(input("Deseja criar um arquivo txt? S/N\n"))
if  dc1 == "S":

    saida2 = nome_arq_ent[:nome_arq_ent.find(".")]+"-"+ datetime.now().strftime('%d_%m_%Y_%H%M')+'.txt'
    with open('D:\experimentos\pasta de imagens\Arquivos gerados\\' + saida2, 'w') as arq_saida:
        arq_saida.write(text)
    print("Arquivo criado")


else:
    pygame.init()

    bg = pygame.image.load('D:\experimentos\pasta de imagens\\' + diretorio[escolha_usuario])

    black = (0, 0, 0)

    win = pygame.display.set_mode((im.width, im.height))
    pygame.display.set_caption("Imagem")


    def redrawGameWindow():
        win.blit(bg, (0, 0))
        pygame.display.update()


    run = True
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.mouse.get_pos()
                i = pygame.mouse.get_pos()

            if event.type == pygame.MOUSEBUTTONUP:
                pygame.mouse.get_pos()
                s = pygame.mouse.get_pos()
                run = False

        redrawGameWindow()

    pygame.quit()

    im_ocr = im.crop((min(i[0], s[0]), min(i[1], s[1]), max(i[0], s[0]), max(i[1], s[1])))

    text = pytesseract.image_to_string(im_ocr, lang='por')
    print("\n", "-" * 10, "Texto extraído", "-" * 10, "\n")
    print(str(text.strip()))
    print("\n", "-" * 10, "Texto extraído", "-" * 10, "\n")

    saida2 = nome_arq_ent[:nome_arq_ent.find(".")] + "-" +"ajustado-"+ datetime.now().strftime('%d_%m_%Y_%H%M') + '.txt'
    with open('D:\experimentos\pasta de imagens\Arquivos gerados\\' + saida2, 'w') as arq_saida:
        arq_saida.write(text)
    print("Arquivo ajustado criado")

