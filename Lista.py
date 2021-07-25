from Cursor import Cursor
from Nodo import Nodo

class Lista_Encadeada: #classe lista, que gerenciara todas operacoes entre os nodos e o cursor
    def __init__(self, tamanho_max):
        self.__cursor = Cursor() #objeto cursor
        self.__tamanho_max = tamanho_max #o tamanho maximo de nodos que a lista ira ter
        self.__tamanho_atual = 0 #o tamanho de nodos atual da lista~
        self.__inicio = Nodo(None) 
        self.__fim = Nodo(None)



    def tamanho_atual(self):
        return self.__tamanho_atual

    def acessarAtual(self):
        return self.__cursor.selecionado

    def inserirAntesAtual(self, dado):  #insere o novo nodo atras do nodo atualmente selecionado pelo cursor
        novo = Nodo(dado)

        if self.cheia(): 
            print('A lista esta cheia!')
        if self.vazia(): #forma especfica pois se a lista tiver vazia o primeiro nodo nao tera nenhum ponteiro
            self.__cursor.selecionado = novo
            self.__tamanho_atual += 1
        if self.__cursor.selecionado.anterior is None: #caso o novo nodo seja colocado antes do primeiro nodo
            self.__cursor.selecionado.anterior = novo
            novo.posterior = self.__cursor.selecionado
            self.__tamanho_atual += 1
        else: #caso o novo nodo seja colocado no meio de dos nodos ja existentes
            self.__cursor.selecionado.anterior.posterior = novo
            novo.anterior = self.__cursor.selecionado.anterior
            self.__cursor.selecionado.anterior = novo
            novo.posterior = self.__cursor.selecionado
            self.__tamanho_atual += 1

    def inserirPosAtual(self, dado): #insere o novo nodo depois do nodo atualmente selecionado
        novo = Nodo(dado)

        if self.cheia():
            print('A lista esta cheia!')
        if self.vazia(): #forma especfica pois se a lista tiver vazia o primeiro nodo nao tera nenhum ponteiro
            self.__cursor.selecionado = novo
            self.__tamanho_atual += 1
        if self.__cursor.selecionado.posterior is None: #caso o cursor estaja na ultima posicao, o novo nodo ira ficar na nova ultima posicao, tendo assim somente o ponterio anterior
            self.__cursor.selecionado.posterior = novo
            novo.anterior = self.__cursor.selecionado
            self.__tamanho_atual += 1
        else: #caso o novo nodo seja colocado no meio de dos nodos ja existentes
            self.__cursor.selecionado.posterior.anterior = novo
            novo.posterior = self.__cursor.selecionado.posterior
            self.__cursor.selecionado.posterior = novo
            novo.anterior = self.__cursor.selecionado
            self.__tamanho_atual += 1

    def inserirFim(self, dado): #insere o nodo na ultma posicao da lista
        if self.vazia(): #caso esteja vazia, o novo nodo e criado sem nenhum ponteiro
            novo = Nodo(dado)
            self.__cursor.selecionado = novo
            self.__tamanho_atual += 1
        else: #leva o cursor para a ultima posicao e chama o metodo de adcionar o novo nodo posteriormente ao selecionado
            self.__cursor.irParaUltimo()
            self.inserirPosAtual(dado)

    def inserirFrente(self, dado): #insere o nodo na primeira posicao da lista
        if self.vazia(): #caso esteja vazia, o novo nodo e criado sem nenhum ponteiro
            novo = Nodo(dado)
            self.__cursor.selecionado = novo
            self.__tamanho_atual += 1
        else: #leva o cursor para a primeira posicao e chama o metodo de adcionar o novo nodo anteriormente ao selecionado
            self.__cursor.irParaPrimeiro()
            self.inserirAntesAtual(dado)

    def inserirNaPosicao(self, k, dado): #insere o nodo na posicao desejada
        self.__cursor.irParaPrimeiro() #leva o cursor para a primeira posicao

        if self.cheia(): 
            print('A lista esta cheia!')
        if k > self.__tamanho_atual: #teste caso a lista ainda nao tenha essa posicao ou a posicao seja maior que o tamanho maximo da lista
            print('A lista ainda tem esse tamanho!')
        if k < 0: #teste caso a posicao digitada seja negativa
            print('Posicao negativa!')
        else: #avanca com o cursor ate a posicao indicada e insere antes do nodo que atualmente ocupa essa posicao
            self.__cursor.avancarKPosicoes(k-1)
            self.inserirAntesAtual(dado)

    def excluirAtual(self): #exclui o nodo atualmente selecionado
        if self.vazia(): #caso a lista esteja vazia
            print('A lista esta vazia!')
        elif self.__tamanho_atual == 1: #caso o nodo seja o unico da lista, sera removido ambos ponterios e o cursor ira apontar para none
            self.__cursor.selecionado.posterior = None
            self.__cursor.selecionado.anterior = None
            self.__cursor.selecionado = None
            self.__tamanho_atual = 0
        elif self.__cursor.selecionado.anterior is None: #caso o nodo selecionado seja o primeiro da lista, o ponteiro posterior do nodo selecionado e o ponteiro anterior do proximo nodo serao removidos
            self.__cursor.selecionado.posterior.anterior = None
            self.__cursor.selecionado = self.__cursor.selecionado.posterior
            self.__tamanho_atual -= 1
        elif self.__cursor.selecionado.posterior is None: #caso o nodo selecionado seja o ultimo da lista, o ponteiro anterior e o ponteiro posterior do nodo de tras serao removidos
            self.__cursor.selecionado.anterior.posterior = None
            self.__cursor.selecionado = self.__cursor.selecionado.anterior
            self.__tamanho_atual -= 1
        else: #caso o nodo selecionado esteja entre dois nodos, o ponteiro posterior do nodo de tras ira marcar o nodo posterior do nodo selecionado, e o ponteiro anterior do nodo da frente ira marcar o nodo anterior do selecionado
            self.__cursor.selecionado.anterior.posterior = self.__cursor.selecionado.posterior
            self.__cursor.selecionado.posterior.anterior = self.__cursor.selecionado.anterior
            self.__cursor.selecionado = self.__cursor.selecionado.posterior
            self.__tamanho_atual -= 1

    def excluirPrim(self): #leva o cursor para o inicio e o exclui pelo metodo exclui atual
        self.__cursor.irParaPrimeiro()
        self.excluirAtual()

    def excluirUlt(self):  #leva o cursor para o fim e o exclui pelo metodo exclui atual
        self.__cursor.irParaUltimo()
        self.excluirAtual()

    def excluirElem(self, dado): #busca o dado pelo metodo que seleciona no cursor o item desejado caso exista, e entao usa o metodo exclui atual
        self.Buscar(dado)
        self.excluirAtual()
        print('Nodo removido')

    def excluirDaPos(self, k): #leva o cursor ao inicio, entao avanca os nodos necessarios para chegar a posicao desejada, entao usa o metodo exclui atual
        self.__cursor.irParaPrimeiro()
        k = k - 1
        if self.vazia():
            print('A lista esta vazia!')
        if k > self.__tamanho_atual or k < 0:
            print('Posicao inexistente!')
        else:
            self.__cursor.avancarKPosicoes(k)
            self.excluirAtual()

    def vazia(self): #retorna boolean caso a lista esteja vazia
        return self.__tamanho_atual == 0

    def cheia(self): #retorna boolean caso a lista esteja cheia
        return self.__tamanho_atual == self.__tamanho_max

    def contem(self, dado): #reutiliza o metodo buscar
        self.Buscar(dado)

    def posicaoDe(self, dado): #acha a posicao numerica na lista do nodo desejado 
        if self.vazia():
            print('A lista esta vazia!')
        else: 
            self.__cursor.irParaPrimeiro() #leva o cursor ao inicio, e uttiliza um contador para posicao
            atual = self.__cursor.selecionado
            posicao = 1

            while atual.dado != dado: #loop que checa se o  dado desejado e o mesmo do atualmente selecionado pelo cursor
                if self.__cursor.selecionado.posterior is None: #caso chegue ao final da lista e o nodo proximo sera none, encerra a busca pois nao existe tal dado na lista
                    print('Dado nao encontrado!')
                    return None
                else: #avanca uma posical no cursor e conta +1 para o contador da posicao
                    self.__cursor.avancarKPosicoes(1)
                    atual = self.__cursor.selecionado
                    posicao = posicao + 1
            print('O dado esta na posicao ' , posicao) #caso tenha encontrado utiliza o print para mostrar a posicao
            return posicao

    def Buscar(self, dado): #busca por um dado na lista, retornando boolean
        self.__cursor.irParaPrimeiro() #leva o cursor para a primeira posicao
        atual = self.__cursor.selecionado

        while atual.dado != dado: #loop que checa se o  dado desejado e o mesmo do atualmente selecionado pelo cursor
            if self.__cursor.selecionado.posterior is None:  #caso chegue ao final da lista e o nodo proximo sera none, encerra a busca pois nao existe tal dado na lista
                print('False')
                return False
            else: #avanca uma posicao no curosr
                self.__cursor.avancarKPosicoes(1)
                atual = self.__cursor.selecionado
            
        print('True') #caso tenha encontrado utiliza o print para mostrar o boolean
        return True