class Bicicleta():
    """
    Self é uma referenca ao proprio obejeto.
    __init__ É o metodo construtor
    """
    def __init__(self, cor, modelo, ano, valor, aro=18):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.aro = aro

    def buzinar(self):
        print("Prim, Prim")

    def parar(self):
        print("Parando bicicleta")

    def correr(self):
        print("Correndo!!!")
# Por padrão o primeiro parametro de um metodo de classe recebe um referencia ao objeto
    def trocar_marcha(num_marcha):
        # dando um print em num_marcha ele imprime a mesma coisa do metodo __str__.
        print("Marcha trocada...", num_marcha)

    def get_cor(self):
        return self.cor

    #def __str__(self):
    #    return f"Bicicleta {self.modelo}, {self.cor}, do ano de {self.ano}"

    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}: {valor}' for chave, valor in self.__dict__.items()])}"

b1 = Bicicleta("vermelha", "caloi", 2022, 9000)
b1.buzinar() # Bicicleta.buzinar(b1)
b1.trocar_marcha()
print(b1.get_cor())
print(b1)