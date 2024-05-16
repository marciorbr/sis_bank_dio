menu = """

[d] Deposito
[s] Sacar
[e] Extrato
[s] Sair

=> """

saldo = 0
limite = 500
extrato = """
"""
numero_saques = 1
LIMITE_SAQUE = 3


while True:

    opcao = input(menu)

    if opcao == "d":
        
        valor = float(input("Digite o valor a do depósito."))
        if valor < 0:
            print("Operação não realizada!, Não é possível depositar valores negativos.")
        else:
            saldo += valor
            extrato += f"Depósito de: R$ {valor:.2f}\n"

    elif opcao == "s":

        valor = float(input("Digite o valor do saque."))
        if numero_saques > LIMITE_SAQUE:
            print("Operação não permitida, saldo insuficiente.")
        elif valor > saldo:
            print("Operação não realizada! Você excedeu o número de saques permitidos.")
        elif valor > 500:
            print("Operação não permitida! Valor do saque não pode ser maio que 500.00")
        else:
            saldo -= valor
            extrato += f"Saque de: R$ {valor:.2f}\n"
            numero_saques += 1

    elif opcao == "e":

        extrato += f"Saldo em conta: R$ {saldo:.2f}\n"
        print(extrato)

    elif opcao == "q":

        break
    
    else:
        print("Operação inválida, por favor seleciona novamente  a opção desejada.")
