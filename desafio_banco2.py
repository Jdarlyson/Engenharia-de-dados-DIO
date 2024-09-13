import textwrap

# Função para exibir o menu ao usuário e coletar a opção escolhida.
def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    # textwrap.dedent remove indentação desnecessária do menu.
    return input(textwrap.dedent(menu))

# Função responsável pelo depósito.
def depositar(saldo, valor, extrato, /):
    # Verifica se o valor informado é válido (maior que zero).
    if valor > 0:
        saldo += valor  # Atualiza o saldo com o valor depositado.
        extrato += f"Depósito:\tR$ {valor:.2f}\n"  # Adiciona a operação no extrato.
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        # Se o valor for inválido, exibe uma mensagem de erro.
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # Retorna o saldo atualizado e o extrato.
    return saldo, extrato

# Função para realizar o saque.
def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Verifica se o valor do saque excede o saldo, o limite ou o número de saques permitidos.
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    # Condições para cada tipo de erro.
    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")

    elif excedeu_limite:
        print("\n@@@ Operação falhou! O valor do saque excede o limite. @@@")

    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")

    elif valor > 0:
        # Se o valor for válido, realiza o saque.
        saldo -= valor  # Diminui o saldo.
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"  # Registra o saque no extrato.
        numero_saques += 1  # Incrementa o número de saques realizados.
        print("\n=== Saque realizado com sucesso! ===")

    else:
        # Caso o valor do saque seja inválido (não positivo).
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")

    # Retorna o saldo atualizado e o extrato.
    return saldo, extrato

# Função para exibir o extrato.
def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    # Verifica se há movimentações no extrato, caso contrário, exibe uma mensagem padrão.
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")

# Função para criar um novo usuário.
def criar_usuario(usuarios):
    # Coleta as informações do novo usuário.
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)  # Verifica se o CPF já está cadastrado.

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    # Coleta os dados pessoais do novo usuário.
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Adiciona o novo usuário à lista de usuários.
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("=== Usuário criado com sucesso! ===")

# Função para filtrar e encontrar um usuário na lista de usuários pelo CPF.
def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

# Função para criar uma nova conta.
def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)  # Busca o usuário pelo CPF.

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        # Cria um dicionário com as informações da conta.
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")

# Função para listar todas as contas cadastradas.
def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        """
        # Exibe os detalhes de cada conta de forma formatada.
        print("=" * 100)
        print(textwrap.dedent(linha))

# Função principal, onde o programa começa a execução.
def main():
    # Variáveis de controle.
    LIMITE_SAQUES = 3  # Limite de saques diários.
    AGENCIA = "0001"  # Número da agência.

    saldo = 0  # Saldo inicial.
    limite = 500  # Limite de saque por operação.
    extrato = ""  # Extrato das operações.
    numero_saques = 0  # Contador de saques realizados.
    usuarios = []  # Lista de usuários cadastrados.
    contas = []  # Lista de contas cadastradas.

    # Loop principal para interagir com o usuário.
    while True:
        opcao = menu()  # Exibe o menu e coleta a opção do usuário.

        # Verifica a opção escolhida pelo usuário e executa a ação correspondente.
        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break  # Encerra o programa.

        else:
            # Caso o usuário selecione uma opção inválida.
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Inicia o programa chamando a função principal.
main()
