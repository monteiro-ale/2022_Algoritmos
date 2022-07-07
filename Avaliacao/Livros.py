# A classe Livro é composta dos atributos id, data de publicação, título e autor. O atributo autor é fracamente privado.
from abc import ABC, abstractmethod
from Publicacao import *
from Node import Node
import time

###################################################################################################
#                                     C L A S S E  L I V R O S                                    #
###################################################################################################

#criacao da classe livros
class Livros(Publicacao):
    def __init__(self, titulo, autor):
        # super().__init__()
        self.titulo = titulo
        self._autor = autor
    
#reimplementação do método cadastrar da classe abstrata
    def cadastrar(self, id, dt_pub):
        self.id = id
        self.dt_pub = dt_pub
#metodo pra pegar atributo autor fracamente privado    
    def getAutor(self):
        return self._autor

#metodo pra pegar título      
    def getTitulo(self):
        return self.titulo

#método em teste
    def getId(self):
        return self.id

#metodo para setar autor fracamente privado
    def setAutor(self, autor):
        self._autor = autor
   
#implementaçao do método de getinfo  
    def getInformacoes(self):
        return super().getInformacoes()+ f"\nAutor: {self._autor}\nTítulo: {self.titulo}\n"




###################################################################################################
#                                    C L A S S E  P I L H A                                       #
###################################################################################################

#classe pilha
class PilhaLivros:
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
    