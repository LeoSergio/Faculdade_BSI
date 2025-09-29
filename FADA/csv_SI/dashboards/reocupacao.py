import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

# Configuração da página
st.set_page_config(page_title="Análise Detalhada por Forma de Ingresso", layout="wide")

# Configurar estilo dos gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Obter o caminho do arquivo
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

st.title("🎓 Dashboard - Análise Detalhada por Forma de Ingresso")

# Pré-processamento dos dados
df["status"] = df["status"].astype(str).str.strip()
df["forma_ingresso"] = df["forma_ingresso"].astype(str).str.strip()

# Função para categorizar status
def categorizar_status(status):
    status_lower = str(status).lower().strip()
    
    if any(palavra in status_lower for palavra in ['concluido', 'concluído', 'formado', 'graduado', 'diploma']):
        return 'Concluído'
    elif any(palavra in status_lower for palavra in ['ativo', 'matriculado', 'cursando', 'regular']):
        return 'Ativo'
    elif any(palavra in status_lower for palavra in ['evadido', 'evasão', 'desistente', 'jubilado', 'abandono']):
        return 'Evadido'
    elif any(palavra in status_lower for palavra in ['cancelado', 'cancelamento']):
        return 'Cancelado'
    elif any(palavra in status_lower for palavra in ['trancado', 'trancamento']):
        return 'Trancado'
    elif any(palavra in status_lower for palavra in ['desligado', 'desligamento']):
        return 'Desligado'
    else:
        return 'Outro'

# Função para limpar e padronizar nomes das formas de ingresso
def padronizar_forma_ingresso(forma):
    forma_lower = str(forma).lower().strip()
    
    # Padronização de termos comuns
    mapeamento = {
        'sisu': 'SISU',
        'sistema de seleção unificada': 'SISU',
        'sistema unificado': 'SISU',
        'vestibular': 'Vestibular',
        'processo seletivo': 'Processo Seletivo',
        'transferência': 'Transferência',
        'transferencia': 'Transferência',
        'reopção': 'Reopção',
        'reingresso': 'Reingresso',
        'vagas residuais': 'Vagas Residuais',
        'vaga residual': 'Vagas Residuais',
        'segunda graduação': 'Segunda Graduação',
        'graduado': 'Segunda Graduação',
        'enem': 'ENEM',
        'mobilidade': 'Mobilidade Acadêmica',
        'convênio': 'Convênio',
        'acordo': 'Convênio'
    }
    
    # Procurar correspondências
    for termo, padrao in mapeamento.items():
        if termo in forma_lower:
            return padrao
    
    # Se não encontrar correspondência, capitalizar primeira letra
    return forma.title()

# Aplicar categorizações
df['categoria_status'] = df['status'].apply(categorizar_status)
df['forma_ingresso_padronizada'] = df['forma_ingresso'].apply(padronizar_forma_ingresso)

# Sidebar com filtros
st.sidebar.header("🔧 Filtros")

# Obter todas as formas de ingresso únicas
formas_disponiveis = ["Todas"] + sorted(df['forma_ingresso_padronizada'].unique())
forma_selecionada = st.sidebar.selectbox("Selecione a forma de ingresso:", formas_disponiveis)

# Aplicar filtro de forma de ingresso
if forma_selecionada == "Todas":
    df_filtrado = df
    titulo_filtro = "Todas as Formas"
else:
    df_filtrado = df[df["forma_ingresso_padronizada"] == forma_selecionada]
    titulo_filtro = forma_selecionada

# Filtro por ano (se disponível)
if 'ano_ingresso' in df.columns:
    anos_disponiveis = ["Todos"] + sorted(df['ano_ingresso'].unique())
    ano_selecionado = st.sidebar.selectbox("Filtrar por ano:", anos_disponiveis)
    
    if ano_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado['ano_ingresso'] == ano_selecionado]
        titulo_filtro += f" - Ano {ano_selecionado}"

# Filtro por gênero (se disponível)
if 'sexo' in df.columns:
    df["sexo"] = df["sexo"].map({"M": "Masculino", "F": "Feminino"})
    genero_opcoes = ["Todos"] + sorted(df['sexo'].unique())
    genero_selecionado = st.sidebar.selectbox("Filtrar por gênero:", genero_opcoes)
    
    if genero_selecionado != "Todos":
        df_filtrado = df_filtrado[df_filtrado['sexo'] == genero_selecionado]
        titulo_filtro += f" - {genero_selecionado}"

# Estatísticas básicas
total_ingressantes = len(df_filtrado)

if total_ingressantes == 0:
    st.warning("Nenhum registro encontrado com os filtros selecionados.")
    st.stop()

# Calcular estatísticas usando a nova categorização
concluidos = len(df_filtrado[df_filtrado['categoria_status'] == 'Concluído'])
ativos = len(df_filtrado[df_filtrado['categoria_status'] == 'Ativo'])
evadidos = len(df_filtrado[df_filtrado['categoria_status'] == 'Evadido'])
cancelados = len(df_filtrado[df_filtrado['categoria_status'] == 'Cancelado'])
trancados = len(df_filtrado[df_filtrado['categoria_status'] == 'Trancado'])

# Calcular taxas
taxa_conclusao = (concluidos / total_ingressantes * 100) if total_ingressantes > 0 else 0
taxa_evasao = (evadidos / total_ingressantes * 100) if total_ingressantes > 0 else 0

# Layout principal
st.header(f"📊 Análise - {titulo_filtro}")

# Métricas principais
col1, col2, col3, col4, col5 = st.columns(5)

with col1:
    st.metric("Total de Ingressantes", f"{total_ingressantes:,}")

with col2:
    st.metric("Concluídos", f"{concluidos:,}", f"{taxa_conclusao:.1f}%")

with col3:
    st.metric("Evadidos", f"{evadidos:,}", f"{taxa_evasao:.1f}%")

with col4:
    st.metric("Ativos", f"{ativos:,}")

with col5:
    st.metric("Cancelados", f"{cancelados:,}")

# ANÁLISE DETALHADA POR FORMA DE INGRESSO
st.write("---")
st.header("📋 Análise Detalhada por Forma de Ingresso")

# Criar análise completa por forma de ingresso
analise_formas = df.groupby('forma_ingresso_padronizada').agg(
    Total=('categoria_status', 'count'),
    Concluídos=('categoria_status', lambda x: (x == 'Concluído').sum()),
    Evadidos=('categoria_status', lambda x: (x == 'Evadido').sum()),
    Ativos=('categoria_status', lambda x: (x == 'Ativo').sum()),
    Cancelados=('categoria_status', lambda x: (x == 'Cancelado').sum()),
    Trancados=('categoria_status', lambda x: (x == 'Trancado').sum()),
    Desligados=('categoria_status', lambda x: (x == 'Desligado').sum()),
    Outros=('categoria_status', lambda x: (x == 'Outro').sum())
).reset_index()

# Calcular taxas
analise_formas['Taxa Conclusão (%)'] = (analise_formas['Concluídos'] / analise_formas['Total'] * 100).round(1)
analise_formas['Taxa Evasão (%)'] = (analise_formas['Evadidos'] / analise_formas['Total'] * 100).round(1)
analise_formas['Taxa Ativo (%)'] = (analise_formas['Ativos'] / analise_formas['Total'] * 100).round(1)

# Ordenar por total de alunos (decrescente)
analise_formas = analise_formas.sort_values('Total', ascending=False)

st.subheader("📊 Tabela Completa - Todas as Formas de Ingresso")
st.dataframe(analise_formas, use_container_width=True, hide_index=True)

# Gráficos comparativos
st.subheader("📈 Visualizações Comparativas")

col1, col2 = st.columns(2)

with col1:
    # Gráfico de barras - Top 10 formas por total de alunos
    fig1, ax1 = plt.subplots(figsize=(12, 8))
    
    top_10_formas = analise_formas.head(10)
    
    bars = ax1.barh(top_10_formas['forma_ingresso_padronizada'], top_10_formas['Total'], 
                    color='steelblue', alpha=0.8)
    
    ax1.set_xlabel('Número de Ingressantes', fontsize=12, fontweight='bold')
    ax1.set_title('Top 10 Formas de Ingresso por Volume', fontsize=14, fontweight='bold')
    ax1.grid(axis='x', alpha=0.3)
    
    # Adicionar valores nas barras
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax1.text(width + max(top_10_formas['Total']) * 0.01, bar.get_y() + bar.get_height()/2.,
                f'{int(width):,}', ha='left', va='center', fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig1)

with col2:
    # Gráfico de taxa de conclusão - Top 10
    fig2, ax2 = plt.subplots(figsize=(12, 8))
    
    # Filtrar formas com pelo menos 10 alunos para taxa mais significativa
    formas_significativas = analise_formas[analise_formas['Total'] >= 10].head(10)
    
    colors = ['#2E8B57' if taxa >= 50 else '#DC143C' if taxa < 30 else '#FF8C00' 
              for taxa in formas_significativas['Taxa Conclusão (%)']]
    
    bars = ax2.barh(formas_significativas['forma_ingresso_padronizada'], 
                    formas_significativas['Taxa Conclusão (%)'], 
                    color=colors, alpha=0.8)
    
    ax2.set_xlabel('Taxa de Conclusão (%)', fontsize=12, fontweight='bold')
    ax2.set_title('Taxa de Conclusão por Forma de Ingresso\n(Formas com 10+ alunos)', 
                  fontsize=14, fontweight='bold')
    ax2.grid(axis='x', alpha=0.3)
    
    # Adicionar valores nas barras
    for i, bar in enumerate(bars):
        width = bar.get_width()
        ax2.text(width + 1, bar.get_y() + bar.get_height()/2.,
                f'{width:.1f}%', ha='left', va='center', fontweight='bold')
    
    plt.tight_layout()
    st.pyplot(fig2)

# Análise de distribuição de status para forma selecionada
if forma_selecionada != "Todas":
    st.write("---")
    st.header(f"🎯 Análise Detalhada - {forma_selecionada}")
    
    status_counts = df_filtrado['categoria_status'].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Gráfico de barras para a forma selecionada
        fig3, ax3 = plt.subplots(figsize=(10, 6))
        colors = ['#2E8B57', '#4169E1', '#DC143C', '#FF8C00', '#9932CC', '#696969', '#8B4513']
        bars = ax3.bar(status_counts.index, status_counts.values, color=colors[:len(status_counts)])
        ax3.set_title(f"Distribuição de Status - {forma_selecionada}", fontsize=14, fontweight='bold')
        ax3.set_ylabel("Quantidade", fontsize=12)
        ax3.tick_params(axis='x', rotation=45)
        ax3.grid(axis='y', alpha=0.3)
        
        # Adicionar valores nas barras
        for bar in bars:
            height = bar.get_height()
            ax3.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig3)
    
    with col2:
        # Gráfico de pizza para a forma selecionada
        fig4, ax4 = plt.subplots(figsize=(8, 8))
        wedges, texts, autotexts = ax4.pie(status_counts.values, labels=status_counts.index, 
                                          autopct='%1.1f%%', startangle=90, 
                                          colors=colors[:len(status_counts)],
                                          textprops={'fontsize': 10})
        
        # Melhorar aparência dos textos
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            
        ax4.set_title(f"Proporção de Status - {forma_selecionada}", fontsize=14, fontweight='bold')
        st.pyplot(fig4)
    
    # Tabela detalhada para a forma selecionada
    status_detalhado = pd.DataFrame({
        'Status': status_counts.index,
        'Quantidade': status_counts.values,
        'Percentual (%)': (status_counts.values / total_ingressantes * 100).round(1)
    })
    
    st.subheader(f"📋 Detalhamento - {forma_selecionada}")
    st.dataframe(status_detalhado, use_container_width=True, hide_index=True)

# Comparação entre formas de ingresso selecionadas
st.write("---")
st.header("🔄 Comparação Entre Formas de Ingresso")

# Multiselect para comparação
formas_para_comparar = st.multiselect(
    "Selecione até 5 formas de ingresso para comparar:",
    analise_formas['forma_ingresso_padronizada'].tolist(),
    default=analise_formas.head(3)['forma_ingresso_padronizada'].tolist(),
    max_selections=5
)

if formas_para_comparar:
    dados_comparacao = analise_formas[analise_formas['forma_ingresso_padronizada'].isin(formas_para_comparar)]
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.subheader("📊 Tabela Comparativa")
        colunas_comparacao = ['forma_ingresso_padronizada', 'Total', 'Concluídos', 'Evadidos', 
                             'Taxa Conclusão (%)', 'Taxa Evasão (%)']
        st.dataframe(dados_comparacao[colunas_comparacao], use_container_width=True, hide_index=True)
    
    with col2:
        # Gráfico comparativo de taxas
        fig5, ax5 = plt.subplots(figsize=(12, 6))
        
        x = np.arange(len(dados_comparacao))
        width = 0.35
        
        bars1 = ax5.bar(x - width/2, dados_comparacao['Taxa Conclusão (%)'], width, 
                       label='Taxa Conclusão', color='#2E8B57', alpha=0.8)
        bars2 = ax5.bar(x + width/2, dados_comparacao['Taxa Evasão (%)'], width, 
                       label='Taxa Evasão', color='#DC143C', alpha=0.8)
        
        ax5.set_xlabel('Forma de Ingresso', fontsize=12)
        ax5.set_ylabel('Taxa (%)', fontsize=12)
        ax5.set_title('Comparação de Taxas Entre Formas de Ingresso', fontsize=14, fontweight='bold')
        ax5.set_xticks(x)
        ax5.set_xticklabels([nome[:15] + '...' if len(nome) > 15 else nome 
                            for nome in dados_comparacao['forma_ingresso_padronizada']], 
                           rotation=45, ha='right')
        ax5.legend()
        ax5.grid(axis='y', alpha=0.3)
        
        # Adicionar valores nas barras
        for bars in [bars1, bars2]:
            for bar in bars:
                height = bar.get_height()
                ax5.text(bar.get_x() + bar.get_width()/2., height,
                        f'{height:.1f}%', ha='center', va='bottom', fontweight='bold', fontsize=9)
        
        plt.tight_layout()
        st.pyplot(fig5)

# EVOLUÇÃO TEMPORAL
if 'ano_ingresso' in df.columns:
    st.write("---")
    st.header("📈 Evolução Temporal por Forma de Ingresso")
    
    # Seletor para formas de ingresso na evolução temporal
    formas_evolucao = st.multiselect(
        "Selecione formas para análise temporal:",
        analise_formas.head(5)['forma_ingresso_padronizada'].tolist(),
        default=analise_formas.head(3)['forma_ingresso_padronizada'].tolist(),
        max_selections=3
    )
    
    if formas_evolucao:
        # Criar dados de evolução
        evolucao_completa = []
        
        for forma in formas_evolucao:
            df_forma = df[df['forma_ingresso_padronizada'] == forma]
            evolucao_forma = df_forma.groupby('ano_ingresso').agg(
                total=('forma_ingresso_padronizada', 'count')
            ).reset_index()
            
            # Calcular concluídos por ano
            concluidos_por_ano = df_forma[df_forma['categoria_status'] == 'Concluído'].groupby('ano_ingresso').size().reset_index(name='concluidos')
            evolucao_forma = evolucao_forma.merge(concluidos_por_ano, on='ano_ingresso', how='left')
            evolucao_forma['concluidos'] = evolucao_forma['concluidos'].fillna(0)
            
            evolucao_forma['taxa_conclusao'] = (evolucao_forma['concluidos'] / evolucao_forma['total'] * 100).round(1)
            evolucao_forma['forma'] = forma
            
            evolucao_completa.append(evolucao_forma)
        
        if evolucao_completa:
            evolucao_df = pd.concat(evolucao_completa, ignore_index=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Gráfico de evolução das taxas de conclusão
                fig6, ax6 = plt.subplots(figsize=(12, 7))
                
                colors = ['#4169E1', '#DC143C', '#2E8B57', '#FF8C00', '#9932CC']
                for i, forma in enumerate(formas_evolucao):
                    data = evolucao_df[evolucao_df['forma'] == forma]
                    if not data.empty:
                        ax6.plot(data['ano_ingresso'], data['taxa_conclusao'], 
                                marker='o', linewidth=3, markersize=8, label=forma[:20], 
                                color=colors[i % len(colors)])
                
                ax6.set_title("Evolução da Taxa de Conclusão por Forma", fontsize=14, fontweight='bold')
                ax6.set_xlabel("Ano de Ingresso", fontsize=12)
                ax6.set_ylabel("Taxa de Conclusão (%)", fontsize=12)
                ax6.legend(fontsize=10)
                ax6.grid(True, alpha=0.3)
                plt.tight_layout()
                st.pyplot(fig6)
            
            with col2:
                # Gráfico de evolução do número de ingressantes
                fig7, ax7 = plt.subplots(figsize=(12, 7))
                
                for i, forma in enumerate(formas_evolucao):
                    data = evolucao_df[evolucao_df['forma'] == forma]
                    if not data.empty:
                        ax7.plot(data['ano_ingresso'], data['total'], 
                                marker='s', linewidth=3, markersize=8, label=forma[:20],
                                color=colors[i % len(colors)], alpha=0.7)
                
                ax7.set_title("Evolução do Número de Ingressantes", fontsize=14, fontweight='bold')
                ax7.set_xlabel("Ano de Ingresso", fontsize=12)
                ax7.set_ylabel("Número de Ingressantes", fontsize=12)
                ax7.legend(fontsize=10)
                ax7.grid(True, alpha=0.3)
                plt.tight_layout()
                st.pyplot(fig7)

# Informações detalhadas na sidebar
st.sidebar.write("---")
st.sidebar.subheader("ℹ️ Resumo dos Dados")
st.sidebar.metric("Forma Selecionada", forma_selecionada)
st.sidebar.metric("Total de Registros", f"{total_ingressantes:,}")
st.sidebar.metric("Taxa de Conclusão", f"{taxa_conclusao:.1f}%")
st.sidebar.metric("Taxa de Evasão", f"{taxa_evasao:.1f}%")

# Ranking das melhores formas
st.sidebar.write("---")
st.sidebar.subheader("🏆 Ranking - Melhores Taxas de Conclusão")
ranking = analise_formas[analise_formas['Total'] >= 10].head(5)  # Pelo menos 10 alunos
for i, (_, row) in enumerate(ranking.iterrows(), 1):
    emoji = "🥇" if i == 1 else "🥈" if i == 2 else "🥉" if i == 3 else f"{i}º"
    st.sidebar.write(f"{emoji} {row['forma_ingresso_padronizada'][:25]}...")
    st.sidebar.write(f"   {row['Taxa Conclusão (%)']}% ({row['Total']} alunos)")

# Download dos dados filtrados
st.sidebar.write("---")
st.sidebar.subheader("💾 Exportar Dados")

csv_completo = analise_formas.to_csv(index=False)
st.sidebar.download_button(
    label="📥 Baixar análise completa (CSV)",
    data=csv_completo,
    file_name=f"analise_formas_ingresso_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv",
    mime="text/csv"
)

if forma_selecionada != "Todas":
    csv_filtrado = df_filtrado.to_csv(index=False)
    st.sidebar.download_button(
        label="📥 Baixar dados filtrados (CSV)",
        data=csv_filtrado,
        file_name=f"dados_{forma_selecionada.lower().replace(' ', '_')}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv",
        mime="text/csv"
    )

# Informações do dataset
st.write("---")
st.header("ℹ️ Informações do Dataset")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("Total de Registros", f"{len(df):,}")

with col2:
    st.metric("Formas de Ingresso Únicas", f"{df['forma_ingresso_padronizada'].nunique():,}")

with col3:
    st.metric("Status Únicos", f"{df['categoria_status'].nunique():,}")

with col4:
    if 'ano_ingresso' in df.columns:
        anos_span = f"{df['ano_ingresso'].min()}-{df['ano_ingresso'].max()}"
        st.metric("Período dos Dados", anos_span)

# Mostrar todas as formas encontradas
if st.checkbox("🔍 Ver todas as formas de ingresso encontradas"):
    formas_originais = df.groupby(['forma_ingresso', 'forma_ingresso_padronizada']).size().reset_index(name='quantidade')
    formas_originais = formas_originais.sort_values('quantidade', ascending=False)
    
    st.subheader("📋 Mapeamento: Forma Original → Forma Padronizada")
    st.dataframe(formas_originais, use_container_width=True, hide_index=True)

# Rodapé informativo
st.write("---")
st.markdown("""
### 📖 **Legenda dos Status**

| Símbolo | Categoria | Descrição |
|---------|-----------|-----------|
| ✅ | **Concluído** | Alunos que finalizaram o curso com sucesso |
| 🔵 | **Ativo** | Alunos atualmente matriculados e cursando |
| ❌ | **Evadido** | Alunos que abandonaram o curso |
| 🟠 | **Cancelado** | Matrículas oficialmente canceladas |
| 🟣 | **Trancado** | Matrículas temporariamente suspensas |
| 🟤 | **Desligado** | Alunos desligados da instituição |
| ⚫ | **Outro** | Outros status não categorizados |

### 🎯 **Principais Formas de Ingresso Identificadas**
- **SISU**: Sistema de Seleção Unificada
- **Vestibular**: Processo seletivo tradicional
- **Transferência**: Transferência de outras instituições
- **Vagas Residuais**: Preenchimento de vagas não ocupadas
- **Reopção**: Mudança de curso dentro da mesma instituição
- **Segunda Graduação**: Para portadores de diploma
- **Reingresso**: Retorno de ex-alunos

---
*Dashboard desenvolvido para análise acadêmica detalhada - Dados atualizados automaticamente*
""")