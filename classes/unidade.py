class Unidade:
    def __init__(self, numero_unidade, nome, numero_filial):
        self.__id = numero_unidade
        self.__nome = nome
        self.__filial = numero_filial

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_filial(self):
        return self.__filial

    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_filial(self, filial):
        self.__filial = filial