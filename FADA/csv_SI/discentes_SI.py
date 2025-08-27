import pandas as pd
import os

def diagnosticar_csv(arquivo_csv):
    print(f"\n=== DIAGNÓSTICO DO ARQUIVO {arquivo_csv} ===")
    
    try:
        with open(arquivo_csv, 'rb') as f:
            primeiros_bytes = f.read(100)
            print(f"Primeiros bytes (raw): {primeiros_bytes}")
        
        with open(arquivo_csv, 'r', encoding='utf-8', errors='ignore') as f:
            linhas = []
            for i, linha in enumerate(f):
                if i < 5:  # Mostra as primeiras 5 linhas
                    linhas.append(linha.strip())
                else:
                    break
            
            print(f"\nPrimeiras {len(linhas)} linhas:")
            for i, linha in enumerate(linhas, 1):
                print(f"Linha {i}: {linha[:100]}{'...' if len(linha) > 100 else ''}")
                
                # Conta separadores comuns
                separadores = [',', ';', '\t', '|']
                contagens = {sep: linha.count(sep) for sep in separadores}
                if any(count > 0 for count in contagens.values()):
                    print(f"         Separadores: {contagens}")
        
        # Tenta detectar encoding
        encodings = ['utf-8', 'latin-1', 'cp1252', 'iso-8859-1']
        for enc in encodings:
            try:
                with open(arquivo_csv, 'r', encoding=enc) as f:
                    f.read(1000)  # Lê os primeiros 1000 caracteres
                print(f"✓ Encoding '{enc}' funciona")
            except UnicodeDecodeError:
                print(f"✗ Encoding '{enc}' falhou")
    
    except Exception as e:
        print(f"Erro no diagnóstico: {e}")


def filtrar_alunos_por_id_curso(arquivo_csv, id_curso='7191770.0', coluna_id_curso='id_curso', salvar_resultado_individual=False, diagnosticar=False): 
    """
    Filtra alunos por ID do curso (Sistemas de Informação = 7191770.0)
    """
    if diagnosticar:
        diagnosticar_csv(arquivo_csv)
    
    try:
        print(f"Lendo arquivo: {arquivo_csv}")
        
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
                print(f"Tentando com: encoding={config.get('encoding')}, separador='{config.get('sep')}'")
                df = pd.read_csv(arquivo_csv, **config)
                print(f"✓ Sucesso com configuração: {config}")
                break
            except Exception as e:
                print(f"✗ Falhou: {e}")
                continue
        
        if df is None:
            try:
                print("Tentando com engine Python (mais tolerante)...")
                df = pd.read_csv(arquivo_csv, encoding='utf-8', sep=None, engine='python', on_bad_lines='skip')
                print("✓ Sucesso com engine Python")
            except Exception as e:
                print(f"✗ Engine Python também falhou: {e}")
                return pd.DataFrame()
        
        if df is None:
            raise Exception("Não foi possível ler o arquivo CSV com nenhuma configuração")
        
        print(f"\nDataset carregado com sucesso!")
        print(f"Total de registros: {len(df)}")
        print(f"Colunas disponíveis: {list(df.columns)}")
        
        # Verifica se a coluna do ID do curso existe
        if coluna_id_curso not in df.columns:
            print(f"\nAviso: Coluna '{coluna_id_curso}' não encontrada.")
            print("Colunas disponíveis:")
            for i, col in enumerate(df.columns, 1):
                print(f"{i}. {col}")
            
            # Tenta encontrar coluna similar para ID do curso
            colunas_similares = [col for col in df.columns if any(palavra in col.lower() for palavra in ['id_curso', 'idcurso', 'curso_id', 'cod_curso', 'codigo_curso'])]
            if colunas_similares:
                coluna_id_curso = colunas_similares[0]
                print(f"Usando coluna similar para ID: '{coluna_id_curso}'")
            else:
                # Tenta encontrar qualquer coluna numérica que possa ser o ID
                for col in df.columns:
                    if df[col].dtype in ['int64', 'float64']:
                        coluna_id_curso = col
                        print(f"Usando coluna numérica: '{coluna_id_curso}'")
                        break
                else:
                    coluna_id_curso = df.columns[0]
                    print(f"Usando primeira coluna: '{coluna_id_curso}'")
        
        # Converte a coluna para string para garantir a comparação
        df[coluna_id_curso] = df[coluna_id_curso].astype(str).str.strip()
        
        # Filtra os alunos pelo ID do curso (Sistemas de Informação)
        mask = df[coluna_id_curso] == str(id_curso)
        alunos_si = df[mask].copy()
        
        print(f"\n--- RESULTADOS ---")
        print(f"Alunos de Sistemas de Informação (ID {id_curso}) encontrados: {len(alunos_si)}")
        
        if len(alunos_si) == 0:
            print(f"\nIDs de curso únicos encontrados no dataset (amostra):")
            ids_unicos = df[coluna_id_curso].unique()[:20]  # Mostra apenas os primeiros 20
            for curso_id in sorted(ids_unicos):
                if pd.notna(curso_id) and str(curso_id).strip() != '' and str(curso_id).strip() != 'nan':
                    print(f"  - ID: {curso_id}")
            
            print(f"\nNenhum aluno com ID de curso {id_curso} encontrado.")
            return pd.DataFrame()
        
        print(f"Percentual do total: {(len(alunos_si)/len(df)*100):.1f}%")
        
        # Salva resultado individual apenas se solicitado
        if salvar_resultado_individual:
            nome_base = os.path.splitext(os.path.basename(arquivo_csv))[0]
            nome_arquivo = f"alunos_si_id_{id_curso}_{nome_base}.csv"
            alunos_si.to_csv(nome_arquivo, index=False, encoding='utf-8')
            print(f"\nResultado individual salvo em: {nome_arquivo}")
        
        return alunos_si
        
    except FileNotFoundError:
        print(f"Erro: Arquivo '{arquivo_csv}' não encontrado.")
        return pd.DataFrame()
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo CSV está vazio.")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro inesperado: {e}")
        return pd.DataFrame()

def analisar_dados_si(df_si, ano):
    if df_si.empty:
        print(f"Nenhum dado para analisar no ano {ano}.")
        return
    
    print(f"\n=== ANÁLISE DOS DADOS {ano} ===")
    print(f"Total de alunos de Sistemas de Informação: {len(df_si)}")
    
    colunas_interesse = ['sexo', 'genero', 'idade', 'periodo', 'semestre', 'status', 'situacao', 'matricula', 'ano_ingresso']
    
    for coluna in colunas_interesse:
        colunas_similares = [col for col in df_si.columns if coluna.lower() in col.lower()]
        
        if colunas_similares:
            coluna_encontrada = colunas_similares[0]
            print(f"\n{coluna_encontrada.upper()}:")
            contagem = df_si[coluna_encontrada].value_counts().head(10)
            for valor, qtd in contagem.items():
                if pd.notna(valor) and str(valor).strip() != '':
                    print(f"  {valor}: {qtd} ({qtd/len(df_si)*100:.1f}%)")


if __name__ == "__main__":
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
    
    # Lista para armazenar todos os alunos de SI
    todos_alunos_si = []
    
    for arquivo in arquivos_csv:
        if not os.path.exists(arquivo):
            print(f"⚠️  Arquivo '{arquivo}' não encontrado. Pulando...")
            continue
        
        print(f"\n{'='*60}")
        print(f"PROCESSANDO: {arquivo}")
        print(f"{'='*60}")
        
        try:
            # Extrai o ano do nome do arquivo
            try:
                ano = int(arquivo.split('_')[1].split('.')[0])
            except:
                ano = "desconhecido"
            
            # Filtra alunos de SI pelo ID - NÃO salva arquivo individual
            alunos_si_ano = filtrar_alunos_por_id_curso(
                arquivo, 
                id_curso=ID_CURSO_SI,
                coluna_id_curso='id_curso',
                salvar_resultado_individual=False,  # Não salva individual
                diagnosticar=True
            )
            
            if not alunos_si_ano.empty:
                # Adiciona coluna com o ano de origem
                alunos_si_ano['ano_arquivo'] = ano
                todos_alunos_si.append(alunos_si_ano)
                
                # Faz análise individual
                analisar_dados_si(alunos_si_ano, ano)

        except Exception as e:
            print(f"Erro ao processar {arquivo}: {e}")
            continue

    # --- CONSOLIDA TODOS OS DADOS ---
    if todos_alunos_si:
        print(f"\n{'='*60}")
        print("CONSOLIDANDO TODOS OS DADOS DE SISTEMAS DE INFORMAÇÃO...")
        
        # Junta todos os DataFrames
        df_consolidado = pd.concat(todos_alunos_si, ignore_index=True)
        
        # Salva o arquivo consolidado
        nome_arquivo_final = f"TODOS_ALUNOS_SISTEMAS_INFORMACAO_ID_{ID_CURSO_SI}.csv"
        df_consolidado.to_csv(nome_arquivo_final, index=False, encoding='utf-8')
        
        print(f"✅ CONSOLIDAÇÃO CONCLUÍDA!")
        print(f"Total de alunos de SI encontrados: {len(df_consolidado)}")
        print(f"Arquivo consolidado salvo como: {nome_arquivo_final}")
        print(f"\nResumo por ano:")
        print(df_consolidado['ano_arquivo'].value_counts().sort_index())
        
        # Mostra informações finais
        print(f"\nColunas no arquivo final: {list(df_consolidado.columns)}")
        
    else:
        print(f"\n❌ Nenhum aluno de Sistemas de Informação (ID {ID_CURSO_SI}) foi encontrado em nenhum dos arquivos.")