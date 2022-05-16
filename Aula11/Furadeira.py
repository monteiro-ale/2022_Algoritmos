# A classe Furadeira deve possuir o atributo/propriedade fracamente privado, potência.
#  Esta classe reimplementa o método getInformacoes() herdado de Furadeira. **Ferramenta

from abc import ABC, abstractmethod
from Ferramenta import Ferramenta

class Furadeira(Ferramenta):

    def __init__(self, potencia):
        self._potencia = potencia
    
    def cadastrar(self, nome, tensao, preco):
        self.nome = nome
        self.tensao = tensao
        self.preco = preco
    
    def getPotencia(self):
        return self._potencia

    def setPotencia(self, potencia):
        self._potencia = potencia
    
    def getInformacoes(self):
        return super().getInformacoes()+ f"\nPotencia: {self._potencia}"