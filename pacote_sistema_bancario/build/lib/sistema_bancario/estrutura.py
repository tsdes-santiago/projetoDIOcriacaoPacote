from abc import ABC, abstractclassmethod, abstractproperty
from datetime import datetime

#################################
# Definição as classes
#################################

# ___________________


class Cliente:
    def __init__(self, id_c):
        self.id = id_c
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append()


class PessoaFisica(Cliente):
    def __init__(self, nome, data, id_c, endereco):
        super().__init__(id_c)
        self.nome = nome
        self.id = id_c
        self.data = data
        self.endereco = endereco


class PessoaJuridica(Cliente):
    def __init__(self, nome, data, id, endereco):
        super().__init__(id_c)
        self.nome = nome
        self.id = id_c
        self.data = data
        self.endereco = endereco


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0.0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo

    @property
    def numero(self):
        return self._numero

    @property
    def agencia(self):
        return self._agencia

    @property
    def cliente(self):
        return self._cliente

    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Operação falhou. Saldo insuficiente.")

        elif valor > 0:
            self._saldo -= valor
            print("Saque realizado com sucesso.")
            return True

        else:
            print("Operação falhou. Valor informado inválido")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print(f"Foram depositados R$ {valor:.2f} na sua conta.")
        else:
            print("Valor invalido. Cancelando operação.")
            return False

        return True


class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor):
        numero_saques = len(
            [
                transacao
                for transacao in self.historico.transacoes
                if transacao["tipo"] == Saque.__name__
            ]
        )

        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou. O valor excede o limite.")

        elif excedeu_saques:
            print("Operação falhou. Você excedeu o limite de saques diários.")

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f"""\
            Agencia:\t {self.agencia}
            C/C: \t \t {self.numero}
            Titular:\t {self.cliente.nome}
        """


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes

    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%s"),
            }
        )


class Transacao(ABC):
    @property
    @abstractproperty
    def valor(self):
        pass

    @abstractclassmethod
    def registrar(self, conta):
        pass


class Saque(Transacao):

    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor

    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.adicionar_transacao(self)
