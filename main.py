from Lista import Lista_Encadeada

Lista = Lista_Encadeada(10) #lista definida com tamanho variavel, sendo definida como  de 10 itens


print('INICIO--Teste de excluir vazio')

print('teste 0')
Lista.excluirPrim()
print('teste 1')
Lista.excluirUlt()
print('teste 2')
Lista.excluirElem(10)
print('teste 3')
Lista.excluirDaPos(3)
print('teste 4')
Lista.excluirAtual()


print('1--Teste de sobrecarregar a lista em 3')
print('teste 0')
Lista.inserirFim(12)
print('teste 1')
Lista.inserirFrente(10)
print('teste 2')
Lista.inserirNaPosicao(2, 11)
print('teste 3')
Lista.inserirPosAtual(22)
print('teste 4')
Lista.inserirFim(31)
print('teste 5')
Lista.inserirFrente(15)
print('teste 6')
Lista.inserirNaPosicao(2, 17)
print('teste 7')
Lista.inserirPosAtual(12)
print('teste 8')
Lista.inserirFrente(15)
print('teste 9')
Lista.inserirNaPosicao(2, 17)
print('teste 10')
Lista.inserirPosAtual(12)
print('teste 11')
Lista.inserirPosAtual(12)
print('teste 12')
Lista.inserirPosAtual(12)

print('2--Teste de buscas')
print('teste 0')
Lista.Buscar(10)
Lista.posicaoDe(10)
print('teste 1')
Lista.Buscar(12)
Lista.posicaoDe(12)

print('3--Teste de cheio/vazio')
print(Lista.tamanho_atual())
print (Lista.cheia())
print (Lista.vazia())

print('FIM--excluir itens')
print('teste 0')
Lista.excluirPrim()
print('teste 1')
Lista.excluirUlt()
print('teste 2')
Lista.excluirElem(10)
print('teste 3')
Lista.excluirDaPos(3)
print('teste 4')
Lista.excluirAtual()

