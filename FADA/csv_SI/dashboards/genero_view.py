import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import streamlit as st
import seaborn as sns
import os

# Configuração da página
st.set_page_config(page_title="Análise de Gênero e Status", layout="wide")

# Configurar estilo dos gráficos
plt.style.use('seaborn-v0_8')
sns.set_palette("husl")

# Volta uma pasta e carrega os dados
caminho_csv = os.path.join("..", "discentes_edit.csv")

try:
    df = pd.read_csv(caminho_csv)
    
    st.title("🎯 Dashboard - Análise por Gênero e Status")

    # Pré-processamento dos dados
    df["sexo"] = df["sexo"].map({"M": "Masculino", "F": "Feminino"})
    df["status"] = df["status"].astype(str).str.strip()

    # Função para categorizar status - CORRIGIDA
    def categorizar_status(status):
        status_lower = str(status).lower().strip()
        
        # Definir categorias de status mais específicas
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

    # Aplicar categorização
    df['categoria_status'] = df['status'].apply(categorizar_status)

    # Sidebar com filtros
    st.sidebar.header("🔧 Filtros")

    # Filtro por gênero
    genero_opcoes = ["Geral", "Masculino", "Feminino"]
    genero_selecionado = st.sidebar.radio("Selecione o gênero:", genero_opcoes)

    # Aplicar filtro de gênero
    if genero_selecionado == "Geral":
        df_filtrado = df
        titulo_genero = "Geral"
    else:
        df_filtrado = df[df["sexo"] == genero_selecionado]
        titulo_genero = genero_selecionado

    # Filtro por ano (opcional)
    if 'ano_ingresso' in df.columns:
        anos_disponiveis = ["Todos"] + sorted(df['ano_ingresso'].unique())
        ano_selecionado = st.sidebar.selectbox("Filtrar por ano:", anos_disponiveis)
        
        if ano_selecionado != "Todos":
            df_filtrado = df_filtrado[df_filtrado['ano_ingresso'] == ano_selecionado]
            titulo_genero += f" - Ano {ano_selecionado}"

    # Estatísticas básicas
    total_ingressantes = len(df_filtrado)
    
    # Calcular estatísticas usando a nova categorização
    concluidos = len(df_filtrado[df_filtrado['categoria_status'] == 'Concluído'])
    ativos = len(df_filtrado[df_filtrado['categoria_status'] == 'Ativo'])
    evadidos = len(df_filtrado[df_filtrado['categoria_status'] == 'Evadido'])
    cancelados = len(df_filtrado[df_filtrado['categoria_status'] == 'Cancelado'])
    trancados = len(df_filtrado[df_filtrado['categoria_status'] == 'Trancado'])
    desligados = len(df_filtrado[df_filtrado['categoria_status'] == 'Desligado'])
    outros = len(df_filtrado[df_filtrado['categoria_status'] == 'Outro'])

    # Calcular taxas
    taxa_conclusao = (concluidos / total_ingressantes * 100) if total_ingressantes > 0 else 0
    taxa_evasao = (evadidos / total_ingressantes * 100) if total_ingressantes > 0 else 0

    # Layout principal
    st.header(f"📊 Análise {titulo_genero}")

    # Métricas principais
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        st.metric("Total de Ingressantes", total_ingressantes)
    
    with col2:
        st.metric("Concluídos", concluidos, f"{taxa_conclusao:.1f}%")
    
    with col3:
        st.metric("Evadidos", evadidos, f"{taxa_evasao:.1f}%")
    
    with col4:
        st.metric("Ativos", ativos)
        
    with col5:
        st.metric("Cancelados", cancelados)

    # Gráfico 1: Distribuição de status
    st.subheader("📈 Distribuição por Status")
    
    status_counts = df_filtrado['categoria_status'].value_counts()
    
    col1, col2 = st.columns(2)
    
    with col1:
        fig1, ax1 = plt.subplots(figsize=(10, 6))
        colors = ['#2E8B57', '#4169E1', '#DC143C', '#FF8C00', '#9932CC', '#696969', '#8B4513']
        bars = ax1.bar(status_counts.index, status_counts.values, color=colors[:len(status_counts)])
        ax1.set_title(f"Distribuição de Status - {titulo_genero}", fontsize=14, fontweight='bold')
        ax1.set_ylabel("Quantidade", fontsize=12)
        ax1.tick_params(axis='x', rotation=45)
        ax1.grid(axis='y', alpha=0.3)
        
        # Adicionar valores nas barras
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{int(height)}', ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig1)

    with col2:
        # Gráfico 2: Pizza com principais categorias
        fig2, ax2 = plt.subplots(figsize=(8, 8))
        wedges, texts, autotexts = ax2.pie(status_counts.values, labels=status_counts.index, 
                                          autopct='%1.1f%%', startangle=90, 
                                          colors=colors[:len(status_counts)],
                                          textprops={'fontsize': 10})
        
        # Melhorar aparência dos textos
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')
            
        ax2.set_title(f"Proporção de Status - {titulo_genero}", fontsize=14, fontweight='bold')
        st.pyplot(fig2)

    # Tabela detalhada
    st.subheader("📋 Tabela Detalhada de Status")
    
    status_detalhado = pd.DataFrame({
        'Categoria': status_counts.index,
        'Quantidade': status_counts.values,
        'Percentual (%)': (status_counts.values / total_ingressantes * 100).round(1)
    })
    
    # Adicionar formatação à tabela
    st.dataframe(
        status_detalhado,
        use_container_width=True,
        hide_index=True
    )

    # ANÁLISE COMPARATIVA POR GÊNERO - CORRIGIDA
    if genero_selecionado == "Geral":
        st.write("---")
        st.header("👥 Análise Comparativa por Gênero")
        
        # Calcular estatísticas por gênero usando a nova categorização
        stats_genero_list = []
        
        for genero in ['Masculino', 'Feminino']:
            df_gen = df[df['sexo'] == genero]
            total = len(df_gen)
            
            if total > 0:
                concluidos_gen = len(df_gen[df_gen['categoria_status'] == 'Concluído'])
                evadidos_gen = len(df_gen[df_gen['categoria_status'] == 'Evadido'])
                ativos_gen = len(df_gen[df_gen['categoria_status'] == 'Ativo'])
                cancelados_gen = len(df_gen[df_gen['categoria_status'] == 'Cancelado'])
                
                stats_genero_list.append({
                    'Gênero': genero,
                    'Total': total,
                    'Concluídos': concluidos_gen,
                    'Taxa Conclusão (%)': round((concluidos_gen / total * 100), 1),
                    'Evadidos': evadidos_gen,
                    'Taxa Evasão (%)': round((evadidos_gen / total * 100), 1),
                    'Ativos': ativos_gen,
                    'Cancelados': cancelados_gen
                })
        
        stats_genero_df = pd.DataFrame(stats_genero_list)
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("📊 Estatísticas Comparativas")
            st.dataframe(stats_genero_df, use_container_width=True, hide_index=True)
        
        with col2:
            st.subheader("📈 Comparação de Taxas")
            fig3, ax3 = plt.subplots(figsize=(10, 6))
            
            x = np.arange(len(stats_genero_df))
            width = 0.35
            
            bars1 = ax3.bar(x - width/2, stats_genero_df['Taxa Conclusão (%)'], width, 
                           label='Taxa de Conclusão', color='#2E8B57', alpha=0.8)
            bars2 = ax3.bar(x + width/2, stats_genero_df['Taxa Evasão (%)'], width, 
                           label='Taxa de Evasão', color='#DC143C', alpha=0.8)
            
            ax3.set_xlabel('Gênero', fontsize=12)
            ax3.set_ylabel('Taxa (%)', fontsize=12)
            ax3.set_title('Comparação de Taxas por Gênero', fontsize=14, fontweight='bold')
            ax3.set_xticks(x)
            ax3.set_xticklabels(stats_genero_df['Gênero'])
            ax3.legend()
            ax3.grid(axis='y', alpha=0.3)
            
            # Adicionar valores nas barras
            for bars in [bars1, bars2]:
                for bar in bars:
                    height = bar.get_height()
                    ax3.text(bar.get_x() + bar.get_width()/2., height,
                            f'{height:.1f}%', ha='center', va='bottom', fontweight='bold')
            
            plt.tight_layout()
            st.pyplot(fig3)

    # EVOLUÇÃO TEMPORAL - MELHORADA PARA AMBOS OS GÊNEROS
    if 'ano_ingresso' in df.columns:
        st.write("---")
        st.header("📈 Evolução Temporal")
        
        if genero_selecionado == "Geral":
            st.subheader("🔄 Evolução por Gênero ao Longo dos Anos")
            
            # Criar dados de evolução para ambos os gêneros
            evolucao_completa = []
            
            for genero in ['Masculino', 'Feminino']:
                df_gen = df[df['sexo'] == genero]
                evolucao_gen = df_gen.groupby('ano_ingresso').agg(
                    total=('sexo', 'count')
                ).reset_index()
                
                # Calcular concluídos por ano para cada gênero
                concluidos_por_ano = df_gen[df_gen['categoria_status'] == 'Concluído'].groupby('ano_ingresso').size().reset_index(name='concluidos')
                evolucao_gen = evolucao_gen.merge(concluidos_por_ano, on='ano_ingresso', how='left')
                evolucao_gen['concluidos'] = evolucao_gen['concluidos'].fillna(0)
                
                evolucao_gen['taxa_conclusao'] = (evolucao_gen['concluidos'] / evolucao_gen['total'] * 100).round(1)
                evolucao_gen['genero'] = genero
                
                evolucao_completa.append(evolucao_gen)
            
            evolucao_df = pd.concat(evolucao_completa, ignore_index=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                # Gráfico de evolução das taxas de conclusão
                fig4, ax4 = plt.subplots(figsize=(12, 7))
                
                for genero in ['Masculino', 'Feminino']:
                    data = evolucao_df[evolucao_df['genero'] == genero]
                    color = '#4169E1' if genero == 'Masculino' else '#DC143C'
                    ax4.plot(data['ano_ingresso'], data['taxa_conclusao'], 
                            marker='o', linewidth=3, markersize=8, label=genero, color=color)
                
                ax4.set_title("Evolução da Taxa de Conclusão por Gênero", fontsize=14, fontweight='bold')
                ax4.set_xlabel("Ano de Ingresso", fontsize=12)
                ax4.set_ylabel("Taxa de Conclusão (%)", fontsize=12)
                ax4.legend(fontsize=12)
                ax4.grid(True, alpha=0.3)
                plt.tight_layout()
                st.pyplot(fig4)
            
            with col2:
                # Gráfico de evolução do número total de ingressantes
                fig5, ax5 = plt.subplots(figsize=(12, 7))
                
                ingressantes_por_ano = df.groupby(['ano_ingresso', 'sexo']).size().unstack(fill_value=0)
                ingressantes_por_ano.plot(kind='bar', ax=ax5, color=['#4169E1', '#DC143C'], alpha=0.8)
                
                ax5.set_title("Evolução do Número de Ingressantes por Gênero", fontsize=14, fontweight='bold')
                ax5.set_xlabel("Ano de Ingresso", fontsize=12)
                ax5.set_ylabel("Número de Ingressantes", fontsize=12)
                ax5.legend(title="Gênero", fontsize=12)
                ax5.tick_params(axis='x', rotation=45)
                ax5.grid(axis='y', alpha=0.3)
                plt.tight_layout()
                st.pyplot(fig5)
            
            # Tabela de evolução detalhada
            st.subheader("📋 Tabela de Evolução Temporal")
            
            # Criar tabela pivô para melhor visualização
            tabela_evolucao = evolucao_df.pivot_table(
                index='ano_ingresso',
                columns='genero',
                values=['total', 'taxa_conclusao'],
                fill_value=0
            ).round(1)
            
            # Renomear colunas para melhor apresentação
            tabela_evolucao.columns = [f'{col[1]} - {col[0].title()}' for col in tabela_evolucao.columns]
            
            st.dataframe(tabela_evolucao, use_container_width=True)
            
        else:
            # Evolução para gênero específico
            st.subheader(f"📊 Evolução Temporal - {genero_selecionado}")
            
            evolucao = df_filtrado.groupby('ano_ingresso').agg(
                total=('sexo', 'count')
            ).reset_index()
            
            # Calcular concluídos por ano
            concluidos_por_ano = df_filtrado[df_filtrado['categoria_status'] == 'Concluído'].groupby('ano_ingresso').size().reset_index(name='concluidos')
            evolucao = evolucao.merge(concluidos_por_ano, on='ano_ingresso', how='left')
            evolucao['concluidos'] = evolucao['concluidos'].fillna(0)
            
            evolucao['taxa_conclusao'] = (evolucao['concluidos'] / evolucao['total'] * 100).round(1)
            
            col1, col2 = st.columns(2)
            
            with col1:
                fig6, ax6 = plt.subplots(figsize=(12, 6))
                color = '#4169E1' if genero_selecionado == 'Masculino' else '#DC143C'
                ax6.plot(evolucao['ano_ingresso'], evolucao['taxa_conclusao'], 
                        marker='o', linewidth=3, markersize=10, color=color)
                ax6.set_title(f"Evolução da Taxa de Conclusão - {genero_selecionado}", 
                             fontsize=14, fontweight='bold')
                ax6.set_xlabel("Ano de Ingresso", fontsize=12)
                ax6.set_ylabel("Taxa de Conclusão (%)", fontsize=12)
                ax6.grid(True, alpha=0.3)
                
                # Adicionar valores nos pontos
                for i, row in evolucao.iterrows():
                    ax6.annotate(f'{row["taxa_conclusao"]:.1f}%', 
                               (row['ano_ingresso'], row['taxa_conclusao']),
                               textcoords="offset points", xytext=(0,10), ha='center',
                               fontweight='bold')
                
                plt.tight_layout()
                st.pyplot(fig6)
            
            with col2:
                st.subheader("📋 Dados Detalhados")
                st.dataframe(evolucao[['ano_ingresso', 'total', 'concluidos', 'taxa_conclusao']], 
                           use_container_width=True, hide_index=True)

    # Informações detalhadas na sidebar
    st.sidebar.write("---")
    st.sidebar.subheader("ℹ️ Resumo do Filtro")
    st.sidebar.metric("Gênero Selecionado", genero_selecionado)
    st.sidebar.metric("Total de Registros", total_ingressantes)
    st.sidebar.metric("Taxa de Conclusão", f"{taxa_conclusao:.1f}%")
    st.sidebar.metric("Taxa de Evasão", f"{taxa_evasao:.1f}%")
    
    if genero_selecionado != "Geral":
        # Comparação com o outro gênero
        outro_genero = "Feminino" if genero_selecionado == "Masculino" else "Masculino"
        df_outro = df[df["sexo"] == outro_genero]
        total_outro = len(df_outro)
        
        if total_outro > 0:
            concluidos_outro = len(df_outro[df_outro['categoria_status'] == 'Concluído'])
            taxa_outro = (concluidos_outro / total_outro * 100)
            diferenca = taxa_conclusao - taxa_outro
            
            st.sidebar.write("---")
            st.sidebar.subheader("🔄 Comparação com Outro Gênero")
            st.sidebar.write(f"**{genero_selecionado}:** {taxa_conclusao:.1f}%")
            st.sidebar.write(f"**{outro_genero}:** {taxa_outro:.1f}%")
            
            if diferenca > 0:
                st.sidebar.success(f"Diferença: +{diferenca:.1f}% a favor")
            elif diferenca < 0:
                st.sidebar.error(f"Diferença: {diferenca:.1f}% abaixo")
            else:
                st.sidebar.info("Diferença: 0% (igual)")

    # Download dos dados filtrados
    st.sidebar.write("---")
    st.sidebar.subheader("💾 Exportar Dados")
    
    csv_filtrado = df_filtrado.to_csv(index=False)
    st.sidebar.download_button(
        label="📥 Baixar dados filtrados (CSV)",
        data=csv_filtrado,
        file_name=f"analise_{genero_selecionado.lower()}_{pd.Timestamp.now().strftime('%Y%m%d_%H%M')}.csv",
        mime="text/csv"
    )

except FileNotFoundError:
    st.error("❌ Arquivo 'discentes_edit.csv' não encontrado na pasta anterior!")
    st.info("💡 Certifique-se de que o arquivo está localizado na pasta correta.")
    st.stop()
except Exception as e:
    st.error(f"❌ Erro ao carregar dados: {str(e)}")
    st.info("💡 Verifique se o arquivo CSV está no formato correto e contém as colunas esperadas.")
    st.stop()

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

---
*Dashboard desenvolvido para análise acadêmica - Dados atualizados automaticamente*
""")