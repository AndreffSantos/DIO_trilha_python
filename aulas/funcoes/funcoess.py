def exebir_mensagem():
    print("Olá, mundo")

def exebir_mensagem_2(nome):
    print(f"Ola, {nome}")

def exebir_mensagem_3(nome="Anônimo"):
    print(f"Ola, {nome}")

exebir_mensagem()
exebir_mensagem_2("André")
exebir_mensagem_2(nome="André")
exebir_mensagem_3()
exebir_mensagem_3("Astolfo")

# Argumentos nomeados
def salvar_carros(marca, modelo, ano, placa):
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")

salvar_carros("FIAT", "palio", 1999, "ABC-1234")
salvar_carros(marca="FIAT", ano=1999, placa="ABC-1234", modelo="palio")