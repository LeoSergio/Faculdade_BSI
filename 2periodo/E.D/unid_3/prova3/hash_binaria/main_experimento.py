# O TESTE (Lê CSVs, roda as 3 operações e gera .res)
import time
import csv
import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hash_binaria import HashBinaria

def salvar_resultado(nome_arq, tempos):
    caminho = os.path.join('..', 'resultados', nome_arq)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'w') as f:
        f.write(f"HashBinaria;{len(tempos)}\n")
        for t in tempos:
            f.write(f"{t:.8f}\n")
    print(f"Salvo: {caminho}")

def executar():
    tabela = HashBinaria(tamanho=100) # Tamanho pequeno para forçar o uso das árvores
    
    # 1. INSERÇÃO
    print("Iniciando Inserção (Hash Binária)...")
    tempos = []
    with open('../csv/inscricao.csv', 'r') as f:
        reader = csv.reader(f)
        for linha in reader:
            cpf = linha[0]
            dados = linha
            
            inicio = time.perf_counter()
            tabela.inserir(cpf, dados)
            fim = time.perf_counter()
            tempos.append((fim - inicio) * 1000)
    salvar_resultado('hash_binaria_insercao.res', tempos)

    # 2. BUSCA
    print("Iniciando Busca (Hash Binária)...")
    tempos = []
    with open('../csv/busca.csv', 'r') as f:
        reader = csv.reader(f)
        for linha in reader:
            cpf = linha[0]
            
            inicio = time.perf_counter()
            tabela.buscar(cpf)
            fim = time.perf_counter()
            tempos.append((fim - inicio) * 1000)
    salvar_resultado('hash_binaria_busca.res', tempos)

    # 3. REMOÇÃO
    print("Iniciando Remoção (Hash Binária)...")
    tempos = []
    with open('../csv/remocao.csv', 'r') as f:
        reader = csv.reader(f)
        for linha in reader:
            cpf = linha[0]
            
            inicio = time.perf_counter()
            tabela.remover(cpf)
            fim = time.perf_counter()
            tempos.append((fim - inicio) * 1000)
    salvar_resultado('hash_binaria_remocao.res', tempos)

if __name__ == "__main__":
    executar()