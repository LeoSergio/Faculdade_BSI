import os

#####################################
##### Projeto Planejamento de Dietas - Versão 1 #####
#####################################

#ATENÇÃO: TENTAR VALIDAR USUARIO(OPCIONAL) LINHA 27
# TRABALHAR NOS PROXIMOS MODULOS
print('CONSULTA ONLINE')
resp = input('Você deseja participar? S/N ')
option = ''
if resp.upper()== 'S':
    while option != '0':
        print('''
    Projeto Nutri-Center
    1-Cadastramento de Clientes:
    2-Objetivos do Paciente:
    3-Planos de Dietas:
    4-Finalização da Consulta e Resultados:
    5-Informações pessoais:
    0-FINALIZAR PROGRAMA
    ''')
        option = input('Escolha sua opção?')

 #MODULO1-CADASTRAMENTO DE PACIENTES

        if option == '1':
            print('DIGITE AS INFORMAÕES PEDIDAS.')
######################################################
            nome = input('Nome Completo: ')
            nome_upper = nome.upper()
            idade = int(input('Qual a sua Idade:'))
            genero = input('Qual o seu Gênero: M/F ')
            peso = float(input('Qual o seu peso atual: '))
            altura = float(input('Qual a sua altura atual: '))
            info = [nome_upper,idade,genero,peso,altura]
                 
            # Imprimindo os dados dos pacientes em formato de coluna
            print('''
                  
            | Nome: {}                                   
            | Idade: {} anos                             
            | Gênero: {}                                 
            | Peso: {} KG                                
            | Altura: {} Metros                          
            
                   
            ######################
######### CADASTRADO COM SUCESSO ##########
            ######################
        '''.format(*info))
            input('Tecle <ENTER> para continuar...')


        elif option == '2':
            print('Módulo2')
            input('Tecle <ENTER> para continuar...')
        elif option == '3':
            print('Módulo3')
            input('Tecle <ENTER> para continuar...')
        elif option == '4':
            print('Módulo4')
            input('Tecle <ENTER> para continuar...')
        elif option == '5':
            print('Módulo5')
            input('Tecle <ENTER> para continuar...')
else:
        print('FIM DO PROGRAMA')


       














