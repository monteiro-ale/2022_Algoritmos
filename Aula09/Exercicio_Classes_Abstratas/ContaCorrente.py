from abc import ABC, abstractmethod
from ContaBancaria import ContaBancaria

class ContaCorrente(ContaBancaria):

    def __init__(self, cartaoCredito = False):
        self.cartaoCredito = cartaoCredito
    
    def cadastrar(self, numConta, agencia, codCliente):
        self.numConta = numConta
        self.agencia = agencia
        self.codCliente = codCliente
        self.saldo = 0
    
    def getSaldo(self):
        return self.saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor
    
    def descontaTarifa(self):
        self.saldo -= 1.50
    
    def getInformacoes(self):
        return super().getInformacoes()+ f"\nCartão de credito: {self.cartaoCredito}"
