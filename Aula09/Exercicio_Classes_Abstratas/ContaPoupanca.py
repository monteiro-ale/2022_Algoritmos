from abc import ABC, abstractmethod
from ContaBancaria import ContaBancaria

class ContaPoupanca(ContaBancaria):

    def __init__(self, cartaoDebito = False):
        self.cartaoDebito = cartaoDebito

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
    
    def rendimentoMes(self):
        self.saldo = self.saldo +(self.saldo * 0.5 / 100)
        

    def getInformacoes(self):
        return super().getInformacoes()+f"\nCartão de debito: {self.cartaoDebito}"