from abc import ABC, abstractmethod

class Computador(ABC):

    def __init__(self):
        self.modelo = None
        self.cor = None
        self.preco = None
    
    @abstractmethod
    def cadastrar(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getInformacoes(self):
        return "Modelo:"+ self.modelo+"\nCor:"+ self.cor+ "\nPreco:"+ self.preco