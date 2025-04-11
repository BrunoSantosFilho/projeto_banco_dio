
print( "Seja bem-vindo ao Black Bank!")
      
      
import os


operação = {

    "1": "Depositar",           
    "2": "Sacar",
    "3": "Extrato",
    "4": "Sair"
}            
 

saldo = 0
extrato = ""
limite_por_saque = 500
limite_saques = 3 
numero_de_saques = 0
iniciacao_do_sistema = True


while True:

    
    if not iniciacao_do_sistema:
        os.system('cls')


    print("\nPor favor, selecione a opção desejada: \n")


    for chave, valor in operação.items():
        print(f"[{chave}] {valor}")


    opção = input("\n => ")


    if opção == "1":
        valor = float(input("\nInforme o valor do depósito: "))
        if valor <= 0:
            print("Valor informado inválido! ")
        elif valor > 0: 
            saldo += valor
            extrato += f"+ R${valor:.2f}\n"
            print("\n\n=============================================")
            print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!\n")
            print("=============================================\n\n")


    elif opção == "2":
        valor = float(input("\nInforme o valor do saque: "))

        if saldo <= 0:
            print("\nSaldo insufuciente para a realização da operação")

        elif valor <= 0:
            print("\nValor informado inválido")

        elif valor > limite_por_saque:
            print("Operação não realizada. O limite de R$500 por saque foi ultrapassado.")

        elif numero_de_saques >= limite_saques:
            print("\nOperação não realizada. O limite de 3 saques foi atingido. ")

        else:
             print("\n\n=============================================")
             print(f"\nSaque de R$ {valor:.2f} realizado com sucesso\n")
             print("=============================================\n\n")
             saldo -= valor
             extrato += f"- R${valor:.2f}\n"
             numero_de_saques += 1


    elif opção == "3":
        print("\n================EXTRATO================\n")

        if not extrato:
            print("Não foram realizadas movimentações. ")

        else:
            print(extrato)

        print(f"\nSaldo atualizado: R$ {saldo:.2f}\n")

        print("=======================================")


    elif opção == "4":
        print("\nObrigado e até logo!\n")
        break
       
       
    else:
        print("\nOpção inválida. ")




      
                   
                   

        
    






