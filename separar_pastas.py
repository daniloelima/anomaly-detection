#esse programa tem como objetivo, ler todos os nomes de arquivos dentro de uma pasta (incluindo os arquivos em subpastas) e
#separar os arquivos Reais ('WELL') em 'qtdfolds' arquivos diferentes

import os #faz a busca dos arquivos no diretorio
import re #faz a busca de um termo dentro de uma string

pasta = './data' #caminho de onde os arquivos serão lidos
saida = './separarfolds' #caminho onde os arquivos serao gerados
qtdfolds = 5

def geraFolds(folds, qtd):
    for i in range(0, qtd):
        #print(i)
        folds.append(open(saida+'/fold'+str(i+1)+'.txt', 'w'))
    #print(folds)
    return folds

folds = []
geraFolds(folds, qtdfolds)
x = 0
for diretorio, subpastas, arquivos in os.walk(pasta):
    for arquivo in arquivos:
        #print(arquivo)
        if re.search('WELL', arquivo, re.IGNORECASE):
            #print("entro")
            x += 1
            folds[x%qtdfolds].write(os.path.join(diretorio, arquivo) + '\n')
