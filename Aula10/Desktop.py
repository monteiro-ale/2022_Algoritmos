from abc import ABC, abstractmethod

from Computador import Computador

class Desktop(Computador):

    def __init__(self, pdf):
        self._potenciaDaFonte = pdf
    
    def cadastrar(self, modelo, cor, preco):
        self.modelo = modelo
        self.cor = cor
        self.preco = preco
    
    def getPotenciaFonte(self):
        return self._potenciaDaFonte

    def setPotenciaFonte(self, pdf):
        self._potenciaDaFonte = pdf

    def getInformacoes(self):
        return super().getInformacoes()+ f"\nPotencia da Fonte{self._potenciaDaFonte}"

    