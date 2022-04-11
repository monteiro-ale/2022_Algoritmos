from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self, nome, cnpj,  telefone="Sem fone", nFuncionarios = 0):
        super().__init__(nome, telefone)
        self.cnpj = cnpj
        self.nFuncionarios = nFuncionarios
    
    def __str__(self):
        return super().__str__()+ "\nCNPJ: "+ self.cnpj+"\nFuncionarios:"+ str(self.nFuncionarios)
