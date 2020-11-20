class Cliente:

    def __init__(self, nome, cpf_cnpj):
        self.__nome = nome
        self.__cpf_cnpj = cpf_cnpj

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome


    @property
    def cpf_cnpj(self):
        return self.__cpf_cnpj

    @cpf_cnpj.setter
    def cpf_cnpj(self, cpf_cnpj):
        self.__cpf_cnpj = cpf_cnpj
