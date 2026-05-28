import time
import os
from estruturas import ListArray, ListLinkedList

# --- (Copie a mesma função 'salvar_resultados' do script da pilha aqui) ---
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
N_OPERACOES = 950 # Use um N menor para Lista (ex: 950), pois O(n^2) é lento
POSICAO_TESTE = 0 # Teste do Pior Caso: Inserir/Remover sempre no início

def rodar_experimento_lista():
    print(f"--- Iniciando Experimentos da LISTA (Pior Caso, pos={POSICAO_TESTE}) ---")
    
    # 1. Teste ListArray
    lista_arr = ListArray()
    tempos_inserir = []
    tempos_remover = []
    
    print("Testando ListArray Inserir (O(n))...")
    for i in range(N_OPERACOES):
        inicio = time.perf_counter()
        lista_arr.inserir(POSICAO_TESTE, i) # Pior Caso
        fim = time.perf_counter()
        tempos_inserir.append((fim - inicio) * 1000)
    
    print("Testando ListArray Remover (O(n))...")
    for _ in range(N_OPERACOES):
        inicio = time.perf_counter()
        lista_arr.remover(POSICAO_TESTE) # Pior Caso
        fim = time.perf_counter()
        tempos_remover.append((fim - inicio) * 1000)
        
    # Salvar resultados ListArray
    salvar_resultados("lista_array_adicionar.res", "ListaArray_Inserir_Inicio", N_OPERACOES, tempos_inserir)
    salvar_resultados("lista_array_remover.res", "ListaArray_Remover_Inicio", N_OPERACOES, tempos_remover)
    salvar_resultados("lista_array_aumentar.res", "ListaArray_Aumentar", len(lista_arr.tempos_aumentar), lista_arr.tempos_aumentar)
    salvar_resultados("lista_array_diminuir.res", "ListaArray_Diminuir", len(lista_arr.tempos_diminuir), lista_arr.tempos_diminuir)

    # 2. Teste ListLinkedList
    lista_ll = ListLinkedList()
    tempos_inserir_ll = []
    tempos_remover_ll = []

    print("Testando ListLinkedList Inserir (O(1))...")
    for i in range(N_OPERACOES):
        inicio = time.perf_counter()
        lista_ll.inserir_pos(POSICAO_TESTE, i) # Melhor Caso
        fim = time.perf_counter()
        tempos_inserir_ll.append((fim - inicio) * 1000)
    
    print("Testando ListLinkedList Remover (O(1))...")
    for _ in range(N_OPERACOES):
        inicio = time.perf_counter()
        lista_ll.remover_pos(POSICAO_TESTE) # Melhor Caso
        fim = time.perf_counter()
        tempos_remover_ll.append((fim - inicio) * 1000)
        
    # Salvar resultados ListLinkedList
    salvar_resultados("lista_ll_adicionar.res", "ListaLL_Inserir_Inicio", N_OPERACOES, tempos_inserir_ll)
    salvar_resultados("lista_ll_remover.res", "ListaLL_Remover_Inicio", N_OPERACOES, tempos_remover_ll)
    
    print("--- Experimentos da LISTA concluídos! ---")

if __name__ == "__main__":
    rodar_experimento_lista()