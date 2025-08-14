from abc import ABC
from abc import abstractclassmethod
from dataclasses import dataclass

@dataclass
class Pessoa(ABC):
    email: str
    telefone: str
    endereco: str
    
    