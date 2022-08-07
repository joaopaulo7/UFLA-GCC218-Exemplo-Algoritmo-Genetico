'''
Trabalho: Exercício sobre Algoritmos Genético da matéria de Inteligência Artificial GCC128
Alunos: Ana Luiza Faria Calixto - João Paulo Paiva Lima

O trabalho tem como intuito encontrar o valor de x para a função f(x) = x*x - 3x + 4, onde x
será o valor máximo.

'''

import GeneticAlgorithm
import random
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.animation import FuncAnimation

algoritmo = GeneticAlgorithm.GeneticAlgorithm(0.01, 0.7, 9, -10, 10, 20)

print(algoritmo.populacao["CROMO"])

algoritmo.avalia_toda_pop()

historico = algoritmo.geracoes()

frames = []

i = 1
for geracao in historico:
    aux = [i, ([random.random() for i in range(3)] + [1])]
    i += 1
    for indiv in geracao["CROMO"]:
        aux.append(algoritmo.decoda_binario(indiv))
    print(aux)
    frames.append(aux)


fig, ax = plt.subplots()
xdata, ydata = [], []

def init():
    ax.set_xlim(-15, 15)
    ax.set_ylim(-20, 150)

def update(frame):
    xs = frame[2:]
    ys = []
    for i in range(len(xs)):
        xs[i] = xs[i]*(1+(random.random()*2-1)*0.004)
        ys.append((xs[i]**2 - 3*xs[i] + 4)*(1+(random.random()*2-1)*0.008))
        
    plt.scatter(xs, ys, s = 200, color = frame[1], edgecolors = "black", label = "Geração " + str(frame[0]))
    ax.legend(loc = 4)

x = np.linspace(-10,10,100)
plt.plot(x, x**2 - 3*x + 4, 'black', zorder = 0)

ani = FuncAnimation(fig, update, frames = frames,
                    init_func=init, blit=True, interval = 2000, repeat = False)


plt.show()
