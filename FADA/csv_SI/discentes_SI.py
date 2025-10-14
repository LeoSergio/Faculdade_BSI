import pandas as pd
import os

def filtrar_alunos_por_id_curso(arquivo_csv, id_curso='7191770.0', coluna_id_curso='id_curso'): 
    """
    Filtra alunos por ID do curso (Sistemas de Informação = 7191770.0)
    Retorna DataFrame vazio se não conseguir processar
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
                # Se não encontrar, retorna vazio
                return pd.DataFrame()
        
        # Converte a coluna para string e filtra
        df[coluna_id_curso] = df[coluna_id_curso].astype(str).str.strip()
        mask = df[coluna_id_curso] == str(id_curso)
        alunos_si = df[mask].copy()
        
        return alunos_si
        
    except Exception:
        return pd.DataFrame()

def gerar_csv_consolidado():
    """
    Função principal que gera o CSV consolidado sem mensagens no terminal
    Retorna True se bem-sucedido, False caso contrário
    """
    # ID do curso de Sistemas de Informação
    ID_CURSO_SI = '7191770.0'
    
    # Lista de arquivos para processar
    arquivos_csv = [
        "csv/discentes_2009.csv",
        "csv/discentes_2010.csv", 
        "csv/discentes_2011.csv",
        "csv/discentes_2012.csv",
        "csv/discentes_2013.csv",
        "csv/discentes_2014.csv",
        "csv/discentes_2015.csv",
        "csv/discentes_2016.csv",
        "csv/discentes_2017.csv",
        "csv/discentes_2018.csv",
        "csv/discentes_2019.csv",
        "csv/discentes_2020.csv",
        "csv/discentes_2021.csv",
        "csv/discentes_2022.csv",
        "csv/discentes_2023.csv",
        "csv/discentes_2024.csv"
    ]
    
    todos_alunos_si = []
    arquivos_processados = 0
    arquivos_com_erro = 0
    
    for arquivo in arquivos_csv:
        if not os.path.exists(arquivo):
            arquivos_com_erro += 1
            continue
        
        try:
            # Extrai o ano do nome do arquivo
            ano = int(arquivo.split('_')[1].split('.')[0])
            
            # Filtra alunos de SI
            alunos_si_ano = filtrar_alunos_por_id_curso(
                arquivo, 
                id_curso=ID_CURSO_SI,
                coluna_id_curso='id_curso'
            )
            
            if not alunos_si_ano.empty:
                # Adiciona coluna com o ano de origem
                alunos_si_ano['ano_arquivo'] = ano
                todos_alunos_si.append(alunos_si_ano)
                arquivos_processados += 1
        
        except Exception:
            arquivos_com_erro += 1
            continue

    # Consolida todos os dados
    if todos_alunos_si:
        try:
            df_consolidado = pd.concat(todos_alunos_si, ignore_index=True)
            
            # Salva o arquivo consolidado
            nome_arquivo_final = f"TODOS_ALUNOS_SISTEMAS_INFORMACAO_ID_123{ID_CURSO_SI}.csv"
            df_consolidado.to_csv(nome_arquivo_final, index=False, encoding='utf-8')
            
            # Única mensagem permitida
            print(f"CSVs lidos com sucesso: {arquivos_processados} arquivos processados, {len(df_consolidado)} alunos encontrados")
            return True
            
        except Exception:
            print("Erro ao consolidar os dados")
            return False
    else:
        print("Nenhum arquivo CSV foi lido com sucesso")
        return False

# Executa a função
if __name__ == "__main__":
    gerar_csv_consolidado()