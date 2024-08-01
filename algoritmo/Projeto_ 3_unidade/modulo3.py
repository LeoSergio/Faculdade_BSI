import validacao
import function
import modulo1
import modulo2
import modulo3
import os

'''
Dados do Paciente:

Nome completo
CPF
Data de nascimento
Telefone de contato

Disponibilidade (dias e horários)

Detalhes do Agendamento:
Data do agendamento
Hora do agendamento
Local da consulta endereço
Duração prevista da consulta
Custo da consulta (se aplicável)

se cpf in dicionario aproveitar agendamento, se nao cadastrar novas informações:

'''
#COLOCAR O HORARIO DENTRO DE UM WHILE

def agendam(cadastro,cad_excluido,agendamento,agendamento_excluido):
    print('MODULO AGENDAMENTO')
    function.agendamento()
    option = input('Qual a sua opção: ')
    if option == '1':
        print('AGENDAR CONSULTA')
        os.system('cls')
                #Adicionando paciente    
        resp = input('Já possui cadastro de paciente? [S/N] --> ')
        if resp.upper() == 'S':
            cpf = input('Digite seu CPF: ').replace('.', '').replace('-', '').replace(' ', '')
            if cpf in cadastro:
                resp = input('Usar Dados do seu cadastro ? [S/N] ')
                if resp.upper() == 'S':
                     agendamento[cpf] = cadastro[cpf]
                     #add horario ao dicionario agendamento
                     agendado = validacao.agendar_consulta(agendamento)
                     agendamento[cpf] = agendado
                     print('NOME: ', cadastro[cpf][0])
                     print(f'CPF: {cpf}')
                     print('TELEFONE: ', cadastro[cpf][6])
                     print('DATA DE NASCIMENTO: ' , cadastro[cpf][1],)
                     print('GÊNERO: ', cadastro[cpf][2])
                     print('PESO: ', cadastro[cpf][3], 'KG')
                     print('ALTURA: ', cadastro[cpf][4])
                     print('IMC: ', cadastro[cpf][5])
                     print('DATA DA CONSULTA: ' , agendado)
                     print('Custo da consulta: R$50,00')       
                elif resp.upper() == 'N': #Não usar os dados do cadastro, usar outros dados.
                     print('DIGITE AS INFORMAÕES PEDIDAS.')
                     nome = input('Nome Completo: ')
                     nome_upper = nome.upper()
                     nome = nome_upper.replace(' ', '') 
                     while True: #VALIDAÇÃO DO PROF. FLAVIUS
                        cpf = input("Informe seu CPF: ")
                        cpf = cpf.replace('.', '')
                        cpf = cpf.replace('-', '')
                        cpf = cpf.replace(' ', '')
                        if cpf in cadastro and validacao.validaCPF(cpf):
                            print('USUARIO JÁ CADASTRADO')
                        elif validacao.validaCPF(cpf):
                                print("CPF Ok!")
                                break
                        else:
                                print("CPF Inválido!")

                     while True:
                        phone_number = input('Número de Tefefone: --> ')
                        if validacao.validate_phone(phone_number):
                            print()
                            break
                        else:
                            print('Número invalido')
                #ADD VALIDAÇÃO DE DATA
                     data_nasc = str(input(" Data de Nascimento: "))
                     while not validacao.date(data_nasc):
                        print("Data Inválida! Tente Novamente.\n(Insira a Data no Formato: xx/xx/xxxx)")
                        print()
                        data_nasc = str(input("-> "))
                        data_nasc = data_nasc.strip()
                        print()

                     while True:
                        genero = input('Qual o seu Gênero: M/F ')
                        if genero.upper() == 'M':
                            genero = 'MASCULINO'
                            break
                        elif genero.upper() =='F':
                            genero= 'FEMININO'
                            break
                        elif (genero.upper() != 'M') and (genero.upper() != 'F'):
                            print('''
                                ###############                  
                        ######### OPÇÃO INVALIDA ########
                                ###############                
        ''')
                     
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
                            imc = round(imc,2)   
                            break
                        except ValueError: #indica que a entrada não é um número válido.
                            print('DIGITE APENAS NÚMEROS')
                     print('HORARIO DA CONSULTA')
                     agendado = validacao.agendar_consulta(agendamento)
                      #ERRO, NÃO ESTA VERIFICANDO SE EXISTE  HORARIOS IGUAIS. CORRIGIR.
                     
                     agendamento[cpf] = [nome,data_nasc,genero,peso,altura,imc,phone_number,agendado]
                     
                     print(agendamento[cpf])
                    
                    # Imprimindo os dados dos pacientes em formato de coluna
                    #os dados estão sendo armazenado no dicionário cadastro, chave CPF.
                     print('NOME: ', agendamento[cpf][0])
                     print(f'CPF: {cpf}')
                     print('TELEFONE: ', agendamento[cpf][6])
                     print('DATA DE NASCIMENTO: ' , agendamento[cpf][1],)
                     print('GÊNERO: ', agendamento[cpf][2])
                     print('PESO: ', agendamento[cpf][3], 'KG')
                     print('ALTURA: ', agendamento[cpf][4])
                     print('IMC: ', agendamento[cpf][5])
                     print('DATA DA CONSULTA: ' , agendamento[cpf][7],)
                     print('Custo da consulta: R$50,00')

                     print('''
                            #######################
                    ######### CADASTRADO COM SUCESSO ##########
                            #######################
                    ''' )

                     input('Tecle <ENTER> para continuar...') #colocar nas outras function
                     function.agendamento()
                     option = input('Digite outra opção: ')
                     

            else:
                print(f'''
#############################################
#########  ERRO, CPF INVÁLIDO OU NÃO ENCONTRADO  #########
#############################################      
''')
                
        elif resp.upper() == 'N':
            print('''
                          ####################################
                #########             CADASTRE-SE             #########
                          ####################################      
''')
            input("Tecle <ENTER> para continuar...")
            modulo1.cad_paciente(cadastro,cad_excluido)
            
    elif option == '2':
        '''
        Falta mostar os arquivos em formato de coluna
        '''
        print('''
                          #######################
                ########## VERIFICAR AGENDAMENTO ###########
                          #######################
                ''' )
        cpf = input('Digite seu CPF: ')
        RED = "\033[91m"
        RESET = "\033[0m"
        agendamento[cpf]
        if cpf in agendamento:
            os.system('cls' if os.name == 'nt' else 'clear')
            print(f'''
            ##############################
            #       AGENDAMENTO         #
            ##############################
            ''')
           
            print('NOME: ', agendamento[cpf][0])
            print(f'CPF: {cpf}')
            print('TELEFONE: ', agendamento[cpf][6])
            print('DATA DE NASCIMENTO: ' , agendamento[cpf][1],)
            print('GÊNERO: ', agendamento[cpf][2])
            print('PESO: ', agendamento[cpf][3], 'KG')
            print('ALTURA: ', agendamento[cpf][4])
            print('IMC: ', agendamento[cpf][5])
            print('DATA DA CONSULTA: ' , agendamento[cpf][7],)
            print('Custo da consulta: R$50,00')
            input('Tecle <ENTER> para continuar...')         
        else:
            print(f'''
{RED}
    #############################################
    #########  ERRO, CPF INVÁLIDO OU NÃO ENCONTRADO  #########
    #############################################      
{RESET}
    ''')
            input('Tecle <ENTER> para continuar...') 
            function.agendamento()
    elif option == '3':
         os.system('cls')
         print('ALTERAR CONSULTA')
         print('''
                          #######################
                #########      ALTERAR DADOS     ##########
                          #######################
                ''' )
         cpf = input('Digite seu CPF: ')
         if cpf in agendamento:              
            resp = input('VOCÊ TEM CERTEZA ? , alterar os seus dados do agendamento ? S/N ')
            if resp.upper() == 'S':
                print(agendamento[cpf])
                    #agendamento[cpf] = [0nome,1data_nasc,2genero,3peso,4altura,5imc]
                option = input('''
                Qual informação deseja alterar?
                        [1]- NOME: 
                        [2]- CPF:        
                        [3]- DATA DE NASCIMENTO:
                        [4]- TELEFONE:   
                        [5]- GENERO:   
                        [6]- PESO:
                        [7]- ALTURA:
                        [8] DATA DO AGENDAMENTO
                        

                -->  ''')
                if option == '1':
                    nome = input('Digite o novo NOME: ')
                    new_name= nome.upper()  
                    agendamento[cpf][0] = new_name                         
                    print('NOVO NOME CADASTRADO: ', agendamento[cpf][0])
                    function.agendamento()
                    option = input('Digite outra opção: ')
                    
                elif option == '2':
                        new_cpf = input('DIGITE O NOVO CPF: ')
                        agendamento[new_cpf] = agendamento.pop(cpf)
                        print(f'NOVO CPF CADASTRADO: ', new_cpf )
                        function.agendamento()
                        option = input('Digite outra opção: ')
                elif option == '3':
                        new_date = input('Digite uma nova DATA DE NASCIMENTO: ')
                        agendamento[cpf][1] = new_date
                        print('NOVA  DATA CADASTRADA: ', agendamento[cpf][1])
                        function.agendamento()
                        option = input('Digite outra opção: ')
                elif option == '4':
                        new_number = input('Digite um novo NÚMERO DE TELEFONE: ')
                        agendamento[cpf][1] = new_number
                        print('NOVA  DATA CADASTRADA: ', agendamento[cpf][1])
                        function.agendamento()
                        option = input('Digite outra opção: ')
                elif option == '5':
                        new_gender = input('Digite o novo GÊNERO ')
                        agendamento[cpf][2] = new_gender
                        print('NOVO GÊNERO CADASTRADO: ', agendamento[cpf][2])
                        function.agendamento()
                        option = input('Digite outra opção: ')
                elif option == '6':
                        new_weight = input('Digite um novo PESO: ')
                        agendamento[cpf][3] = new_weight
                        print('NOVO PESO CADASTRADO: ', agendamento[cpf][3])
                        print('IMC ALTERADO, NOVO IMC --> ', agendamento[cpf][5])
                        function.agendamento()
                        option = input('Digite outra opção: ')
                elif option == '7':
                        new_height = input('Digite uma nova ALTURA: ')
                        agendamento[cpf][4] = new_height
                        print('NOVO PESO CADASTRADO: ', agendamento[cpf][4])
                        print('IMC ALTERADO, NOVO IMC --> ', agendamento[cpf][5])
                        function.agendamento()
                        option = input('Digite outra opção: ')
                else:
                        print('ERRO AO TENTAR ALTERAR OS DADOS')
                        function.agendamento()
                        option = input('Digite outra opção: ')

            else:
                    print('Voltou ao menu!')
                    function.agendamento()
                    option = input('Digite outra opção: ')

         else:
            print('CPF NÃO ENCONTRADO OU NÃO CADASTRADO')
            function.agendamento()
            option = input('Digite outra opção: ')



    elif option == '4':
        print('EXCLUIR CONSULTA')
        print('''
                          #######################
                #########   REMOVER AGENDAMENTO  ##########
                          #######################
                ''' )
        cpf = input('Digite seu CPF: ')
        if cpf in agendamento:
            option = input('Você deseja remover suas informações ? [S/N] ')
            if option.upper() == 'S':                        
                        agendamento_excluido[cpf] = agendamento[cpf] 
                        del agendamento[cpf]
                        print(agendamento_excluido[cpf])                       
                        print('INFORMAÇÕES EXCLUIDA COM SUCESSO: ')
                        function.agendamento()
                        option = input('Digite outra opção: ')
            else:
                print("Exclusão não realizada!")
                function.agendamento()
                option = input('Digite outra opção: ')                    
        else:
            print("Paciente inexistente!")
            input("Tecle <ENTER> para continuar...")
            function.agendamento()
            option = input('Digite outra opção: ')
    elif option == '5':
             os.system('cls')
             crn = input('digite o CRN: -->') #Conselho Federal de Nutrição
             function.reports_scheduling(agendamento,agendamento_excluido)
    
    elif option == '0':
        function.main_menu()
    else:
        print('OPÇÃO INVÁLIDA')