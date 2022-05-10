class Pessoa:

    def __init__(self,codigo, nome, endereco, telefone):
        
        self.__codigo = codigo
        self.nome = nome
        self._endereco = endereco
        self.__telefone = telefone


    def getCodigo(self):
        return self.__codigo


    def setCodigo(self, valor):
        self.__codigo = valor


    def getNome(self):
        return self.nome
    

    def setNome(self, nome):
        self.nome = nome


    def getEndereco(self):
        return self._endereco
    

    def setEndereco(self, address):
        self._endereco = address


    def getTelefone(self):
        return self.__telefone
    
    def setTelefone(self, fone):
        self.__telefone = fone

    def __str__(self):
        return f"Código: {self.__codigo}\nNome: {self.nome}\nEndereço:{self._endereco}\nTelefone: {self.__telefone}"
