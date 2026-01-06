
from typing import Dict, List, Optional
from core.persistencia import Persistencia
from core.produto import Produto

class ProdutoPersistencia(Persistencia[Produto]):

    def __init__(self) -> None:
        self._store: Dict[str, Produto] = {}

    def buscar_por_id(self, id: str) -> Optional[Produto]:
        return self._store.get(id)

    def listar_todos(self) -> List[Produto]:
        return list(self._store.values())

    def salvar(self, obj: Produto) -> None:
        self._store[obj.id] = obj

    def excluir(self, id: str) -> None:
        self._store.pop(id, None)