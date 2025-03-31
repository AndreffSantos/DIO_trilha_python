menu = '''
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>'''
global saldo
saldo = 0
limite = 500
saques = 0
LIMITE_SAQUES = 3
movimentacoes = []


def deposito(valor):
    global saldo
    if (valor < 0):
        print('Valor invalido para deposito')
    else:
        saldo += valor
        movimentacoes.append(valor)
        print(f'Saldo: {saldo}')


def sacar(valor):
    global saldo, saques
    if (valor > saldo or valor > limite):
        print('Valor indisponivel para saque')
    elif (saques == LIMITE_SAQUES):
        print('Você ja atingiu o limite de saques diarios')
    else:
        saldo -= valor
        saques += 1
        movimentacoes.append(-valor)
        print(f'Saldo: {saldo}')


def extrato():
    for movimentacao in movimentacoes:
        if (movimentacao > 0):
            print(f'Deposito: {movimentacao}')
        else:
            print(f'Saque: {movimentacao}')
    print(f'Saldo atual: {saldo}')


while True:
    operacao = input(menu)

    if (operacao == 'd'):
        deposito(int(input('Insira o valor: ')))

    elif (operacao == 's'):
        sacar(int(input('Insira o valor para ser sacado: ')))

    elif (operacao == 'e'):
        extrato()

    elif (operacao == 'q'):
        print('Encerando')
        break

    else:
        print('Operação invalida')
