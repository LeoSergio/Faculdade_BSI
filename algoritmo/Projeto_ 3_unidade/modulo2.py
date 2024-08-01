import function
import validacao
import modulo1
import os


def mod_dieta(cadastro,dietas,dietas_excluida):
    function.cad_dieta()
    option = input('Qual sua opção? --> ')
    while option != '0':
        if option == '1': #Nome da dieta, alimentos alergicos,horario das refeições, horario das refeições
            print('CADASTRAR DIETA')
            cpf = input("Informe seu CPF: ")
            cpf = cpf.replace('.', '')
            cpf = cpf.replace('-', '')
            cpf = cpf.replace(' ', '')
            if cpf in cadastro:
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
                obj = validacao.valida_obj(cadastro,cpf,dietas)

#13971335462
                dietas[nome] = [nome,alimento, obj,cpf]

                print('NOME DA DIETA: ', {nome})
                print( dietas[nome][1],)
                print('OBJETIVO DA DIETA: ', dietas[nome][2])
                print(validacao.plan_dieta(cadastro,cpf))

                print('''
                            #######################
                ######### CADASTRADO COM SUCESSO ##########
                            #######################
                ''' )
                function.cad_dieta()
                option = input('Qual sua opção? --> ')
        
            else:
                print('CPF INVALIDO OU NÃO CADASTRADO')
                function.cad_dieta()
                option = input('Qual sua opção? --> ')
        elif option == '2':
                print('''
                          #######################
                ##########    VERIFICAR DIETAS     ###########
                          #######################
                ''' )
                cpf = input('Digite seu cpf: ')
                if cpf in dietas:
                    nome =  validacao.exibir_dieta(cadastro,cpf,dietas)
                    input('Tecle <ENTER> para continuar...') 
                    function.cad_dieta()
                    option = input('Digite outra opção: ')
                else:
                    print('''
                          #############################################
                #########  ERRO, CPF INVÁLIDO OU NÃO ENCONTRADO    #########
                          #############################################      
''')
                    input('Tecle <ENTER> para continuar...') 
                    function.cad_dieta()
                    option = input('Digite outra opção: ')

        elif option == '3':
            print('''
                          #######################
                #########      ALTERAR DIETAs     ##########
                          #######################
                ''' )
            cpf = input('Digite seu CPF: ')

            if cpf in cadastro:              
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
                        nome_antigo = input('Digite o NOME DA DIETA atual que deseja editar: ')
                        new_name = input('Digite o novo NOME: ').upper()

                        if nome_antigo in dietas:
                            dietas[new_name] = dietas.pop(nome_antigo)
                            print(f'NOME ATUALIZADO: {nome_antigo} para {new_name}')
                        else:
                            print(f'O nome "{nome_antigo}" não foi encontrado no dicionário.')
                       
                        
                     elif option == '2':
                            new_alergia = input('POSSUI ALGUM ALERGIA: [S/N] ')
                            dietas[nome][0] = new_alergia
                            if dietas[nome][0].upper() == 'S':
                                 alergia = input('Qual alimento você tem alergia: ')
                                 dietas[nome][0] = alergia
                            elif dietas[nome][0].upper() == 'N':
                                 dietas[nome][0] == 'Não possiu Alergia'                                 
                            

                     elif option == '3':
                          obj=validacao.valida_obj(cadastro,cpf,dietas)
                          print('NOPVO OBJETIVO CADASTRADO: ', obj )
                     elif option == '4':
                          hora = validacao.hora(cpf)
                          print('NOVO HORARIO CADASTRADO: ', hora )

                input('Tecle <ENTER> para continuar...')
                function.cad_dieta()
                option = input('Qual sua opção? --> ')

            else:
                print('''
                          #############################################
                #########  ERRO, CPF INVÁLIDO OU NÃO ENCONTRADO    #########
                          #############################################      
''')
                input('Tecle <ENTER> para continuar...')
                function.cad_dieta()
                option = input('Digite outra opção: ')
            


        elif option == '4':
            print('EXCLUIR DIETA')
            os.system('cls')           
            print('''
                          #######################
                #########      REMOVER DIETA     ##########
                          #######################
                ''' )
            cpf = input('Digite seu CPF: ').replace('.', '').replace('-', '').replace(' ', '')
            if cpf in cadastro:           
                option = input('Você deseja remover suas informações ? [S/N] ')
                if option.upper() == 'S':
                    nome = input('Digite o nome da dieta: ')
                    nome = validacao.valida_nome(nome)
                    if nome:
                        if nome in dietas:
                            dietas_excluida[nome] = dietas[nome]
                            del dietas[nome]
                            print('INFORMAÇÕES EXCLUÍDAS COM SUCESSO: ')
                        else:
                            print('NOME INVÁLIDO OU NÃO ENCONTRADO')
                    else:
                        print('Nome da dieta inválido.')
                elif option.upper() == 'N':
                    print("Exclusão não realizada!")
                else:
                    print('OPÇÃO INVÁLIDA')                    
            else:
                print('''
                          #############################################
                #########  ERRO, CPF INVÁLIDO OU NÃO ENCONTRADO    #########
                          #############################################      
''')

            input("Tecle <ENTER> para continuar...")
            function.cad_dieta()
            option = input('Digite outra opção: ')
        #PEGAR OS DADOS QUE SERIAM EXCLUIDOS COLOCAR EM UM DICIONARIO VAZIO.
        elif option == '5':
             os.system('cls')
             cpf = input('Digite seu CPF: ')
             if cpf in cadastro:
                  dietas[cpf]=validacao.plan_dieta(cadastro,cpf)
                  input('Tecle <ENTER> para continuar...')
                  function.cad_dieta()
                  option = input('Digite outra opção: ')
             else:
                  print('CPF invalido ou não Cadastrado ')
                  input('Tecle <ENTER> para continuar...')
                  function.cad_dieta()
                  option = input('Digite outra opção: ')
        elif option == '6':
             os.system('cls')
             crn = input('digite o CRN: -->') #Conselho Federal de Nutrição
             function.reports_diets(dietas, dietas_excluida,cadastro)
             function.cad_dieta()
             option = input('Digite outra opção: ')
        elif option == '0':
             function.main_menu()
             option = input('Qual sua opção? --> ')

        else:
            print('OPÇÃO INVÁLIDA')