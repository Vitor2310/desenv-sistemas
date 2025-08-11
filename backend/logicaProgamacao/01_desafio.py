#criar menu de opçoes e pedir a opção desejada
#criar uma função de deposito
#criar uma opção de saque
#criar funçao de ver saldo
#ao digitar "sair" encerrar o programa


saldo = 0  # saldo inicial

def deposito():
    global saldo
    valor = float(input("Digite o valor para depósito: R$"))
    if valor > 0:
        saldo += valor
        print("Depósito realizado com sucesso.")
    else:
        print("Valor inválido.")

def saque():
    valor = float(input("Digite o valor para saque: R$"))
    if valor > 0 and valor <= saldo:
        saldo -= valor
        print("Saque realizado com sucesso.")
    elif valor > saldo:
        print("Saldo insuficiente.")
    else:
        print("Valor inválido.")

while True:
    print("Menu:")
    print("1 - Depósito")
    print("2 - Saque")
    print("3 - Ver Saldo")
    print("Digite 'sair' para encerrar.")

    opcao = input("Escolha uma opção: ")