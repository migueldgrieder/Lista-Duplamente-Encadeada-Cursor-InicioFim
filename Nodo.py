class Nodo: # um nodo da lista, que possui seu dado, um atributo apontando para o nodo anterior e outro para o nodo posterior 
    def __init__(self, dado=0, anterior=None, posterior=None):
        self.__dado = dado
        self.__anterior = anterior
        self.__posterior = posterior
    # em caso de unico nodo da lista, primeiro da lista ou none, seu ponteiro podera apontar para none
    @property
    def dado(self):
        return self.__dado

    @dado.setter
    def dado(self, dado):
        self.__dado = dado

    @property
    def anterior(self):
        return self.__anterior

    @anterior.setter
    def anterior(self, anterior):
        self.__anterior = anterior

    @property
    def posterior(self):
        return self.__posterior

    @posterior.setter
    def posterior(self, posterior):
        self.__posterior = posterior