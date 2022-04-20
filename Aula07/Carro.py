from Veiculo import Veiculo
from Automovel import Automovel

class Carro(Automovel):

    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, qtdPortas):
        super().__init__(marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.qtdPortas = qtdPortas
    
    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        print(f"Quantidade de Portas: {self.qtdPortas}")