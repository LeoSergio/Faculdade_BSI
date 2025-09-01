import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados
df = pd.read_csv("discentes_edit.csv")

st.title("📊 Dashboard - Ingresso no Curso por Gênero")

# Exibir primeiros registros
st.write("Visualização inicial dos dados:")


# Mapear os valores
df["sexo"] = df["sexo"].map({"M": "Masculino", "F": "Feminino"})

# Contagem por gênero
contagem = df["sexo"].value_counts()

st.subheader("Quantidade de alunos por gênero")
st.bar_chart(contagem)

# Mostrar números totais
st.write("**Total por gênero:**")
st.write(contagem)

# Identificar tendência
if contagem["Masculino"] > contagem["Feminino"]:
    st.success("📈 A tendência é entrarem mais **homens** no curso.")
elif contagem["Feminino"] > contagem["Masculino"]:
    st.success("📈 A tendência é entrarem mais **mulheres** no curso.")
else:
    st.info("⚖️ O ingresso está equilibrado entre homens e mulheres.")

# Gráfico de pizza
fig, ax = plt.subplots()
ax.pie(contagem, labels=contagem.index, autopct='%1.1f%%', startangle=90)
ax.set_title("Distribuição de Ingressantes por Gênero")
st.pyplot(fig)




# Carregar os dados
df = pd.read_csv("discentes_edit.csv")

st.title("📈 Tendência de ingresso feminino no curso")

# Mapear os valores de sexo
df["sexo"] = df["sexo"].map({"M": "Masculino", "F": "Feminino"})

# Troque pelo nome real da coluna do ano/semestre no seu CSV
col_ano = "ano_ingresso"  # ajuste aqui

# Agrupar quantidade de mulheres por ano
tendencia_mulheres = df[df["sexo"] == "Feminino"].groupby(col_ano).size()

# Criar gráfico de linha
fig, ax = plt.subplots()
tendencia_mulheres.plot(kind="line", marker="o", ax=ax)
ax.set_title("Tendência de ingresso feminino ao longo do tempo")
ax.set_xlabel("Ano de ingresso")
ax.set_ylabel("Número de mulheres")
st.pyplot(fig)




# Carregar os dados

df = pd.read_csv("discentes_edit.csv")

st.title("📊 Percentual de Conclusão no Curso")

# Verifica se a coluna status existe
if "status" not in df.columns:
    st.error("Coluna 'status' não encontrada no dataset!")
    st.write("Colunas disponíveis:", df.columns.tolist())
else:
    # Total de ingressantes
    total_ingresso = len(df)

    # Total de concluintes (mais flexível)
    total_concluido = len(df[df["status"].str.upper().str.contains("CONCLU", na=False)])

    # Calcula percentual
    if total_ingresso > 0:
        percentual_concluido = (total_concluido / total_ingresso) * 100
    else:
        percentual_concluido = 0

    # Exibe resultados
    st.write(f"**Total de ingressantes:** {total_ingresso}")
    st.write(f"**Total de concluintes:** {total_concluido}")
    st.write(f"✅ **Percentual de conclusão:** {percentual_concluido:.2f}%")

    # Gráfico comparativo
    fig, ax = plt.subplots(figsize=(8, 6))
    bars = ax.bar(["Ingressantes", "Concluintes"], [total_ingresso, total_concluido], 
                 color=["skyblue", "green"])
    
    # Adiciona valores nas barras
    for bar in bars:
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
                f'{int(height)}', ha='center', va='bottom')
    
    ax.set_ylabel("Quantidade de alunos")
    ax.set_title("Comparativo: Ingressantes vs Concluintes")
    st.pyplot(fig)

    # Estatísticas adicionais
    st.write("---")
    st.write("**Distribuição de status:**")
    st.write(df["status"].value_counts())






import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
import streamlit as st

df = pd.read_csv("discentes_edit.csv")

st.title("📈 Projeção de ingresso feminino após 2024")

# Mapear os valores de sexo
df["sexo"] = df["sexo"].map({"M": "Masculino", "F": "Feminino"})

# Troque pelo nome real da coluna do ano/semestre no seu CSV
col_ano = "ano_ingresso"  # ajuste aqui

# Agrupar quantidade de mulheres por ano
tendencia_mulheres = df[df["sexo"] == "Feminino"].groupby(col_ano).size().reset_index()
tendencia_mulheres.columns = [col_ano, 'quantidade']

# Criar modelo de regressão para prever anos futuros
X = tendencia_mulheres[col_ano].values.reshape(-1, 1)
y = tendencia_mulheres['quantidade'].values

model = LinearRegression()
model.fit(X, y)

# Prever para anos futuros (2025-2030)
anos_futuros = np.array([2025, 2026, 2027, 2028, 2029, 2030]).reshape(-1, 1)
previsoes = model.predict(anos_futuros)

# Criar DataFrame com previsões
previsao_df = pd.DataFrame({
    'ano': anos_futuros.flatten(),
    'quantidade_prevista': previsoes.astype(int)
})

st.write("### 📊 Previsão de ingressantes femininas (2025-2030)")
st.dataframe(previsao_df)

# Gráfico com tendência histórica + projeção
fig, ax = plt.subplots(figsize=(12, 6))

# Dados históricos
ax.plot(tendencia_mulheres[col_ano], tendencia_mulheres['quantidade'], 
        'bo-', label='Dados históricos', linewidth=2, markersize=8)

# Projeção futura
ax.plot(previsao_df['ano'], previsao_df['quantidade_prevista'], 
        'ro--', label='Projeção', linewidth=2, markersize=8)

ax.set_title("Tendência e Projeção de ingresso feminino", fontsize=16)
ax.set_xlabel("Ano de ingresso", fontsize=12)
ax.set_ylabel("Número de mulheres", fontsize=12)
ax.grid(True, alpha=0.3)
ax.legend()
ax.tick_params(axis='x', rotation=45)

st.pyplot(fig)

# Estatísticas da projeção
st.write("### 📈 Estatísticas da projeção")
media_prevista = previsoes.mean()
crescimento_anual = model.coef_[0]

st.write(f"**Média prevista (2025-2030):** {media_prevista:.1f} mulheres/ano")
st.write(f"**Taxa de crescimento anual:** {crescimento_anual:.1f} mulheres/ano")
st.write(f"**Tendência:** {'Crescimento' if crescimento_anual > 0 else 'Queda' if crescimento_anual < 0 else 'Estabilidade'}")

# Previsão específica para 2024 se não estiver nos dados
if 2024 not in tendencia_mulheres[col_ano].values:
    previsao_2024 = model.predict([[2024]])[0]
    st.write(f"**Previsão para 2024:** {previsao_2024:.1f} mulheres")

# Análise adicional: proporção mulheres/homens
st.write("---")
st.write("### 👥 Análise de proporção por ano")

# Calcular proporção por ano
total_por_ano = df.groupby(col_ano).size()
mulheres_por_ano = df[df["sexo"] == "Feminino"].groupby(col_ano).size()
proporcao_mulheres = (mulheres_por_ano / total_por_ano * 100).fillna(0)

st.write("**Proporção de mulheres por ano (%):**")
for ano, proporcao in proporcao_mulheres.items():
    st.write(f"- {ano}: {proporcao:.1f}%")