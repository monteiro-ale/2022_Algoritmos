from Aluno import Aluno

class AlunoEnsinoMedio(Aluno):

    def __init__(self, nome, matricula, codigo = 0, ano = 0):
        super().__init__(nome, matricula, codigo)
        self.ano = ano
    
    def __str__(self):
        return super().__str__()+ "\nAno:"+ str(self.ano)
    
    def getAnoAluno(self):
        return self.ano