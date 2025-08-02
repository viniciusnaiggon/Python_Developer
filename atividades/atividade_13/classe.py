# classe
class Conta:
    # construtor
    def __init__(self, titular, cpf, agencia, conta, saldo):
        # atributos
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo

    # Método de ação
    def consultar(self):
        return f"Titular: {self.titular} /n CPF: {self.cpf} /n Agência: {self.agencia} /n Conta: {self.conta} /n Saldo: {self.saldo}"
    