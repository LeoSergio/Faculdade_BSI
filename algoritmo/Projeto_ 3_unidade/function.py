import validacao
import function
import modulo1
import modulo2
import modulo3
import os



def main_menu():
            print('''
      ##########################################
######    Projeto Planejamento de Dietas       #####
      #########################################
''')
            print('''
        PROJETO NUTRI-CENTER

    ###########################

    [1]- Módulo Paciente: 
    [2]- Módulo de Dietas:        
    [3]- Módulo Agendamento/Consulta:   
    [4]- Módulo Informações:   
    [0]- SAIR  

    ##########################
        ''')


def menu_cad(): #CRUD 1
    print('''
        PROJETO NUTRI-CENTER

    ###########################

    [1]- Cadastrar-se: 
    [2]- Informações do Paciente:        
    [3]- Alterar informações:   
    [4]- Remover Paciente:
    [5]- Relatório    
    [0]- SAIR  

    ###########################
        ''')     

def cad_dieta():
    print('''
        PROJETO NUTRI-CENTER

    ###########################

    [1]- Cadastrar Dieta: 
    [2]- Verificar Dietas:        
    [3]- Alterar Dietas:   
    [4]- Remover Dietas:
    [5]- Plano de Dieta 
    [6]- Relatório   
    [0]- SAIR  

    ###########################
        ''')

def agendamento():
    print('''
        PROJETO NUTRI-CENTER

    ###########################

    [1]- Cadastrtar Agendamento: 
    [2]- Verificar Agendamento:        
    [3]- Alterar Agendamento:   
    [4]- Remover Agendamento:
    [5]- Relatório  
    [0]- SAIR  

    ###########################
        ''')
############################################################

RED = "\033[31m"
RESET = "\033[0m"
def reports_clients(cadastro,cad_excluido):
    cadastro = cadastro
    cadastro_ex = cad_excluido
    
    # Limpa a tela de maneira compatível com diferentes sistemas operacionais
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(cadastro) == 0 and len(cadastro_ex) == 0:
        print("#========================================#")
        print("#========== SEM INFORMAÇÕES ==========#")
        print("#========================================#")
        print()
        print("--" * 25)
    # Exibir clientes cadastrados
    for cpf in cadastro:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#========================================#")
        print("#========== PACIENTES CADASTRADOS ==========#")
        print("#========================================#")
        print()
        print("--" * 25)
       
        print('NOME: ', cadastro[cpf][0])
        print(f'CPF: {cpf}')
        print('DATA DE NASCIMENTO: ', cadastro[cpf][1])
        print('TELEFONE: ', cadastro[cpf][6])
        print('GÊNERO: ', cadastro[cpf][2])
        print('PESO: ', cadastro[cpf][3])
        print('ALTURA: ', cadastro[cpf][4])
        print('IMC: ', cadastro[cpf][5])
        print("--" * 25)
    
    # Exibir clientes excluídos
    for cpf in cadastro_ex:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#========================================#")
        print("#========== PACIENTES REMOVIDOS ==========#")
        print("#========================================#")
        print()
        print("--" * 25)
        print(f'{RED}NOME: {cadastro_ex[cpf][0]}{RESET}')
        print(f'{RED}CPF: {cpf}{RESET}')
        print(f'{RED}DATA DE NASCIMENTO: {cadastro_ex[cpf][1]}{RESET}')
        print(f'{RED}TELEFONE: {cadastro_ex[cpf][6]}{RESET}')
        print(f'{RED}GÊNERO: {cadastro_ex[cpf][2]}{RESET}')
        print(f'{RED}PESO: {cadastro_ex[cpf][3]}{RESET}')
        print(f'{RED}ALTURA: {cadastro_ex[cpf][4]}{RESET}')
        print(f'{RED}IMC: {cadastro_ex[cpf][5]}{RESET}')
        print(f'{RED}{"--" * 25}{RESET}')
    
    print()
    input("Pressione <ENTER> para continuar.")

def reports_diets(dietas,dietas_excluida):
    dietas = dietas
    dietas_excluida = dietas_excluida
    
    # Limpa a tela de maneira compatível com diferentes sistemas operacionais
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if len(dietas) == 0 and len(dietas_excluida) == 0:
        print("#========================================#")
        print("#========== SEM INFORMAÇÕES ==========#")
        print("#========================================#")
        print()
        print("--" * 25)
    else:
        # Exibir dietas cadastradas
        if len(dietas) > 0:
            print("#========================================#")
            print("#========== DIETAS CADASTRADAS ==========#")
            print("#========================================#")
            print("--" * 25)
            for nome in dietas:
                print(f'NOME DA DIETA: {nome}')
                print(f'DETALHE DA DIETA: {dietas[nome][0]}')
                print(f'OBJETIVO DA DIETA: {dietas[nome][1]}')
                print("--" * 25)
        
        # Exibir dietas removidas
        if len(dietas_excluida) > 0:
            print("#========================================#")
            print("#========== DIETAS REMOVIDAS ==========#")
            print("#========================================#")
            print("--" * 25)
            for nome in dietas_excluida:
                print(f'{RED}NOME DA DIETA: {nome}{RESET}')
                print(f'{RED}DETALHE DA DIETA: {dietas_excluida[nome][0]}{RESET}')
                print(f'{RED}OBJETIVO DA DIETA: {dietas_excluida[nome][1]}{RESET}')
                print("--" * 25)
    
    input("Pressione <ENTER> para continuar.")

def reports_scheduling(agendamento,agendamento_excluido):
    agendamento = agendamento
    agendamento_excluido = agendamento_excluido
    
    # Limpa a tela de maneira compatível com diferentes sistemas operacionais
    os.system('cls' if os.name == 'nt' else 'clear')
    if len(agendamento) == 0 and len(agendamento_excluido) == 0:
        print("#========================================#")
        print("#========== SEM INFORMAÇÕES ==========#")
        print("#========================================#")
        print()
        print("--" * 25)
    # Exibir clientes cadastrados
    for cpf in agendamento:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("#========================================#")
        print("#========== AGENDAMENTOS CADASTRADAS ==========#")
        print("#========================================#")
        print()
        print("--" * 25)
        print()
        print('NOME: ', agendamento[cpf][0])
        print()
        print(f'CPF: {cpf}')
        print()
        print('DATA DE NASCIMENTO: ', agendamento[cpf][1])
        print()
        print('TELEFONE: ', agendamento[cpf][6])
        print()
        print('GÊNERO: ', agendamento[cpf][2])
        print()
        print('PESO: ', agendamento[cpf][3])
        print()
        print('ALTURA: ', agendamento[cpf][4])
        print()
        print('IMC: ', agendamento[cpf][5])
        print()
        print("--" * 25)
    
    # Exibir clientes excluídos
    for cpf in agendamento_excluido:
        print("#========================================#")
        print("#========== AGENDAMENTO REMOVIDOS ==========#")
        print("#========================================#")
        print()
        print("--" * 25)
        print(f'{RED}NOME: {agendamento_excluido[cpf][0]}{RESET}')
        print(f'{RED}CPF: {cpf}{RESET}')
        print(f'{RED}DATA DE NASCIMENTO: {agendamento_excluido[cpf][1]}{RESET}')
        print(f'{RED}TELEFONE: {agendamento_excluido[cpf][6]}{RESET}')
        print(f'{RED}GÊNERO: {agendamento_excluido[cpf][2]}{RESET}')
        print(f'{RED}PESO: {agendamento_excluido[cpf][3]}{RESET}')
        print(f'{RED}ALTURA: {agendamento_excluido[cpf][4]}{RESET}')
        print(f'{RED}IMC: {agendamento_excluido[cpf][5]}{RESET}')
        print(f'{RED}{"--" * 25}{RESET}')
    
    print()
    input("Pressione <ENTER> para continuar.")
    

