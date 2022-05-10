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
        self.numConta = numConta
        self.agencia = agencia
        self.codCliente = codCliente
        self.saldo = 0

    @abstractmethod
    def getSaldo(self):
        return self.saldo

    @abstractmethod
    def depositar(self, valor):
        self.saldo += valor

    def getInformacoes(self):
        return f"Numero da Conta : {self.numConta}\nAgencia :{self.agencia}\nCodigo :{self.codCliente}\nSaldo :{self.saldo}"
    

