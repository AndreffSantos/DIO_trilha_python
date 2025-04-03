class Cachorro:
    """
        Metodo construtor
    """
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    """
       Metodo destrutor é o __del__ mas não é tão necessario em python
       pois ele tem um gabage collector que lida com isso.
    """
    def __del__(self):
        print(f"Removendo instancia de classe. {self.nome}")

    def falar(self):
        print("Auau.")

def criar_cachorro():
    c = Cachorro("Chappie", "branco e preto")
    print(c.nome)

criar_cachorro()
cao = Cachorro("Duke", "preto")

print("Olá mundo")
# Para forçar a romeção de um instâcia usa-se a palavra reservada del e o nome da instância.
del cao
print("Olá mundo")
print("Olá mundo")

