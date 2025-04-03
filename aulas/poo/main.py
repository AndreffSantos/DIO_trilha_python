# Alguns paradigmas
# Imperativo ou procedural.
# Funcional.
# Orientado a enventos.
# Orientado a objetos.
class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("ZZZZzzz...")

cao_1 = Cachorro("Chappie", "Caramelo", False)
cao_2 = Cachorro("Duke", "Preto")

cao_2.latir()
print(cao_2.nome)