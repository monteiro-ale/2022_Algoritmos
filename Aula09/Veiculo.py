

from abc import ABCMeta, abstractmethod
from abc import ABCMeta

class Veiculo(metaclass = ABCMeta):

    @property
    def modelo(self):
        return self.__modelo

    @modelo.setter
    @abstractmethod
    def modelo(self, valor):
        self.__modelo = valor

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, valor):
        self.__ano = valor

    def imprimir(self):
        print("Modelo: ", self.__modelo)
        print("Ano: ", self.__ano)

    @abstractmethod
    def imprimirEspecifico(self):
        super().imprimir()
        print
