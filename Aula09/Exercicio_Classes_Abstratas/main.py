from abc import ABC, abstractmethod
from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca

#Teste conta corrente
c1 = ContaCorrente(True)
c1.cadastrar('03345-1', '4463', 256)
c1.depositar(500)
c1.descontaTarifa()
c1.sacar(50)
print(c1.getInformacoes())
print(c1.getSaldo())

print('\n\n')

# Teste conta poupança
c2 = ContaPoupanca(True)
c2.cadastrar('042785-2', '3387', 989)
c2.depositar(200)
c2.rendimentoMes()
c2.sacar(20)
print(c2.getInformacoes())