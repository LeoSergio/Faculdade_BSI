#testando a biblioteca pypdf para criação de dashboards.
import os
from pypdf import PdfReader
import tabula
import sys

# ======================================================================
# CONFIGURAÇÃO
#
# ▼▼▼ COLOQUE O NOME DO SEU ARQUIVO DE HISTÓRICO AQUI ▼▼▼
NOME_DO_ARQUIVO_PDF = "meu_historico.pdf" 
# ======================================================================


def extrair_com_pypdf(caminho_pdf):
    """
    Versão 1: Tenta extrair usando PyPDF.
    Resultado esperado: Uma string longa e desformatada ("sopa de letras").
    """
    print("--- Iniciando extração com PyPDF ---")
    if not os.path.exists(caminho_pdf):
        print(f"Erro: Arquivo não encontrado em {caminho_pdf}")
        return

    try:
        reader = PdfReader(caminho_pdf)
        texto_completo = ""
        
        print(f"O PDF tem {len(reader.pages)} página(s).")
        
        for i, pagina in enumerate(reader.pages):
            print(f"\n[Texto extraído da Página {i+1} (PyPDF)]:\n")
            texto_da_pagina = pagina.extract_text()
            print(texto_da_pagina)
            texto_completo += texto_da_pagina
            
        print("\n--- Extração com PyPDF concluída ---")
        
    except Exception as e:
        print(f"Ocorreu um erro ao ler o PDF com PyPDF: {e}")


def extrair_com_tabula(caminho_pdf):
    """
    Versão 2: Tenta extrair usando Tabula-py.
    Resultado esperado: Um DataFrame (tabela) limpo e estruturado.
    """
    print("--- Iniciando extração com Tabula-py ---")
    if not os.path.exists(caminho_pdf):
        print(f"Erro: Arquivo não encontrado em {caminho_pdf}")
        return

    try:
        # Tenta ler as tabelas de todas as páginas
        # 'lattice=True' é bom para tabelas com linhas visíveis
        # 'stream=True' é bom para tabelas sem linhas (baseado em espaço)
        # Tente mudar os parâmetros se um não funcionar.
        
        # O Tabula-py retorna uma LISTA de DataFrames (um por tabela encontrada)
        lista_de_tabelas = tabula.read_pdf(caminho_pdf, pages='all', lattice=True)
        
        if not lista_de_tabelas:
            print("\nAVISO: O Tabula (modo lattice) não encontrou tabelas com linhas visíveis.")
            print("Tentando modo 'stream' (baseado em espaçamento)...")
            lista_de_tabelas = tabula.read_pdf(caminho_pdf, pages='all', stream=True)

        if not lista_de_tabelas:
            print("\nResultado: Nenhuma tabela foi encontrada pelo Tabula em nenhum modo.")
            return

        print(f"\nSucesso! O Tabula encontrou {len(lista_de_tabelas)} tabela(s) no PDF.")

        for i, tabela in enumerate(lista_de_tabelas):
            print(f"\n[Tabela {i+1} extraída (Tabula-py)]:\n")
            # O .to_string() garante que ele mostre todas as colunas no terminal
            print(tabela.to_string())
            
        print("\n--- Extração com Tabula-py concluída ---")

    except Exception as e:
        # O erro mais comum é o Java não estar instalado ou não estar no PATH
        if "java" in str(e).lower():
            print("\n❌ ERRO FATAL COM TABULA: Java não foi encontrado!")
            print("   Por favor, instale o Java (JDK ou JRE) e tente novamente.")
            print("   Após instalar, reinicie seu terminal ou computador.")
        else:
            print(f"\nOcorreu um erro ao ler o PDF com Tabula: {e}")


# --- PONTO DE ENTRADA DO SCRIPT ---
if __name__ == "__main__":
    
    # Verifica se o Python consegue encontrar o Java
    # Isso é necessário para o Tabula
    if sys.platform == "win32":
        java_check = os.system("java -version 2> NUL") # Windows
    else:
        java_check = os.system("java -version 2> /dev/null") # Linux/Mac
        
    if java_check != 0:
        print("="*70)
        print("🚨 ATENÇÃO: JAVA NÃO FOI DETECTADO NO SEU SISTEMA.")
        print("   O 'tabula-py' (Versão 2) PRECISA de Java para funcionar.")
        print("   A demonstração do Tabula provavelmente falhará.")
        print("   Por favor, instale o Java (JRE ou JDK).")
        print("="*70)
    else:
        print("✅ Java detectado. O Tabula-py deve funcionar.")

    # --- DEMONSTRAÇÃO 1 ---
    print("\n" * 2)
    print("=" * 70)
    print(" 🚀 DEMONSTRAÇÃO 1: Usando PyPDF (Extração de Texto Bruto)")
    print("=" * 70)
    print("Preste atenção em como o texto da tabela vem misturado, sem colunas.")
    print("-" * 70)
    extrair_com_pypdf(NOME_DO_ARQUIVO_PDF)
    
    
    # --- DEMONSTRAÇÃO 2 ---
    print("\n" * 3)
    print("=" * 70)
    print(" 🚀 DEMONSTRAÇÃO 2: Usando Tabula-py (Extração de Tabela)")
    print("=" * 70)
    print("Preste atenção em como o resultado já vem em formato de tabela (DataFrame).")
    print("-" * 70)
    extrair_com_tabula(NOME_DO_ARQUIVO_PDF)