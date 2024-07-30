import function
import modulo1
import modulo2
import modulo3
import modulo4
import os
import pickle

# Função para carregar dados ou criar um novo arquivo
def carregar_ou_criar_arquivo(nome_arquivo, conteudo_default):
    try:
        with open(nome_arquivo, "rb") as arq:
            return pickle.load(arq)
    except FileNotFoundError:
        with open(nome_arquivo, "wb") as arq:
            pickle.dump(conteudo_default, arq)
        return conteudo_default

# Função para salvar dados no arquivo
def salvar_arquivo(nome_arquivo, dados):
    with open(nome_arquivo, "wb") as arq:
        pickle.dump(dados, arq)

# Carregar dados dos arquivos
cadastro = carregar_ou_criar_arquivo("cadastro.dat", {})
cad_excluido = carregar_ou_criar_arquivo("cad_excluido.dat", {})
dietas = carregar_ou_criar_arquivo("dietas.dat", {})
dietas_excluida = carregar_ou_criar_arquivo("dietas_excluida.dat", {})
agendamento = carregar_ou_criar_arquivo("agendamento.dat", {})
agendamento_excluido = carregar_ou_criar_arquivo("agendamento_excluido.dat", {})

######################### MENU-PRINCIPAL #####################################
def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    function.main_menu()
    option = input('Escolha uma opção? --> ')
    while option != '0':
        os.system('cls' if os.name == 'nt' else 'clear')
        if option == '1':
            modulo1.cad_paciente()
            function.main_menu()
        elif option == '2':
            print('CADASTRAMENTO DE DIETAS')
            modulo2.mod_dieta()
            function.main_menu()
        elif option == '3':
            print('Módulo3- Agendamento')
            modulo3.agendam()
            function.main_menu()
        elif option == '4':
            print('Módulo4')
            function.main_menu()
            modulo4.my_information()
            input('Tecle <ENTER> para continuar...')
        else: 
            print('OPÇÃO INVÁLIDA')
            function.main_menu()
        option = input('Digite outra opção: ')
    
    # Salvar dados atualizados ao final do programa
    salvar_arquivo("cadastro.dat", cadastro)
    salvar_arquivo("cad_excluido.dat", cad_excluido)
    salvar_arquivo("dietas.dat", dietas)
    salvar_arquivo("dietas_excluida.dat", dietas_excluida)
    salvar_arquivo("agendamento.dat", agendamento)
    salvar_arquivo("agendamento_excluido.dat", agendamento_excluido)
    
    print('FIM DO PROGRAMA') 

if __name__ == "__main__":
    main()
