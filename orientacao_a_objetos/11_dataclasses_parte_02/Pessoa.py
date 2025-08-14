
from abc import ABC
from abc import classmethod
from dataclasses import dataclass

@dataclass
@classmethod
class Pessoa(ABC):
    nome: str = ""
    email: str = ""
    cpf: str = ""
    idade: int = 0
    altura: float