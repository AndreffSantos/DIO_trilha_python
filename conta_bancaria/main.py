def criar_usuario(usuarios):
    cpf = input("Insira seu cpf:\t")

    if existe_usuario(cpf, usuarios):
        print("cpf já cadastrado.")

    else:
        nome = input("Informe o nome:\t")
        data_nascimento = input("Informe sua data de nascimento:\t")
        endereco = input("Informe seu endereço:\t")

        usuarios.append({
            "cpf": cpf,
            "nome": nome,
            "data_de_nascimento": data_nascimento,
            "endereço": endereco
        })

        print(f"Usuário {nome} criado com sucesso!")

def criar_conta(agencia, numero_conta ,contas, usuarios):
    cpf = input("Insira o cpf do Cliente:\t")
    usuario = existe_usuario(cpf, usuarios)
    if usuario:
        print("Conta criada")
    else:
        print("O CPF informado não é de um Cliente cadastrado!")
        contas.append({
            "cliente": usuario,
            "agencia": agencia,
            "conta": numero_conta,
        })

def existe_usuario(cpf, usuarios):
    usuario_existe = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_existe[0] if usuario_existe else False

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}.\n"
        print("Depósito realizado.")
    else:
        print("Valor invalido para deposito")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo or valor > limite:
        print("Valor indisponivel para saque.")
    elif(numero_saques >= limite_saques):
        print("Numero maximo de saques atingido")
    elif(valor > 0):
        saldo -= valor
        numero_saques += 1
        extrato += f"Saque:\tR$ {valor:.2f}.\n"
        print("Saque realizado.")
    else:
        print("Erro operacional.")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("EXTRATO")
    if extrato:
        print(extrato)
    else:
        print("Sem hostorico de movimentações")
    print(f"Saldo:\tR$ {saldo}")


def main():
    MENU = """
    [nu] Novo cliente
    [nc] Nova conta
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    =>\t"""
    LIMITE_DE_SAQUE = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    while True:
        operacao = input(MENU)

        if (operacao == "d"):
            valor = float(input("Insira o valor a depositar: "))
            print(extrato)
            saldo, extrato = depositar(saldo, valor, extrato)

        elif (operacao == "s"):
            valor = int(input("Insira o valor para ser sacado: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_DE_SAQUE
            )

        elif (operacao == "e"):
            exibir_extrato(saldo, extrato=extrato)

        elif (operacao == "nu"):
            criar_usuario(usuarios)

        elif (operacao == "nc"):
            numero_conta = len(contas) + 1
            criar_conta(AGENCIA, numero_conta, contas, usuarios)

        elif (operacao == "q"):
            print("Encerrando")
            break

        else:
            print("Operação invalida")

main()