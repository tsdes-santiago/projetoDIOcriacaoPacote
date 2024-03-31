from .estrutura import *
from .operacoes_clientes import filtrar_cliente, recuperar_conta_cliente

def sacar(clientes):
    id_c = input("Informe o CPF/CNPJ: \t")
    cliente = filtrar_cliente(id_c, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return 
    
    valor = float(input("Informe o valor do saque: \t"))
    transacao = Saque(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)

def depositar(clientes):
    id_c = input("informe o CPF/CNPJ: ")
    cliente = filtrar_cliente(id_c, clientes)
    
    if not cliente:
        print("Cliente não encontrado.")
        return 
    
    valor = float(input("Informe o valor do depósito: \t"))
    transacao = Deposito(valor)

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    id_c = input("Informe o CPF/CNPJ: \t")
    cliente = filtrar_cliente(id_c, clientes)

    if not cliente:
        print("Cliente não encontrado.")
        return 

    conta = recuperar_conta_cliente(cliente)

    if not conta:
        return
    
    print('#'*10, 'EXTRATO', '#'*10)
    transacoes = conta.historico.transacoes

    extrato = ""

    if not transacoes:
        extrato = "Não foram realizadas movimentações."
    else:
        for transacao in transacoes:
            extrato += f"{transacao['tipo']}: \n \t R$ {transacao['valor']:.2f} \n"

    print(extrato)
    print(f"Saldo: \n \t R$ {conta.saldo:.2f}")
    print('#'*40)

def operar_conta(clientes, contas):
    
    #Menu para movimentar a conta
    menu_conta = """
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair

    =>"""

    #Recebe a opção selecionada pelo cliente e executa a ação
    while True:

        opcao = input(menu_conta)

        if opcao == 'd':
            print('Deposito')
            
            depositar(clientes)

        elif opcao == 's':

            print('Saque')
            sacar(clientes)
        
        elif opcao == 'e':
            exibir_extrato(clientes)

        elif opcao == 'q':
            break

        else:
            print("Operação invalida, por favor selecione nomavente a operação desejada")
    return None
