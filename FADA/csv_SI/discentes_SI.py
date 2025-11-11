import pandas as pd
import os
import re

# ==============================================================================
# FUNÇÃO DE FILTRAGEM (PERMANECE IGUAL, POIS É EXCELENTE E REUTILIZÁVEL)
# ==============================================================================
def filtrar_alunos_por_id_curso(arquivo_csv, id_curso='7191770.0', coluna_id_curso='id_curso'): 
    """
    Filtra alunos por ID do curso a partir de um único arquivo CSV.
    É robusta a diferentes formatos de CSV (separador, codificação).
    Retorna um DataFrame do pandas.
    """
    try:
        # Tenta diferentes configurações de leitura
        configs = [
            {'encoding': 'utf-8', 'sep': ','},
            {'encoding': 'utf-8', 'sep': ';'},
            {'encoding': 'latin-1', 'sep': ','},
            {'encoding': 'latin-1', 'sep': ';'},
            {'encoding': 'cp1252', 'sep': ','},
            {'encoding': 'cp1252', 'sep': ';'},
            {'encoding': 'utf-8', 'sep': ',', 'on_bad_lines': 'skip'},
            {'encoding': 'utf-8', 'sep': ';', 'on_bad_lines': 'skip'},
        ]
        
        df = None
        
        for config in configs:
            try:
                df = pd.read_csv(arquivo_csv, **config)
                break
            except:
                continue
        
        # Se todas as tentativas falharem, tenta com engine Python
        if df is None:
            try:
                df = pd.read_csv(arquivo_csv, encoding='utf-8', sep=None, engine='python', on_bad_lines='skip')
            except:
                return pd.DataFrame()
        
        # Verifica se a coluna do ID do curso existe
        if coluna_id_curso not in df.columns:
            # Tenta encontrar coluna similar
            colunas_similares = [col for col in df.columns if any(palavra in col.lower() for palavra in ['id_curso', 'idcurso', 'curso_id', 'cod_curso', 'codigo_curso'])]
            if colunas_similares:
                coluna_id_curso = colunas_similares[0]
            else:
                return pd.DataFrame()
        
        # Converte a coluna para string para garantir a comparação correta e filtra
        df[coluna_id_curso] = df[coluna_id_curso].astype(str).str.strip()
        mask = df[coluna_id_curso] == str(id_curso)
        alunos_filtrados = df[mask].copy()
        
        return alunos_filtrados
        
    except Exception:
        return pd.DataFrame()

# ==============================================================================
# TAREFA 1: GERAR CSV CONSOLIDADO PARA SITUAÇÃO DOS DISCENTES
# ==============================================================================
def gerar_csv_situacoes():
    """
    Processa a lista de arquivos de SITUAÇÃO e gera um CSV consolidado.
    """
    print("\n--- Iniciando processamento de SITUAÇÕES de discentes ---")
    ID_CURSO_SI = '7191770.0'
    
    # ATENÇÃO: ADICIONE AQUI TODOS OS SEUS ARQUIVOS DE SITUAÇÃO
    arquivos_csv_situacoes = [
        "situacao_discentes/situacoes-discentes-2012.1.csv",
        "csv/situacao_discentes/situacoes-discentes-2012.2.csv",
        # Adicione os outros arquivos de situação aqui. Ex:
        # "csv/situacao_discentes/situacoes-discentes-2013.1.csv",
        # ...
    ]
    
    todos_os_dados = []
    
    for arquivo in arquivos_csv_situacoes:
        if not os.path.exists(arquivo):
            print(f"AVISO: Arquivo não encontrado, pulando: {arquivo}")
            continue
        
        dados_filtrados = filtrar_alunos_por_id_curso(arquivo, id_curso=ID_CURSO_SI)
        
        if not dados_filtrados.empty:
            match = re.search(r'(\d{4}\.\d|\d{4})', arquivo)
            periodo = match.group(1) if match else 'desconhecido'
            dados_filtrados['periodo_arquivo'] = periodo
            todos_os_dados.append(dados_filtrados)
            print(f"  -> Processado: {arquivo} ({len(dados_filtrados)} registros encontrados)")

    if todos_os_dados:
        df_consolidado = pd.concat(todos_os_dados, ignore_index=True)
        nome_arquivo_final = "SITUACOES_ALUNOS_SISTEMAS_INFORMACAO.csv"
        df_consolidado.to_csv(nome_arquivo_final, index=False, encoding='utf-8')
        print(f"✅ Arquivo de SITUAÇÕES gerado com sucesso: '{nome_arquivo_final}' ({len(df_consolidado)} registros no total)")
    else:
        print("Nenhum registro de Sistemas de Informação encontrado nos arquivos de situação fornecidos.")

# ==============================================================================
# TAREFA 2: GERAR CSV CONSOLIDADO PARA DISCENTES EGRESSOS
# ==============================================================================
def gerar_csv_egressos():
    """
    Processa a lista de arquivos de EGRESSOS e gera um CSV consolidado.
    """
    print("\n--- Iniciando processamento de discentes EGRESSOS ---")
    ID_CURSO_SI = '7191770.0'
    
    # ATENÇÃO: ADICIONE AQUI TODOS OS SEUS ARQUIVOS DE EGRESSOS
    arquivos_csv_egressos = [
        "csv/egressos/discentes-egressos-2009.csv",
        "csv/egressos/discentes-egressos-2010.csv",
        # Adicione os outros arquivos de egressos aqui. Ex:
        # "csv/egressos/discentes-egressos-2011.csv",
        # ...
    ]
    
    todos_os_dados = []
    
    for arquivo in arquivos_csv_egressos:
        if not os.path.exists(arquivo):
            print(f"AVISO: Arquivo não encontrado, pulando: {arquivo}")
            continue

        dados_filtrados = filtrar_alunos_por_id_curso(arquivo, id_curso=ID_CURSO_SI)
        
        if not dados_filtrados.empty:
            match = re.search(r'(\d{4})', arquivo)
            ano = match.group(1) if match else 'desconhecido'
            dados_filtrados['ano_arquivo'] = ano
            todos_os_dados.append(dados_filtrados)
            print(f"  -> Processado: {arquivo} ({len(dados_filtrados)} registros encontrados)")

    if todos_os_dados:
        df_consolidado = pd.concat(todos_os_dados, ignore_index=True)
        nome_arquivo_final = "EGRESSOS_SISTEMAS_INFORMACAO.csv"
        df_consolidado.to_csv(nome_arquivo_final, index=False, encoding='utf-8')
        print(f"✅ Arquivo de EGRESSOS gerado com sucesso: '{nome_arquivo_final}' ({len(df_consolidado)} registros no total)")
    else:
        print("Nenhum registro de Sistemas de Informação encontrado nos arquivos de egressos fornecidos.")

# ==============================================================================
# BLOCO DE EXECUÇÃO PRINCIPAL
# ==============================================================================
if __name__ == "__main__":
    gerar_csv_situacoes()
    gerar_csv_egressos()
    print("\nProcessamento concluído.")