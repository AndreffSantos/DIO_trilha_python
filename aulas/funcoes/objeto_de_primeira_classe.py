def somar(a, b):
    return a + b

def exiber_resultado(a, b, func):
    resultado = func(a, b)
    print(f"O resultado de {a} + {b} é = {resultado}")

exiber_resultado(1, 2, somar)