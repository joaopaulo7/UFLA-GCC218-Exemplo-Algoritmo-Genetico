'''Nesse arquivo, criamos uma classe que representará o Algoritmo Genético'''

import random
import copy



class GeneticAlgorithm:

    '''Este método representa o construtor da classe onde são inicializados os atributos
    referentes à taxa de mutação e crossover, o intervalo de valores de x, o número de
    indivíduos da população, e um dicionário  contendo cada população e sua avaliacção a
    partir da função.'''
    def __init__(self, mutacao, crossover, geracoes, x_min, x_max, num_indiv):

        self.taxa_mut = mutacao
        self.taxa_cross = crossover
        self.geracao = geracoes
        self.x_min = x_min
        self.x_max = x_max
        self.num_indiv = num_indiv
        
        self.populacao = {"CROMO": self.gera_populacao_inicial(), "AVAL": []}

    '''Este método é responsável por avaliar toda a população atual e inserir no dicionário'''
    def avalia_toda_pop(self):
        avaliacao = []
        for pop in self.populacao["CROMO"]:
            avaliacao.append(self.avalia_x(GeneticAlgorithm.decoda_binario(pop)))
        self.populacao["AVAL"] = avaliacao
        
    '''Este método gera uma população inicial aleatória'''
    def gera_populacao_inicial(self):
        lista = []
        for i in range(self.num_indiv):
            lista.append(random.choices([0, 1], k = 5))
        return lista

    '''Este método é responsável por realizar a escolha de um indivíduo a partir da seleção 
    aleatória de dois indivíduos e pela avaliação do melhor dos dois.'''
    def torneio(self):
        index_first = random.choice(range(self.num_indiv))
        index_second = random.choice(range(self.num_indiv))

        if(self.populacao["AVAL"][index_first] > self.populacao["AVAL"][index_second]):
            return self.populacao["CROMO"][index_first]
        else:
            return self.populacao["CROMO"][index_second]
    
    '''Este método é responsável por gerar uma nova população. Dois indivíduos são gerados
    ca partir das características do pai e da mãe. Há uma porcentagem de chances de cada filho
    sofrer mutação e/ou crossover.'''
    def gera_populacao(self):
        nova_geracao = []
        while(len(nova_geracao) < self.num_indiv):
            pai = self.torneio()
            mae = self.torneio()
            filho1 = pai
            filho2 = mae
           
            '''Probabilidade de crossover'''
            if(random.random() < self.taxa_cross):
                filho1, filho2 = self.crossover(pai, mae, 5)
            

            '''Probabilidade de mutação'''
            if(random.random() < self.taxa_mut):
                self.mutacao(filho1, 5)

            '''Probabilidade de mutação'''
            if(random.random() < self.taxa_mut):
                self.mutacao(filho2, 5)
            
            nova_geracao = nova_geracao + [filho1, filho2]
        
        '''A nova geração será inserida no dicionário da população'''
        self.populacao["CROMO"] = nova_geracao

    '''Método estático que transforma o número binário em decimal'''
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

  
    '''Este método avalia o valor de x com base na função especificada. Caso o valor de x esteja
    fora do intervalo, é retornado False.'''
    def avalia_x(self, x):
        if(x < self.x_min or x > self.x_max):
            return False
        else:
            return x**2 - 3*x + 4 

    '''Este método realiza o crossover em dois indivíduos. Cada um recebe uma parte da mãe e uma
    outra parte do pai, podendo ser mais ou menos de cada um, a partir de um valor aleatório.'''
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

    '''Este método realiza a mutação do indivíduo, escolhendo um index aleatório para
    a troca de bits.'''
    @staticmethod
    def mutacao(indiv, tam_bit):
        gene = random.choice(range(tam_bit))
        indiv[gene] = 1 if indiv[gene] == 0 else 1 


    '''Este método pega o histórico de todas as gerações e avaliações.'''
    def geracoes(self):
        historico_avaliacoes = []
        historico_avaliacoes.append(copy.deepcopy(self.populacao))
        for i in range(self.geracao):
            self.avalia_toda_pop()
            self.gera_populacao()
            print(self.populacao["AVAL"])
            historico_avaliacoes.append(copy.deepcopy(self.populacao))

        return historico_avaliacoes
    

    

