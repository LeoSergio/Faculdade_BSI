import function
import validacao
import modulo1
import os

dieta = {}
def mod_dieta():
    function.cad_dieta()
    option = input('Qual sua opção? --> ')
    while option != '0':
        if option == '1': #Nome da dieta, alimentos alergicos,horario das refeições, horario das refeições
            print('CADASTRAR DIETA')
            cpf = input('Digite seu cpf: ')
            #validaCPF()
            if cpf in modulo1.cadastro:               
                name_dieta = input('Qual o nome da dieta? --> ')
                alergia = input('Algum comer alergico ? [S/N] ')
                if alergia.upper() == 'S':
                    alimento_alergia = input('Qual alimento você tem alergia? ')
                    alimento = 'ALERGIA: ', alimento_alergia
                else:
                    print( 'Não é alergico!')
                    alimento = 'Não tem alergia'
                    #INTERFACE
                print('''
                         CADASTRAR OBJETIVOS
''')
                obj = validacao.valida_obj(cpf)

                hora = validacao.hora(cpf)

                dieta[cpf] = [name_dieta, alimento, obj, hora]

                print('NOME DA DIETA: ', dieta[cpf][0])
                print( dieta[cpf][1],)
                print('OBJETIVO DA DIETA: ', dieta[cpf][2])
                print('HORÁRIO: ', dieta[cpf][3])
                print('IMC: ', modulo1.cadastro[cpf][5])
                print(validacao.plan_dieta(cpf))

                print('''
                          #######################
                ######### CADASTRADO COM SUCESSO ##########
                          #######################
                ''' )
                function.cad_dieta()
                option = input('Qual sua opção? --> ')
            else:
                 print('CPF inválido ou não encontrado, cadastre-se!!')
                 function.cad_dieta()
                 option = input('Qual sua opção? --> ')

        elif option == '2':
                print('''
                          #######################
                ##########    VERIFICAR DIETAS     ###########
                          #######################
                ''' )
                cpf = input('Digite seu CPF: ')           
                if cpf in modulo1.cadastro:
                    print('NOME DA DIETA: ', dieta[cpf][0])
                    print('ALERGIA: ', dieta[cpf][1])
                    print('OBJETIVO: ' , dieta[cpf][2])
                    print('HORARIO: ', dieta[cpf][3])
                    input('Tecle <ENTER> para continuar...') 
                    function.menu_cad()
                    option = input('Digite outra opção: ')
                else:
                    print('''
                          #############################################
                #########  ERRO, CPF INVÁLIDO, TENTE NOVAMENTE  #########
                          #############################################      
''')
                    input('Tecle <ENTER> para continuar...') 
                    function.menu_cad()
                    option = input('Digite outra opção: ')

        elif option == '3':
            print('''
                          #######################
                #########      ALTERAR DIETA     ##########
                          #######################
                ''' )
            cpf = input('Digite seu CPF: ')

            if cpf in modulo1.cadastro:              
                resp = input('VOCÊ TEM CERTEZA ? , alterar os seus dados ? S/N ')
                if resp.upper() == 'S':
                     print(dieta[cpf])
                     option = input('''
                    Qual informação deseja alterar?
                            [1]- NOME DA DIETA: 
                            [2]- ALERGIA:        
                            [3]- OBJETIVO:   
                            [4]- HORARIO:   

                    -->  ''')
                     if option == '1':
                        nome = input('Digite o novo NOME: ')
                        new_name= nome.upper()  
                        dieta[cpf][0] = new_name                         
                        print('NOVO NOME CADASTRADO: ', dieta[cpf][0])
                        

                     elif option == '2':
                            new_alergia = input('POSSUI ALGUM ALERGIA: [S/N] ')
                            dieta[cpf][1] = new_alergia
                            if dieta[cpf][1].upper() == 'S':
                                 alergia = input('Qual alimento você tem alergia: ')
                                 dieta[cpf][1] = alergia
                            elif dieta[cpf][1].upper() == 'N':
                                 dieta[cpf][1] == 'Não possiu Alergia'                                 
                            

                     elif option == '3':
                          obj=validacao.valida_obj(cpf)
                          print('NOPVO OBJETIVO CADASTRADO: ', obj )
                     elif option == '4':
                          hora = validacao.hora(cpf)
                          print('NOVO HORARIO CADASTRADO: ', hora )

                input('Tecle <ENTER> para continuar...')
                function.cad_dieta()
                option = input('Qual sua opção? --> ')

            elif dieta == {}:
                 print('ERRO')
                 print('Não possui cadastro, Cadastra-se !!!')
                 function.menu_cad()
                 option = input('Digite outra opção: ')
            else:
                print('Paciente inexistente')
                function.menu_cad()
                option = input('Digite outra opção: ')
            print('ALTERAR DIETA')
            function.cad_dieta()
            option = input('Qual sua opção? --> ')


        elif option == '4':
            print('EXCLUIR DIETA')
            function.cad_dieta()
            option = input('Qual sua opção? --> ')
        elif option == '0':
             function.main_menu()
             option = input('Qual sua opção? --> ')

        else:
            print('OPÇÃO INVÁLIDA')