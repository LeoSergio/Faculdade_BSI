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

