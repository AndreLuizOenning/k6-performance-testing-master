class Empresa:    
    def __init__(self, numero_empresa,nome, pais):
        self.__id = numero_empresa
        self.__nome = nome
        self.__pais = pais

    def get_id(self):
        return self.__id
    def get_nome(self):
        return self.__nome
    def get_pais(self):
        return self.__pais
    def set_id(self, id):
        self.__id = id
    def set_nome(self, nome):
        self.__nome = nome
    def set_pais(self, pais):
        self.__pais = pais


    
    




