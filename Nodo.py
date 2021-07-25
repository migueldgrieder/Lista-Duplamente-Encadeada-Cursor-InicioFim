class Nodo: # um nodo da lista, que possui seu dado, um atributo apontando para o nodo anterior e outro para o nodo posterior 
    def __init__(self, dado, anterior=None, posterior=None):
        self.__dado = dado
        self.__anterior = anterior
        self.__posterior = posterior
    # em caso de unico nodo na lista, primeiro da lista ou o ultimo, seu ponteiro podera apontar para none  (nunca apontara para as referencias de inicio e fim)
    @property
    def dado(self):
        return self.__dado

    @dado.setter #um nodo nao pode ter como dado o none
    def dado(self, dado):
        if dado == None:
            dado = 0
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