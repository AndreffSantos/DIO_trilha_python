"""
    O que é emcapsulamento: Em termos mais simples, o encapsulamento é como uma cápsula que
    protege os dados internos de um objeto, permitindo que eles sejam acessados e modificados
    apenas por meio de métodos específicos.
"""
# Recursos publicos e privadas.
class Conta:
    def __init__(self, agencia, saldo=0):
        self._saldo = saldo
        self.agencia = agencia

    def depositar(self, valor):
        # ...
        self._saldo += valor

    def sacar(self, valor):
        # ...
        self._saldo -= valor

    def mostrar_saldo(self):
        # ...
        return self._saldo

conta = Conta(1)
conta.depositar(100)
print(conta._saldo)

# Qual a diferença entre _saldo e __saldo