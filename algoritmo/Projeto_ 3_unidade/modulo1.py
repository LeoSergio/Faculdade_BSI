import validacao
import function
import modulo1
import modulo2
import os
     ##########################################
##### Projeto Planejamento de Dietas      #####
     #########################################


cadastro = {#nome,genero,peso,altura,imc
     
}
cad_excluido = {

}

#FAZER O RELATORIO de cada modulo
######################### MENU-PRINCIPAL #####################################
       



############################ MODULO1-CADASTRAMENTO DE PACIENTES ###############################
import function
import validacao
import os

def cad_paciente():
    os.system('cls')
    function.menu_cad()
    option = input('Qual sua opção? --> ')
    while option!='0':
        if option == '1':
                os.system('cls')
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


                cadastro[cpf] = [nome,data_nasc,genero,peso,altura,imc,phone_number]

                # Imprimindo os dados dos pacientes em formato de coluna
                #os dados estão sendo armazenado no dicionário cadastro, chave CPF.
                print('NOME: ', cadastro[cpf][0])
                print(f'CPF: {cpf}')
                print('DATA DE NASCIMENTO: ' , cadastro[cpf][1],)
                print('TELEFONE: ', cadastro[cpf][6])
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
                    print('NOME: ', cadastro[cpf][0])
                    print(f'CPF: ', cpf )
                    print('DATA DE NASCIMENTO: ' , cadastro[cpf][1])
                    print('GÊNERO: ', cadastro[cpf][2])
                    print('PESO: ', cadastro[cpf][3])
                    print('ALTURA: ', cadastro[cpf][4])
                    print('IMC: ', cadastro[cpf][5])
                    input('Tecle <ENTER> para continuar...') 
                    function.menu_cad()
                    option = input('Digite outra opção: ')
                    
                else:
                    print('''
                          #############################################
                #########  ERRO, CPF INVÁLIDO OU NÃO ENCONTRADO    #########
                          #############################################      
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
                print('CPF NÃO ENCONTRADO OU NÃO CADASTRADO')
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
             agendamento = function.gerar_relatorio_pacientes(cadastro)
             if function.gerar_relatorio_pacientes(agendamento):
                  print()
             else:
                  print('Cadastre-se')
             
        elif option == '0':
            os.system('cls')
            print('Fim do programa')
            function.main_menu()
            option = input('Digite outra opção: ')

        else:
            print('OPÇÃO INVÁLIDA!')
            function.menu_cad()
            option = input('Digite outra opção: ')
############################# MODULO 2 - Dietas.##########################################


############################ Modulo 3 - Cosulta ######################################


################################### Modulo 4 - Minhas informações.##############################
def my_information():
  os.system('cls')
  print('''
  minhas informações:
  nome: Leandro Sérgio da Silva 
  curso: Sistema de informação
  Professor: Flaviu...
  instituição: UFRN-CAICO
  Github:Leo.sergio...
  e-mail: leandrooos222@gmail.com
  whatsapp: (84) 9 9619-7364
  Instagram:
  ''')
 #para inicializar a function main