menu = """

[c ] Cadastrar Cliente
[cc] Cadastrar Conta Corrente
[d ] Deposito
[s ] Sacar
[e ] Extrato
[q ] Sair

=> """

def depositar(saldo, valor, extrato, /):
    if valor < 0:
        print("Operação não realizada!, Não é possível depositar valores negativos.")
    else:
        saldo += valor
        extrato += f"Depósito de: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques > limite_saques:
        print("Operação não realizada! Você excedeu o número de saques permitidos.")
    elif valor > saldo:
        print("Operação não permitida, saldo insuficiente.")
    elif valor > limite:
        print("Operação não permitida! Valor do saque não pode ser maio que 500.00")
    else:
        saldo -= valor
        extrato += f"Saque de: R$ {valor:.2f}\n"
        numero_saques += 1
    return saldo, extrato, numero_saques

def get_extrato(saldo,/,*,extrato):
    print("\n===================== EXTRATO ======================")
    print("\n------------------ MOVIMENTAÇÔES --------------------")
    print(extrato)
    print("----------------------- SALDO -----------------------\n")
    print(f"Saldo em conta: R$ {saldo:.2f}\n")
    # extrato += f"Saldo em conta: R$ {saldo:.2f}\n"
    # print(extrato)

def cadastrar_cliente(clientes, cpf, nome, dt_nascimento, rua, bairro, cidade, uf):
    clientes[cpf] = {'nome': nome, 'dt_nascimento': dt_nascimento, 'enderco':{'rua':rua, 'bairro': bairro, 'cidade': cidade, 'uf': uf}}
    print('Cliente dadastrado com sucesso!')
    return clientes

def cadastrar_conta_corrente(contas, contador_numero_conta , agencia, cpf):
    contador_numero_conta += 1
    contas[contador_numero_conta] = {'cpf': cpf,'agencia': agencia}
    return contas

saldo = 0
limite = 500
extrato = """
"""
numero_saques = 1
LIMITE_SAQUE = 3
AGENCIA = '0001'
contador_numero_conta = 0

clientes = {}
contas = {}

while True:

    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("Digite o valor a do depósito.\n"))

        saldo, extrato = depositar(saldo, valor, extrato)

    elif opcao == "s":

        valor = float(input("Digite o valor do saque.\n"))

        saldo, extrato, numero_saques = sacar(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUE)

    elif opcao == "e":

        get_extrato(saldo, extrato=extrato)

    elif opcao == "c":

        print("Digite os dados do cliente!\n")
        cpf = int(input("Digite o CPF no formato - 111111\n"))
        if cpf in clientes:
            print("Já existe um cliente cadastrado com este CPF!")
        else:
            nome = str(input("Digite o nome do cliente\n"))
            dt_nascimento = str(input("Digite a data de nascimento no formato - 05/05/1955\n"))
            rua = str(input("Digite o nome da rua\n"))
            bairro = str(input("Digite o nome do bairro\n"))
            cidade = str(input("Digite o nome da cidade\n"))
            uf = str(input("Digite o Estado UF\n"))

            clientes = cadastrar_cliente(clientes, cpf, nome, dt_nascimento, rua, bairro, cidade, uf)

    elif opcao == "cc":

        print("Para cadastrar uma conta corrente digite os dados abaixo\n")
        cpf = int(input("Digite o CPF do cliente no formato - 111111\n"))
        if cpf not in clientes:
            print("Não existe cliente cadastrado com esse CPF\n")
            print("PRIMEIRO EFETUE O CADASTRO DO CLIENTE!")
        else:
            agencia = AGENCIA
            cadastrar_conta_corrente(contas, contador_numero_conta , agencia, cpf)

    elif opcao == "q":

        break
    
    else:
        print("Operação inválida, por favor seleciona novamente  a opção desejada.")