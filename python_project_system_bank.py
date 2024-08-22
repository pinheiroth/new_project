print("====================================================================")
print("   Bem vindo(a) ao python bank insira a opção desejada por favor    ")
menu = """

[d] - Depositar
[s] - Sacar
[e] - Extrato
[q] - Sair 

"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITES_SAQUES = 3

while True:

 
    opcao =input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("O valor informado é invalido")
            print("Favor informar  penas valores positivos !!")

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = numero_saques >= LIMITES_SAQUES

        if excedeu_saldo:
            print("Você não possui saldo suficiente para esta transação.")
            print("Tente outro valor.")
        elif excedeu_limite:
            print("O valor do saque excede o limite.")    
        elif excedeu_saque:
            print("Número limite de saques diarios excedido")
            print("Tente novamente mais tarde !")
        elif valor > 0:
            saldo-= valor
            extrato+= f"Saque: R$ {valor:.2f}\n" 
            numero_saques += 1 
        print("O valor informado é invalido")      

    elif opcao == "e":
        print("\n******************************")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo/: R${saldo:2f}")
        print("******************************")

    elif opcao == "q":
        print("Operação finalizada.")
        print("Volte sempre !!") 
        break
                  

    else:
        print("Operação inválida, selecione novamente a operação desejada.")        
print("====================================================================")