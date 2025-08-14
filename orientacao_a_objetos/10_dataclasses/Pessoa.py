
from dataclasses import dataclass

@dataclass
class Pessoa:
    nome: str = ""
    email: str = ""
    cpf: str = ""
    idade: int = 0
    altura: float = 0.0

    
    def __str__(self):
        return f"nome: {self.nome}\nEmail: {self.email}\nCPF: {self.cpf}\nIdade: {len(self)}\nAltura: {self.altura}"