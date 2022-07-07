# Construa um software em Python que implemente uma Pilha de livros e uma Pilha de Revistas.
# As classes Livro e Revista herdam da classe Publicação, os atributos e métodos comuns às duas classes.
# A classe Livro é composta dos atributos id, data de publicação, título e autor. O atributo autor é fracamente privado.
# A classe Revista é composta dos atributos id, data de publicação, preço. O atributo preço é fortemente privado.
# Todas classes devem ter um método para imprimir as informações dos seus respectivos atributos.
# Implemente uma tela com um menu (funcionando) que permita ao usuário:
# -> Adicionar e remover livros da Pilha.
# -> Adicionar e remover revistas da Pilha.
# -> Imprimir a Pilha de livros e a Pilha de revistas.
# Pode ser entregue um zip com os arquivos ou o link do repositório no GitHub contendo o código desenvolvido

#imports 
import time
from abc import ABC, abstractmethod
from Publicacao import Publicacao
from Livros import *
from Node import Node
from Revista import *

#instanciando pilhas
pilha_de_livros = PilhaLivros()
pilha_de_revistas = PilhaRevista()

#função para adicionar livros
def adc_livro():
    id = input('Digite o ID do livro:\n')
    if pilha_de_livros.deduplicaId(id):
        while pilha_de_livros.deduplicaId(id):
            print("\n=========================================\n")
            print("Atenção: O ID informado já foi cadastrado!")
            print("\n=========================================\n")
            time.sleep(0.4)
            id = input("Digite um ID diferente: ")
    dt_pub = input('Digite a data de publicação\n')
    titulo = input('Digite o titulo do livro\n')
    autor = input('Digite o nome do Autor\n').capitalize()
    livro = Livros(titulo, autor)
    livro.cadastrar(id, dt_pub)
    livro.setAutor(autor)
    pilha_de_livros.empilhar(livro)
    print('\n **** Livro cadastrado! ****\n')
    time.sleep(0.5)
    

#função para adicionar revistas
def adc_revista():
    id = input('Digite o ID da revista:\n')
    if pilha_de_revistas.deduplicaId(id):
        while pilha_de_revistas.deduplicaId(id):
            print("\n=========================================\n")
            print("Atenção: O ID informado já foi cadastrado!")
            print("\n=========================================\n")
            time.sleep(0.4)
            id = input("Digite um ID diferente: ")
    dt_pub = input('Digite a data de publicação\n')
    preco = input('Digite o preço da revista\n')
    revista = Revista(preco)
    revista.cadastrar(id, dt_pub)
    revista.setPreco(preco)
    pilha_de_revistas.empilhar(revista)
    print('\n **** Revista cadastrada! ****\n')
    time.sleep(0.5)

#função para remover livros da pilha
def removelivro():
    if pilha_de_livros.__len__() == 0:
        print("\nA pilha de Livros está vazia!\n")
        time.sleep(0.5)
        return main()
    print("========================================================")
    option = input(f"Tem certeza que deseja remover o último livro cadastrado?\n {pilha_de_livros.retornaTopo()}\n========================================================\nDigite S para Sim\nDigite N para Não\n").upper()
    if option == "S":
        pilha_de_livros.desempilhar()
        print("========================================================")
        print("****Livro removido com sucesso, voltando ao menu****\n========================================================")
        time.sleep(1)
    elif option == "N":
        print("========================================================")
        print("****Livro não removido, voltando ao menu****\n========================================================")
        time.sleep(1)
        return main()
    else: print("Opção não é válida")

#função para remover revistas da pilha
def removerevista():
    if pilha_de_revistas.__len__() == 0:
        print("A pilha de Revistas está vazia!")
        time.sleep(0.5)
        return main()
    option = input(f"Tem certeza que deseja remover a última Revista cadastrada?\n{pilha_de_revistas.retornaTopo()}\nDigite S para Sim\nDigite N para Não\n").upper()
    if option == "S":
        pilha_de_revistas.desempilhar()
        print("========================================================")
        print("****Revista removida com sucesso, voltando ao menu****\n========================================================")
        time.sleep(1)
    elif option == "N":
        print("========================================================")
        print("****Revista não removida, voltando ao menu****\n========================================================")
        time.sleep(1)
        return main()
    else: print("Opção não é válida")

#função para imprimir livros
def imprimelivros():
    print(pilha_de_livros.imprimir())
    time.sleep(1)

#função para imprimir revistas
def imprimerevistas():
    print(pilha_de_revistas.imprimir())
    time.sleep(1)




menu_principal =  """
  ================================
  --------------MENU--------------
  ================================
  0- Finalizar o Programa
  1- Adicionar Livros
  2- Remover Livros
  3- Adicionar Revista
  4- Remover Revista
  5- Imprimir a Pilha de livros
  6- Imprimir a Pilha de revistas
  ================================
  Escolha: """

def main():
    teclado = input(menu_principal)
    if teclado == "0":
        print("Programa encerrado")
        quit()
    elif teclado == "1": adc_livro()
    elif teclado == "2": removelivro()
    elif teclado == "3": adc_revista()
    elif teclado == "4": removerevista()
    elif teclado == "5": imprimelivros()
    elif teclado == "6": imprimerevistas()
    main()

main()

