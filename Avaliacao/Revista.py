# A classe Revista é composta dos atributos id, data de publicação, preço. O atributo preço é fortemente privado.

from Publicacao import Publicacao
from Node import Node
import time

###################################################################################################
#                                   C L A S S E  R E V I S T A                                    #
###################################################################################################

#criacao da classe revista
class Revista(Publicacao):
    def __init__(self, preco):
        # super().__init__()
        self.__preco = preco

#reimplementação do método cadastrar da classe abstrata
    def cadastrar(self, id, dt_pub):
        self.id = id
        self.dt_pub = dt_pub

#metodo pra pegar atributo privado    
    def getPreco(self):
        return self.__preco

#método que reotorna o id
    def getId(self):
        return self.id

#metodo para setar atributo privado
    def setPreco(self, preco):
        self.__preco = preco

#implementaçao do método de getinfo  
    def getInformacoes(self):
        return super().getInformacoes()+ f"\nPreço: {self.__preco}\n"

###################################################################################################
#                                   C L A S S E  P I L H A                                        #
###################################################################################################
#classe pilha
class PilhaRevista:
    def __init__(self):
        self.top = None
        self.size = 0

#adiciona itens na pilha
    def empilhar(self, elem):
        node = Node(elem)
        node.prox = self.top
        self.top = node
        self.size +=1

#remove o item que está no topo
    def desempilhar(self):
        if self.size > 0:
            node = self.top
            self.top = self.top.prox
            self.size -= 1
            return node.dado
        else:
            print("A pilha está vazia.")

#mostra ultimo item inserido
    def retornaTopo(self):
        if self.size > 0:
            return self.top.dado.getInformacoes()
        else:
            print("A pilha está vazia.")

#retorna o tamanho da pilha
    def __len__(self):
        return self.size

#método que verifica se o id já foi cadastrado
    def deduplicaId(self, id):
        i = self.top
        while(i):
            if i.dado.getId() == id:
                return True
            else: i = i.prox
        return False

#imprime os dados da pilha
    def imprimir(self):
        if self.top == None:
            print("A Pilha está vazia!")
        else:
            print("""================================
--------------PILHA--------------
================================""")
            time.sleep(0.4)
            i = self.top
            while(i):
                print(i.dado.getInformacoes())
                time.sleep(0.3)
                i = i.prox
            print(f"\n****Tamanho da pilha: {self.size}****\n")
    