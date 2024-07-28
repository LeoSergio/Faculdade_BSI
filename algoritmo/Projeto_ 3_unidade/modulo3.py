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


def agendam():
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
            if cpf in modulo1.cadastro:
                print('NOME: ', modulo1.cadastro[cpf][0])
                #print(f'CPF: ', modulo1.cadastro.cpf )
                print('DATA DE NASCIMENTO: ' , modulo1.cadastro[cpf][1])
                print('GÊNERO: ', modulo1.cadastro[cpf][2])
                resp = input('Alterar Dados do cadastro ? ')
                if resp.upper() == 'S':
                     option = input('''
                    Qual informação deseja alterar?
                            [1]- NOME: 
                            [2]- CPF:        
                            [3]- DATA DE NASCIMENTO:   
                            [4]- GENERO:   
                    -->  ''')
                     if option == '1':
                        nome = input('Digite o novo NOME: ')
                        new_name= nome.upper()  
                        modulo1.cadastro[cpf][0] = new_name                         
                        print('NOVO NOME CADASTRADO: ', modulo1.cadastro[cpf][0])
                        function.menu_cad()
                        option = input('Digite outra opção: ')
                     elif option == '2':
                            new_cpf = input('DIGITE O NOVO CPF: ')
                            modulo1.cadastro[new_cpf] = modulo1.cadastro.pop(cpf)
                            print(f'NOVO CPF CADASTRADO: ', new_cpf )
                            function.menu_cad()
                            option = input('Digite outra opção: ')
                     elif option == '3':
                          new_date = input('Digite uma nova DATA DE NASCIMENTO: ')
                          modulo1.cadastro[cpf][1] = new_date
                          print('NOVA  DATA CADASTRADA: ', modulo1.cadastro[cpf][1])
                          function.menu_cad()
                          option = input('Digite outra opção: ')
                     elif option == '4':
                          new_gender = input('Digite o novo GÊNERO ')
                          modulo1.cadastro[cpf][2] = new_gender
                          print('NOVO GÊNERO CADASTRADO: ', modulo1.cadastro[cpf][2])
                          function.menu_cad()
                          option = input('Digite outra opção: ')
                     



        if resp.upper() == 'N':
            print('DIGITE AS INFORMAÕES PEDIDAS.')
            nome = input('Nome Completo: ')
            nome_upper = nome.upper()
            nome = nome_upper.replace(' ', '') 
            while True: #VALIDAÇÃO DO PROF. FLAVIUS
                cpf = input("Informe seu CPF: ")
                cpf = cpf.replace('.', '')
                cpf = cpf.replace('-', '')
                cpf = cpf.replace(' ', '')
                if cpf in modulo1.cadastro and validacao.validaCPF(cpf):
                        print('USUARIO JÁ CADASTRADO')
                elif validacao.validaCPF(cpf):
                        print("CPF Ok!")
                        break
                else:
                        print("CPF Inválido!")

            ##################################################
            phone_number = input('Número de Tefefone: --> ')
            validacao.validate_phone(phone_number)
            #ADD VALIDAÇÃO DE DATA
            

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
                            ############### ''')   
    elif option == '2':
        print('VERIFICAR CONSULTA')
    elif option == '3':
        print('ALTERAR CONSULTA')
    elif option == '4':
        print('EXCLUIR CONSULTA')
    elif option == '0':
        function.main_menu()
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