import os

#####################################
##### Projeto Planejamento de Dietas - Versão 1 #####
#####################################

print('CONSULTA ONLINE')
resp = input('Você deseja participar? S/N ')
option = ''
if resp.upper()== 'S':
    while option != '0':
        os.system('clear')
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
        if option == '1':
            print('DIGITE AS INFORMAÕES PEDIDAS.')
            ######################################################
            nome = input('Nome Completo: ')
            idade = int(input('Qual a sua Idade:'))
            genero = input('Qual o seu Gênero: M/F ')
            peso = float(input('Qual o seu peso atual: '))
            altura = float(input('Qual a sua altura atual: '))
            pacientes=[nome,idade,genero, peso,altura]

            # Imprimindo os dados dos pacientes em formato de coluna
            print('''
                Nome: {},
                Idade: {},
                Gênero: {},
                Peso: {},
                Altura: {}

                ######################
            ######### CADASTRADO COM SUCESSO ##########
                ######################
            '''.format(*pacientes))
            input('Tecle <ENTER> para continuar...')


        #ALTERAÇÕES NECESSÁRIAS. ATENÇÃO!!!
        #Falta fazer o paciente voltar ao menu de seleção
        #Tentar bloquear o usuario para ele não fazer mais de um cadastro.
        #Colocar as informações em apenas um formato. ex: maiuscula(string) para ficar igual.
        #Corrigir em vez do if colocar while, pode facilitar a movimentação do usuario.


        elif option == '2':
            print('Módulo2')
            input('Tecle <ENTER> para continuar...')
        elif option == '3':
            print('Módulo3')
        elif option == '4':
            print('Módulo4')
        elif option == '5':
            print('Módulo5')
else:
        print('FIM DO PROGRAMA')


        #MODULO1-CADASTRAMENTO DE PACIENTES














