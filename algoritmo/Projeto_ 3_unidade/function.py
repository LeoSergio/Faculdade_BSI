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
    [2]- Módulo Dietas Personalizadas:        
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
    [5]- Plano de Dieta  
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
    [0]- SAIR  

    ###########################
        ''')

def agendamento():
    print('''
        PROJETO NUTRI-CENTER

    ###########################

    [1]- Agendar consulta: 
    [2]- Verificar Consulta:        
    [3]- Alterar Consulta:   
    [4]- Remover Consulta:   
    [0]- SAIR  

    ###########################
        ''')
def plan_dieta(cpf):
    imc = modulo1.cadastro[cpf][5]
    print('''
    #####################################
    #         PLANO DE DIETA             #
    #####################################
    ''')
    
    if imc < 18.5:
        print('Seu IMC indica que você está abaixo do peso. Plano de dieta para ganho de peso:')
        print('1. Coma mais frequentemente.')
        print('2. Escolha alimentos ricos em nutrientes.')
        print('3. Tente shakes e smoothies.')
    elif imc >= 18.5 and imc < 25:
        print('Seu IMC está na faixa normal. Plano de dieta para manutenção de peso:')
        print('1. Mantenha uma dieta balanceada.')
        print('2. Controle as porções.')
        print('3. Mantenha-se ativo.')
    else:
        print('Seu IMC indica que você está acima do peso. Plano de dieta para perda de peso:')
        print('1. Reduza calorias de forma controlada.')
        print('2. Coma mais proteínas.')
        print('3. Reduza a ingestão de carboidratos.')
