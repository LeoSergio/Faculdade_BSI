'''

'''


# Lista que armazena o histórico de páginas
historico = []

def adicionar_pagina(pagina):
    historico.append(pagina)
    print(f"Página '{pagina}' adicionada ao histórico.")

def exibir_ultimas_paginas():
    if len(historico) == 0:
        print("Histórico vazio.")
    else:
        print("Últimas 5 páginas visitadas:")
        # Mostra apenas as últimas 5 páginas
        for pagina in historico[-5:]:
            print("-", pagina)

def limpar_historico():
    historico.clear()
    print("Histórico limpo.")

# Simulação
adicionar_pagina("google.com")
adicionar_pagina("youtube.com")
adicionar_pagina("github.com")
adicionar_pagina("ufrn.br")
adicionar_pagina("stackoverflow.com")


exibir_ultimas_paginas()  # Vai mostrar só as 5 últimas

limpar_historico()
