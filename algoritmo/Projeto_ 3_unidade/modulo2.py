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
            cpf = input("Informe seu CPF: ")
            cpf = cpf.replace('.', '')
            cpf = cpf.replace('-', '')
            cpf = cpf.replace(' ', '')
            if cpf in modulo1.cadastro:
                nome = input('Digite o nome da dieta: ')
                nome = validacao.valida_nome(nome)
                
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

                print('''
                            CADASTRAR HORÁRIO
    ''')
                hora = validacao.hora(cpf)

                dieta[nome] = [alimento, obj, hora,cpf]

                print('NOME DA DIETA: ', {nome})
                print( dieta[nome][1],)
                print('OBJETIVO DA DIETA: ', dieta[nome][1])
                print('HORÁRIO: ', dieta[nome][2])
                print(validacao.plan_dieta(cpf))

                print('''
                            #######################
                ######### CADASTRADO COM SUCESSO ##########
                            #######################
                ''' )
                function.cad_dieta()
                option = input('Qual sua opção? --> ')
           

        elif option == '2':
                print('''
                          #######################
                ##########    VERIFICAR DIETAS     ###########
                          #######################
                ''' )
                cpf = input('Digite seu cpf: ')
                nome =  validacao.exibir_dieta()
                input('Tecle <ENTER> para continuar...') 
                function.cad_dieta()
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
                        dieta[nome] = new_name                         
                        print('NOVO NOME CADASTRADO: ', {nome})
                        
                     elif option == '2':
                            new_alergia = input('POSSUI ALGUM ALERGIA: [S/N] ')
                            dieta[nome][0] = new_alergia
                            if dieta[nome][0].upper() == 'S':
                                 alergia = input('Qual alimento você tem alergia: ')
                                 dieta[nome][0] = alergia
                            elif dieta[nome][0].upper() == 'N':
                                 dieta[nome][0] == 'Não possiu Alergia'                                 
                            

                     elif option == '3':
                          obj=validacao.valida_obj(cpf)
                          print('NOPVO OBJETIVO CADASTRADO: ', obj )
                     elif option == '4':
                          hora = validacao.hora(cpf)
                          print('NOVO HORARIO CADASTRADO: ', hora )

                input('Tecle <ENTER> para continuar...')
                function.cad_dieta()
                option = input('Qual sua opção? --> ')

            else:
                print('Paciente inexistente')
                input('Tecle <ENTER> para continuar...')
                function.cad_dieta()
                option = input('Digite outra opção: ')
            


        elif option == '4':
            print('EXCLUIR DIETA')
            #PEGAR OS DADOS QUE SERIAM EXCLUIDOS COLOCAR EM UM DICIONARIO VAZIO.
            function.cad_dieta()
            option = input('Qual sua opção? --> ')
        elif option == '0':
             function.main_menu()
             option = input('Qual sua opção? --> ')

        else:
            print('OPÇÃO INVÁLIDA')