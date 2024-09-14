
import random


def buscaBinaria(inicio,fim,dados,buscando):

    while(inicio <= fim):
        meio = int((inicio + fim)/2)
        if (buscando > dados [meio]):
            inicio = meio +1
        elif (buscando <dados[meio]):
            fim = meio - 1
        else:
            return meio

    return -1

dados = random.sample(range(10),10)
dados.sort()
print(dados)

buscando = int(input('digite o valor que deseja buscar'))
achou = buscaBinaria(0, len(dados),dados,buscando)

if (achou == -1):
    print('valor encontrado')
else:
    print('valor encontrado na posição {}'.format(achou))




tempo_final = tem