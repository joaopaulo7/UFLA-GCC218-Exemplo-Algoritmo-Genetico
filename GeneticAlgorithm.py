import random

inft = 1000000

class GeneticAlgorithm:

    def __init__(self, mutacao, crossover, geracoes, x_min, x_max, num_indiv):

        self.taxa_mut = mutacao
        self.taxa_cross = crossover
        self.geracoes = geracoes
        self.x_min = x_min
        self.x_max = x_max
        self.num_indiv = num_indiv
        
        self.populacao = {"CROMO": self.gera_populacao_inicial(), "AVAL": [0]*num_indiv}


    def gera_populacao_inicial(self):
        lista = []
        for i in range(self.num_indiv):
            lista.append(random.choices([0, 1], k = 5))
        return lista

    #def gera_populacao():


    @staticmethod
    def decoda_binario(num_bin):
        soma = 0 
        for i in range(1, len(num_bin)):
            if(num_bin[i] == 1):
                soma = soma + 2**(len(num_bin)-i -1)
        if(num_bin[0] == 1):
            return -soma
        else:
            return soma

  
    def avalia_x(self, x):
        if(x < self.x_min or x > self.x_max):
            return 0
        else:
            return x**2 - 3*x + 4 

    @staticmethod
    def crossover(indiv_um, indv_2, tam_bit):
        corte = random.choice(range(1, tam_bit-1))

        primeira_parte_1 = indiv_um[:corte]
        segunda_parte_1 = indv_2[corte:]
        primeira_parte_2 = indiv_um[:corte]
        segunda_parte_2 = indv_2[:corte]

        filho_1 = primeira_parte_1 + segunda_parte_1
        filho_2 = primeira_parte_2 + segunda_parte_2

        return filho_1, filho_2


    @staticmethod
    def mutacao(indiv, tam_bit):
        gene = random.choice(range(tam_bit))
        indiv[gene] = 1 if indiv[gene] == 0 else 1 

