menu = """
[1] Depósito
[2] Saque
[3] Ver Extrato
[4] Sair

Escolha uma opção: """

saldo = 0.0
limite_saque = 500.0
historico_extrato = ""
quantidade_saques = 0
SAQUES_PERMITIDOS = 3

while True:
    escolha = input(menu)

    if escolha == "1":
        deposito = float(input("Informe o valor do depósito: "))

        if deposito > 0:
            saldo += deposito
            historico_extrato += f"Depósito: R$ {deposito:.2f}\n"
            print("Depósito realizado com sucesso!")
        else:
            print("Erro: Valor de depósito inválido.")

    elif escolha == "2":
        saque = float(input("Informe o valor do saque: "))

        saldo_insuficiente = saque > saldo
        limite_excedido = saque > limite_saque
        saques_excedidos = quantidade_saques >= SAQUES_PERMITIDOS

        if saldo_insuficiente:
            print("Erro: Saldo insuficiente para realizar o saque.")
        elif limite_excedido:
            print(f"Erro: O valor do saque ultrapassa o limite de R$ {limite_saque:.2f}.")
        elif saques_excedidos:
            print(f"Erro: Você atingiu o limite de {SAQUES_PERMITIDOS} saques diários.")
        elif saque > 0:
            saldo -= saque
            historico_extrato += f"Saque: R$ {saque:.2f}\n"
            quantidade_saques += 1
            print("Saque realizado com sucesso!")
        else:
            print("Erro: Valor de saque inválido.")

    elif escolha == "3":
        print("\n======= EXTRATO =======")
        if not historico_extrato:
            print("Nenhuma movimentação registrada.")
        else:
            print(historico_extrato)
        print(f"Saldo atual: R$ {saldo:.2f}")
        print("========================")

    elif escolha == "4":
        print("Encerrando o sistema...")
        break

    else:
        print("Opção inválida, por favor, tente novamente.")
