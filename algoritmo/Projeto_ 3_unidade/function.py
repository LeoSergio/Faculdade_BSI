import validacao
import function
import modulo1
import modulo2
import modulo3
import os



def main_menu():
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
    if len(cadastro) == 0 and len(cadastro_ex) == 0:
        print("#========================================#")
        print("#========== SEM INFORMAÇÕES ==========#")
        print("#========================================#")
        print()
        print("--" * 25)
    else:
         if len(cadastro) > 0:
            print("#========================================#")
            print("#========== PACIENTES CADASTRADOS ==========#")
            print("#========================================#")
            print("--" * 25)
         
    # Exibir clientes cadastrados
            for cpf in cadastro:
                print('NOME: ', cadastro[cpf][0])
                print(f'CPF: {cpf}')
                print('DATA DE NASCIMENTO: ', cadastro[cpf][1])
                print('TELEFONE: ', cadastro[cpf][6])
                print('GÊNERO: ', cadastro[cpf][2])
                print('PESO: ', cadastro[cpf][3])
                print('ALTURA: ', cadastro[cpf][4])
                print('IMC: ', cadastro[cpf][5])
                print("--" * 25)
         if len(cad_excluido) > 0:
            print("#========================================#")
            print("#========== PACIENTES REMOVIDOS ==========#")
            print("#========================================#")
            print("--" * 25)
    
    # Exibir clientes excluídos
            for cpf in cadastro_ex:
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

def display_patient_info(cpf, cadastro):
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=" * 50)
    print(f"{GREEN}{'INFORMAÇÕES DO PACIENTE':^50}{RESET}")
    print("=" * 50)
    print(f'NOME: ', cadastro[cpf][0])
    print(f"CPF: {cpf}")
    print(f"DATA DE NASCIMENTO: {cadastro[cpf][1]}")
    print(f"TELEFONE: {cadastro[cpf][6]}")
    print(f"GÊNERO: {cadastro[cpf][2]}")
    print(f"PESO: {cadastro[cpf][3]} KG")
    print(f"ALTURA: {cadastro[cpf][4]}")
    print(f"IMC: {cadastro[cpf][5]}")
    print("=" * 50)
    
    print(f'''
    {GREEN}#########################{RESET}
    {GREEN}## CADASTRADO COM SUCESSO {GREEN}##{RESET}
    {GREEN}#########################{RESET}
    ''')

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
            for nome in dietas: #ERRO NO FOR, ESTA EXIBINDO DIETAS A MAIS
                print(f'NOME DA DIETA:{dietas[nome][0]} ')
                print(f'DETALHE DA DIETA: {dietas[nome][1]}')
                print(f'OBJETIVO DA DIETA: {dietas[nome][2]}')
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

def reports_scheduling(agendamento, agendamento_excluido):
    # Limpa a tela de maneira compatível com diferentes sistemas operacionais
    os.system('cls' if os.name == 'nt' else 'clear')
    
    if len(agendamento) == 0 and len(agendamento_excluido) == 0:
        print("#========================================#")
        print("#========== SEM INFORMAÇÕES ==========#")
        print("#========================================#")
        print()
        print("--" * 25)
    else:
        # Exibir agendamentos cadastrados
        if len(agendamento) > 0:
            print("#========================================#")
            print("#========== AGENDAMENTOS CADASTRADOS ==========#")
            print("#========================================#")
            print()
            print("--" * 25)
            for cpf in agendamento:
                print(agendamento)
                if agendamento[cpf]:
                    print('NOME: ', agendamento[cpf][0])
                    print(f'CPF: {cpf}')
                    print('DATA DE NASCIMENTO: ', agendamento[cpf][1])
                    
                    print('GÊNERO: ', agendamento[cpf][2])
                    print('PESO: ', agendamento[cpf][3])
                    print('ALTURA: ', agendamento[cpf][4])
                    print('IMC: ', agendamento[cpf][5])
                    print("--" * 25)
        
        # Exibir agendamentos removidos
        if len(agendamento_excluido) > 0:
            print("#========================================#")
            print("#========== AGENDAMENTOS REMOVIDOS ==========#")
            print("#========================================#")
            print()
            print("--" * 25)
            for cpf in agendamento_excluido:
                if agendamento_excluido[cpf]:
                    print(f'NOME: {agendamento_excluido[cpf][0]}')
                    print(f'CPF: {cpf}')
                    print(f'DATA DE NASCIMENTO: {agendamento_excluido[cpf][1]}')
                    print(f'TELEFONE: {agendamento_excluido[cpf][6]}')
                    print(f'GÊNERO: {agendamento_excluido[cpf][2]}')
                    print(f'PESO: {agendamento_excluido[cpf][3]}')
                    print(f'ALTURA: {agendamento_excluido[cpf][4]}')
                    print(f'IMC: {agendamento_excluido[cpf][5]}')
                    print(f'{"--" * 25}')
    
    print()
    input("Pressione <ENTER> para continuar.")
    

