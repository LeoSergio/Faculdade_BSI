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
def exibir_agendamentos():
    for agendamento in agendamento:
        print('--- Agendamento ---')
        print(f"Paciente: {agendamento['paciente']['nome']}")
        print(f"Nutricionista: {agendamento['nutricionista']['nome']}")
        print(f"Data: {agendamento['agendamento']['data']}")
        print(f"Hora: {agendamento['agendamento']['hora']}")
        print(f"Motivo: {agendamento['agendamento']['motivo']}")
        print(f"Observações: {agendamento['agendamento']['observacoes']}")
        print(f"Local: {agendamento['agendamento']['local']}")
        print(f"Documentos: {agendamento['agendamento']['documentos']}")
        print(f"Duração: {agendamento['agendamento']['duracao']}")
        print(f"Custo: {agendamento['agendamento']['custo']}")
        print('-------------------')

