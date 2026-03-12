class Filial:
    def __init__(self, numero_filial,nome, pais, empresa_id):
        self.__id = numero_filial
        self.__id_empresa = empresa_id
        self.__nome = nome
        self.__pais = pais

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_pais(self):
        return self.__pais
    def get_empresa_id(self):
        return self.__id_empresa
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_pais(self, pais):
        self.__pais = pais
    def set_empresa_id(self, empresa_id):
        self.__id_empresa = empresa_id
        