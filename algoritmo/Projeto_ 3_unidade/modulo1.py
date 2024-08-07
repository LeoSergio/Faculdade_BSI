import validacao
import function
import os
     ##########################################
##### Projeto Planejamento de Dietas      #####
     #########################################



############################ MODULO1-CADASTRAMENTO DE PACIENTES ###############################
def cad_paciente(cadastro,cad_excluido):
    os.system('cls')
    function.menu_cad()
    option = input('Qual sua opção? --> ')
    while option!='0':
        if option == '1':
               os.system('cls')
                #Adicionando paciente
               RED =   "\033[91m"
               GREEN = "\033[91m"
               RESET = "\033[0m"

               # Inform user to enter the required information
               print('''
               
               ===========================================
                    DIGITE AS INFORMAÇÕES PEDIDAS
               ===========================================
               
               ''')

               # Input for name
               nome = input('Nome Completo: ')
               nome_upper = nome.upper()
               nome = nome_upper.replace(' ', '') 

               # CPF validation loop
               while True:  # VALIDAÇÃO DO PROF. FLAVIUS
                    cpf = input("Informe seu CPF: ")
                    cpf = cpf.replace('.', '')
                    cpf = cpf.replace('-', '')
                    cpf = cpf.replace(' ', '')
                    if cpf in cadastro and validacao.validaCPF(cpf):
                         print(f'{RED}USUÁRIO JÁ CADASTRADO{RESET}')
                    elif validacao.validaCPF(cpf):
                         print("CPF Ok!")
                         break
                    else:
                         print(f'{RED}CPF INVÁLIDO!{RESET}')

               # Phone number validation loop
               while True:
                    phone_number = input('Número de Telefone: --> ')
                    if validacao.validate_phone(phone_number):
                         print(f'{RED}Número de telefone válido!{RESET}')
                         break
                    else:
                         print(f'{RED}Número inválido{RESET}')

               # Date of birth validation loop
               data_nasc = str(input("Data de Nascimento (xx/xx/xxxx): "))
               while not validacao.date(data_nasc):
                    print(f'{RED}Data Inválida! Tente Novamente.\n(Insira a Data no Formato: xx/xx/xxxx){RESET}')
                    data_nasc = str(input("-> "))
                    data_nasc = data_nasc.strip()
                    print()

               # Gender validation loop
               while True:
                    genero = input('Qual o seu Gênero (M/F): ')
                    if genero.upper() == 'M':
                         genero = 'MASCULINO'
                         break
                    elif genero.upper() == 'F':
                         genero = 'FEMININO'
                         break
                    else:
                         print(f'''
                    {GREEN}
                    ===========================================
                         OPÇÃO INVÁLIDA! DIGITE M OU F
                    ===========================================
                    {RESET}
                    ''')

               # Weight and height input with numeric validation
               while True:
                    print('''
                    {GREEN}
                    ===========================================
                         DIGITE APENAS NÚMEROS
                    ===========================================
                    {RESET}
                    ''')
                    peso = input('Qual o seu peso atual (kg): ')
                    altura = input('Qual a sua altura atual em metros: ')

                    try:
                         peso_float = float(peso)
                         altura_float = float(altura)
                         imc = peso_float / (altura_float**2)
                         imc = round(imc, 2)
                         break
                    except ValueError:  # Indicates invalid number input
                         print(f'''
                    {RED}
                    ===========================================
                    DIGITE APENAS NÚMEROS VÁLIDOS!
                    ===========================================
                    {RESET}
                         ''')


               cadastro[cpf] = [nome,data_nasc,genero,peso,altura,imc,phone_number]

                # Imprimindo os dados dos pacientes em formato de coluna
                #os dados estão sendo armazenado no dicionário cadastro, chave CPF.
               function.display_patient_info(cpf, cadastro)
                

               input('Tecle <ENTER> para continuar...') #colocar nas outras function
               function.menu_cad()
               option = input('Digite outra opção: ')
                

                                # VERIFICAR#
        elif option == '2':
                os.system('cls')
                print('''
                          #######################
                ##########    VERIFICAR DADOS     ###########
                          #######################
                ''' )
                cpf = input('Digite seu CPF: ')           
                if cpf in cadastro:
                    function.display_patient_info(cpf,cadastro)
                    input('Tecle <ENTER> para continuar...') 
                    function.menu_cad()
                    option = input('Digite outra opção: ')
                    
                else:
                    RED = "\033[91m"
                    RESET = "\033[0m"
                    print(f'''
{RED}
          #############################################
#########    ERRO, CPF INVÁLIDO OU NÃO ENCONTRADO     #########
          ############################################# 
{RESET}
                                   ''')
                    function.menu_cad()
                    option = input('Digite outra opção: ')
                    
        elif option == '3':
            os.system('cls')

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
                     #cadastro[cpf] = [0nome,1data_nasc,2genero,3peso,4altura,5imc]
                     option = input('''
                    Qual informação deseja alterar?
                            [1]- NOME: 
                            [2]- CPF:        
                            [3]- DATA DE NASCIMENTO:   
                            [4]- GENERO:   
                            [5]- PESO:
                            [6]- ALTURA :

                    -->  ''')
                     if option == '1':
                        nome = input('Digite o novo NOME: ')
                        new_name= nome.upper()  
                        cadastro[cpf][0] = new_name                         
                        print('NOVO NOME CADASTRADO: ', cadastro[cpf][0])
                        function.menu_cad()
                        option = input('Digite outra opção: ')
                     elif option == '2':
                            new_cpf = input('DIGITE O NOVO CPF: ')
                            cadastro[new_cpf] = cadastro.pop(cpf)
                            print(f'NOVO CPF CADASTRADO: ', new_cpf )
                            function.menu_cad()
                            option = input('Digite outra opção: ')
                     elif option == '3':
                          new_date = input('Digite uma nova DATA DE NASCIMENTO: ')
                          cadastro[cpf][1] = new_date
                          print('NOVA  DATA CADASTRADA: ', cadastro[cpf][1])
                          function.menu_cad()
                          option = input('Digite outra opção: ')
                     elif option == '4':
                          new_gender = input('Digite o novo GÊNERO ')
                          cadastro[cpf][2] = new_gender
                          print('NOVO GÊNERO CADASTRADO: ', cadastro[cpf][2])
                          function.menu_cad()
                          option = input('Digite outra opção: ')
                     elif option == '5':
                          new_weight = input('Digite um novo PESO: ')
                          cadastro[cpf][3] = new_weight
                          print('NOVO PESO CADASTRADO: ', cadastro[cpf][3])
                          print('IMC ALTERADO, NOVO IMC --> ', cadastro[cpf][5])
                          function.menu_cad()
                          option = input('Digite outra opção: ')
                     elif option == '6':
                          new_height = input('Digite uma nova ALTURA: ')
                          cadastro[cpf][4] = new_height
                          print('NOVO PESO CADASTRADO: ', cadastro[cpf][4])
                          print('IMC ALTERADO, NOVO IMC --> ', cadastro[cpf][5])
                          function.menu_cad()
                          option = input('Digite outra opção: ')

                     else:
                          print('ERRO AO TENTAR ALTERAR OS DADOS')
                          function.menu_cad()
                          option = input('Digite outra opção: ')

                else:
                     print('Voltou ao menu!')
                     function.menu_cad()
                     option = input('Digite outra opção: ')

            else:
                 RED = "\033[91m"
                 RESET = "\033[0m"
                 print(f'''
{RED}
          #############################################
#########    ERRO, CPF INVÁLIDO OU NÃO ENCONTRADO    #########
          ############################################# 
{RESET}
                                   ''')
                 function.menu_cad()
                 option = input('Digite outra opção: ')

        elif option == '4': 
             os.system('cls')           
             print('''
                          #######################
                #########      REMOVER USUÁRIO     ##########
                          #######################
                ''' )
             cpf = input('Digite seu CPF: ')
             if cpf in cadastro:
                option = input('Você deseja remover suas informações ? [S/N] ')
                if option.upper() == 'S':                        
                          cad_excluido[cpf] = cadastro[cpf] 
                          del cadastro[cpf]
                          print(cad_excluido[cpf])                       
                          print('INFORMAÇÕES EXCLUIDA COM SUCESSO: ')
                          function.menu_cad()
                          option = input('Digite outra opção: ')
                else:
                    print("Exclusão não realizada!")
                    function.menu_cad()
                    option = input('Digite outra opção: ')                    
             else:
                print("Paciente inexistente!")
                input("Tecle <ENTER> para continuar...")
                function.menu_cad()
                option = input('Digite outra opção: ')

        elif option == '5':
             os.system('cls')
             crn = input('digite o CRN: -->') #Conselho Federal de Nutrição
             function.reports_clients(cadastro,cad_excluido)
             function.menu_cad()
             option = input('Digite outra opção: ')
             
        elif option == '0':
            os.system('cls')
            print('Fim do programa')
            function.main_menu()
            option = input('Digite outra opção: ')

        else:
          RED = "\033[91m"
          RESET = "\033[0m"
          print(f'''
{RED}
         ###############                  
######### OPÇÃO INVALIDA ########
          ############### 
{RESET}
                              ''')
          function.menu_cad()
          option = input('Digite outra opção: ')
