class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self.nome = nome
        self.__ano_nascimento = ano_nascimento

    @property
    def idade(self):
        ano_atual = 2025
        return ano_atual - self.__ano_nascimento

p = Pessoa("André", 1995)
print(f"Nome: {p.nome} \tIdade: {p.idade}")