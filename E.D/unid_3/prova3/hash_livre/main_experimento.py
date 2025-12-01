#O TESTE (Lê CSVs, roda as 3 operações em sequência e gera .res)
import time
import csv
import os
import sys

# Adiciona o diretório pai ao path para importar módulos se necessário
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from hash_livre import HashLivre

def salvar_resultado(nome_arq, tempos):
    caminho = os.path.join('..', 'resultados', nome_arq)
    os.makedirs(os.path.dirname(caminho), exist_ok=True)
    with open(caminho, 'w') as f:
        f.write(f"HashLivre;{len(tempos)}\n")
        for t in tempos:
            f.write(f"{t:.8f}\n")
    print(f"Salvo: {caminho}")

def executar():
    tabela = HashLivre()
    
    # 1. INSERÇÃO
    print("Iniciando Inserção (Hash Livre)...")
    tempos = []
    with open('../csv/insercao.csv', 'r') as f:
        reader = csv.reader(f)
        # next(reader) # Descomente se o CSV tiver cabeçalho
        for linha in reader:
            cpf = linha[0]
            dados = linha # Guarda a linha toda como dados
            
            inicio = time.perf_counter()
            tabela.inserir(cpf, dados)
            fim = time.perf_counter()
            tempos.append((fim - inicio) * 1000) # ms
    salvar_resultado('hash_livre_insercao.res', tempos)

    # 2. BUSCA
    print("Iniciando Busca (Hash Livre)...")
    tempos = []
    with open('../csv/busca.csv', 'r') as f:
        reader = csv.reader(f)
        for linha in reader:
            cpf = linha[0]
            
            inicio = time.perf_counter()
            tabela.buscar(cpf)
            fim = time.perf_counter()
            tempos.append((fim - inicio) * 1000)
    salvar_resultado('hash_livre_busca.res', tempos)

    # 3. REMOÇÃO
    print("Iniciando Remoção (Hash Livre)...")
    tempos = []
    with open('../csv/remocao.csv', 'r') as f:
        reader = csv.reader(f)
        for linha in reader:
            cpf = linha[0]
            
            inicio = time.perf_counter()
            tabela.remover(cpf)
            fim = time.perf_counter()
            tempos.append((fim - inicio) * 1000)
    salvar_resultado('hash_livre_remocao.res', tempos)

if __name__ == "__main__":
    executar()