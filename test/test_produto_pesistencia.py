from unittest import TestCase

from adapters.memoria_produto import ProdutoPersistencia
from core.produto import Produto, Status


class TestProdutoPersistencia(TestCase):

    def test_deve_testar_a_persistencia_do_produto(self):
        produto = Produto("Produto Persistencia", 25.0)
        persistencia = ProdutoPersistencia()
        persistencia.salvar(produto)
        produto_persistido = persistencia.buscar_por_id(produto.id)
        self.assertIsNotNone(produto_persistido)
        self.assertEqual(produto_persistido.nome, "Produto Persistencia")
        self.assertEqual(produto_persistido.preco, 25.0)

    def test_deve_listar_todos_os_produtos(self):
        produto1 = Produto("Produto 1", 10.0)
        produto2 = Produto("Produto 2", 20.0)
        persistencia = ProdutoPersistencia()
        persistencia.salvar(produto1)
        persistencia.salvar(produto2)
        produtos = persistencia.listar_todos()
        self.assertEqual(len(produtos), 2)

    def test_deve_excluir_produto(self):
        produto = Produto("Produto a ser excluído", 15.0)
        persistencia = ProdutoPersistencia()
        persistencia.salvar(produto)
        persistencia.excluir(produto.id)
        produto_excluido = persistencia.buscar_por_id(produto.id)
        self.assertIsNone(produto_excluido)

    def test_deve_atualizar_produto(self):
        produto = Produto("Produto a ser atualizado", 30.0)
        persistencia = ProdutoPersistencia()
        persistencia.salvar(produto)
        produto.preco = 35.0
        persistencia.salvar(produto)
        produto_atualizado = persistencia.buscar_por_id(produto.id)
        self.assertIsNotNone(produto_atualizado)
        self.assertEqual(produto_atualizado.preco, 35.0)
