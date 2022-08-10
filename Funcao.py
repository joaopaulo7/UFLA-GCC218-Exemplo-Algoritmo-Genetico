'''
Trabalho: Exercício sobre Algoritmos Genético da matéria de Inteligência Artificial GCC128
Alunos: Ana Luiza Faria Calixto - João Paulo Paiva Lima

O trabalho tem como intuito encontrar o valor de x para a função f(x) = x*x - 3x + 4, onde x
será o valor máximo.

'''

#Importamos as bibliotecas necessárias e a classe do AG
import GeneticAlgorithm
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation


#Criamos uma instância do algoritmo genético para a otimização
algoritmo = GeneticAlgorithm.GeneticAlgorithm(0.05, 0.7, 9, -10, 10, 20)


#Chama a função que cria as gerações, as avalia.
historico = algoritmo.geracoes()


#Cria um vetor para guardar as informações dos frames da animação
frames = []

#percorre as gerações
i = 1
for geracao in historico:
    
    #Cria uma lista para guardar as informações das gerações.
    #  Inclusive, gera uma cor aletória para cada geração.
    aux = [i, ([random.random() for i in range(3)] + [1])]
    i += 1
    
    #Adiciona os valores de avaliação aos frames da animação
    for indiv in geracao["CROMO"]:
        aux.append(algoritmo.decoda_binario(indiv))
    frames.append(aux)


#Cria o gráfico de fundo 
fig, ax = plt.subplots()
xdata, ydata = [], []


#Inicia o gráfico e define os limites
def init():
    ax.set_xlim(-16, 16)
    ax.set_ylim(-20, 184)


#Faz o update dos frames da animação
def update(frame):
    xs = frame[2:]
    ys = []
    
    #Aplica ruidos nos valores de X e Y para criar a impressão de volume de pontos. 
    for i in range(len(xs)):
        xs[i] = xs[i]*(1+(random.random()*2-1)*0.004)
        ys.append((xs[i]**2 - 3*xs[i] + 4)*(1+(random.random()*2-1)*0.008))
    
    #faz o espalhamento dos pontos (indivíduos) no gráfico, separando as gerações por cor.
    plt.scatter(xs, ys, s = 200, color = frame[1], edgecolors = "black", label = "Geração " + str(frame[0]))
    ax.legend(loc = 4)


#Traça a linha.
x = np.linspace(-10,10,100)
plt.plot(x, x**2 - 3*x + 4, 'black', zorder = 0)


#Cria a animção.
ani = FuncAnimation(fig, update, frames = frames,
                    init_func=init, blit=True, interval = 2000, repeat = False)

#Mostra a gráfico/animação.
plt.show()
