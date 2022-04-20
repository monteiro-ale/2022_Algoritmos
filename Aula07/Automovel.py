from Veiculo import Veiculo

class Automovel(Veiculo):

    def __init__(self, marca, qtdRodas, modelo, velocidade, potenciaDoMotor):
        super().__init__(marca, qtdRodas, modelo, velocidade)
        self.potenciaDoMotor = potenciaDoMotor

    def imprimirInformacoes(self):
        Veiculo.imprimirInformacoes(self)
        print(f"Potência do Motor: {self.potenciaDoMotor}")