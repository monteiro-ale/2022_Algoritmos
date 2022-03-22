

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def getNomePessoa(self):
        return self.nome
    
    def getIdadePessoa(self):
        return self.idade

p1 = Pessoa("João", 23)
print(p1.getNomePessoa(),p1.getIdadePessoa())