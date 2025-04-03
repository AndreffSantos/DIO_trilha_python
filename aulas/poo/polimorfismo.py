class Pai:
    def andar(self):
        print("Andando")

class Filho(Pai):
    def andar(self):
        print("Filho andando!")

class Filha(Pai):
    def andar(self):
        print("Filha andando!")

def caminhada(obj):
    obj.andar()

caminhada(Filho())
caminhada(Filha())
caminhada(Pai())