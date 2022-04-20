from Veiculo import Veiculo
from Bicicleta import Bicicleta
from Automovel import Automovel
from Moto import Moto
from Carro import Carro

#TESTE 1 VEICULO
v1 = Veiculo("Volkswagen", 4, "gol", 40)
v1.imprimirInformacoes()
v1.acelerar(40)
v1.imprimirInformacoes()

#TESTE 2 BICICLETA (HERDA DE VEICULO)
v2 = Bicicleta("Monark",2 , "rx180", 10, 16, False)
v2.imprimirInformacoes()
v2.frear(10)
v2.imprimirInformacoes()

# TESTE 3 AUTOMOVEL (HERDA DE VEICULO)
v3 = Automovel("Fiat", 4, "Uno", 60, "72cv")
v3.imprimirInformacoes()
v3.acelerar(30)
v3.imprimirInformacoes()
v3.frear(10)
v3.imprimirInformacoes()

#TESTE 4 MOTO (HERDA DE AUTOMOVEL)
v4 = Moto("Honda", 2, "Titan", 50, "15cv", False)
v4.imprimirInformacoes()
v4.acelerar(50)
v4.imprimirInformacoes()
v4.frear(30)

#TESTE 5 CARRO (HERDA DE AUTOMOVEL)
v5 = Carro("Chevrolet", 4, "Onix", 60, "78cv", 4)
v5.acelerar(20)
v5.imprimirInformacoes()
v5.frear(50)