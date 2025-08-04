import json

# classe
class Conta:
    # construtor
    def __init__(self, titular, cpf, agencia, conta, saldo=0.0):
        # atributos
        self.titular = titular
        self.cpf = cpf
        self.agencia = agencia
        self.conta = conta
        self.saldo = saldo
        self.extrato = []

    # Método de ação
    def consultar(self):
        return (
            f"Titular: {self.titular} \n"
            f"CPF: {self.cpf} \n"
            f"Agência: {self.agencia} \n"
            f"Conta: {self.conta} \n"
            f"Saldo: {self.saldo:.2}"
            )
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.extrato.append(f"Depósito: R$ {valor:.2f}")
            return True
        return False
    
    def sacar(self, valor):
        if 0 < valor <= self.saldo:
            self.saldo -= valor
            self.extrato.append(f"Saque: R$ {valor:.2f}")
            return True
        return False
    
    def gerar_extrato(self):
        return self.extrato if self.extrato else ["Nenhuma movimentação realizada."]

    def salvar_extrato_em_json(self):
        dados = {
            "titular": self.titular,
            "cpf": self.cpf,
            "agencia": self.agencia,
            "conta": self.conta,
            "saldo": self.saldo,
            "extrato": self.gerar_extrato()
        }
        with open(f"extrato_{self.conta}.json", "w", encoding="utf-8") as f:
            json.dump(dados, f, ensure_ascii=False, indent=4)