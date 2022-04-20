class Veiculo:

    def __init__(self, marca, qtdRodas, modelo, velocidade):
        self.marca = marca
        self.qtdRodas = qtdRodas
        self.modelo = modelo
        self.velocidade = velocidade

    def imprimirInformacoes(self):
        print(f"Marca: {self.marca}\nQuantidade de Rodas: {self.qtdRodas}\nModelo: {self.modelo}\nVelocidade: {self.velocidade}")

    def acelerar(self, vel):
        setvel = self.velocidade + vel
        self.velocidade = setvel
        print(f"Velocidade setada em {self.velocidade}")

    def frear(self, red):
        setred = self.velocidade - red
        self.velocidade = setred
        print(f"Velocidade reduzida para {self.velocidade}")
