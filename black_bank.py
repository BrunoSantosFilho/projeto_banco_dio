
"""
Este projeto foi desenvolvido com apoio do ChatGPT 
por estar iniciando meus estudos em Programação Orientada a 
Objetos, contei com suporte para estruturar o sistema e entender 
melhor como funcionam os conceitos de abstração, herança, polimorfismo e 
composição.

Ainda estou aprendendo e pretendo continuar estudando Python, 
aprimorar meus conhecimentos e voltar a trabalhar neste projeto 
com mais domínio no futuro.

"""


from abc import ABC, abstractmethod

# -------------------------------
# Interface Transacao (Classe Abstrata)
# -------------------------------
class Transacao(ABC):
    @abstractmethod
    def registrar(self, conta):
        pass

# -------------------------------
# Classe Deposito (Herança + Polimorfismo)
# -------------------------------
class Deposito(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.depositar(self.valor)

# -------------------------------
# Classe Saque (Herança + Polimorfismo)
# -------------------------------
class Saque(Transacao):
    def __init__(self, valor):
        self.valor = valor

    def registrar(self, conta):
        return conta.sacar(self.valor)

# -------------------------------
# Classe Historico (Composição)
# -------------------------------
class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar(self, descricao):
        self.transacoes.append(descricao)

    def exibir(self):
        print("\nHistórico de transações:")
        if not self.transacoes:
            print("- Nenhuma transação registrada.")
        for transacao in self.transacoes:
            print(f"- {transacao}")

# -------------------------------
# Classe Cliente
# -------------------------------
class Cliente:
    def __init__(self, nome):
        self.nome = nome

# -------------------------------
# Classe Conta
# -------------------------------
class Conta:
    def __init__(self, numero, cliente):
        self._numero = numero
        self._cliente = cliente
        self._saldo = 0
        self._historico = Historico()

    def sacar(self, valor):
        if valor > 0 and valor <= self._saldo:
            self._saldo -= valor
            self._historico.adicionar(f"Saque: R${valor:.2f}")
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Saque inválido.")
            return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            self._historico.adicionar(f"Depósito: R${valor:.2f}")
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
            return True
        else:
            print("Depósito inválido.")
            return False

    def mostrar_saldo(self):
        print(f"\nSaldo atual: R${self._saldo:.2f}")

    def mostrar_historico(self):
        self._historico.exibir()

# -------------------------------
# Teste do sistema (Simulação)
# -------------------------------
if __name__ == "__main__":
    cliente = Cliente("Bruno")
    conta = Conta("001", cliente)

    # Criando transações
    t1 = Deposito(300)
    t2 = Saque(100)

    # Executando transações
    t1.registrar(conta)
    t2.registrar(conta)

    # Exibindo saldo e histórico
    conta.mostrar_saldo()
    conta.mostrar_historico()
                   
                   

        
    






