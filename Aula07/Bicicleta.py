from Veiculo import Veiculo

class Bicicleta(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, velocidade, numMarchas, bagageiro = True):
        Veiculo.__init__(self, marca, qtdRodas, modelo, velocidade)
        self.numMarchas = numMarchas
        self.bagageiro = bagageiro

    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f"Número de marchas: {self.numMarchas}\nBagageiro: {self.bagageiro}")
