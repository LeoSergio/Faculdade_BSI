import os

     ##########################################
##### Projeto Planejamento de Dietas - Versão 1 #####
     #########################################

# 
# Oq foi feito na ultima att do projeto?
'''
1-Adicionei funções ao projeto.
2- se a resposta do usuario for sim, chama a função main e executa ela de acordo com as opções do usuario.
    PROXIMOS PASSOS:
1-IMPORTANTE. Parar para ajeitar como vai ser a estrutura do programa na execução.
ex: MÓDULO PACIENTE: 
    add paciente, remover paciente, verificar informações do paciente.
FAZER ISSO PARA OS DEMAIS. OBS: Olhar o model do prof.

'''

print('CONSULTA ONLINE')
def main_menu():
            print('''
            Projeto Nutri-Center
        [1]-Cadastramento de Clientes:
        [2]-Objetivos do Paciente:
        [3]-Planos de Dietas:
        [4]-Finalização da Consulta e Resultados:
        [5]-Informações pessoais:
        [0]-FINALIZAR PROGRAMA
        ''')
        
        #MODULO1-CADASTRAMENTO DE PACIENTES
def perfil():
    #Adicionando paciente    
    print('DIGITE AS INFORMAÕES PEDIDAS.')
    nome = input('Nome Completo: ')
    nome_upper = nome.upper()
    idade = int(input('Qual a sua Idade:'))
    genero = input('Qual o seu Gênero: M/F ')
    peso = float(input('Qual o seu peso atual: '))
    altura = float(input('Qual a sua altura atual: '))
    info = [nome_upper,idade,genero,peso,altura]
        
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
    '''.format(*info))
    input('Tecle <ENTER> para continuar...') #colocar nas outras function
def main():
    resp = input('Você deseja participar? S/N ')
    if resp.upper() == 'S':
        main_menu()
        option = input('Escolha uma opção?')
        while option != '0':
            if option == '1':
                perfil()
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
            
            
if __name__ == "__main__":
    main() #para inicializar a function main

       














