# O sistema possuirá uma classe abstrata chamada de Ferramenta que deve conter os atributos/propriedades
#  nome, tensão e preço. Esta classe também deve possuir um método getInformacoes()
#  que retorna todos os valores dos atributos. Esta classe também possui um método abstrato cadastrar().

# O projeto também deve possuir as classes concretas, Furadeira e Lixadeira que herdam da classe 
# Ferramenta.

# A classe Furadeira deve possuir o atributo/propriedade fracamente privado, potência.
#  Esta classe reimplementa o método getInformacoes() herdado de Furadeira.

# A classe Lixadeira possui o atributo/propriedade fortemente privado, rotações. 
# Esta classe reimplementa o método getInformacoes() herdado de Furadeira.

# Construa um menu com as opções para cadastrar as ferramentas suportadas pelo sistema.

# Você pode enviar os arquivos do projeto ou criar um repositório no Github e 
# enviar só o link do repositório.


from abc import ABC, abstractmethod
from Ferramenta import Ferramenta
from Furadeira import Furadeira
from Lixadeira import Lixadeira


def adc_furadeira():
    nome = input('Digite o modelo da Furadeira:\n').upper()
    tensao = input('Digite a tensao\n')
    preco = input('Digite o preço\n')
    potencia = input('Digite a potência\n')

    furadeira = Furadeira(potencia)
    furadeira.cadastrar(nome, tensao, preco)
    furadeira.setPotencia(potencia)
    print('\n **** Furadeira cadastrada! ****\n')
    print(furadeira.getInformacoes())
    print('\n')
    

def adc_lixadeira():
    nome = input('Digite o modelo da Lixadeira:\n').upper()
    tensao = input('Digite a tensao\n')
    preco = input('Digite o preço\n')
    rotacao = input('Digite a rotação\n')

    lixadeira = Lixadeira(rotacao)
    lixadeira.cadastrar(nome, tensao, preco)
    lixadeira.setRotacao(rotacao)
    print('\n **** Lixadeira cadastrada! ****\n')
    print(lixadeira.getInformacoes())
    print('\n')




menu_principal =  """
  ================================
  --------------MENU--------------
  ================================
  0- Finalizar o Programa
  1- Adicionar Furadeira
  2- Adicionar Lixadeira
  ================================
  Escolha: """


def main():
    teclado = input(menu_principal)
    if teclado == "0":
        print('Programa encerrado')
    elif teclado == "1": adc_furadeira()
    elif teclado == "2": adc_lixadeira()
    
    main()
main()


