import validacao
import function

cadastro = {}
############################ MODULO1-CADASTRAMENTO DE PACIENTES ###############################
def cad_paciente():
    function.menu_cad()
    option = input('Qual sua opção? --> ')
    while option!='0':
        if option == '1':
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
                    if validacao.validaCPF(cpf):
                            print("CPF Ok!")
                            break
                    else:
                            print("CPF Inválido!")


                            #DATA DE NASCIMENTO#
                print('''
                    DATA DE NASCIMENTO
''')
                ano = input('Qual o ano do seu nascimento? ')
                mes = input('Qual o mês do seu nascimento? ')
                dia = input('Qual o dia do seu nascimento? ')
                data_nasc = ano,mes,dia
                validacao.dataNasc()

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


                cadastro[cpf] = [nome,data_nasc,genero,peso,altura,imc]
                # Imprimindo os dados dos pacientes em formato de coluna
                #os dados estão sendo armazenado no dicionário cadastro, chave CPF.
                print('NOME: ', cadastro[cpf][0])
                print(f'CPF: {cpf}')
                print('DATA DE NASCIMENTO: ' , cadastro[cpf][1],)
                print('GÊNERO: ', cadastro[cpf][2])
                print('PESO: ', cadastro[cpf][3], 'KG')
                print('ALTURA: ', cadastro[cpf][4])
                print('IMC: ', cadastro[cpf][5])

                print('''
                          #######################
                ######### CADASTRADO COM SUCESSO ##########
                          #######################
                ''' )

                input('Tecle <ENTER> para continuar...') #colocar nas outras function
                function.menu_cad()
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

                    break


                #PEDIR O CPF PRA VERIFICAR AS INFORMAÇÕES
                elif cadastro == {}:
                    print('ERRO')
                    print('DADOS NÃO ENCONTRADOS!')
                    function.menu_cad()
                    option = input('Digite outra opção: ')
                    break


                else:
                    print('''
                          #############################################
                #########  ERRO, CPF INVÁLIDO, TENTE NOVAMENTE  #########
                          #############################################      
''')
                    function.menu_cad()
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

            elif cadastro == {}:
                 print('ERRO')
                 print('Não possui cadastro, Cadastra-se !!!')
                 function.menu_cad()
                 option = input('Digite outra opção: ')
            else:
                print('Paciente inexistente')
                function.menu_cad()
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


        elif option == '0':
            print('Fim do programa')
            function.main_menu()
            option = input('Digite outra opção: ')

        else:
            print('OPÇÃO INVÁLIDA!')
            function.menu_cad()
            option = input('Digite outra opção: ')