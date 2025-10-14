import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Any


#Edit os mapas, se algo der errado foi nessa alteração.

# --- 1. Constantes e Configurações ---
CAMINHO_CSV = "../discentes_edit.csv"
COLUNAS = {
    "status": "status",
    "forma_ingresso": "forma_ingresso",
    "ano_ingresso": "ano_ingresso",
    "status_cat": "categoria_status",
    "ingresso_cat": "forma_ingresso_padronizada"
}
MAPA_STATUS = {
    'Concluído': ['concluido', 'concluído', 'formado', 'graduado', 'diploma'],
    'Ativo': ['ativo', 'matriculado', 'formando', 'regular'],
    'Cancelado': ['cancelado', 'cancelamento'],
    'Trancado': ['trancado', 'trancamento'],
}
MAPA_INGRESSO = {
    'SISU': ['sisu', 'sistema de seleção unificada', 'sistema unificado'],
    'Vestibular': ['vestibular'],
    'Processo Seletivo': ['processo seletivo'],
    'Transferência': ['transferência', 'transferencia'],
    'Reopção': ['reopção'],
    'Reingresso': ['reingresso'],
    'Vagas Residuais': ['vagas residuais', 'vaga residual'],
}

st.set_page_config(page_title="Análise por Forma de Ingresso", layout="wide")
plt.style.use('seaborn-v0_8')


# --- 2. Funções de Carga e Processamento de Dados ---
@st.cache_data
def carregar_e_preparar_dados(caminho: str) -> pd.DataFrame:
    """Carrega, limpa e pré-processa os dados, tudo em uma única função cacheada."""
    try:
        df = pd.read_csv(caminho)
    except FileNotFoundError:
        st.error(f"Arquivo não encontrado: {caminho}")
        return pd.DataFrame()

    def categorizar_status(status: str) -> str:
        status_lower = str(status).lower().strip()
        for categoria, chaves in MAPA_STATUS.items():
            if any(chave in status_lower for chave in chaves):
                return categoria
        return 'Outro'

    def padronizar_ingresso(forma: str) -> str:
        forma_lower = str(forma).lower().strip()
        for padrao, chaves in MAPA_INGRESSO.items():
            if any(chave in forma_lower for chave in chaves):
                return padrao
        return forma.title() if isinstance(forma, str) else 'Não Informado'
    
    if COLUNAS["ano_ingresso"] in df.columns:
        df[COLUNAS["ano_ingresso"]] = pd.to_numeric(df[COLUNAS["ano_ingresso"]], errors='coerce').dropna().astype(int)

    df[COLUNAS["status_cat"]] = df[COLUNAS["status"]].apply(categorizar_status)
    df[COLUNAS["ingresso_cat"]] = df[COLUNAS["forma_ingresso"]].apply(padronizar_ingresso)
    
    return df

@st.cache_data
def calcular_estatisticas_gerais(df: pd.DataFrame) -> pd.DataFrame:
    """Calcula as estatísticas agregadas por forma de ingresso."""
    analise = df.groupby(COLUNAS["ingresso_cat"])[COLUNAS["status_cat"]].value_counts().unstack(fill_value=0)
    analise['Total'] = analise.sum(axis=1)
    
    if 'Concluído' in analise.columns:
        analise['Taxa Conclusão (%)'] = (analise['Concluído'] / analise['Total'] * 100).round(1)
    if 'Evadido' in analise.columns:
        analise['Taxa Evasão (%)'] = (analise['Evadido'] / analise['Total'] * 100).round(1)

    return analise.sort_values('Total', ascending=False)

# --- 3. Funções de Componentes do Dashboard ---

# MUDANÇA: Função da sidebar reintroduzida para o filtro de ano.
def renderizar_sidebar(df: pd.DataFrame) -> Any:
    """Cria e gerencia o filtro de ano na barra lateral."""
    st.sidebar.header("Filtros")
    ano_selecionado = "Todos"
    if COLUNAS["ano_ingresso"] in df.columns:
        anos_disponiveis = ["Todos"] + sorted(df[COLUNAS["ano_ingresso"]].unique())
        ano_selecionado = st.sidebar.selectbox(
            "Filtrar por ano de ingresso:", 
            anos_disponiveis
        )
    return ano_selecionado

def renderizar_tabela_completa(df_stats: pd.DataFrame, ano_selecionado: Any):
    """Exibe a tabela completa com todas as formas de ingresso, respeitando o filtro de ano."""
    titulo_ano = f"para o ano de {ano_selecionado}" if ano_selecionado != "Todos" else "para todos os anos"
    st.header(f"Análise Detalhada por Forma de Ingresso")
    st.write(f"A tabela abaixo apresenta um resumo completo do desempenho de todas as formas de ingresso, filtrado {titulo_ano}.")
    
    colunas_para_exibir = ['Total', 'Concluído', 'Evadido', 'Ativo', 'Taxa Conclusão (%)', 'Taxa Evasão (%)']
    colunas_validas = [col for col in colunas_para_exibir if col in df_stats.columns]
    st.dataframe(df_stats[colunas_validas], use_container_width=True)

def renderizar_ferramenta_comparacao(df_stats: pd.DataFrame):
    """Cria a seção interativa para comparar formas de ingresso."""
    st.write("---")
    st.header("Ferramenta de Comparação")
    st.write("Selecione duas ou mais formas de ingresso abaixo para compará-las diretamente (respeitando o filtro de ano).")

    formas_disponiveis = df_stats.index.tolist()
    formas_selecionadas = st.multiselect(
        "Selecione as formas de ingresso para comparar:",
        options=formas_disponiveis,
        default=formas_disponiveis[:3]
    )

    if not formas_selecionadas:
        st.info("Selecione pelo menos uma forma de ingresso para visualizar a comparação.")
        return

    dados_comparacao = df_stats[df_stats.index.isin(formas_selecionadas)]

    st.subheader("Visualizações Comparativas")
    col1, col2 = st.columns(2)
    with col1:
        st.write("#### Volume de Ingressantes")
        fig, ax = plt.subplots(figsize=(10, 6))
        dados_comparacao['Total'].sort_values().plot(kind='barh', ax=ax, color='steelblue')
        ax.set_xlabel("Número de Ingressantes")
        ax.set_ylabel("")
        ax.bar_label(ax.containers[0], padding=3)
        st.pyplot(fig)
    with col2:
        if 'Taxa Conclusão (%)' in dados_comparacao.columns:
            st.write("#### Taxa de Conclusão")
            fig, ax = plt.subplots(figsize=(10, 6))
            dados_comparacao['Taxa Conclusão (%)'].sort_values().plot(kind='barh', ax=ax, color='seagreen')
            ax.set_xlabel("Taxa de Conclusão (%)")
            ax.set_ylabel("")
            ax.set_xlim(0, 100)
            ax.bar_label(ax.containers[0], fmt='%.1f%%', padding=3)
            st.pyplot(fig)

def renderizar_evolucao_temporal(df: pd.DataFrame, formas_populares: List[str]):
    """Exibe a análise da evolução temporal. Ignora o filtro de ano da sidebar."""
    st.write("---")
    st.header("Evolução Temporal por Forma de Ingresso")
    
    formas_selecionadas = st.multiselect(
        "Selecione até 3 formas para analisar a evolução temporal:",
        options=formas_populares,
        default=formas_populares[:2],
        max_selections=3
    )

    if not formas_selecionadas:
        st.info("Selecione uma forma de ingresso para ver sua evolução.")
        return

    df_filtrado = df[df[COLUNAS["ingresso_cat"]].isin(formas_selecionadas)]
    
    evolucao = df_filtrado.groupby([COLUNAS["ano_ingresso"], COLUNAS["ingresso_cat"]])[COLUNAS["status_cat"]].value_counts().unstack(fill_value=0)
    evolucao['Total'] = evolucao.sum(axis=1)
    if 'Concluído' in evolucao.columns:
        evolucao['Taxa Conclusão (%)'] = (evolucao['Concluído'] / evolucao['Total'] * 100)
    
    evolucao = evolucao.reset_index()

    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=evolucao, x=COLUNAS["ano_ingresso"], y='Taxa Conclusão (%)', hue=COLUNAS["ingresso_cat"], marker='o', linewidth=2.5)
    ax.set_title("Evolução da Taxa de Conclusão ao Longo dos Anos")
    ax.set_ylabel("Taxa de Conclusão (%)")
    ax.set_xlabel("Ano de Ingresso")
    ax.grid(True, which='both', linestyle='--', linewidth=0.5)
    ax.legend(title='Forma de Ingresso')
    st.pyplot(fig)

def renderizar_info_dataset(df: pd.DataFrame):
    """Exibe métricas gerais sobre o dataset completo. Ignora o filtro de ano."""
    st.write("---")
    st.header("Informações do Dataset Completo")
    col1, col2, col3 = st.columns(3)
    col1.metric("Total de Registros", f"{len(df):,}")
    col2.metric("Formas de Ingresso Únicas", f"{df[COLUNAS['ingresso_cat']].nunique():,}")
    if COLUNAS["ano_ingresso"] in df.columns:
        anos_span = f"{int(df[COLUNAS['ano_ingresso']].min())} - {int(df[COLUNAS['ano_ingresso']].max())}"
        col3.metric("Período dos Dados", anos_span)

# --- 4. Função Principal ---
def main():
    st.title("Análise de Desempenho por Forma de Ingresso")
    
    df_original = carregar_e_preparar_dados(CAMINHO_CSV)

    if df_original.empty:
        st.stop()

    # MUDANÇA: O filtro da sidebar é chamado aqui.
    ano_selecionado = renderizar_sidebar(df_original)

    # MUDANÇA: Cria um DataFrame filtrado para as análises dinâmicas.
    df_filtrado = df_original.copy()
    if ano_selecionado != "Todos":
        df_filtrado = df_original[df_original[COLUNAS["ano_ingresso"]] == ano_selecionado]

    # Calcula as estatísticas com base nos dados filtrados (ou não).
    estatisticas_filtradas = calcular_estatisticas_gerais(df_filtrado)

    if estatisticas_filtradas.empty:
        st.warning("Nenhum dado encontrado para o ano selecionado.")
        st.stop()

    # SEÇÃO 1: Tabela Completa (Usa dados filtrados pelo ano)
    renderizar_tabela_completa(estatisticas_filtradas, ano_selecionado)

    # SEÇÃO 2: Ferramenta de Comparação Interativa (Usa dados filtrados pelo ano)
    renderizar_ferramenta_comparacao(estatisticas_filtradas)

    # SEÇÃO 3: Evolução Temporal (Usa dados ORIGINAIS, ignorando o filtro de ano)
    if COLUNAS["ano_ingresso"] in df_original.columns:
        estatisticas_originais = calcular_estatisticas_gerais(df_original)
        formas_populares = estatisticas_originais.index.tolist()
        renderizar_evolucao_temporal(df_original, formas_populares)

    # SEÇÃO 4: Informações do Dataset (Usa dados ORIGINAIS, ignorando o filtro de ano)
    renderizar_info_dataset(df_original)

if __name__ == "__main__":
    main()