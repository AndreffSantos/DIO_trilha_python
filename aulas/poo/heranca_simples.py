class Veiculo:
    def __init__(self, cor, placa, numero_rodas):
        self.cor = cor
        self.placa = placa
        self.numero_rodas = numero_rodas

    def ligar_motor(self):
        print("Ligando motor")

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

class Motocicleta(Veiculo):
    pass

class Carro(Veiculo):
    pass

class Caminhao(Veiculo):
    def __init__(self, cor, placa, numero_rodas, carregado=False):
        self.carregado = carregado
        super().__init__(cor, placa, numero_rodas)

    def esta_carregado(self):
        print(f"{'Sim,' if self.carregado else 'Não'} esta carregado")

moto = Motocicleta("preta", "1234", 2)
moto.ligar_motor()

carro = Carro("branco", "ABC-1234", 4)
carro.ligar_motor()
caminhao = Caminhao("branco", "ABC-1234", 8)

print(moto)
print(carro)
print(caminhao)

