import os

     ##########################################
##### Projeto Planejamento de Dietas      #####
     #########################################

# Oq foi feito na ultima att do projeto?
'''
Conseguir armazenar os dados no dicionário info
MODULO 1:
    CADASTRAMENTO DE PACIENTE
        *FALTA VERIFICAR CPF
FAZER AS OUTRAS FUNCTION
    
'''     
print('CONSULTA ONLINE')
info=[]
def main_menu():
            print('''
        PROJETO NUTRI-CENTER

    ###########################

    [1]- Módulo Paciente Objetivos: 
    [2]- Módulo Dietas:        
    [3]- Módulo consulta:   
    [4]- Módulo Informações:   
    [0]- SAIR  

    ###########################
        ''')

        #MODULO1-CADASTRAMENTO DE PACIENTES
def menu_cad():
    print('''
        PROJETO NUTRI-CENTER

    ###########################

    [1]- Cadastrar-se: 
    [2]- Verificar informações:        
    [3]- Alterar informações:   
    [4]- Remover Usuário:   
    [0]- SAIR  

    ###########################
        ''')
def cad_paciente():
    menu_cad()
    option = input('Qual sua opção? ')
    while option!='0':
        if option == '1':
            cad = input('Cadastra-se S/N ')
            if cad.upper()=='N':
                print('Escolha outra opção!')
                main_menu()  
            while cad.upper() == 'S':
                #Adicionando paciente    
                print('DIGITE AS INFORMAÕES PEDIDAS.')
                nome = input('Nome Completo: ')
                nome_upper = nome.upper()
                cpf = input('Digite seu CPF: ')
                idade = input('DATA DE NASCIMENTO: dd/mm/aaaa ') #DATA DENASCIMENTO
                genero = input('Qual o seu Gênero: M/F ')
                peso = float(input('Qual o seu peso atual: '))
                altura = float(input('Qual a sua altura atual: '))
                imc = peso/(altura**2)
                
                cadastro = { # dicionário
                    "Nome": nome_upper,
                    "CPF": cpf,
                    "Idade": idade,
                    "Gênero": genero,
                    "Peso": peso,
                    "Altura": altura,
                    "IMC": imc
                }
                info.append(cadastro)
                
                # Imprimindo os dados dos pacientes em formato de coluna
                print('''

                | Nome: {}                                   
                | Idade: {} anos                             
                | Gênero: {}                                 
                | Peso: {} KG                                
                | Altura: {} Metros                          


                            ######################
                ######### CADASTRADO COM SUCESSO ##########
                            ######################
                '''.format(*cadastro))
                input('Tecle <ENTER> para continuar...') #colocar nas outras function
                cad = input('Adicionar outro cadastro? S/N ')
        elif option == '2':
            print('verificar_info()')
            menu_cad()
            option = input('Digite outra opção: ')
        elif option == '3':
            print('alterar_info()')
            menu_cad()
            option = input('Digite outra opção: ')
        elif option == '4':
            print('remover_usuario()')
            menu_cad()
            option = input('Digite outra opção: ')
        elif option == '0':
            print('Fim do programa')
            main_menu()
            option = input('Digite outra opção: ')
        else:
            print('OPÇÃO INVÁLIDA!')
            option = input('Digite outra opção: ')
def main():
    resp = input('Você deseja participar? S/N ')
    if resp.upper() == 'S':
        main_menu()
        option = input('Escolha uma opção? --> ')
        while option != '0':
            if option == '1':
                cad_paciente()
                main_menu()
                option = input('Digite outra opção: ')
            elif option == '2':
                print('Objetivos do paciente')
                print('perder peso')
                print('ganhar peso')
                print('motivos de saúde')
                input('Tecle <ENTER> para continuar...')
                main_menu()
                option = input('Digite outra opção: ')      
            elif option == '3':
                print('Módulo3')
                main_menu()
                option = input('Digite outra opção: ') 
            elif option == '4':
                print('Módulo4')
                main_menu()
                option = input('Digite outra opção: ') 
            elif option == '5':
                print('Módulo5')
                main_menu()
                option = input('Digite outra opção: ')
            elif option == '0':
                print('Programa finalizado.')
                
            else:
                print('OPÇÃO INVÁLIDA')
                option = input('Digite outra opção: ')
        print('FIM DO PROGRAMA')        
    else:
        print('FIM DO PROGRAMA')

print(info)
if __name__ == "__main__":
    main() #para inicializar a function main
















