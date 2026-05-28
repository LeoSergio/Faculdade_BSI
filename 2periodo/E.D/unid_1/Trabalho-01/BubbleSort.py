'''
Códigos dos algoritmos BubbleSort 
autor: Arthur Souza, copiado ou adaptado do livro: Fundamentos os Python, Estrutura de Dados    
'''

def trocarPosicao(lista, indiceI, indiceJ):
    '''
    Troca itens de posição dentro da lista
    '''
    temp = lista[indiceJ]
    lista[indiceJ] = lista[indiceI]
    lista[indiceI] = temp

def bubbleSort(lista):
    '''
    BubbleSort iterativo
    '''
    n = len(lista)
    while n > 1:
        i = 1
        while i < n:
            #print(f'i: {i}, n: {n}')
            if lista[i] < lista[i - 1]:
                trocarPosicao(lista, i, i - 1)
            i += 1
        n -= 1
    return lista

def bubbleSortRec(lista, n=0):
    '''
    BubbleSort Recursivo
    '''
    if n == 0: n = len(lista)
    if n <= 1:
        return lista
    else:
        i = 1
        while i < n:
            #print(f'i: {i}, n: {n}')
            if lista[i] < lista[i - 1]:
                trocarPosicao(lista, i, i - 1)
            i += 1
        return bubbleSortRec(lista,n-1)

def bubbleSortBest(lista):
    '''
    BubbleSort otimizado para melhor caso
    '''
    n = len(lista)
    for i in range(n):
        trocou = False
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                trocarPosicao(lista,i,j)
                trocou = True
        if not trocou:
            break
    return lista

        
if __name__ == "__main__":
    lista = [3,2,8,1,5]
    print(bubbleSort(lista))