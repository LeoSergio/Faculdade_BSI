'''
Algoritmo QuickSort com Particionamento Lomuto
Adaptado do material em https://joaoarthurbm.github.io/eda/posts/quick-sort/
'''

def trocarPosicao(lista, indiceI, indiceJ):
    temp = lista[indiceJ]
    lista[indiceJ] = lista[indiceI]
    lista[indiceI] = temp

def particao(lista, esquerda, direita):
    pivot = lista[esquerda]
    fronteira = esquerda
    for i in range(esquerda+1,direita+1):
        if(lista[i] <= pivot):
            fronteira += 1
            trocarPosicao(lista,i,fronteira)
    trocarPosicao(lista,esquerda,fronteira)
    return fronteira

def quickSortAux(lista,esquerda,direita):
    if(esquerda < direita):
        indexPivot = particao(lista,esquerda,direita)
        quickSortAux(lista,esquerda, indexPivot - 1)
        quickSortAux(lista,indexPivot+1,direita)

def quickSort(lista):
    quickSortAux(lista,0,len(lista)-1)

def quickSortIterative(lista):
    quickSortIterativeAux(lista,0,len(lista)-1)


def quickSortIterativeAux(lista, esq, dir):
    '''
    Copiado de https://www.geeksforgeeks.org/dsa/iterative-quick-sort/
    '''
    # Create an auxiliary stack
    tamanho = dir - esq + 1
    listaAuxiliar = [0] * (tamanho)

    # initialize top of stack
    inicio = -1

    # push initial values of l and h to stack
    inicio = inicio + 1
    listaAuxiliar[inicio] = esq
    inicio = inicio + 1
    listaAuxiliar[inicio] = dir

    # Keep popping from stack while is not empty
    while inicio >= 0:

        # Pop h and l
        dir = listaAuxiliar[inicio]
        inicio = inicio - 1
        esq = listaAuxiliar[inicio]
        inicio = inicio - 1

        # Set pivot element at its correct position in
        # sorted array
        p = particao( lista, esq, dir )

        # If there are elements on left side of pivot,
        # then push left side to stack
        if p-1 > esq:
            inicio = inicio + 1
            listaAuxiliar[inicio] = esq
            inicio = inicio + 1
            listaAuxiliar[inicio] = p - 1

        # If there are elements on right side of pivot,
        # then push right side to stack
        if p + 1 < dir:
            inicio = inicio + 1
            listaAuxiliar[inicio] = p + 1
            inicio = inicio + 1
            listaAuxiliar[inicio] = dir

if __name__ == "__main__":
    #lista = [1, 3, 5, 2, 1, 3, 2, 3]
    lista = [1,2,3,4,5,6]
    n = len(lista)
    quickSortIterative(lista)
    #quickSort(lista, 0, n-1)
    print(lista)