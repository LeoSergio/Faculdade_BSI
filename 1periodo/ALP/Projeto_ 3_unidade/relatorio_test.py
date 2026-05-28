import os 
import modulo1
def reports_clients():
    os.system('cls || clear')
    print("#========================================#")
    print("#========== Relatório Clientes ==========#")
    print("#========================================#")
    print()
    print()
    print("--" * 25)
    print("||" * 25)
    print("--" * 25)
    for modulo1.cadastro['cpf'] in modulo1.cadastro:
        print("Cpf do Cliente: ", modulo1.cpf)
        print()
        print("Nome do Cliente: ",modulo1.cadastro['cpf'][0])
        print()
        print("Telefone do Cliente: ",modulo1.cadastro['cpf'][1])
        print("--" * 25)
        print("||" * 25)
        print("--" * 25)
    print()
    input("Pressione <ENTER> para continuar.")
reports_clients()