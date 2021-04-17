from cliente import Cliente
from categoria_produto import CategoriaProduto

class Produto:

    def __init__(self, codigo: int, descricao: str, categoria_produto: CategoriaProduto, quantidade: int, preco_unitario: float, preco_total:float):
        self.__codigo = codigo
        self.__descricao = descricao
        self.__categoria_produto = categoria_produto
        self.__quantidade = quantidade
        self.__preco_unitario = preco_unitario
        self.__cliente = []
        self.__preco_total = preco_total

    @property
    def codigo(self):
        return self.__codigo

    @codigo.setter
    def codigo(self, codigo):
        self.__codigo = codigo

    @property
    def descricao(self):
        return self.__codigo

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao

    @property
    def categoria_produto(self):
        return self.__categoria_produto

    @categoria_produto.setter
    def categoria_produto(self, categoria_produto:CategoriaProduto):
        if isinstance(categoria_produto, CategoriaProduto):
            self.__categoria_produto = categoria_produto

    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade

    @property
    def preco_unitario(self):
        return self.__preco_unitario

    @preco_unitario.setter
    def preco_unitario(self, preco_unitario):
        self.__preco_unitario = preco_unitario

    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente: Cliente):
        if isinstance(cliente, Cliente):
            self.__cliente.append(cliente)

    @property
    def preco_total(self):
        return self.__preco_total

    def calcula_preco_total(self):
        #cada produto possa calcular o seu preço total (quantidade multiplicada pelo preço unitário).
        self.__preco_total = self.__preco_unitario * self.__quantidade

