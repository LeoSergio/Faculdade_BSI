from validacao import validaCPF
import os
import datetime



     ##########################################
##### Projeto Planejamento de Dietas      #####
     #########################################

'''
    obs: add informações no modulo 2
    LISTA DE DIETAS E LISTA DOS PESOS DO IMC
'''

cadastro = {#nome_upper,genero,peso,altura,imc,obj
     
}

dieta={

}
agenda = {

}

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

def main_menu():
            print('''
        PROJETO NUTRI-CENTER

    ###########################

    [1]- Módulo Paciente Objetivos: 
    [2]- Módulo Dietas:        
    [3]- Módulo Agendamento/Consulta:   
    [4]- Módulo Informações:   
    [0]- SAIR  

    ##########################
        ''')


def menu_cad():
    print('''
        PROJETO NUTRI-CENTER

    ###########################

    [1]- Cadastrar-se: 
    [2]- Verificar informações:        
    [3]- Alterar informações:   
    [4]- Remover Usuário:   
    [0]- SAIR  

    ###########################
        ''')
######################### MENU-PRINCIPAL #####################################
def main():
        os.system('cls')
        main_menu()
        option = input('Escolha uma opção? --> ')
        while option != '0':
            if option == '1':
                cad_paciente()
                main_menu()
                option = input('Digite outra opção: ')
            elif option == '2':
                print('CADASTRAMENTO DE DIETAS')
                dieta()
                main_menu()
                option = input('Digite outra opção: ')     
            elif option == '3':
                print('Módulo3')
                agenda()
                main_menu()
                option = input('Digite outra opção: ') 
            elif option == '4':
                print('Módulo4')
                main_menu()
                my_information()
                input('Tecle <ENTER> para continuar...')

                option = input('Digite outra opção: ') 

            else:
                print('OPÇÃO INVÁLIDA')
                option = input('Digite outra opção: ')
        print('FIM DO PROGRAMA')       



############################ MODULO1-CADASTRAMENTO DE PACIENTES ###############################
def cad_paciente():
    os.system('cls')
    menu_cad()
    option = input('Qual sua opção? --> ')
    while option!='0':
        if option == '1':
                os.system('cls')
                #Adicionando paciente    
                print('DIGITE AS INFORMAÕES PEDIDAS.')
                nome = input('Nome Completo: ')
                nome_upper = nome.upper()
                nome = nome_upper.replace(' ', '') 
                while True: #VALIDAÇÃO DO PROF. FLAVIUS
                    cpf = input("Informe seu CPF: ")
                    cpf = cpf.replace('.', '')
                    cpf = cpf.replace('-', '')
                    cpf = cpf.replace(' ', '')
                    if validaCPF(cpf):
                            print("CPF Ok!")
                            break
                    else:
                            print("CPF Inválido!")
                

                            #DATA DE NASCIMENTO#
                while True:
                    print('''
                          |Data de nascimento, DIGITE APENAS NÚMEROS :|                     
                          ''')
                    day = (input('Qual o dia do seu nascimento? '))
                    month= (input('Qual o mês do seu nascimento? '))
                    year= (input('Qual o ano do seu nascimento? '))
                    data_nasc = day,month,year
                    try: #converter a entrada para um número de ponto flutuante.
                        day_float = float(day)
                        month_float = float(month)
                        year_float = float(year)
                        data_float = day_float, month_float,year_float
                        break
                    except ValueError: #indica que a entrada não é um número válido.
                        print('DIGITE APENAS NÚMEROS')

                '''while (month > 12) or (day > 31):
                     print('data invalida')
                     month = int(input('Qual o mês do seu nascimento? ')) 
                print('DATA DE NASCIMENTO: %d / %d / %d '(day,month,year)) 
                year_atual = data_atual.year() 

                idade = year_atual-year
                data_atual = 2024 #Colocar comando de pegar hora automático
                year= data_atual - idade
                '''
                genero = input('Qual o seu Gênero: M/F ')

                while True:
                     print('''
                          | DIGITE APENAS NÚMEROS :|                     
                          ''')
                     peso = input('Qual o seu peso atual: ')
                     altura =input('Qual a sua altura atual em metros: ')

                     try:                             
                        peso_float= float(peso)
                        altuta_float = float(altura) 
                        imc = peso_float / (altuta_float**2)   

                        break
                     except ValueError: #indica que a entrada não é um número válido.
                        print('DIGITE APENAS NÚMEROS')
                obj= input('''
                Qual o seu objetivo?
                1 - Perder peso
                2 - Ganhar peso
                                -->   ''')
                while obj !=  '1' and obj!='2':
                     print('Erro no cadastro, objetivo inválido')
                     obj = input('''
                Qual o seu objetivo?
                1 - Perder peso
                2 - Ganhar peso

''')
                cadastro[cpf] = [nome_upper,data_nasc,genero,peso,altura,imc,obj]
                # Imprimindo os dados dos pacientes em formato de coluna
                #os dados estão sendo armazenado no dicionário cadastro, chave CPF.
                print('NOME: ', cadastro[cpf][0])
                print(f'CPF: {cpf}')
                print('DATA DE NASCIMENTO: ' , cadastro[cpf][1],)
                print('GÊNERO: ', cadastro[cpf][2])
                print('PESO: ', cadastro[cpf][3], 'KG')
                print('ALTURA: ', cadastro[cpf][4])
                print('IMC: ', cadastro[cpf][5])
                print('OBJETIVO: ', cadastro[cpf][6])
                print('''
                          #######################
                ######### CADASTRADO COM SUCESSO ##########
                          #######################
                ''' )

                input('Tecle <ENTER> para continuar...') #colocar nas outras function
                menu_cad()
                option = input('Digite outra opção: ')
                print(cadastro[cpf])

                                # VERIFICAR#
        elif option == '2':
            while True:
                print('''
                          #######################
                ##########    VERIFICAR DADOS     ###########
                          #######################
                ''' )
                cpf = input('Digite seu CPF: ')           
                if cpf in cadastro:
                    print('NOME: ', cadastro[cpf][0])
                    print(f'CPF: ', cpf )
                    print('DATA DE NASCIMENTO: ' , cadastro[cpf][1])
                    print('GÊNERO: ', cadastro[cpf][2])
                    print('PESO: ', cadastro[cpf][3])
                    print('ALTURA: ', cadastro[cpf][4])
                    print('IMC: ', cadastro[cpf][5])
                    print('OBJETIVO: ', cadastro[cpf][6])
                    break


                #PEDIR O CPF PRA VERIFICAR AS INFORMAÇÕES
                elif cadastro == {}:
                    print('ERRO')
                    print('DADOS NÃO ENCONTRADOS!')
                    menu_cad()
                    option = input('Digite outra opção: ')
                    break


                else:
                    print('''
                          #############################################
                #########  ERRO, CPF INVÁLIDO, TENTE NOVAMENTE  #########
                          #############################################      
''')
                    menu_cad()
                    option = input('Digite outra opção: ')
                                                  

        elif option == '3':

            print('''
                          #######################
                #########      ALTERAR DADOS     ##########
                          #######################
                ''' )
            cpf = input('Digite seu CPF: ')
            if cpf in cadastro:              
                resp = input('VOCÊ TEM CERTEZA ? , alterar os seus dados ? S/N ')
                if resp.upper() == 'S':
                     print(cadastro[cpf])
                     #cadastro[cpf] = [0nome_upper,1data_nasc,2genero,3peso,4altura,5imc,6obj]
                     option = input('''
                    Qual informação deseja alterar?
                            [1]- NOME: 
                            [2]- CPF:        
                            [3]- DATA DE NASCIMENTO:   
                            [4]- GENERO:   
                            [5]- PESO:
                            [6]- ALTURA :
                            [7]- OBJETIVO:                                            
                    -->  ''')
                     if option == '1':
                        nome = input('Digite o novo NOME: ')
                        new_name= nome.upper()  
                        cadastro[cpf][0] = new_name                         
                        print('NOVO NOME CADASTRADO: ', cadastro[cpf][0])
                        menu_cad()
                        option = input('Digite outra opção: ')
                     elif option == '2':
                            new_cpf = input('DIGITE O NOVO CPF: ')
                            cadastro[new_cpf] = cadastro.pop(cpf)
                            print(f'NOVO CPF CADASTRADO: ', new_cpf )
                            menu_cad()
                            option = input('Digite outra opção: ')
                     elif option == '3':
                          new_date = input('Digite uma nova DATA DE NASCIMENTO: ')
                          cadastro[cpf][1] = new_date
                          print('NOVA  DATA CADASTRADA: ', cadastro[cpf][1])
                          menu_cad()
                          option = input('Digite outra opção: ')
                     elif option == '4':
                          new_gender = input('Digite o novo GÊNERO ')
                          cadastro[cpf][2] = new_gender
                          print('NOVO GÊNERO CADASTRADO: ', cadastro[cpf][2])
                          menu_cad()
                          option = input('Digite outra opção: ')
                     elif option == '5':
                          new_weight = input('Digite um novo PESO: ')
                          cadastro[cpf][3] = new_weight
                          print('NOVO PESO CADASTRADO: ', cadastro[cpf][3])
                          print('IMC ALTERADO, NOVO IMC --> ', cadastro[cpf][5])
                          menu_cad()
                          option = input('Digite outra opção: ')
                     elif option == '6':
                          new_height = input('Digite uma nova ALTURA: ')
                          cadastro[cpf][4] = new_height
                          print('NOVO PESO CADASTRADO: ', cadastro[cpf][4])
                          print('IMC ALTERADO, NOVO IMC --> ', cadastro[cpf][5])
                          menu_cad()
                          option = input('Digite outra opção: ')
                     elif option == '7':
                          new_obj = input('''
                Qual o novo objetivo?
                1 - Perder peso
                2 - Ganhar peso
                                -->   ''')
                          while obj !=  '1' and obj!='2':
                            print('Erro no cadastro, objetivo inválido')
                          obj = input('''
                Qual o novo objetivo?
                1 - Perder peso
                2 - Ganhar peso
-->  ''')
                          cadastro[cpf][6] = new_obj
                          print('NOVO OBJETIVO CADASTRADO: ', cadastro[cpf][6])
                          menu_cad()
                          option = input('Digite outra opção: ')
                     else:
                          print('ERRO AO TENTAR ALTERAR OS DADOS')
                          menu_cad()
                          option = input('Digite outra opção: ')

                else:
                     print('Voltou ao menu!')
                     menu_cad()
                     option = input('Digite outra opção: ')

            elif cadastro == {}:
                 print('ERRO')
                 print('Não possui cadastro, Cadastra-se !!!')
                 menu_cad()
                 option = input('Digite outra opção: ')
            else:
                print('Paciente inexistente')
                menu_cad()
                option = input('Digite outra opção: ')

        elif option == '4':            
             print('''
                          #######################
                #########      REMOVER USUÁRIO     ##########
                          #######################
                ''' )
             cpf = input('Digite seu CPF: ')
             if cpf in cadastro:
                option = input('Você deseja remover suas informações ? [S/N] ')
                if option.upper() == 'S':                        
                          del cadastro[cpf]                        
                          print('INFORMAÇÕES EXCLUIDA COM SUCESSO: ')
                          menu_cad()
                          option = input('Digite outra opção: ')
                else:
                    print("Exclusão não realizada!")
                    menu_cad()
                    option = input('Digite outra opção: ')                    
             else:
                print("Paciente inexistente!")
                input("Tecle <ENTER> para continuar...")
                menu_cad()
                option = input('Digite outra opção: ')


        elif option == '0':
            print('Fim do programa')
            main_menu()
            option = input('Digite outra opção: ')

        else:
            print('OPÇÃO INVÁLIDA!')
            menu_cad()
            option = input('Digite outra opção: ')

############################# MODULO 2 - Dietas.##########################################
def dieta():
    cad_dieta()
    option = input('Qual sua opção? --> ')
    while option != '0':
        if option == '1':
            print('CADASTRAR')
            cad_dieta()
            option = input('Qual sua opção? --> ')
        elif option == '2':
            print('VERIFICAR INFORMAÇÕES')
            cad_dieta()
            option = input('Qual sua opção? --> ')
        elif option == '3':
            print('ALTERAR DIETA')
            cad_dieta()
            option = input('Qual sua opção? --> ')
        elif option == '4':
            print('EXCLUIR DIETA')
            cad_dieta()
            option = input('Qual sua opção? --> ')
        elif option == '0':
             main_menu()
             option = input('Qual sua opção? --> ')
           
        else:
            print('OPÇÃO INVÁLIDA')
    #Alimentos alergicos 

############################ Modulo 3 - Cosulta ######################################
def agenda():
    print('MODULO AGENDAMENTO')
    agendamento()
    option = input('Qual a sua opção: ')
    if option == '1':
        print('AGENDAR CONSULTA')
    elif option == '2':
        print('VERIFICAR CONSULTA')
    elif option == '3':
        print('ALTERAR CONSULTA')
    elif option == '4':
        print('EXCLUIR CONSULTA')
    elif option == '0':
        main_menu()
    else:
        print('OPÇÃO INVÁLIDA')
    '''cpf = input('Digite seu CPF: ')
    if cpf in cadastro:
        print('conulta resultado')
    if cadastro == {}:
        print('ERRO')
        print('Não possui cadastro, Cadastra-se no modulo paciente.')'''

  #para imprimir a receita, Fazer meio q um login antes, com cpf de preferência!
  #imprimir a receita
  #Se não tiver todas as informações, dá erro avançar se as informações estiverem comPletas

################################### Modulo 4 - Minhas informações.##############################
def my_information():
  os.system('cls')
  print('''
  minhas informações:
  nome: Leandro Sérgio da Silva 
  curso: Sistema de informação
  Professor: Flaviu...
  instituição: UFRN-CAICO
  Github:Leo.sergio...
  e-mail: leandrooos222@gmail.com
  whatsapp: (84) 9 9619-7364
  Instagram:
  ''')
if __name__ == "__main__":
    main() #para inicializar a function main
    