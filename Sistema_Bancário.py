



menu =  """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> 

"""

saldo = 0 
limite = 500
extrato =" "
numero_saque = 0
LIMITE_SAQUE = 3 

#Laçco de repetição

while True:

    opcao = input(menu)

    if opcao == "d":
        print("Deposito:")
        valor = float(input("Digite o valor que deseja depositar: "))
        
        #Aqui estou armazenando o valor depositado , para assim poder mostra no Extrato.
        if valor > 0:
            saldo += valor 
            extrato += f"Depósito: R${valor:.2f}\n"  
   
        else :
            print("erro , valor informado invalido.!")
    
    elif opcao == "s":
        print("Sacar")

        valor = float(input("Qual o valor que deseja sacar: "))

        excedeu_saldo = valor > saldo 

        excedeu_limite = valor > limite

        excedeu_saques = numero_saque >= LIMITE_SAQUE

        if excedeu_saldo :
            print(f"Erro , saldo insuficiente!\n")

        elif excedeu_limite :
            print("Erro , limite de saque excedido!")

        elif excedeu_saques:
            print("Erro , Limite de saques diario excedido!")

        elif valor > 0:
            saldo -= valor 
            extrato += f"Saque: R${valor:.2f}\n"
            numero_saque += 1
        
        else :
            print("Erro , valor inválido!")
            

    elif opcao == "e":
        print("**********Extrato*************")
        print("Não houve movimentações."if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("********************************")

    elif opcao == "q":
        break

    else :
        print("Operação invalidada , selecione outra opção!")

        







        

        










































