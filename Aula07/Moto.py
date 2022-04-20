from Veiculo import Veiculo
from Automovel import Automovel

class Moto(Automovel):

    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor, partidaEletrica = True):
        super().__init__(marca, qtdRodas, modelo, velocidade, potenciaDoMotor)
        self.partidaEletrica = partidaEletrica

    def imprimirInformacoes(self):
        Automovel.imprimirInformacoes(self)
        print(f"Partida Elétrica: {self.partidaEletrica}")