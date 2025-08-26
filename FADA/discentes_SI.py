import pandas as pd
import os

def diagnosticar_csv(arquivo_csv):
    """
    Diagnostica problemas em um arquivo CSV
    
    Args:
        arquivo_csv (str): Caminho para o arquivo CSV
    """
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


def filtrar_alunos_sistema_informacao(arquivo_csv, coluna_curso='curso', salvar_resultado=True, diagnosticar=False):
    """
    Filtra alunos de Sistema de Informação de um CSV de discentes
    
    Args:
        arquivo_csv (str): Caminho para o arquivo CSV
        coluna_curso (str): Nome da coluna que contém o curso
        salvar_resultado (bool): Se deve salvar o resultado em um novo arquivo
        diagnosticar (bool): Se deve fazer diagnóstico do arquivo antes de tentar ler
    
    Returns:
        pd.DataFrame: DataFrame com apenas os alunos de Sistema de Informação
    """
    
    if diagnosticar:
        diagnosticar_csv(arquivo_csv)
    
    try:
        # Tenta diferentes configurações para ler o CSV
        print(f"Lendo arquivo: {arquivo_csv}")
        
        # Lista de configurações para tentar
        configs = [
            {'encoding': 'utf-8', 'sep': ','},
            {'encoding': 'utf-8', 'sep': ';'},
            {'encoding': 'latin-1', 'sep': ','},
            {'encoding': 'latin-1', 'sep': ';'},
            {'encoding': 'utf-8', 'sep': ',', 'quoting': 1},  # QUOTE_ALL
            {'encoding': 'utf-8', 'sep': ';', 'quoting': 1},
            {'encoding': 'utf-8', 'sep': ',', 'error_bad_lines': False, 'warn_bad_lines': True},
            {'encoding': 'utf-8', 'sep': ';', 'error_bad_lines': False, 'warn_bad_lines': True},
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
        
        # Se ainda não conseguiu, tenta com pandas engine python (mais lento mas mais tolerante)
        if df is None:
            try:
                print("Tentando com engine Python (mais tolerante)...")
                df = pd.read_csv(arquivo_csv, encoding='utf-8', sep=None, engine='python')
                print("✓ Sucesso com engine Python")
            except Exception as e:
                print(f"✗ Engine Python também falhou: {e}")
        
        # Se ainda não conseguiu, tenta detectar o separador automaticamente
        if df is None:
            try:
                print("Tentando detectar separador automaticamente...")
                with open(arquivo_csv, 'r', encoding='utf-8') as f:
                    primeira_linha = f.readline()
                    print(f"Primeira linha: {primeira_linha[:100]}...")
                    
                    # Conta possíveis separadores
                    separadores = [',', ';', '\t', '|']
                    contagens = {sep: primeira_linha.count(sep) for sep in separadores}
                    sep_provavel = max(contagens, key=contagens.get)
                    print(f"Separador mais provável: '{sep_provavel}' (aparece {contagens[sep_provavel]} vezes)")
                
                df = pd.read_csv(arquivo_csv, encoding='utf-8', sep=sep_provavel, on_bad_lines='skip')
                print("✓ Sucesso com detecção automática")
            except Exception as e:
                print(f"✗ Detecção automática falhou: {e}")
        
        if df is None:
            raise Exception("Não foi possível ler o arquivo CSV com nenhuma configuração")
        
        # Mostra informações básicas do dataset
        print(f"\nDataset carregado com sucesso!")
        print(f"Total de registros: {len(df)}")
        print(f"Colunas disponíveis: {list(df.columns)}")
        
        # Verifica se a coluna do curso existe
        if coluna_curso not in df.columns:
            print(f"\nAviso: Coluna '{coluna_curso}' não encontrada.")
            print("Colunas disponíveis:")
            for i, col in enumerate(df.columns, 1):
                print(f"{i}. {col}")
            
            # Permite ao usuário escolher a coluna correta
            escolha = input("\nDigite o número da coluna que contém o curso: ")
            try:
                coluna_curso = df.columns[int(escolha) - 1]
            except (ValueError, IndexError):
                print("Escolha inválida. Usando a primeira coluna.")
                coluna_curso = df.columns[0]
        
        # Remove espaços em branco e converte para lowercase para comparação
        df[coluna_curso] = df[coluna_curso].astype(str).str.strip().str.lower()
        
        # Lista de possíveis nomes para Sistema de Informação
        nomes_si = [
            'sistema de informação',
            'sistemas de informação',
            'sistema de informacao',
            'sistemas de informacao',
            'si',
            'sistema informação',
            'sistemas informação'
        ]
        
        # Filtra os alunos de Sistema de Informação
        mask = df[coluna_curso].isin(nomes_si)
        alunos_si = df[mask].copy()
        
        print(f"\n--- RESULTADOS ---")
        print(f"Alunos de Sistema de Informação encontrados: {len(alunos_si)}")
        
        if len(alunos_si) == 0:
            print("\nCursos únicos encontrados no dataset:")
            cursos_unicos = df[coluna_curso].unique()
            for curso in sorted(cursos_unicos):
                if pd.notna(curso):
                    print(f"  - {curso}")
            
            print("\nNenhum aluno de Sistema de Informação encontrado.")
            print("Verifique se o nome do curso está correto no arquivo.")
            return pd.DataFrame()
        
        # Mostra algumas estatísticas
        print(f"Percentual do total: {(len(alunos_si)/len(df)*100):.1f}%")
        
        # Mostra uma amostra dos dados
        print(f"\n--- AMOSTRA DOS DADOS ---")
        print(alunos_si.head())
        
        # Salva o resultado se solicitado
        if salvar_resultado:
            nome_arquivo = f"alunos_sistema_informacao_{pd.Timestamp.now().strftime('%Y%m%d_%H%M%S')}.csv"
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

def analisar_dados_si(df_si):
    """
    Faz uma análise básica dos dados dos alunos de Sistema de Informação
    
    Args:
        df_si (pd.DataFrame): DataFrame com os alunos de SI
    """
    if df_si.empty:
        print("Nenhum dado para analisar.")
        return
    
    print("\n=== ANÁLISE DOS DADOS ===")
    print(f"Total de alunos de Sistema de Informação: {len(df_si)}")
    
    # Analisa colunas comuns
    colunas_interesse = ['sexo', 'genero', 'idade', 'periodo', 'semestre', 'status', 'situacao']
    
    for coluna in colunas_interesse:
        # Procura por colunas com nomes similares
        colunas_similares = [col for col in df_si.columns if coluna.lower() in col.lower()]
        
        if colunas_similares:
            coluna_encontrada = colunas_similares[0]
            print(f"\n{coluna_encontrada.upper()}:")
            contagem = df_si[coluna_encontrada].value_counts()
            for valor, qtd in contagem.items():
                if pd.notna(valor):
                    print(f"  {valor}: {qtd} ({qtd/len(df_si)*100:.1f}%)")

# Exemplo de uso
if __name__ == "__main__":
    # Substitua pelo caminho do seu arquivo CSV
    arquivo_csv = "discentes_2024.csv"
    
    # Verifica se o arquivo existe
    if not os.path.exists(arquivo_csv):
        print(f"Arquivo '{arquivo_csv}' não encontrado.")
        print("Certifique-se de que o arquivo está no mesmo diretório do script.")
        print("Ou forneça o caminho completo para o arquivo.")
    else:
        # Filtra os alunos de Sistema de Informação com diagnóstico
        print("\nExecutando com diagnóstico...")
        alunos_si = filtrar_alunos_sistema_informacao(arquivo_csv, diagnosticar=True)
        
        # Faz análise dos dados se houver resultados
        if not alunos_si.empty:
            analisar_dados_si(alunos_si)
            
            # Opção para visualizar dados específicos
            print("\n=== OPÇÕES ADICIONAIS ===")
            resposta = input("Deseja ver informações específicas de alguma coluna? (s/n): ")
            if resposta.lower() == 's':
                print("\nColunas disponíveis:")
                for i, col in enumerate(alunos_si.columns, 1):
                    print(f"{i}. {col}")
                
                try:
                    escolha = int(input("\nEscolha o número da coluna: ")) - 1
                    coluna_escolhida = alunos_si.columns[escolha]
                    print(f"\nDados da coluna '{coluna_escolhida}':")
                    print(alunos_si[coluna_escolhida].value_counts())
                except (ValueError, IndexError):
                    print("Escolha inválida.")