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

                obj= input('''
                    Cadastrar objetivo:
                    1 - Perder peso
                    2 - Ganhar Massa Muscular
                                    -->   ''')
                while obj !=  '1' and obj!='2':
                        print('Erro no cadastro, objetivo inválido')
                        obj = input('''
                    Qual o seu objetivo?
                    1 - Perder peso
                    2 - Ganhar peso

    ''')
                if obj == '1':
                     obj = 'Perder peso'
                elif obj == '2':
                     obj = 'Ganhar Massa muscular'

                hora = input('''Quais os horarios das refeições?
                              1 - Manhâ
                              2 - Tarde
                              3- Cafe da tarde
                              4 - Noite                                                     
                              ''')
                while hora !=  '1' and hora !='2' and hora !='3' and hora !='4':
                        print('Erro no cadastro, Horario inválido')
                        hora = input('''Quais os horarios das refeições?
                              1 - Manhâ
                              2 - Tarde
                              3- Cafe da tarde
                              4 - Noite                                                     
                              ''')
                if hora == '1':
                     hora = 'Manhâ'
                elif hora == '2':
                     hora = 'Tarde'
                elif hora == '3':
                     hora = 'Cafe da tarde'
                elif hora == '4':
                     hora = 'Noite'

                dieta[cpf] = [name_dieta, alimento, obj, hora]
                function.cad_dieta()
                option = input('Qual sua opção? --> ')
            else:
                 print('CPF inválido ou não encontrado, cadastre-se!!')
                 function.cad_dieta()
                 option = input('Qual sua opção? --> ')

        elif option == '2':
             while True:
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
                        function.menu_cad()
                        option = input('Digite outra opção: ')

                     elif option == '2':
                            new_alergia = input('POSSUI ALGUM ALERGIA: [S/N] ')
                            dieta[cpf][1] = new_alergia
                            if dieta[cpf][1].upper() == 'S':
                                 alergia = input('Qual alimento você tem alergia: ')
                                 dieta[cpf][1] = alergia
                            elif dieta[cpf][1].upper() == 'N':
                                 dieta[cpf][1] == 'Não possiu Alergia'                                 
                            function.menu_cad()
                            option = input('Digite outra opção: ')

                     elif option == '3':
                          new_obj = input('Digite um novo objetivo: ')
                          new_obj= input('''
                    Cadastrar objetivo:
                    1 - Perder peso
                    2 - Ganhar Massa Muscular
                                    -->   ''')
                          while new_obj !=  '1' and new_obj!='2':
                                    print('Erro no cadastro, objetivo inválido')
                                    new_obj = input('''
                                Qual o seu objetivo?
                                1 - Perder peso
                                2 - Ganhar peso

    ''')
                          if new_obj == '1':
                                new_obj = 'Perder peso'
                          elif new_obj == '2':
                                new_obj = 'Ganhar Massa muscular'
                                dieta[cpf][2] = new_obj
                                print('NOVO OBJETIVO CADASTRADO: ', dieta[cpf][2])
                                function.menu_cad()
                                option = input('Digite outra opção: ')
                     elif option == '4':
                          new_hora = input('''Quais os horarios das refeições?
                              1 - Manhâ
                              2 - Tarde
                              3- Cafe da tarde
                              4 - Noite                                                     
                              ''')
                while new_hora !=  '1' and new_hora !='2' and new_hora !='3' and new_hora !='4':
                        print('Erro no cadastro, Horario inválido')
                        new_hora = input('''Quais os horarios das refeições?
                              1 - Manhâ
                              2 - Tarde
                              3- Cafe da tarde
                              4 - Noite                                                     
                              ''')
                if new_hora == '1':
                     new_hora = 'Manhâ'
                elif new_hora == '2':
                     new_hora = 'Tarde'
                elif new_hora == '3':
                     new_hora = 'Cafe da tarde'
                elif new_hora == '4':
                     new_hora = 'Noite'

                dieta[cpf][3]= new_hora
                print('NOVO HORARIO CADASTRADO: ', dieta[cpf][3])
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