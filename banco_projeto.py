"""
deposito, saque e extrato
"""
import os

SAQUE_DIARIO = 3

extrato = ''
saldo = 0
numeros_saque = 0
limite_saque = 500

while(True):

    menu = """
    MENU 
    [1] Deposito
    [2] Saque
    [3] Extrato
    [4] Sair
    """
    opcao = input(f"{menu}\nEscolha: ")

    if opcao == '1':
        valor_deposito = float(input("\nEntre com o valor do depósito: "))

        if valor_deposito < 0:
            os.system('cls')
            print("\nO valor não pode ser negativo.")
        else:
            os.system('cls')
            saldo += valor_deposito
            extrato += f"\nDeposito: R$ {valor_deposito:.2f}."
            print(f"O valor de R$ {valor_deposito:.2f} foi depositado com sucesso.")
    
    if opcao == '2':
        valor_saque = float(input("\nEntre com o valor a ser sacado: "))
        
        if(valor_saque <= saldo):
            os.system('cls')
            numeros_saque += 1
            if numeros_saque >= SAQUE_DIARIO:
                os.system('cls')
                print("Não foi possivel realizar o saque pois excedeu o limite diario de saques.")
            else:
                print(f"\nO saque de R$ {valor_saque} foi realizado com sucesso.")
                extrato += f"\nSaque: R$ {valor_saque:.2f}."
                saldo -= valor_saque

        elif valor_saque > saldo:
            os.system('cls')
            print("Não foi possivel realizar o saque por falta de saldo.")

        elif valor_saque > limite_saque:
            os.system('cls')
            print("Não foi possivel realizar o saque por falta de limite de saque.")

    if opcao == '3':
        os.system('cls')
        print("\n")
        print("#" * 10, "Extrato", "#" * 10)
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")



            




