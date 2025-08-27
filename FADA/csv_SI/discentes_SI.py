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


def filtrar_alunos_sistema_informacao(arquivo_csv, coluna_curso='nome_curso', salvar_resultado=True, diagnosticar=False): 
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
        config_usada = None
        
        for config in configs:
            try:
                print(f"Tentando com: encoding={config.get('encoding')}, separador='{config.get('sep')}'")
                df = pd.read_csv(arquivo_csv, **config)
                config_usada = config
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
        
        if df is None:
            raise Exception("Não foi possível ler o arquivo CSV com nenhuma configuração")
        
       
        print(f"\nDataset carregado com sucesso!")
        print(f"Total de registros: {len(df)}")
        print(f"Colunas disponíveis: {list(df.columns)}")
        
        
        if coluna_curso not in df.columns:
            print(f"\nAviso: Coluna '{coluna_curso}' não encontrada.")
            print("Colunas disponíveis:")
            for i, col in enumerate(df.columns, 1):
                print(f"{i}. {col}")
            
            
            colunas_similares = [col for col in df.columns if 'curso' in col.lower() or 'cur_n' in col.lower()]
            if colunas_similares:
                coluna_curso = colunas_similares[0]
                print(f"Usando coluna similar: '{coluna_curso}'")
            else:
                
                try:
                    escolha = input("\nDigite o número da coluna que contém o curso: ")
                    coluna_curso = df.columns[int(escolha) - 1]
                except (ValueError, IndexError):
                    print("Escolha inválida. Usando a primeira coluna.")
                    coluna_curso = df.columns[0]
        
        
        df[coluna_curso] = df[coluna_curso].astype(str).str.strip().str.lower()
        
       
        nomes_si = [
            'sistema de informação',
            'sistemas de informação', 
            'sistema de informacao',
            'sistemas de informacao',
            'si',
            'sistema informação',
            'sistemas informação',
            'bacharelado em sistemas de informação',
            'bsi'
        ]
        
        
        mask = df[coluna_curso].str.contains('|'.join(nomes_si), case=False, na=False)
        alunos_si = df[mask].copy()
        
        print(f"\n--- RESULTADOS ---")
        print(f"Alunos de Sistema de Informação encontrados: {len(alunos_si)}")
        
        if len(alunos_si) == 0:
            print("\nCursos únicos encontrados no dataset:")
            cursos_unicos = df[coluna_curso].unique()
            for curso in sorted(cursos_unicos):
                if pd.notna(curso) and curso != 'nan':
                    print(f"  - {curso}")
            
            print("\nNenhum aluno de Sistema de Informação encontrado.")
            print("Verifique se o nome do curso está correto no arquivo.")
            return pd.DataFrame()
        
        
        print(f"Percentual do total: {(len(alunos_si)/len(df)*100):.1f}%")
        
        
        print(f"\n--- AMOSTRA DOS DADOS ---")
        print(alunos_si.head())
        
       
        if salvar_resultado:
            nome_base = os.path.splitext(os.path.basename(arquivo_csv))[0]
            nome_arquivo = f"alunos_si_{nome_base}.csv"
            alunos_si.to_csv(nome_arquivo, index=False, encoding='utf-8')
            print(f"\nResultado salvo em: {nome_arquivo}")
        
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
    print(f"Total de alunos de Sistema de Informação: {len(df_si)}")
    
    
    colunas_interesse = ['sexo', 'genero', 'idade', 'periodo', 'semestre', 'status', 'situacao', 'matricula']
    
    for coluna in colunas_interesse:
       
        colunas_similares = [col for col in df_si.columns if coluna.lower() in col.lower()]
        
        if colunas_similares:
            coluna_encontrada = colunas_similares[0]
            print(f"\n{coluna_encontrada.upper()}:")
            contagem = df_si[coluna_encontrada].value_counts().head(10)  # Mostra apenas os 10 primeiros
            for valor, qtd in contagem.items():
                if pd.notna(valor) and str(valor).strip() != '':
                    print(f"  {valor}: {qtd} ({qtd/len(df_si)*100:.1f}%)")


if __name__ == "__main__":
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
    
    
    for arquivo in arquivos_csv:
        # Verifica se o arquivo existe
        if not os.path.exists(arquivo):
            print(f"⚠️  Arquivo '{arquivo}' não encontrado. Pulando...")
            continue
        
        print(f"\n{'='*60}")
        print(f"PROCESSANDO: {arquivo}")
        print(f"{'='*60}")
        
       
        try:
            ano = int(arquivo.split('_')[1].split('.')[0])
        except:
            ano = "desconhecido"
        
        
        alunos_si = filtrar_alunos_sistema_informacao(arquivo,  coluna_curso='nome_curso',diagnosticar=True)
        
       
        if not alunos_si.empty:
            analisar_dados_si(alunos_si, ano)