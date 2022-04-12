from Aluno import Aluno
from AlunoEnsinoMedio import AlunoEnsinoMedio
from AlunoGraduacao import AlunoGraduacao

a1 = Aluno("Andre", "022133", 133)
print(a1)
print("\n")

a2 = AlunoEnsinoMedio("Matheus", "025485", 322, 2)
print(a2)
print("\n")

a3 = AlunoGraduacao("Bruno", "05587714", 155, 3)
print(a3)
print("\n")

# Imprmindo cada um usando os métodos construidos nas classes
print(a1.getNomeAluno())
print(a1.getCodNumber())
print(a1.getMatriculaAluno())
print("\n")
print(a2.getNomeAluno())
print(a2.getCodNumber())
print(a2.getMatriculaAluno())
print(a2.getAnoAluno())
print("\n")
print(a3.getNomeAluno())
print(a3.getCodNumber())
print(a3.getMatriculaAluno())
print(a3.getSemestreAluno())