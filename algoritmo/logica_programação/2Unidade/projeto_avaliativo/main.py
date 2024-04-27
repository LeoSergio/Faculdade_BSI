import os

#####################################
##### Projeto Planejamento de Dietas - Versão 1 #####
#####################################

print('CONSULTA ONLINE')
resp = input('Você deseja participar? S/N ')
option =''
if resp.upper() == 'S':    
    if option !=0:
        print('''
    Projeto Nutri-Center
1-Cadastramento de Clientes:
2-Planos de Atendimento:
3-Objetivos do Paciente:
4-Planos de Dietas:
5-Finalização da Consulta e Resultados:
6-Informações pessoais:
''')
        option = int(input('Escolha sua opção: '))

else:
    print('FIM DO PROGRAMA')
        #MODULO1-CADASTRAMENTO DE PACIENTES
if option == 1:
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


elif option == 2:
    print('Módulo2')
elif option == 3:
    print('Módulo3')
elif option == 4:
    print('Módulo4')
elif option == 5:
    print('Módulo5')
elif option == 6:
    print('Módulo6')












