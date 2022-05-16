# O sistema possuirá uma classe abstrata chamada de Ferramenta que deve conter os atributos/propriedades
#  nome, tensão e preço. Esta classe também deve possuir um método getInformacoes()
#  que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

from abc import ABC, abstractmethod

class Ferramenta(ABC):

    def __init__(self):
        self.nome = None
        self.tensao
        self.preco
    
    @abstractmethod
    def cadastrar(self, nome, tensao, preco):
        pass

    def getInformacoes(self):
        return f"Nome da Ferramenta: {self.nome}\nTensão: {self.tensao}\nPreco: {self.preco}\n"
    
