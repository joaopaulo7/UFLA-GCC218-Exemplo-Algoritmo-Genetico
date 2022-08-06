import random

inft = 1000000

def geraIndivuduos(numIndv):
    lista = []
    for i in range(numIndv):
        lista.append(random.choices([0, 1], k = 5))
    return lista
    
def decodaBinario(numBin):
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

def cossover(indv1, indv2):
    corte = random.choice(range(5))
    


pop = geraIndivuduos(4)

for i in pop:
    print(i, end = " ")
    x = decodaBinario(i)
    print(x, end = "->")
    print(avalia(x))

print(range(5))
