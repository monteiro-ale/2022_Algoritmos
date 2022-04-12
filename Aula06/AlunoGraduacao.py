from Aluno import Aluno

class AlunoGraduacao(Aluno):

    def __init__(self, nome, matricula, codigo=0, semestre = 0):
        super().__init__(nome, matricula, codigo)
        self.semestre = semestre

    def __str__(self):
        return super().__str__()+ f"\nSemestre: {str(self.semestre)}"
    
    def getSemestreAluno(self):
        return self.semestre