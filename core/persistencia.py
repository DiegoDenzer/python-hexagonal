from typing import Protocol, List, Optional, TypeVar

T = TypeVar('T')


class Leitura(Protocol[T]):
    def obter_por_id(self, id: str) -> Optional[T] | None: ...
    def listar_todos(self) -> List[T]: ...


class Escrita(Protocol[T]):
    def salvar(self, obj: T) -> None:
        ...
    def excluir(self, id: str) -> None:
        pass

class Persistencia(Leitura[T], Escrita[T], Protocol[T]):
    ...