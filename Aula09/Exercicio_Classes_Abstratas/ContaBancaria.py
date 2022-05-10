# Implementar a classe abstrata
# ContaBancaria com os
# métodos cadastrar e
# depositar e as respectivas
# classes concretas.

from abc import ABC, abstractmethod

class ContaBancaria(ABC):

    def __init__(self):
        self.numConta = None
        self.agencia
        self.codCliente
        self.saldo
    
    @abstractmethod
    def cadastrar(self, numConta, agencia, codCliente):
        pass

    @abstractmethod
    def getSaldo(self):
        pass

    @abstractmethod
    def depositar(self, valor):
        pass

    def getInformacoes(self):
        return f"Numero da Conta : {self.numConta}\nAgencia :{self.agencia}\nCodigo :{self.codCliente}\nSaldo :{self.saldo}"
    

