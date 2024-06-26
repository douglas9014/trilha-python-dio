menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500        # Valor limite por operação de saque.
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3   # Quantidade limite de saques por sessão.

"""
TODO:
[ ] Separar todas as operações em funções.
    [x] Depositar
    [ ] Sacar
    [ ] Extrato

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

[ ] Regras para a passagem de argumentos para as funções:
    [ ] Saque: receber argumentos apenas por nome (ex: saldo=varSaldo).
            Entrada: saldo, valor, extrato, limite, numero_saques, limite_saques.
            Saída: saldo, extrato.

    [x] Depósito: receber argumento apenas por posição.
            Entrada: saldo, valor, extrato
            Saída: saldo, extrato.

    [ ] Extrato: receber argumentos por posição e nome.
            Posicionais: saldo
            Nomeados: extrato

[ ] Informar ao usuário o valor limite do saque quando o limite for excedido.
[ ] Quando o limite de operações de saque for excedido, negar a operação sem que o usuário tenha que inserir um valor de saque primeiro.
"""

# Argumentos das funções por somente posição, posição ou nome e somente nome:
# def nome_funcao(posicao1, posicao2, /, posicao_ou_nome, *, nome1, nome2):

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")
    
    return saldo, extrato


while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(saldo, valor, extrato)
        
    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite.")

        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "e":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================")

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
