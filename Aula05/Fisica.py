from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self, idade):
        super().__init__()
        self.idade = idade
        print("Pessoa Fisica construida")
    
    def __str__(self):
        return super().__str__()+ f"\nIdade {str(self.idade)}"