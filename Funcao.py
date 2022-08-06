'''
Trabalho: Exercício sobre Algoritmos Genético da matéria de Inteligência Artificial GCC128
Alunos: Ana Luiza Faria Calixto - João Paulo Paiva Lima

O trabalho tem como intuito encontrar o valor de x para a função f(x) = x*x - 3x + 4, onde x
será o valor máximo.

'''

import GeneticAlgorithm

algoritmo = GeneticAlgorithm.GeneticAlgorithm(0.01, 0.7, 5, -10, 10, 4)

print(algoritmo.populacao["AVAL"])






