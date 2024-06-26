menu = """

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

"""
TODO:
[x] Separar todas as operações em funções.
    [x] Depositar
    [x] Sacar
    [x] Extrato

    Criar novas funções:
        [ ] Criar usuário
            [ ] Armazenar usuários em uma lista.
            [ ] Dados do usuário: nome, data de nascimento, CPF, endereço.
                [ ] CPF: registrar somente números e não permitir CPFs repetidos
                [ ] Endereço: "Logradouro, Número - Bairro - Cidade/UF"
    
        [ ] Criar conta corrente (vinculada a um usuário)
            [ ] Armazenar contas em uma lista.
                Toda conta deve sempre ser associada a um usuário cadastrado.
                Um usuário pode ter mais de uma conta, mas uma conta pertence a apenas um usuário.
                Usuário (1) --- (N) Conta
            [ ] Composição da conta: agência, número da conta, usuário
                [ ] Número da conta: Sequencial começando em 1.
                [ ] Agência: Sempre "0001".

        [ ] Listar usuários
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

def depositar(saldo, extrato, /):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("Depósito efetuado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


def sacar(*, saldo, extrato, limite, numero_saques, LIMITE_SAQUES):
    if numero_saques >= LIMITE_SAQUES: # Se a quantidade de operações de saque feitas pelo usuário for execeder o limite de operações de saque.
        print("Operação falhou! Limite de operações de saque excedido.")
    else:
        valor = float(input("Informe o valor do saque: "))

        if valor > saldo: # Se o valor de saque informado pelo usuário for maior que o saldo.
            print("Operação falhou! Você não tem saldo suficiente.")

        elif valor > limite: # Se o valor de saque foi maior do que o valor limite por operação de saque.
            print(f"Operação falhou! O valor limite para cada operação de saque é R$ {limite}")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque:\t\tR$ {valor:.2f}\n"
            numero_saques += 1
            print(f"Saque efetuado com sucesso!\nOperações de saque restantes: {LIMITE_SAQUES - numero_saques}.")

        else:
            print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def emitir_extrato(saldo, /, *, extrato=extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato) # Esta linha é impressa somente quando o extrato está vazio.
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("=========================================")

    # Quando uma função não termina com um [return], "None" (classe 'NoneType') é retornado por padrão pelo Python.


while True:
    opcao = input(menu)

    if opcao == "d":
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
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
