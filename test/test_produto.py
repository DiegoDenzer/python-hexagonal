from unittest import TestCase

from core.produto import Produto


class TestProduto(TestCase):

    def test_ativar_com_valor_zero(self):
        produto = Produto("Produto Teste", 0)
        self.assertRaises(ValueError, produto.ativar)

    def test_ativar_sem_valor(self):
        produto = Produto("Produto Teste", 10)
        produto.preco = None  # Removendo o valor do preço
        self.assertRaises(ValueError, produto.ativar)


    def test_ativar_com_valor_positivo(self):
        produto = Produto("Produto Teste", 50)
        produto.ativar()
        self.assertEqual(produto.status.name, "ATIVO")

    def test_desativar_sem_valor(self):
        produto = Produto("Produto Teste", 19)
        produto.preco = None  # Removendo o valor do preço
        self.assertRaises(ValueError, produto.desativar)

    def test_desativar_com_valor(self):
        produto = Produto("Produto Teste", 19)
        self.assertRaises(ValueError, produto.desativar)

    def test_desativar_valor_negativo(self):
        produto = Produto("Produto Teste", 1)
        produto.preco = -20  # Definindo um valor negativo para o preço
        self.assertRaises(ValueError, produto.desativar)

    def test_desativar_valor_zero(self):
        produto = Produto("Produto Teste", 0)
        produto.desativar()
        self.assertEqual(produto.status.name, "INATIVO")

    def test_criar_produto_com_nome_vazio(self):
        self.assertRaises(ValueError, Produto, "", 10)

    def test_criar_produto_com_valor_positivo(self):
        produto = Produto("Produto Teste", 10)
        self.assertEqual(produto.nome, "Produto Teste")
        self.assertEqual(produto.preco, 10)
        self.assertEqual(produto.status.name, "PENDENTE")

    def test_criar_produto_com_valor_negativo(self):
        self.assertRaises(ValueError, Produto, "Produto Teste", -5)

    def test_criar_produto_com_valor_zero(self):
        produto = Produto("Produto Teste", 0)
        self.assertEqual(produto.nome, "Produto Teste")
        self.assertEqual(produto.preco, 0)
        self.assertEqual(produto.status.name, "PENDENTE")

    def test_id_gerado_automaticamente(self):
        produto = Produto("Produto Teste", 10)
        self.assertIsNotNone(produto.id)
        self.assertIsInstance(produto.id, str)

