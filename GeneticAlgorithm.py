import random
import copy

inft = 1000000

class GeneticAlgorithm:

    def __init__(self, mutacao, crossover, geracoes, x_min, x_max, num_indiv):

        self.taxa_mut = mutacao
        self.taxa_cross = crossover
        self.geracao = geracoes
        self.x_min = x_min
        self.x_max = x_max
        self.num_indiv = num_indiv
        
        self.populacao = {"CROMO": self.gera_populacao_inicial(), "AVAL": []}


    def avalia_toda_pop(self):
        avaliacao = []
        for pop in self.populacao["CROMO"]:
            avaliacao.append(self.avalia_x(GeneticAlgorithm.decoda_binario(pop)))
        self.populacao["AVAL"] = avaliacao
        
    
    def gera_populacao_inicial(self):
        lista = []
        for i in range(self.num_indiv):
            lista.append(random.choices([0, 1], k = 5))
        return lista

    def torneio(self):
        index_first = random.choice(range(self.num_indiv))
        index_second = random.choice(range(self.num_indiv))

        if(self.populacao["AVAL"][index_first] > self.populacao["AVAL"][index_second]):
            return self.populacao["CROMO"][index_first]
        else:
            return self.populacao["CROMO"][index_second]
    
    
    def gera_populacao(self):
        nova_geracao = []
        while(len(nova_geracao) < self.num_indiv):
            pai = self.torneio()
            mae = self.torneio()
            filho1 = pai
            filho2 = mae
            
            if(random.random() < self.taxa_cross):
                filho1, filho2 = self.crossover(pai, mae, 5)
            

            if(random.random() < self.taxa_mut):
                self.mutacao(filho1, 5)

            if(random.random() < self.taxa_mut):
                self.mutacao(filho2, 5)
            
            nova_geracao = nova_geracao + [filho1, filho2]
        
        self.populacao["CROMO"] = nova_geracao

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
            return False
        else:
            return x**2 - 3*x + 4 

    @staticmethod
    def crossover(indiv_um, indv_dois, tam_bit):
        corte = random.choice(range(1, tam_bit-1))

        primeira_parte_1 = indiv_um[:corte]
        segunda_parte_1 = indv_dois[corte:]
        primeira_parte_2 = indiv_um[:corte]
        segunda_parte_2 = indv_dois[corte:]

        filho_1 = primeira_parte_1 + segunda_parte_1
        filho_2 = primeira_parte_2 + segunda_parte_2

        return filho_1, filho_2


    @staticmethod
    def mutacao(indiv, tam_bit):
        gene = random.choice(range(tam_bit))
        indiv[gene] = 1 if indiv[gene] == 0 else 1 


    def geracoes(self):
        historico_avaliacoes = []
        historico_avaliacoes.append(copy.deepcopy(self.populacao))
        for i in range(self.geracao):
            self.avalia_toda_pop()
            self.gera_populacao()
            print(self.populacao["AVAL"])
            historico_avaliacoes.append(copy.deepcopy(self.populacao))

        return historico_avaliacoes
    

    

