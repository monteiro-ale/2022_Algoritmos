# Método que recebe parâmetro e tem retorno
def getPi():
    return 3.14

# Método que não recebe nenhum parâmtro e não retorna nada
def imprimePi():
    print("O valor de PI é:" ,getPi() )

# Método que recebe um parâmetro e tem  retorno
def calculaAreaCirculo(raio):
    area = getPi() * (raio * raio)
    return area

# Método que recebe um parâmetro e não retorna nada

def imprimirAreaCirculo(r):
    print( "A área do círculo com raio ", r , "é" ,calculaAreaCirculo(raio = r) )

def calcularAreaPlana ( largura, comprimento ):
    area = float (largura) * float (comprimento)
    return area


# Bloco de execução

#print( "O valor de Pi é:" ,getPi() )
#imprimePi()
imprimirAreaCirculo(4)
print ( "A área plana é de:" , calcularAreaPlana("2" , 3.5) )