from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

p1 = Pessoa("João", "(51)1122334")
#print(p1)

# f1 = Fisica(20)
# print(f1)

pj = Juridica("João da Silva ME.", "00.111.222/000013", "3322-1144", 3)
print(pj.nome)