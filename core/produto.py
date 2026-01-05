import uuid
from enum import Enum
from dataclasses import dataclass, field
from uuid import UUID
class Status(Enum):
    INATIVO = 0
    ATIVO = 1
    PENDENTE = 2

@dataclass
class Produto:

    nome: str
    preco: float
    id: str = field(init=False, default_factory=lambda: str(uuid.uuid4()))
    status: Status = field(init=False, default=Status.PENDENTE)

    def __post_init__(self):
        if not self.nome:
            raise ValueError("O nome não pode estar vazio")
        if self.preco < 0:
            raise ValueError("O preço não deve ser negativo")



    def ativar(self):
        if getattr(self, "preco", None) is None:
            raise ValueError("Preço não definido.")
        if self.preco <= 0:
            raise ValueError("Preço inválido para ativação.")
        self.status = Status.ATIVO

    def desativar(self):

        if getattr(self, "preco", None) is None:
            raise ValueError("Preço não definido.")

        if self.preco != 0:
            raise ValueError("Preço inválido para desativação.")

        self.status = Status.INATIVO





