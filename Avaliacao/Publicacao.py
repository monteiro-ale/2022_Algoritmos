from abc import ABC, abstractmethod


###################################################################################################
#                                  C L A S S E  P U B L I C A C A O                               #
###################################################################################################
class Publicacao(ABC):

    def __init__(self):
        self.id = None
        self.dt_pub
    
    @abstractmethod
    def cadastrar(self, id, dt_pub):
        pass

    def getInformacoes(self):
        return f"ID: {self.id}\nData de Publicação: {self.dt_pub}"