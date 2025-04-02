def listar_args(texto, *args):
    message = texto + "\n"
    for arg in args:
        message += arg + "\n"
    print(message)

listar_args("arg", "arg")
def teste(**kwargs):
    message = "\n".join(f"{chave.title()}: {valor}" for chave, valor in kwargs.items())
    print(message)

teste(nome="Andre", idade=29, ocupacao="Estudante")