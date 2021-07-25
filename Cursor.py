class Cursor: #classe do cursor, que ira ter o atributo selecionado que sera um objeto nodo ou none, e outro da lista que a instancia
    def __init__(self, listade):
        self.__selecionado = 0
        self.__listade = listade

    @property
    def selecionado(self):
        return self.__selecionado

    @selecionado.setter
    def selecionado(self, selecionado):
        self.__selecionado = selecionado

    def irParaPrimeiro(self):        
        self.__selecionado = self.__listade.inicio().posterior

    def irParaUltimo(self):
        self.__selecionado = self.__listade.fim().anterior

    def avancarKPosicoes(self, k):
        for i in range(k):
            self.__selecionado = self.__selecionado.posterior

    def retocederKPosicoes(self, k):
        for i in range(k):
            self.__selecionado = self.__selecionado.anterior