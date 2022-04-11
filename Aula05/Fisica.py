from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self, nomeF, idadeF):
        super().__init__(nomeF)
        self.idadeF = idadeF
        print("Pessoa Fisica construida")
    
    def __str__(self):
        return super().__str__()+ f"\nIdade {str(self.idade)}"