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
agendamento = {}

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
                resp = input('Usar Dados do seu cadastro ? [S/N] ')
                if resp.upper() == 'S':
                     agendamento[cpf] = modulo1.cadastro
                     #add horario ao dicionario agendamento
                     print(agendamento[cpf])
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
                        if cpf in modulo1.cadastro and validacao.validaCPF(cpf):
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
                     print('HORARIO DA CONSULTA')
                     agendado = validacao.agendar_consulta() #ERRO, NÃO ESTA VERIFICANDO SE EXISTE  HORARIOS IGUAIS. CORRIGIR.
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

                     
                


                     agendamento[cpf] = [nome,data_nasc,genero,peso,altura,imc,phone_number,agendado]

                    # Imprimindo os dados dos pacientes em formato de coluna
                    #os dados estão sendo armazenado no dicionário cadastro, chave CPF.
                     print('NOME: ', agendamento[cpf][0])
                     print(f'CPF: {cpf}')
                     print('TELEFONE: ', agendamento[cpf][6])
                     print('DATA DE NASCIMENTO: ' , agendamento[cpf][1],)
                     print('DATA DA CONSULTA: ' , agendamento[cpf][7],)
                     print('GÊNERO: ', agendamento[cpf][2])
                     print('PESO: ', agendamento[cpf][3], 'KG')
                     print('ALTURA: ', agendamento[cpf][4])
                     print('IMC: ', agendamento[cpf][5])

                     print('''
                            #######################
                    ######### CADASTRADO COM SUCESSO ##########
                            #######################
                    ''' )

                     input('Tecle <ENTER> para continuar...') #colocar nas outras function
                     function.menu_cad()
                     option = input('Digite outra opção: ')
                     



        elif resp.upper() == 'N':
            print('''
                          ####################################
                #########             CADASTRE-SE             #########
                          ####################################      
''')
            input("Tecle <ENTER> para continuar...")
            modulo1.cad_paciente()
            
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