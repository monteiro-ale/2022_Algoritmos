class Pessoa:

    def __init__(self, nome = "Sem Nome", telefone = "Sem fone"):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}"
