# • Faça um programa em Python que implemente uma busca
# sequencial de um número inteiro.
# – Dica:
# • Duas classes: classe de busca e classe de teste
# • utilize uma lista vazia para iniciar
# 1. Faça uma função que crie uma lista de 500 valores inteiros randômicos
# 2. Faça uma função chamada buscaSequencial(elemento) que entre um valor e retorne a sua posição na lista ou uma mensagem caso não tenha encontrado
# 3. Faça uma classe de teste com as seguintes chamadas:
# ret = buscaSequencial(10)
# print(ret)
# ret = buscaSequencial(100)
# print(ret)
# ret = buscaSequencial(355)
# print(ret)
# ret = buscaSequencial(433)
# print(ret)

import random

class Busca:
    def __init__(self):
        self.vetor = []

    def criaVetor(self, inicio, fim):

        vetor = list(range(inicio, fim))
        random.shuffle(vetor)
        self.vetor = vetor
        

    def buscaSequencial(self, valor):
        i=0
        while i < len(self.vetor): 
            if self.vetor[i] == valor:
                return f"Lista gerada:{self.vetor}\n Elemento encontrado na posição {i}"
            i+=1
        return f"Elemento não encontrado"

busca1 = Busca()

busca1.criaVetor(1,30)

print(busca1.buscaSequencial(5))




