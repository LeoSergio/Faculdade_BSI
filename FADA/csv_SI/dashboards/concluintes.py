import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

# Configuração inicial para evitar warning do matplotlib
plt.rcParams['figure.figsize'] = [8, 6]

# Volta uma pasta e acessa o arquivo CSV
caminho_csv = os.path.join("..", "discentes_edit.csv")

try:
    # Verifica se o arquivo existe
    if not os.path.exists(caminho_csv):
        st.error(f"❌ Arquivo não encontrado: {caminho_csv}")
        st.write("📁 Estrutura de pastas:")
        
        # Mostra o diretório atual
        st.write(f"**Diretório atual:** {os.getcwd()}")
        
        # Mostra o que há uma pasta acima
        pasta_anterior = os.path.join("..")
        if os.path.exists(pasta_anterior):
            st.write(f"**Conteúdo da pasta anterior (**`../`**):**")
            for item in os.listdir(pasta_anterior):
                if os.path.isdir(os.path.join(pasta_anterior, item)):
                    st.write(f"📂 {item}/")
                elif item.endswith('.csv'):
                    st.write(f"📄 {item}")
                else:
                    st.write(f"📝 {item}")
        else:
            st.write("Pasta anterior não existe")
            
    else:
        # Lê o arquivo CSV
        df = pd.read_csv(caminho_csv)
        
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
            fig, ax = plt.subplots()
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

except FileNotFoundError:
    st.error("❌ Arquivo não encontrado!")
    st.write("Verifique se o arquivo 'discentes_edit.csv' está na pasta anterior.")
    
except pd.errors.EmptyDataError:
    st.error("❌ O arquivo CSV está vazio!")
    
except Exception as e:
    st.error(f"❌ Erro inesperado: {e}")
    st.write("Detalhes do erro:", str(e))