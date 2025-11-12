import time
import os
from estruturas import QueueArray, QueueLinkedList

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
N_OPERACOES = 950

def rodar_experimento_fila():
    print("--- Iniciando Experimentos da FILA ---")
    
    # 1. Teste QueueArray
    fila_arr = QueueArray()
    tempos_enqueue = []
    tempos_dequeue = []
    
    print("Testando QueueArray Enqueue...")
    for i in range(N_OPERACOES):
        inicio = time.perf_counter()
        fila_arr.enqueue(i)
        fim = time.perf_counter()
        tempos_enqueue.append((fim - inicio) * 1000)
    
    print("Testando QueueArray Dequeue (O(n))...")
    for _ in range(N_OPERACOES):
        inicio = time.perf_counter()
        fila_arr.dequeue() # Esta é a operação O(n)
        fim = time.perf_counter()
        tempos_dequeue.append((fim - inicio) * 1000)
        
    # Salvar resultados QueueArray
    salvar_resultados("fila_array_adicionar.res", "FilaArray_Enqueue", N_OPERACOES, tempos_enqueue)
    salvar_resultados("fila_array_remover.res", "FilaArray_Dequeue", N_OPERACOES, tempos_dequeue)
    salvar_resultados("fila_array_aumentar.res", "FilaArray_Aumentar", len(fila_arr.tempos_aumentar), fila_arr.tempos_aumentar)
    salvar_resultados("fila_array_diminuir.res", "FilaArray_Diminuir", len(fila_arr.tempos_diminuir), fila_arr.tempos_diminuir)

    # 2. Teste QueueLinkedList
    fila_ll = QueueLinkedList()
    tempos_enqueue_ll = []
    tempos_dequeue_ll = []

    print("Testando QueueLinkedList Enqueue (O(1))...")
    for i in range(N_OPERACOES):
        inicio = time.perf_counter()
        fila_ll.enqueue(i)
        fim = time.perf_counter()
        tempos_enqueue_ll.append((fim - inicio) * 1000)
    
    print("Testando QueueLinkedList Dequeue (O(1))...")
    for _ in range(N_OPERACOES):
        inicio = time.perf_counter()
        fila_ll.dequeue()
        fim = time.perf_counter()
        tempos_dequeue_ll.append((fim - inicio) * 1000)
        
    # Salvar resultados QueueLinkedList
    salvar_resultados("fila_ll_adicionar.res", "FilaLL_Enqueue", N_OPERACOES, tempos_enqueue_ll)
    salvar_resultados("fila_ll_remover.res", "FilaLL_Dequeue", N_OPERACOES, tempos_dequeue_ll)
    
    print("--- Experimentos da FILA concluídos! ---")

if __name__ == "__main__":
    rodar_experimento_fila()