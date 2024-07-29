import validacao
import function
import main
import modulo1
import modulo2
import modulo3
import os

'''
COLOCAR DIETAS DE ACORDO COM O OBJETIVO, PODE COPIAR DO IMC
FAZER AGENDAMENTO, MOSTRAR HORARIOS DISPONIVEIS PELO TURNO.

ERROS: LEITURA DO CPF ESTA ERRADA NO MODULO2 CADASTRAR DIETA: ERRO NA VERIFICAÇÃO.
'''




######################### MENU-PRINCIPAL #####################################
def main():
        os.system('cls')
        function.main_menu()
        option = input('Escolha uma opção? --> ')
        while option != '0':
            if option == '1':
                os.system('cls')
                modulo1.cad_paciente()
                function.main_menu()
                option = input('Digite outra opção: ')
            elif option == '2':
                os.system('cls')
                print('CADASTRAMENTO DE DIETAS')
                modulo2.mod_dieta()
                function.main_menu()
                option = input('Digite outra opção: ')     
            elif option == '3':
                os.system('cls')
                print('Módulo3- Agendamento')
                modulo3.agendam()
                function.main_menu()
                option = input('Digite outra opção: ') 
            elif option == '4':
                os.system('cls')
                print('Módulo4')
                function.main_menu()
                my_information()
                input('Tecle <ENTER> para continuar...')

                option = input('Digite outra opção: ') 

            else: 
                print('OPÇÃO INVÁLIDA')
                function.main_menu()
                option = input('Digite outra opção: ')
        print('FIM DO PROGRAMA')       



############################ MODULO1-CADASTRAMENTO DE PACIENTES ###############################

'''
13971335462
12345678909
84996197364

'''
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
if __name__ == "__main__":
    main() #para inicializar a function main