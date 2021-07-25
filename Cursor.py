class Cursor: #classe do cursor, que ira ter o atributo selecionado que sera um objeto nodo ou none
    def __init__(self):
        self.__selecionado = None

    @property
    def selecionado(self):
        return self.__selecionado

    @selecionado.setter
    def selecionado(self, selecionado):
        self.__selecionado = selecionado

    def irParaPrimeiro(self):
        while self.__selecionado.anterior is not None:
            self.__selecionado = self.__selecionado.anterior

    def irParaUltimo(self):
        while self.__selecionado.posterior is not None:
            self.__selecionado = self.__selecionado.posterior

    def avancarKPosicoes(self, k):
        for i in range(k):
            self.__selecionado = self.__selecionado.posterior

    def retocederKPosicoes(self, k):
        for i in range(k):
            self.__selecionado = self.__selecionado.anterior