import Pessoa
from dataclasses import dataclass

@dataclass
class PessoaFisica(Pessoa.Pessoa):
    nome: str
    cpf: str
    idade: int
    
    def __str__(self):
        return f"{"_"*20} Dados pessoais: {"_"*20}\n\nNome:{self.nome}\nIdade: {len(self)}\nCPF: {self.cpf}"