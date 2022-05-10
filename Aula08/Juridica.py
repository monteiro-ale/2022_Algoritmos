from Pessoa import Pessoa

class Juridica(Pessoa):

    def __init__(self,codigo, nome, endereco, telefone, cnpj, nFuncionarios = 0):
        Pessoa.__init__(self, codigo, nome, endereco, telefone)
        self.__cnpj = cnpj
        self.__nFuncionarios = nFuncionarios
    

    def getCnpj(self):
        return self.__cnpj
    

    def getNFuncionarios(self):
        return self.__nFuncionarios

    def setCnpj(self, cnpj):
        self.__cnpj = cnpj
    
    def setNFuncionarios(self, num):
        self.__nFuncionarios = num

    def __str__(self):
        return super().__str__()+ f"\nCNPJ: {self.__cnpj}\nFuncionarios :{str(self.__nFuncionarios)}"