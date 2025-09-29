import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

plt.rcParams['figure.figsize'] = [8, 6]

# Caminho do arquivo
caminho_csv = os.path.join("..", "discentes_edit.csv")

try:
    if not os.path.exists(caminho_csv):
        st.error(f"Arquivo não encontrado: {caminho_csv}")
        st.stop()

    # Ler dados
    df = pd.read_csv(caminho_csv)

    st.title("Análise de Cancelamentos")

    # Normalizar colunas
    df["status"] = df["status"].astype(str).str.lower().str.strip()

    # Detectar coluna de ano
    colunas_ano = ['ano_ingresso']
    coluna_ano = None
    for col in colunas_ano:
        if col in df.columns:
            coluna_ano = col
            break

    if not coluna_ano:
        st.error("Não foi encontrada nenhuma coluna de ano no dataset.")
        st.stop()

    # Converter ano para inteiro
    df[coluna_ano] = pd.to_numeric(df[coluna_ano], errors="coerce")
    df = df.dropna(subset=[coluna_ano])
    df[coluna_ano] = df[coluna_ano].astype(int)

    # Seleção de ano
    anos_disponiveis = sorted(df[coluna_ano].unique())
    ano_selecionado = st.selectbox("Selecione o ano de ingresso", options=anos_disponiveis, index=0)

    df_ano = df[df[coluna_ano] == ano_selecionado]

    # Estatísticas básicas - APENAS CANCELADOS
    total_ingressantes = len(df_ano)
    concluintes = df_ano["status"].str.contains("conclu", case=False, na=False).sum()
    cancelados = df_ano["status"].str.contains("cancel", case=False, na=False).sum()

    taxa_conclusao = (concluintes / total_ingressantes * 100) if total_ingressantes > 0 else 0
    taxa_cancelados = (cancelados / total_ingressantes * 100) if total_ingressantes > 0 else 0

    st.subheader(f"Estatísticas - Ano {ano_selecionado}")
    col1, col2, col3 = st.columns(3)

    col1.metric("Ingressantes", total_ingressantes)
    col2.metric("Concluintes", concluintes, f"{taxa_conclusao:.1f}%")
    col3.metric("Cancelados", cancelados, f"{taxa_cancelados:.1f}%", delta_color="inverse")

    # Distribuição dos status
    st.write("Distribuição de status")
    st.bar_chart(df_ano["status"].value_counts())

    # Análise detalhada de cancelamentos
    st.subheader("🔍 Análise Detalhada de Cancelamentos")
    
    # Criar categorias para análise
    df_ano['categoria_status'] = df_ano['status'].apply(
        lambda x: 'Concluído' if 'conclu' in str(x).lower() 
        else 'Cancelado' if 'cancel' in str(x).lower()
        else 'Outros'
    )
    
    # Gráfico de pizza para cancelamentos
    fig_pizza, ax_pizza = plt.subplots(figsize=(8, 6))
    categorias_status = df_ano['categoria_status'].value_counts()
    ax_pizza.pie(categorias_status.values, labels=categorias_status.index, autopct='%1.1f%%', startangle=90)
    ax_pizza.set_title(f"Distribuição de Status - Ano {ano_selecionado}")
    st.pyplot(fig_pizza)

    # Comparação temporal (2009–2020) - APENAS CANCELADOS
    st.subheader("Evolução Temporal (2009–2020) - Cancelamentos")
    df_periodo = df[(df[coluna_ano] >= 2009) & (df[coluna_ano] <= 2020)]

    resumo = df_periodo.groupby(coluna_ano).agg(
        total=('status', 'count'),
        concluintes=('status', lambda x: x.str.contains("conclu", case=False, na=False).sum()),
        cancelados=('status', lambda x: x.str.contains("cancel", case=False, na=False).sum())
    ).reset_index()

    resumo["taxa_conclusao"] = (resumo["concluintes"] / resumo["total"] * 100).round(2)
    resumo["taxa_cancelados"] = (resumo["cancelados"] / resumo["total"] * 100).round(2)

    st.dataframe(resumo)

    # Gráfico de evolução - APENAS CANCELADOS
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(resumo[coluna_ano], resumo["taxa_conclusao"], label="Taxa de Conclusão", marker="o", linewidth=2)
    ax.plot(resumo[coluna_ano], resumo["taxa_cancelados"], label="Taxa de Cancelados", marker="s", linestyle="--", color='red')
    
    ax.set_title("Evolução das Taxas de Conclusão e Cancelamentos (2009–2020)")
    ax.set_xlabel("Ano de ingresso")
    ax.set_ylabel("Percentual (%)")
    ax.legend()
    ax.grid(True, alpha=0.3)
    ax.tick_params(axis='x', rotation=45)
    st.pyplot(fig)

    # Análise de tendência de cancelamentos
    st.subheader("📈 Tendência de Cancelamentos")
    
    # Calcular média móvel para suavizar a tendência
    resumo['cancelados_mm'] = resumo['taxa_cancelados'].rolling(window=3, min_periods=1).mean()
    
    fig_tendencia, ax_tendencia = plt.subplots(figsize=(12, 6))
    ax_tendencia.bar(resumo[coluna_ano], resumo["taxa_cancelados"], alpha=0.6, label='Cancelamentos Anuais', color='red')
    ax_tendencia.plot(resumo[coluna_ano], resumo["cancelados_mm"], label='Tendência (Média Móvel 3 anos)', 
                      color='darkred', linewidth=3, marker='o')
    
    ax_tendencia.set_title("Tendência da Taxa de Cancelamentos")
    ax_tendencia.set_xlabel("Ano de ingresso")
    ax_tendencia.set_ylabel("Percentual de Cancelamentos (%)")
    ax_tendencia.legend()
    ax_tendencia.grid(True, alpha=0.3)
    ax_tendencia.tick_params(axis='x', rotation=45)
    st.pyplot(fig_tendencia)

    # Estatísticas consolidadas - APENAS CANCELADOS
    st.subheader("📊 Estatísticas Consolidadas (2009-2024)")

    # --- INÍCIO DA SOLUÇÃO ---
    # 1. Crie um novo DataFrame filtrando o período correto (2009-2024) a partir do DF original
    df_consolidado = df[(df[coluna_ano] >= 2009) & (df[coluna_ano] <= 2024)]

    # 2. Calcule os totais a partir deste novo DataFrame
    total_consolidado = len(df_consolidado)
    concluintes_consolidado = df_consolidado["status"].str.contains("conclu", case=False, na=False).sum()
    cancelados_consolidado = df_consolidado["status"].str.contains("cancel", case=False, na=False).sum()

    # Verifica se o total é maior que zero para evitar divisão por zero
    if total_consolidado > 0:
        taxa_conclusao_consolidada = (concluintes_consolidado / total_consolidado * 100)
        taxa_cancelamento_consolidada = (cancelados_consolidado / total_consolidado * 100)
    else:
        taxa_conclusao_consolidada = 0
        taxa_cancelamento_consolidada = 0

    # 3. Exiba os novos valores calculados
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Total de Ingressantes (2009-2024)", f"{total_consolidado:,}")
    with col2:
        st.metric("Total de Concluintes", f"{concluintes_consolidado:,}", 
                  f"{taxa_conclusao_consolidada:.1f}%")
    with col3:
        st.metric("Total de Cancelados", f"{cancelados_consolidado:,}", 
                  f"{taxa_cancelamento_consolidada:.1f}%", delta_color="inverse")
    # --- FIM DA SOLUÇÃO ---


    # Análise dos cancelamentos por ano
    st.subheader("📋 Detalhamento de Cancelamentos por Ano")
    
    cancelamentos_por_ano = resumo[['ano_ingresso', 'total', 'cancelados', 'taxa_cancelados']].copy()
    cancelamentos_por_ano['percentual'] = (cancelamentos_por_ano['cancelados'] / cancelamentos_por_ano['total'] * 100).round(1)
    cancelamentos_por_ano = cancelamentos_por_ano.sort_values('taxa_cancelados', ascending=False)
    
    st.dataframe(cancelamentos_por_ano)

    # Top 5 anos com maior taxa de cancelamento
    st.subheader("🥇 Top 5 Anos com Maior Taxa de Cancelamento")
    top_cancelamentos = cancelamentos_por_ano.head(5)
    st.dataframe(top_cancelamentos)

    # Análise detalhada por status
    st.subheader("Filtrar por Status")
    status_selecionado = st.selectbox("Selecione um status", options=df["status"].unique())
    df_status = df_ano[df_ano["status"] == status_selecionado]

    st.write(f"Alunos com status '{status_selecionado}' no ano {ano_selecionado}: {len(df_status)}")
    
    if len(df_status) > 0:
        st.dataframe(df_status)
    else:
        st.info("Nenhum aluno encontrado com este status para o ano selecionado.")

except Exception as e:
    st.error(f"Erro inesperado: {e}")