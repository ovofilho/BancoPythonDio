

saldo = 0
limite = 500
extrato = ""
numero_saques = 0

LIMITE_SAQUES = 3

menu = """

Menu:
[d] Depositar
[s] Sacar
[e] Extrato
[x] Sair
=> """

while True:
    opcao = input(f"O Saldo atual é {saldo}, O limite é {limite} {menu}\n")
    
    if opcao == 'd':
        x = float(input("Qua valor deseja depositar?"))
        if x>0:
            
            diferenca = 500 - limite
            if x<=diferenca:
                limite += x
                
                
            else:
                x -= diferenca
                limite = 500
                saldo += x
                
            print("Valor depositado com sucesso.")
            extrato += f"\n{x} depositado com sucesso \nSaldo = {saldo} \nLimite = {limite}\n"
                
            
        else:
            print("Valor inválido para depósito.")
    elif opcao == 'e':
        print("====================Extrato====================")
        print(extrato)
        print("Fim do extrato")
        
    elif opcao=='s':
        
        x = float(input("Informe o valor que quer sacar: "))
        if x>0:
            if x > saldo + limite:
                print("Saldo insuficiente:")
            elif x> saldo:
                x-= saldo
                saldo = 0
                limite -= x
                extrato += f"\n{x} depositado com sucesso \nSaldo = {saldo} \nLimite = {limite}\n"
                
            else:
                saldo -= x
                extrato += f"\n{x} depositado com sucesso \nSaldo = {saldo} \nLimite = {limite}\n"
                print("Valor sacado com sucesso.")
            
        else:
            print("Valor inválido.")
    elif opcao=='x':
        print("Escolheu sair:")
        break
        
    else:
        print("opção inválida:")