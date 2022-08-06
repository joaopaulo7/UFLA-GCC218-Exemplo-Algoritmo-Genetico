import random

inft = 1000000

def gera_populacao_inicial(numIndv):
    lista = []
    for i in range(numIndv):
        lista.append(random.choices([0, 1], k = 5))
    return lista


def decoda_binario(numBin):
    soma = 0 
    for i in range(len(numBin)-1, 0, -1):
        if(numBin[i] == 1):
            soma = soma + 2**(len(numBin)-i -1)
    if(numBin[0] == 1):
        return -soma
    else:
        return soma

def avalia(x):
    if(x < -10 or x > 10):
        return 0
    else:
        return x**2 - 3*x + 4 

def crossover(indv1, indv2, tam_bit):
    corte = random.choice(1, tam_bit-1)

    primeira_parte_1 = indv1[:corte]
    segunda_parte_1 = indv2[corte:]
    primeira_parte_2 = indv1[:corte]
    segunda_parte_2 = indv2[:corte]

    filho_1 = primeira_parte_1 + segunda_parte_1
    filho_2 = primeira_parte_2 + segunda_parte_2

    return filho_1, filho_2


def mutacao(indiv, tam_bit):
    gene = random.choice(range(tam_bit))
    indiv[gene] = 1 if indiv[gene] == 1 else 0 

    

pop = gera_populacao_inicial(4)

for i in pop:
    print(i, end = " ")
    x = decoda_binario(i)
    print(x, end = "->")
    print(avalia(x))
