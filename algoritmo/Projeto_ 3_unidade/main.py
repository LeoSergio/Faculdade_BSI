import validacao
import function
import main
import modulo1
import modulo2
import modulo3
import os
import pickle


###################### MODULO1 ########################
cadastro = {#nome,genero,peso,altura,imc  
}
try:
    arq_cadastro = open("cadastro.dat", "rb")
    cadastro = pickle.load(arq_cadastro)
except:
    arq_cadastro = open("cadastro.dat", "wb")
arq_cadastro.close()

cad_excluido = {}
try:
    arq_cad_excluido = open("cad_excluido.dat", "rb")
    cad_excluido = pickle.load(arq_cad_excluido)
except:
    arq_cad_excluido = open("cad_excluido.dat", "wb")
arq_cad_excluido.close()

###################### MODULO2 ########################
dietas = {}
try:
    arq_dietas = open("dietas.dat", "rb")
    dietas = pickle.load(arq_dietas)
except:
    arq_dietas = open("dietas.dat", "wb")
arq_dietas.close()

dietas_excluida = {}
try:
    arq_dietas_excluida = open("dietas_excluida.dat", "rb")
    dietas_excluida = pickle.load(arq_dietas_excluida)
except:
    arq_dietas_excluida = open("dietas_excluida.dat", "wb")
arq_dietas_excluida.close()

###################### MODULO3 ########################
agendamento = {}
try:
    arq_agendamento = open("agendamento.dat", "rb")
    agendamento = pickle.load(arq_agendamento)
except:
    arq_agendamento = open("agendamento.dat", "wb")
arq_agendamento.close()

agendamento_excluido = {}
try:
    arq_agendamento_excluido = open("agendamento_excluido.dat", "rb")
    agendamento_excluido = pickle.load(arq_agendamento_excluido)
except:
    arq_agendamento_excluido = open("agendamento_excluido.dat", "wb")
arq_agendamento_excluido.close()


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

M2 = R6
M3 = R5
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
###################### MODULO1 ########################
arq_cadastro = open("cadastro.dat", "wb")
pickle.dump(cadastro, arq_cadastro)
arq_cadastro.close()

arq_cad_excluido = open("cad_excluido.dat", "wb")
pickle.dump(cad_excluido, arq_cad_excluido)
arq_cad_excluido.close()
###################### MODULO2 ########################
arq_dietas = open("dietas.dat", "wb")
pickle.dump(dietas, arq_dietas)
arq_dietas.close()

arq_dietas_excluida = open("dietas_excluida.dat", "wb")
pickle.dump(dietas_excluida, arq_dietas_excluida)
arq_dietas_excluida.close()

###################### MODULO3 ########################
arq_agendamento = open("agendamento.dat", "wb")
pickle.dump(agendamento, arq_agendamento)
arq_agendamento.close()

arq_agendamento_excluido = open("agendamento_excluido.dat", "wb")
pickle.dump(agendamento_excluido, arq_agendamento_excluido)
arq_agendamento_excluido.close()
if __name__ == "__main__":
    main() #para inicializar a function main