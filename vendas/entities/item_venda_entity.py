class ItemVendaDetalhes:

    def __init__(self, venda_id, produto, quantidade, valor):
        self.__venda_id = venda_id
        self.__produto = produto
        self.__quantidade = quantidade
        self.__valor = valor


    @property
    def venda_id(self):
        return self.__venda_id

    @venda_id.setter
    def venda_id(self, venda_id):
        self.__venda_id = venda_id


    @property
    def produto(self):
        return self.__produto

    @produto.setter
    def produto(self, produto):
        self.__produto = produto


    @property
    def quantidade(self):
        return self.__quantidade

    @quantidade.setter
    def quantidade(self, quantidade):
        self.__quantidade = quantidade


    @property
    def valor(self):
        return self.__valor

    @valor.setter
    def valor(self, valor):
        self.__valor = valor

