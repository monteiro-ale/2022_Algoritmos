
class Aluno:
    def __init__(self, nome, matricula, codigo = 12):
        self.codigo = codigo
        self.nome = nome
        self.matricula = matricula

    def __str__(self):
        return "Nome:"+ self.nome+"\nMatricula:"+ self.matricula+ "\nCodigo:"+ str(self.codigo)

    def getNomeAluno(self):
        return self.nome
    
    def getMatriculaAluno(self):
        return self.matricula

    def getCodNumber(self):
        return self.codigo

