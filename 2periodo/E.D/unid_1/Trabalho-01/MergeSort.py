"""
Algoritmo MergeSort 
Código do MergeSort comentado e com print de auxílio
Autor: Arthur Souza
Adaptado de https://panda.ime.usp.br/panda/static/pythonds_pt/05-OrdenacaoBusca/OMergeSort.html
"""
def mergeSortRec(lista):
    # Caso a lista tenha uma posição, está ordenada
    if len(lista) <= 1:
        return lista

    # Divide a lista ao meio
    meio = len(lista) // 2
    listaEsqueda = lista[:meio]
    listaDireita = lista[meio:]
    
    # Ordena as metades recursivamente
    listaEsqueda = mergeSortRec(listaEsqueda)
    listaDireita = mergeSortRec(listaDireita)

    # Combina as metades da lista
    return merge(listaEsqueda, listaDireita)

def mergeListas(listas):
    lista = []
    for i in range(0, len(listas) // 2):
        lista.append(merge(listas[i*2], listas[i*2 + 1]))
    if len(listas) % 2:
        lista.append(listas[-1])
    return lista

def mergeSortIterativo(lista):
    '''
    MergeSort Bottom-UP
    Adaptado de https://akiradev.netlify.app/posts/algoritmo-merge-sort/
    '''
    # Cria uma lista com sublistas de um elemento
    listas = []
    for x in lista:
        listas.append([x])

    # Cria combina as listas
    while len(listas) > 1:
        listas = mergeListas(listas)
    return listas[0]

def merge(listaEsquerda, listaDireita):
    listaCombinada = []
    indiceEsquerdo = 0  # Indica o elemento da lista esquerda
    indiceDireito = 0  # Indica o elemento da lista direita

    # Compara os elementos das listas, selecionando o menor e incluindo na lista combinada
    while indiceEsquerdo < len(listaEsquerda) and indiceDireito < len(listaDireita):
        if listaEsquerda[indiceEsquerdo] < listaDireita[indiceDireito]:
            listaCombinada.append(listaEsquerda[indiceEsquerdo])
            indiceEsquerdo += 1
        else:
            listaCombinada.append(listaDireita[indiceDireito])
            indiceDireito += 1
    # Adiciona elementos restantes da lista esquerda
    while indiceEsquerdo < len(listaEsquerda):
        listaCombinada.append(listaEsquerda[indiceEsquerdo])
        indiceEsquerdo += 1

    # Adiciona elementos restantes da lista direita
    while indiceDireito < len(listaDireita):
        listaCombinada.append(listaDireita[indiceDireito])
        indiceDireito += 1

    return listaCombinada


if __name__ == "__main__":
    lista = [3,2,8,1,5]
    #listaOrdenada = mergeSortRec(lista)
    listaOrdenada = mergeSortIterativo(lista)
    print(f"Ordenada: {listaOrdenada}")