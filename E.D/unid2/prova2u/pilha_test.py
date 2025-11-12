import time
import os
from estruturas import StackArray, StackLinkedList

# --- FUNÇÃO AUXILIAR PARA SALVAR ARQUIVOS .RES ---
def salvar_resultados(nome_arquivo, nome_algoritmo, n, tempos):
    if not os.path.exists('resultados'):
        os.makedirs('resultados')
    caminho = os.path.join('resultados', nome_arquivo)
    try:
        with open(caminho, "w") as f:
            f.write(f"{nome_algoritmo};{n}\n")
            for t in tempos:
                f.write(f"{t}\n")
        print(f"Resultados salvos com sucesso em: {caminho}")
    except Exception as e:
        print(f"Erro ao salvar o arquivo {caminho}: {e}")

# --- PARÂMETROS DO EXPERIMENTO ---
N_OPERACOES = 950

def rodar_experimento_pilha():
    print("--- Iniciando Experimentos da PILHA ---")
    
    # 1. Teste StackArray
    pilha_arr = StackArray()
    tempos_push = []
    tempos_pop = []
    
    print("Testando StackArray Push...")
    for i in range(N_OPERACOES):
        inicio = time.perf_counter()
        pilha_arr.push(i)
        fim = time.perf_counter()
        tempos_push.append((fim - inicio) * 1000)
    
    print("Testando StackArray Pop...")
    for _ in range(N_OPERACOES):
        inicio = time.perf_counter()
        pilha_arr.pop()
        fim = time.perf_counter()
        tempos_pop.append((fim - inicio) * 1000)
        
    # Salvar resultados StackArray
    salvar_resultados("pilha_array_adicionar.res", "PilhaArray_Push", N_OPERACOES, tempos_push)
    salvar_resultados("pilha_array_remover.res", "PilhaArray_Pop", N_OPERACOES, tempos_pop)
    salvar_resultados("pilha_array_aumentar.res", "PilhaArray_Aumentar", len(pilha_arr.tempos_aumentar), pilha_arr.tempos_aumentar)
    salvar_resultados("pilha_array_diminuir.res", "PilhaArray_Diminuir", len(pilha_arr.tempos_diminuir), pilha_arr.tempos_diminuir)

    # 2. Teste StackLinkedList
    pilha_ll = StackLinkedList()
    tempos_push_ll = []
    tempos_pop_ll = []

    print("Testando StackLinkedList Push...")
    for i in range(N_OPERACOES):
        inicio = time.perf_counter()
        pilha_ll.push(i)
        fim = time.perf_counter()
        tempos_push_ll.append((fim - inicio) * 1000)
    
    print("Testando StackLinkedList Pop...")
    for _ in range(N_OPERACOES):
        inicio = time.perf_counter()
        pilha_ll.pop()
        fim = time.perf_counter()
        tempos_pop_ll.append((fim - inicio) * 1000)
        
    # Salvar resultados StackLinkedList
    salvar_resultados("pilha_ll_adicionar.res", "PilhaLL_Push", N_OPERACOES, tempos_push_ll)
    salvar_resultados("pilha_ll_remover.res", "PilhaLL_Pop", N_OPERACOES, tempos_pop_ll)
    
    print("--- Experimentos da PILHA concluídos! ---")

if __name__ == "__main__":
    rodar_experimento_pilha()