import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
import seaborn as sns
import os

# --- 1. Constantes e Configurações Iniciais ---

CAMINHO_CSV = os.path.join("..", "discentes_edit.csv")
COLUNA_GENERO = "sexo"
COLUNA_STATUS = "status"
COLUNA_ANO = "ano_ingresso"
COLUNA_CATEGORIA_STATUS = 'categoria_status'

MAPA_GENERO = {"M": "Masculino", "F": "Feminino"}
MAPA_STATUS = {
    'Concluído': ['concluido', 'concluído', 'formado', 'graduado', 'diploma'],
    'Ativo': ['ativo', 'matriculado', 'cursando', 'regular'],
    # Removido 'Evadido'
    'Cancelado': ['cancelado', 'cancelamento', 'desistente', 'abandono', 'evasão', 'jubilado'],
    'Trancado': ['trancado', 'trancamento'],
    'Desligado': ['desligado', 'desligamento']
}
CORES_STATUS = ['#2E8B57', '#4169E1', '#FF8C00', '#9932CC', '#696969', '#8B4513']

st.set_page_config(page_title="Análise de Gênero e Status", layout="wide")
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")


# --- 2. Funções de Processamento ---

def categorizar_status(status: str) -> str:
    status_lower = str(status).lower().strip()
    for categoria, palavras_chave in MAPA_STATUS.items():
        if any(palavra in status_lower for palavra in palavras_chave):
            return categoria
    return 'Outro'


@st.cache_data
def carregar_dados(caminho: str) -> pd.DataFrame:
    if not os.path.exists(caminho):
        raise FileNotFoundError(f"Arquivo não encontrado em: {caminho}")
    
    df = pd.read_csv(caminho)
    df[COLUNA_GENERO] = df[COLUNA_GENERO].map(MAPA_GENERO)
    df[COLUNA_CATEGORIA_STATUS] = df[COLUNA_STATUS].apply(categorizar_status)
    return df


# --- 3. UI - Sidebar ---

def configurar_sidebar(df: pd.DataFrame):
    st.sidebar.header("🔧 Filtros")
    
    genero_opcoes = ["Geral"] + list(df[COLUNA_GENERO].unique())
    genero_selecionado = st.sidebar.radio("Selecione o gênero:", genero_opcoes)

    ano_selecionado = None
    if COLUNA_ANO in df.columns:
        anos_disponiveis = ["Todos"] + sorted(df[COLUNA_ANO].unique())
        ano_selecionado = st.sidebar.selectbox("Filtrar por ano:", anos_disponiveis)

    return genero_selecionado, ano_selecionado


# --- 4. Componentes ---

def exibir_metricas(df: pd.DataFrame):
    total = len(df)
    if total == 0:
        st.warning("Nenhum dado encontrado para os filtros selecionados.")
        return

    status_counts = df[COLUNA_CATEGORIA_STATUS].value_counts()

    concluidos = status_counts.get('Concluído', 0)
    cancelados = status_counts.get('Cancelado', 0)
    
    taxa_conclusao = (concluidos / total * 100) if total > 0 else 0
    taxa_evasao = (cancelados / total * 100) if total > 0 else 0

    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Total de Ingressantes", total)
    with col2:
        st.metric("Concluídos", concluidos, f"{taxa_conclusao:.1f}%")
    with col3:
        st.metric("Cancelados", cancelados, f"{taxa_evasao:.1f}%")
    with col4:
        st.metric("Ativos", status_counts.get('Ativo', 0))


def exibir_graficos_distribuicao(df, titulo):
    st.subheader("📈 Distribuição por Status")
    status_counts = df[COLUNA_CATEGORIA_STATUS].value_counts()
    
    col1, col2 = st.columns([0.6, 0.4])
    
    with col1:
        fig, ax = plt.subplots(figsize=(10, 6))
        bars = ax.bar(status_counts.index, status_counts.values, color=CORES_STATUS[:len(status_counts)])
        ax.set_title(f"Distribuição de Status - {titulo}")
        ax.set_ylabel("Quantidade")
        ax.tick_params(axis='x', rotation=45)
        ax.grid(axis='y', alpha=0.3)
        ax.bar_label(bars)
        st.pyplot(fig)

    with col2:
        fig, ax = plt.subplots(figsize=(8, 8))
        ax.pie(
            status_counts.values, labels=status_counts.index, autopct='%1.1f%%',
            startangle=90, colors=CORES_STATUS[:len(status_counts)]
        )
        ax.set_title(f"Proporção de Status - {titulo}")
        st.pyplot(fig)


def exibir_analise_comparativa(df):
    st.write("---")
    st.header("👥 Análise Comparativa por Gênero")

    stats = df.groupby(COLUNA_GENERO)[COLUNA_CATEGORIA_STATUS].value_counts().unstack(fill_value=0)
    stats['Total'] = stats.sum(axis=1)
    stats['Taxa Conclusão (%)'] = (stats['Concluído'] / stats['Total'] * 100).round(1)
    stats['Taxa Evasão (%)'] = (stats['Cancelado'] / stats['Total'] * 100).round(1)

    col1, col2 = st.columns(2)
    with col1:
        st.dataframe(stats[['Total', 'Concluído', 'Cancelado', 'Ativo', 'Taxa Conclusão (%)', 'Taxa Evasão (%)']])

    with col2:
        fig, ax = plt.subplots(figsize=(10, 6))
        stats_plot = stats[['Taxa Conclusão (%)', 'Taxa Evasão (%)']]
        stats_plot.plot(kind='bar', ax=ax)
        ax.set_title("Comparação de Taxas")
        ax.tick_params(axis='x', rotation=0)
        ax.grid(axis='y', alpha=0.3)
        st.pyplot(fig)


# --- 5. Main ---

def main():
    try:
        df_original = carregar_dados(CAMINHO_CSV)
        st.title("🎯 Dashboard - Análise por Gênero e Status")

        genero_selecionado, ano_selecionado = configurar_sidebar(df_original)

        df_filtrado = df_original.copy()
        titulo = "Geral"

        if genero_selecionado != "Geral":
            df_filtrado = df_filtrado[df_filtrado[COLUNA_GENERO] == genero_selecionado]
            titulo = genero_selecionado

        if ano_selecionado and ano_selecionado != "Todos":
            df_filtrado = df_filtrado[df_filtrado[COLUNA_ANO] == ano_selecionado]
            titulo += f" - Ano {ano_selecionado}"

        st.header(f"📊 Análise {titulo}")
        exibir_metricas(df_filtrado)

        if not df_filtrado.empty:
            exibir_graficos_distribuicao(df_filtrado, titulo)
            if genero_selecionado == "Geral":
                exibir_analise_comparativa(df_filtrado)

    except FileNotFoundError as e:
        st.error(f"❌ Erro: {e}")
    except Exception as e:
        st.error(f"❌ Ocorreu um erro inesperado: {e}")


if __name__ == "__main__":
    main()
