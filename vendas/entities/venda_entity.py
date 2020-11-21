class Venda:

    def __init__(self, cliente, data, forma_pagamento, valor_total):
        self.__cliente = cliente
        self.__data = data
        self.__forma_pagamento = forma_pagamento
        self.__valor_total = valor_total


    @property
    def cliente(self):
        return self.__cliente

    @cliente.setter
    def cliente(self, cliente):
        self.__cliente = cliente


    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, data):
        self.__data = data


    @property
    def forma_pagamento(self):
        return self.__forma_pagamento

    @forma_pagamento.setter
    def forma_pagamento(self, forma_pagamento):
        self.__forma_pagamento = forma_pagamento


    @property
    def valor_total(self):
        return self.__valor_total

    @valor_total.setter
    def valor_total(self, valor_total):
        self.__valor_total = valor_total

