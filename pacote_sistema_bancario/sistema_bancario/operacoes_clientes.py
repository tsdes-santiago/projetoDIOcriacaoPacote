from .estrutura import *

def criar_cliente(clientes):
    id_c = input("informe o CPF/CNPJ:")
    cliente = filtrar_cliente(id_c, clientes)
    
    if cliente:
        print("Cliente já cadastrado.")
        return 

    nome = input("Informe o nome completo: ")
    data = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/UF): ")

    cliente = PessoaFisica(nome=nome, data = data, id_c = id_c, endereco=endereco)

    clientes.append(cliente)

    print("Cliente cadastrado com sucesso!")

def criar_conta(numero_conta, clientes, contas):
    id_c = input("Informe o CPF/CNPJ:")
    cliente = filtrar_cliente(id_c, clientes)

    if not cliente:
        print("Cliente não encontrado. Cadastre o novo cliente.")
        return
    
    conta = ContaCorrente.nova_conta(cliente = cliente, numero = numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print('Conta criada com sucesso!')

def filtrar_cliente(id_c, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.id == id_c]

    return clientes_filtrados[0] if clientes_filtrados else None
def listar_contas(contas):
    for conta in contas:
        print("#"*40)
        print(str(conta))

def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta.")
        return
    # ADICIONAR METODO PARA SELECIONAR CONTAS
    return cliente.contas[0]