class Categoria:

    def __init__(self, cod = 0, nomeC = None):
        self.nomeC = nomeC
        self.cod = cod


    def cadastrar(self):
        print("Categoria ", self.nomeC)
        print("Codigo ", self.cod)
        print("Cadastrado com sucesso")

    def __str__(self):
        return str(self.cod)+ "-" +self.nomeC