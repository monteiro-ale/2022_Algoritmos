# A classe Lixadeira possui o atributo/propriedade fortemente privado, rotações. 
# Esta classe reimplementa o método getInformacoes() herdado de Furadeira. ** Ferramenta

from abc import ABC, abstractmethod
from Ferramenta import Ferramenta

class Lixadeira(Ferramenta):

    def __init__(self, rotacoes):
        self.__rotacoes = rotacoes
    
    def cadastrar(self, nome, tensao, preco):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco
    
    def getRotacoes(self):
        return self.__rotacoes

    def setRotacao(self, rotacoes):
        self.__rotacoes = rotacoes
    
    def getInformacoes(self):
        return super().getInformacoes()+ f"\nRotação: {self.__rotacoes}"

