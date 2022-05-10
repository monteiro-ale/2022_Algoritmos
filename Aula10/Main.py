from abc import ABC, abstractmethod
from Computador import Computador
from Notebook import Notebook
from Desktop import Desktop

pc = Desktop('10w')
pc.cadastrar('405xp', 'preto', 'R$1500')

print(pc.getInformacoes())

print(pc.getPotenciaFonte())
pc.setPotenciaFonte('40w')
print(pc.getPotenciaFonte())

pc2 = Notebook('3horas')
pc2.cadastrar('hp pavilion', 'cinza', 'R$1000')
print(pc2.getInformacoes())