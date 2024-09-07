menu = """

[0] Depositar
[1] Sacar
[2] Extrato
[3] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:     # Loop infinito

    opcao = input(menu)  # Vaipuxar o menu desenvolvido no incio.

    if opcao == "0":
        valor = float(input("Informe o valor do deposito: "))   # Sera perguntado sobre o valor de deposito desejado

        if valor > 0:                                           # O valor tem que ser acima de 0
            saldo += valor                                      # Sendo maior que 0 será adicionado no saldo.
            extrato += f"Deposito: R$ {valor:.2f}\n"            # Aqui esta concatenando a string deposito com valor formatado com 2 casas decimas

        else:
            print("Operação falhou! O valor informado é inválido.")     # Caso o valor seja digitado abaixo de 0 (negativo) sera gerando essa frase

    elif opcao == "1":
        valor = float(input("Informe o valor do saque: "))            # Sera perguntado sobre o valor de saque desejado

        excedeu_saldo = valor > saldo                                 # Aqui será comparado se o valor é mairo que o saldo.

        excedeu_limite = valor > limite                               # Aqui sera comparado se o valor é maior que o limite de saque.

        excedeu_saques = numero_saques >= LIMITE_SAQUES               # Aqui compara se o numero de saques é >= ao limite de saques (ate 3 saques).

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")        

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou!	Número maximo de saques excedido")

        elif valor > 0:                                                   # O valor tem que ser acima de 0
            saldo -= valor                                                # Sendo menor que 0 será informado da invalidade. 
            extrato += f"saque: R$ {valor:.2f}\n"                         # Valor positivo sera encrementado e concatenado com extrato e valor.
            numero_saques += 1                                            # aqui é para que o saque não comece do 0 e sim de 1.

        else:
            print("Operação falhou! O valor informado é invalido.")        # caso esteja tentando sacar um valor negativo, aparecerar essa string

    elif opcao == "2":
        print("\n================ Extrato ================")
        print("Não foram realizados movimentações." if not extrato else extrato)  # se não tiver movimentação de extrato, sera exibido a mensagem. Caso contrario será mostrado a variavel extrato.
        print(f"\nSaldo: R$ {saldo:.2f}")                                         # Valor total do saldo.
        print("================ Extrato ================")
        
    elif opcao == "2":
        print ("Extrato")

    elif opcao == "3":
        break

    else:
        print("Operação inválida, por favor selecione a opção desejada.")