from Pessoa import Pessoa
from Fisica import Fisica
from Juridica import Juridica

p1 = Pessoa(125, 'Andre', 'Rua a', 51993045261)

print(p1)

#Testando get e set

# print(p1.getTelefone())
# print(p1.getNome())
# print(p1.getEndereco())
# print(p1.getCodigo())

p1.setCodigo(889)
p1.setEndereco('Rua b')
p1.setNome('Paulo')
p1.setTelefone(51998657741)

print(p1)
print('\n\n')

# print(p1.getTelefone())
# print(p1.getNome())
# print(p1.getEndereco())
# print(p1.getCodigo())


p2 = Fisica(133, 'Roberto', 'rua c', 51993654854, 548996574, 18, 70, 1.71)

print(p2)
print('\n\n')
# Testando get e set

# print(p2.calculaIMC())
# print(p2.getCodigo())
# print(p2.getCpf())
# print(p2.getEndereco())
# print(p2.getNome())
# print(p2.getTelefone())

# p2.setCodigo(125)
# p2.setCpf(5489960221)
# p2.setEndereco('Rua d')
# p2.setTelefone(51987421335)

# print(p2.calculaIMC())
# print(p2.getCodigo())
# print(p2.getCpf())
# print(p2.getEndereco())
# print(p2.getNome())
# print(p2.getTelefone())

p3 = Juridica(489, 'CASA DO CODIGO LTDA', 'Rua E', 5133647858, '458702-0001354', 32)
print(p3)

#teste nos setters do cnpj...

p3.setCnpj('485002-0001358')
p3.setNFuncionarios(45)
print(p3)