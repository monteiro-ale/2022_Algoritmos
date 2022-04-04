from Categoria import Categoria

class Produto:

    def __init__(self, cod = None, nomeP = None, precoP = 0.0, qtd = 0, catP = None):
        self.cod = cod
        self.nomeP = nomeP
        self.precoP = precoP
        self.qtd = qtd
        self.catP = catP

    def cadastrar(self):
        print("Codigo ", self.cod)
        print("Nome ", self.nomeP)
        print("Preco ", self.precoP)
        print("Qtd ", self.qtd)
        print("Caregoria ", self.catP)
        print("Cadastrado com sucesso")

    def setCategoria(self, categoria = Categoria()):
        self.catP = categoria
