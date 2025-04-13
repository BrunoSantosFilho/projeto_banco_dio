

import os


def depositar(valor, saldo, extrato, /):
    if valor <= 0:
        print("Valor informado inválido")
    else:
        saldo += valor
        extrato += f"+ R${valor:.2f}\n"
        print("\n\n=============================================")
        print(f"\nDepósito de R$ {valor:.2f} realizado com sucesso!\n")
        print("=============================================\n\n")
    return saldo, extrato


def sacar(*, valor, saldo, extrato, limite_por_saque, limite_saques, numero_de_saques):
    if valor > saldo:
        print("\nSaldo insuficiente para a realização da operação")
    elif valor <= 0:
        print("\nValor informado inválido")
    elif valor > limite_por_saque:
        print("Operação não realizada. O limite de R$500 por saque foi ultrapassado.")
    elif numero_de_saques >= limite_saques:
        print("\nOperação não realizada. O limite de 3 saques foi atingido.")
    else:
        print("\n\n=============================================")
        print(f"\nSaque de R$ {valor:.2f} realizado com sucesso\n")
        print("=============================================\n\n")
        saldo -= valor
        extrato += f"- R${valor:.2f}\n"
        numero_de_saques += 1
    return saldo, extrato, numero_de_saques


def exibir_extrato(saldo, *, extrato):
    print("\n================EXTRATO================\n")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo atualizado: R${saldo:.2f}\n")
    print("=======================================")


def criar_usuario(usuarios):
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (dd/mm/aaaa): ")
    cpf = input("Informe os dígitos do CPF (apenas números): ")

    print("\nInforme o endereço.\n")
    logradouro = input("Logradouro: ")
    numero = input("Número: ")
    bairro = input("Bairro: ")
    cidade = input("Cidade: ")
    estado = input("Estado: ")

    endereco = f"{logradouro}, {numero} - {bairro} - {cidade}/{estado}"

    usuario_existente = []
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_existente.append(usuario)

    if usuario_existente:
        print("Usuário já cadastrado.")
        return

    novo_usuario = {
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    }

    usuarios.append(novo_usuario)
    print("\nUsuário cadastrado com sucesso!\n")



def criar_conta_corrente(usuarios, contas, numero_conta, agencia):
    cpf = input("Informe os dígitos do CPF: ")

    usuario_encontrado = None
    for usuario in usuarios:
        if usuario["cpf"] == cpf:
            usuario_encontrado = usuario
            break

    if not usuario_encontrado:
        print("Falha na criação da conta. Usuário não encontrado.")
        return numero_conta

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario_encontrado
    }

    contas.append(conta)
    print("Conta criada com sucesso!")
    return numero_conta + 1



print("Seja bem-vindo ao Black Bank!")

opcoes_menu = {
    "1": "Depositar",
    "2": "Sacar",
    "3": "Extrato",
    "4": "Criar Usuário",
    "5": "Criar Conta Corrente",
    "6": "Sair"
}

saldo = 0
extrato = ""
limite_por_saque = 500
limite_saques = 3
numero_de_saques = 0
usuarios = []
contas = []
agencia = "0001"
numero_conta = 1
iniciacao_do_sistema = True

while True:
    if not iniciacao_do_sistema:
        os.system('cls')

    print("\nPor favor, selecione a opção desejada:\n")
    for chave, valor in opcoes_menu.items():
        print(f"[{chave}] {valor}")

    opcao = input("\n => ")

    if opcao == "1":
        valor = float(input("\nInforme o valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "2":
        valor = float(input("\nInforme o valor do saque: "))
        saldo, extrato, numero_de_saques = sacar(
            valor=valor,
            saldo=saldo,
            extrato=extrato,
            limite_por_saque=limite_por_saque,
            limite_saques=limite_saques,
            numero_de_saques=numero_de_saques
        )

    elif opcao == "3":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "4":
        criar_usuario(usuarios)

    elif opcao == "5":
        numero_conta = criar_conta_corrente(usuarios, contas, numero_conta, agencia)

    elif opcao == "6":
        print("\nObrigado e até logo!\n")
        break

    else:
        print("\nOpção inválida.")


      
                   
                   

        
    






