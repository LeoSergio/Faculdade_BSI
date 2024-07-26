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
        resp = input('Já possui cadastro ? [S/N] --> ')
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