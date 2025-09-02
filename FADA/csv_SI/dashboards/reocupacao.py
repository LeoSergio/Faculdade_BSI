import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuração da página
st.set_page_config(page_title="Análise SISU vs Outros", layout="wide")

# Obter o caminho do arquivo (ajuste conforme sua estrutura de pastas)
caminho_arquivo = os.path.join(os.path.dirname(os.path.dirname(__file__)), "discentes_edit.csv")

# Verificar se o arquivo existe
if not os.path.exists(caminho_arquivo):
    st.error(f"❌ Arquivo não encontrado: {caminho_arquivo}")
    st.stop()

# Carregar os dados
try:
    df = pd.read_csv(caminho_arquivo)
except Exception as e:
    st.error(f"❌ Erro ao carregar arquivo: {e}")
    st.stop()

st.title("🎓 Análise de Conclusão: SISU vs Outras Formas de Ingresso")

# Pré-processamento dos dados
df["status"] = df["status"].astype(str).str.lower().str.strip()
df["forma_ingresso"] = df["forma_ingresso"].astype(str).str.lower().str.strip()

# Definir categorias: SISU vs Outros
def categorizar_ingresso(forma):
    forma = str(forma).lower()
    if any(termo in forma for termo in ['sisu', 'sistema de seleção unificada']):
        return "SISU"
    else:
        return "Outras Formas"

df["categoria_ingresso"] = df["forma_ingresso"].apply(categorizar_ingresso)

# Filtrar apenas alunos com status válidos para análise
status_conclusao = ['concluido', 'concluído', 'formado', 'graduado']
status_ativos = ['ativo', 'matriculado']
status_nao_concluidos = ['evadido', 'trancado', 'jubilado', 'desligado', 'cancelado']

# Criar coluna simplificada de status
df['status_simplificado'] = df['status'].apply(lambda x: 
    'Concluído' if x in status_conclusao else
    'Ativo' if x in status_ativos else
    'Não Concluído' if x in status_nao_concluidos else
    'Outro'
)

# Análise principal: Comparação SISU vs Outros
st.header("📊 Comparação Geral")

# Calcular estatísticas por categoria
analise_geral = df.groupby('categoria_ingresso').agg(
    total_alunos=('status', 'count'),
    concluidos=('status', lambda x: x.isin(status_conclusao).sum()),
    ativos=('status', lambda x: x.isin(status_ativos).sum()),
    nao_concluidos=('status', lambda x: x.isin(status_nao_concluidos).sum())
).reset_index()

analise_geral['taxa_conclusao'] = (analise_geral['concluidos'] / analise_geral['total_alunos'] * 100).round(2)
analise_geral['taxa_evasao'] = (analise_geral['nao_concluidos'] / analise_geral['total_alunos'] * 100).round(2)

# Exibir métricas principais
col1, col2, col3, col4 = st.columns(4)

with col1:
    total_sisu = analise_geral[analise_geral['categoria_ingresso'] == 'SISU']['total_alunos'].values[0]
    st.metric("👥 Total SISU", f"{total_sisu:,}")

with col2:
    total_outros = analise_geral[analise_geral['categoria_ingresso'] == 'Outras Formas']['total_alunos'].values[0]
    st.metric("👥 Total Outros", f"{total_outros:,}")

with col3:
    taxa_sisu = analise_geral[analise_geral['categoria_ingresso'] == 'SISU']['taxa_conclusao'].values[0]
    st.metric("✅ Taxa SISU", f"{taxa_sisu}%")

with col4:
    taxa_outros = analise_geral[analise_geral['categoria_ingresso'] == 'Outras Formas']['taxa_conclusao'].values[0]
    st.metric("✅ Taxa Outros", f"{taxa_outros}%")

# Gráfico de comparação
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Gráfico 1: Taxa de Conclusão
categorias = analise_geral['categoria_ingresso']
taxas = analise_geral['taxa_conclusao']

bars1 = ax1.bar(categorias, taxas, color=['#1f77b4', '#ff7f0e'], alpha=0.8)
ax1.set_ylabel('Taxa de Conclusão (%)', fontweight='bold')
ax1.set_title('Taxa de Conclusão por Categoria de Ingresso', fontweight='bold', fontsize=14)
ax1.grid(axis='y', alpha=0.3)

for bar in bars1:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 1,
            f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')

# Gráfico 2: Distribuição absoluta
concluidos = analise_geral['concluidos']
nao_concluidos = analise_geral['nao_concluidos'] + analise_geral['ativos']

ax2.bar(categorias, concluidos, label='Concluídos', color='green', alpha=0.7)
ax2.bar(categorias, nao_concluidos, bottom=concluidos, label='Não Concluídos/Ativos', color='red', alpha=0.7)
ax2.set_ylabel('Número de Alunos', fontweight='bold')
ax2.set_title('Distribuição de Alunos por Situação', fontweight='bold', fontsize=14)
ax2.legend()
ax2.grid(axis='y', alpha=0.3)

plt.tight_layout()
st.pyplot(fig)

# Tabela detalhada
st.header("📋 Dados Detalhados")
st.dataframe(analise_geral)

# Análise por ano (se houver coluna de ano)
if 'ano_ingresso' in df.columns or 'ano' in df.columns:
    st.header("📈 Evolução Temporal")
    
    # Tentar encontrar coluna de ano
    coluna_ano = 'ano_ingresso' if 'ano_ingresso' in df.columns else 'ano'
    
    evolucao = df.groupby([coluna_ano, 'categoria_ingresso']).agg(
        total=('status', 'count'),
        concluidos=('status', lambda x: x.isin(status_conclusao).sum())
    ).reset_index()
    
    evolucao['taxa'] = (evolucao['concluidos'] / evolucao['total'] * 100).round(2)
    
    # Gráfico de evolução
    fig_evol, ax_evol = plt.subplots(figsize=(12, 6))
    
    for categoria in evolucao['categoria_ingresso'].unique():
        dados = evolucao[evolucao['categoria_ingresso'] == categoria]
        ax_evol.plot(dados[coluna_ano], dados['taxa'], 
                    marker='o', label=categoria, linewidth=2, markersize=8)
    
    ax_evol.set_xlabel('Ano de Ingresso', fontweight='bold')
    ax_evol.set_ylabel('Taxa de Conclusão (%)', fontweight='bold')
    ax_evol.set_title('Evolução da Taxa de Conclusão por Ano', fontweight='bold', fontsize=14)
    ax_evol.legend()
    ax_evol.grid(alpha=0.3)
    plt.xticks(rotation=45)
    
    st.pyplot(fig_evol)

# Estatísticas adicionais
st.header("🔍 Análise Detalhada")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Distribuição por Status - SISU")
    sisu_status = df[df['categoria_ingresso'] == 'SISU']['status_simplificado'].value_counts()
    st.dataframe(sisu_status)

with col2:
    st.subheader("Distribuição por Status - Outras Formas")
    outros_status = df[df['categoria_ingresso'] == 'Outras Formas']['status_simplificado'].value_counts()
    st.dataframe(outros_status)

# Informações do dataset
st.header("ℹ️ Informações do Dataset")
st.write(f"Total de registros: {len(df):,}")
st.write(f"Formas de ingresso únicas: {df['forma_ingresso'].nunique()}")
st.write(f"Status únicos encontrados: {df['status'].nunique()}")

# Mostrar amostra dos dados
if st.checkbox("Mostrar amostra dos dados"):
    st.dataframe(df[['forma_ingresso', 'categoria_ingresso', 'status', 'status_simplificado']].head(10))