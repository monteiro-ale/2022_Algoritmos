# Construir um algoritmo que contenha 3 listas, cada lista contendo:
# • Nomes de produtos
# • Preços de cada produto
# • Quantidades de cada produto
# • Construir uma função para imprimir um dos produtos da lista e uma
# função para retirar um dos produtos das listas. As funções devem receber
# um parâmetro que será usado para acessar a posição dos itens das listas
# que serão impressos ou retirados.

produtos = ["teclado", "mouse", "headset"]
precos = ["R$150", "R$50", "R$200"]
qtd = [6,10,7]

def imprimeTodosProdutos():
    print(produtos,'\n',precos,'\n',qtd)

def getProdutos(indice):
    return produtos[indice]

def getPreco(indice):
    return precos[indice]

def getQtd(indice):
    return qtd[indice]

def imprimeProdutos(indice):
    print("Os produto selecionado foi: " ,getProdutos(indice))

def imprimePreco(indice):
    print("O preço é: " ,getPreco(indice))

def imprimeQtd(indice):
    print("A quantidade é: " ,getQtd(indice))

def removeProduto(indice):
    produtos.pop(indice)

def removePreco(indice):
    precos.pop(indice)

def removeQtd(indice):
    qtd.pop(indice)



# Bloco de execução

# imprimeTodosProdutos()    

# imprimeProdutos(0)
# imprimeQtd(0)
# imprimePreco(0)

removeProduto(1)
removePreco(1)
removeQtd(1)

imprimeTodosProdutos()
