#Criando um sistema bancário
#Com depósito, saque e extrato
#Deposito: deve ser exibido em extrato inteiro e positivo
#Saque:3 saques diarios com limite de 500 reais por saque caso naoo tenha
#saldo em conta, deve exibir uma mensagem
#todos os saques armazenados em uma variavel e exibidos na operacao extrato
#Extrato: listar todos os depositos e saques, saldo atual da conta
#e devem ser exibidos R$xxxxx.xx

nome = input("Insira o seu nome: ")
print("Olá, {}! Escolha uma das opções abaixo".format(nome))
#Criando as opções

menu =  """

 [1] Depósito
 [2] Saque
 [3] Extrato
 [4] Sair


=> """

#Definindo variaveis em minúsculas e constantes em maiúsculas

saldo = 0
limite = 0
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

#criando laço de repetição com menu

while True:
    opcao = input(menu)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Escolha um valor inteiro e positivo!")

        
    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Saldo insuficiente!") 
        elif excedeu_limite:
            print("O valor do saque excede o limite!")

        elif excedeu_saques:
            print("Número maximo de saques excedidos")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("O valor informado é inválido: ")

    elif opcao == "3":
        print("\n===== EXxtrato de {} =====".format(nome))
        print("Não foram realizadas movimentações!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f} ")
        print("======================================")

    elif opcao == "4":
        break
    else:
        print("Operação inválida, retorne ao menu!")
   

