from Pessoa import Pessoa

class Fisica(Pessoa):

    def __init__(self,codigo, nome, endereco, telefone, cpf, idadeF, pesoF, alturaF):
        super().__init__(codigo, nome, endereco, telefone)
        self.__cpf = cpf
        self.idadeF = idadeF
        self.pesoF = pesoF
        self.alturaF = alturaF

    
    def getCpf(self):
        return self.__cpf
    
    def setCpf(self, cpf):
        self.__cpf = cpf
    

    def calculaIMC(self):
        imc = self.pesoF / self.alturaF ** 2
        return f"O IMC de {self.nome} é {imc}"


    def __str__(self):
        return super().__str__()+ f"\nIdade {str(self.idadeF)}\nPeso: {str(self.pesoF)}\nAltura: {str(self.alturaF)}"