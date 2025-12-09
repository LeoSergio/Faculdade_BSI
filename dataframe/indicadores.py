#    INDICADORES COM FUNÇÃO
# -----------------------------------------------------------------
#1 - O sistema DEVE exigir a Média geral do semestre. 
#2 - O sistema DEVE exigir a Média geral por disciplina em relação à turma. 
#3 - O sistema DEVE permitir ao aluno visualizar o prazo para a conclusão padrão/máximo por semestre.
#4 - Percentual do curso (Pendências e Integralizadas)
#6 - Ranking da pior e melhor média por semestre.
#7 - Frequência geral nas aulas das disciplinas que está matriculado.
# -----------------------------------------------------------------
#    INDICADORES SEM FUNÇÃO
# -----------------------------------------------------------------
#1 - O sistema DEVE permitir ao aluno visualizar suas notas nas disciplinas que está matriculado e tbm nas disciplinas cursadas anteriormente, filtrando por período/ano.
#2 - O sistema DEVE permitir ao aluno visualizar a frequência (%) nas aulas (filtrando por disciplina).
#3 - O sistema DEVE permitir ao aluno visualizar as disciplinas que faltam cursar.  
#4 - O sistema DEVE permitir ao aluno visualizar o período atual que está cursando.
#5 - O sistema DEVE permitir ao aluno visualizar o MC e MCN: além de mostrar os índices mostrar também o significado delas.

# -----------------------------------------------------------------
# Função 1 - Média geral das disciplinas de um semestre
# -----------------------------------------------------------------
def media_geral_semestre(disciplinas, semestre):
    medias = [
        d["media"]
        for d in disciplinas
        if d["ano_periodo"] == semestre and isinstance(d["media"], (int, float))
    ]

    if not medias:
        return None

    return sum(medias) / len(medias)

# -----------------------------------------------------------------
# Função 2 - Comparação da média de um aluno com a média da turma
# -----------------------------------------------------------------
def comparacao_media_turma(disciplina_info):
    medias_validas = [
        m for m in disciplina_info["medias_turma"]
        if isinstance(m, (int, float))
    ]

    if not medias_validas:
        return None

    media_turma = sum(medias_validas) / len(medias_validas)

    return disciplina_info["media_aluno"], media_turma


# Função 3 - O sistema DEVE permitir ao aluno visualizar o prazo para a conclusão padrão/máximo por semestre.
from datetime import datetime

def prazo_conclusao (ano_ingresso, periodo_atual):

    conclusao_padrao = ano_ingresso + 3
    conclusao_max = ano_ingresso + 5

    # Identificando ano atual
    hoje = datetime.now()
    ano_atual = hoje.year

    # Calculando prazo em semestres. Os números retornados são referentes a quantidade de semestre que ainda falta cursar ou pode permanecer.
    prazo_padrao = (conclusao_padrao - ano_atual) * 2
    prazo_max = (conclusao_max - ano_atual) * 2

    return prazo_padrao, prazo_max


# Função 4 - Percentual do curso (Pendências e Integralizadas) - Com base na carga horária total obrigatória + optativa
def percentual_integralizado (integralizado):
    percentual_integralizado = (integralizado * 100) / 3000
    percentual_pendente = 100 - percentual_integralizado
    return percentual_integralizado, percentual_pendente

# Função 5 - O sistema DEVE permitir ao aluno visualizar a quantidade de disciplinas em que ele foi APRN/APR/REP/REPF/REPMF. 
def contar_status(situacoes):
    # O parâmetro situacoes é a lista das situações do aluno em cada disciplina (extraído do histórico)
    categorias = {
        "APRN": 0,
        "APR": 0,
        "REP": 0,
        "REPF": 0,
        "REPMF": 0
    }

    for status in situacoes:
        if status in categorias:
            categorias[status] += 1

    return categorias

# -----------------------------------------------------------------
# Função 6 - Ranking da pior e melhor média por semestre
# -----------------------------------------------------------------
def ranking_melhor_pior(disciplinas, semestre):
    notas = [
        d["media"]
        for d in disciplinas
        if d["ano_periodo"] == semestre and isinstance(d["media"], (int, float))
    ]

    if not notas:
        return None

    notas.sort()
    pior = notas[0]
    melhor = notas[-1]

    return pior, melhor


# --------------------------
#      ÁREA DE TESTES
# --------------------------

if __name__ == "__main__":

    resultado = prazo_conclusao(2023, 1)
    print("Resultado para ingresso 2023:", resultado)

    feito, faltante = percentual_integralizado(1350)
    print(f"Integralizado: {feito:.2f}%")
    print(f"Pendente:     {faltante:.2f}%")
