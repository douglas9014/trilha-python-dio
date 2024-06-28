menu = """

[nu] Novo usuário
[lu] Listar usuários

[nc] Nova conta
[lc] Listar contas

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

Por favor, escolha uma das operações: """

saldo = 0
limite = 500        # Valor limite por operação de saque.
extrato = ""
numero_saques = 0   # Quantidade de operações de saque efetuadas pelo usuário.
LIMITE_SAQUES = 3   # Quantidade limite de saques por sessão.
usuarios = {}

# # Dados pré-carregados para testes:
# usuarios = {"12345679801": {
#                 "nome": "Fulano",
#                 "data_nascimento": "01/01/2000",
#                 "endereco": {"logradouro": "Rua dos Bobos",
#                             "numero": "0",
#                             "bairro": "Jardim da Infância",
#                             "cidade": "Nostalgia",
#                             "uf": "AC"}},
#             "11223344556": {
#                 "nome": "Ciclano",
#                 "data_nascimento": "31/12/1999",
#                 "endereco": {"logradouro": "Avenida Brasil",
#                             "numero": "171",
#                             "bairro": "Vila Alpha",
#                             "cidade": "Cascalhos",
#                              "uf": "SC"}}}


"""
TODO Desafio do curso:
[x] Separar todas as operações em funções.
    [x] Depositar
    [x] Sacar
    [x] Extrato

    [ ] Criar novas funções:
        [x] Criar usuário
            [x] Armazenar usuários em uma lista.
            [x] Dados do usuário: nome, data de nascimento, CPF, endereço.
                [x] CPF: registrar somente números e não permitir CPFs repetidos
                [x] Endereço: "Logradouro, Número - Bairro - Cidade/UF"
    
        [ ] Criar conta corrente (vinculada a um usuário)
            [ ] Armazenar contas em uma lista.
                Toda conta deve sempre ser associada a um usuário cadastrado.
                Um usuário pode ter mais de uma conta, mas uma conta pertence a apenas um usuário.
                Usuário (1) --- (N) Conta
            [ ] Composição da conta: agência, número da conta, usuário
                [ ] Número da conta: Sequencial começando em 1.
                [ ] Agência: Sempre "0001".

        [x] Listar usuários
        [ ] Listar contas

[x] Regras para a passagem de argumentos para as funções:
    [x] Saque: receber argumentos apenas por nome (ex: saldo=varSaldo).
            Entrada: saldo, valor, extrato, limite, numero_saques, limite_saques.
            Saída: saldo, extrato.

    [x] Depósito: receber argumento apenas por posição.
            Entrada: saldo, valor, extrato
            Saída: saldo, extrato.

    [x] Extrato: receber argumentos por posição e nome.
            Posicionais: saldo
            Nomeados: extrato

[x] Mudanças e adições além do que foi estipulado pelo desafio:
    [x] Receber do usuário a entrada do valor dentro das funções de Saque e Depósito, ao invés de fazer isso no Menu.
    [x] Quando o limite de operações de saque for excedido, negar a operação sem que o usuário tenha que inserir um valor de saque primeiro.
    [x] Informar ao usuário o valor limite do saque quando o limite for excedido.
    [x] Usar tabulação para alinhar os valores no extrato.
"""

# Argumentos das funções por somente posição, posição ou nome e somente nome:
# def nome_funcao(posicao1, posicao2, /, posicao3, nome1=varNome1, *, nome2=varNome2, nome3=varNome3):

# Cria e insere um cabeçalho com um título (quando um texto é recebido)
# ou um rodapé sem título (quando nenhum texto é recebido):
def inserir_borda(texto):
    if texto:
        print("\n" + str(" " + texto.upper() + " ").center(40, "="))
    else:
        print("=" * 40)
    # Quando uma função não termina com um [return], "None" (classe 'NoneType') é retornado por padrão pelo Python.
    # return None

# Coleta os dados de um novo usuário e grava no registro de usuários:
def novo_usuario(usuarios):
    inserir_borda("cadastrar novo usuário")

    cpf = input("Informe o CPF do usuário (somente números): ")
    
    if cpf in usuarios: # Impede que CPFs repetidos sejam cadastrados.
        print("Operação falhou! O CPF informado já está cadastrado.")
    else:
        nome = input("Informe o nome do usuário: ")
        data_nascimento = input("Informe a data de nascimento (dd/mm/yyyy): ")
        
        print("\nInsira abaixo os dados do endereço.")
        logradouro = input("Logradouro: ")
        numero = input("Número: ")
        bairro = input("Bairro: ")
        cidade = input("Cidade: ")
        uf = input("UF (sigla do estado): ")

        usuarios.update({cpf: {
                        "nome": nome,
                        "data_nascimento": data_nascimento,
                        "endereco": {"logradouro": logradouro,
                                    "numero": numero,
                                    "bairro": bairro,
                                    "cidade": cidade,
                                    "uf": uf}}})
        
        print("\n\nUsuário cadastrado com sucesso!")

    inserir_borda(None)
    return usuarios

# Exibe formatado todos os dados de todos os usuários:
def listar_usuarios(usuarios):
    inserir_borda("usuários")

    if usuarios: # Se a lista de usuários conter registros:
        for cpf, dados in usuarios.items(): # Listar todos os usuários
            print("CPF: "+ cpf +
                "\nNome: " + dados["nome"] +
                "\nData de nascimento: " + dados["data_nascimento"] +
                "\nEndereço: " + dados["endereco"]["logradouro"] + ", " +
                                dados["endereco"]["numero"] + " - " +
                                dados["endereco"]["bairro"] + " - " +
                                dados["endereco"]["cidade"] + "/" +
                                dados["endereco"]["uf"] + "\n"
                )
    else: # Se a lista de usuários estiver vazia.
        print("Nenhum usuário cadastrado.")
    
    inserir_borda(None)


# Recebe um valor para ser depositado e atualiza o extrato:
def depositar(saldo, extrato, /):
    inserir_borda("depósito")

    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    inserir_borda(None)
    return saldo, extrato

# Recebe um valor para ser sacado, verifica se os requisitos são atendidos e registra no extrato:
def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    inserir_borda("saque")

    if numero_saques >= LIMITE_SAQUES: # Se a quantidade de operações de saque feitas pelo usuário for execeder o limite de operações de saque.
        print("Operação falhou! Limite de operações de saque excedido.")
    
    else:
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo: # Se o valor de saque informado pelo usuário for maior que o seu saldo.
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite: # Se o valor de saque foi maior do que o valor limite por operação de saque.
            print(f"Operação falhou! O valor limite para cada operação de saque é R$ {limite}.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque efetuado com sucesso!\nOperações de saque restantes: {LIMITE_SAQUES - numero_saques}.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    inserir_borda(None)
    return saldo, extrato, numero_saques

# Exibe todos os registros no extrato e o saldo:
def emitir_extrato(saldo, /, *, extrato=extrato):
    inserir_borda("extrato")
    print("Não foram realizadas movimentações." if not extrato else extrato) # Esta linha é impressa somente quando o extrato está vazio.
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    inserir_borda(None)

# Recebe a operação escolhida pelo usuário e chama a função relacionada:
while True:
    opcao = input(menu) # Exibe o menu e recebe a operação escolhida.

    if opcao == "nu":
        usuarios = novo_usuario(usuarios)

    elif opcao =="lu":
        listar_usuarios(usuarios)

    elif opcao =="nc":
        inserir_borda("cadastrar nova conta")
        print("Operação indisponível nesta versão.")
        inserir_borda(None)

    elif opcao =="lc":
        inserir_borda("contas")
        print("Operação indisponível nesta versão.")
        inserir_borda(None)

    elif opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
        
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(
            saldo=saldo,
            extrato=extrato,
            limite=limite,
            numero_saques=numero_saques,
            LIMITE_SAQUES=LIMITE_SAQUES
        )

    elif opcao == "e":
        emitir_extrato(saldo, extrato=extrato)

    elif opcao == "q":
        break # Sai do loop infinito [while True:], encerrando o programa.

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
