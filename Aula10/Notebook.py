from abc import ABC, abstractmethod

from Computador import Computador

class Notebook(Computador):

    def __init__(self, tempoBateria):
        self.__tempoBateria = tempoBateria
    
    def cadastrar(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getTempoBateria(self):
        return self.__tempoBateria

    def setTempoBateria(self, tempo):
        self.__tempoBateria = tempo

    def getInformacoes(self):
        return super().getInformacoes()+ f"\nTempo de Bateria {self.__tempoBateria}"
    