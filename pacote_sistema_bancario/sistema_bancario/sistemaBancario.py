
from .operacoes_clientes import *
from .operacoes_conta import *

#---------------------
#Começo execução
#Menu para cadastrar usuário ou acessar conta
def menu():
    menu = """

    [m] Movimentar Conta
    [c] Cadastrar Cliente
    [ac] Adicionar Conta
    [lc] Listar Contas
    [q] Sair
    =>"""
    return input(menu)

#Exibe o menu e espera a resposta do usuário

def run_sistema(clientes, contas):
        
    while True:
        opcao = menu()
        
        if opcao == 'm':
            operar_conta(clientes, contas)
        
        elif opcao == 'c':
            print('Cadastrar cliente')
            criar_cliente(clientes)
            
        elif opcao == 'ac':
            numero_conta = len(contas)+1
            criar_conta(numero_conta, clientes, contas)
        
        elif opcao == 'lc':
           listar_contas(contas) 
        
        elif opcao == 'q':
            break
        
        else:
            print("Operação invalida, por favor selecione novamente a operação desejada")
