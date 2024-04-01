import os
from tkinter.filedialog import askdirectory #importando somente a função askdirector dentro do tkinter

caminho = askdirectory(title="selecione uma pasta") # A função askdirectory abre um popup no pc para selecionar a pasta. salva o caminho da pasta

lista_arquivos = os.listdir(caminho) #salva na var os arquivos que tem naque diretorio selecionado
#print(lista_arquivos)
locais = {
    "imagens": [".png", ".jpeg", ".img"], #aqui salva os novos arquivos nas pastas. 1 nome da pasta: 2 extensoes arquivos
    "planilhas Excel": [".xlsx"],
    "Arquivos Word": [".docx"],
    "Arquivos PDF": [".pdf"],
    "Arquivos de Audio": [".mp3", ".aac"],
    "Arquivos de video": [".mp4", ".mov", ".wmv", ".webm" ]
}

for arquivo in lista_arquivos: # salva o nome do arquivo na var arquivo.
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}") #splitext passa o caminho/arquivo - caminho 01arquivo/extensao .pdf
    for pasta in locais: #pra cada pasta dentro dos locais, verifica se a extensão esta dentro da lista
        if extensao in locais[pasta]: #pegando o valor dentro da lista
            if not os.path.exists(f"{caminho}/{pasta}"): #verifica se não existe a pasta
                os.mkdir(f"{caminho}/{pasta}") #criar uma pasta
            os.rename(f"{caminho}/{arquivo}", f"{caminho}/{pasta}/{arquivo}") #rename, cami/nomeantigo, "caminho/nomenovo" 
print('Arquivos organizados com Sucesso')  