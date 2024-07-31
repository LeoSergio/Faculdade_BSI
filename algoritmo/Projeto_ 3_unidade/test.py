import os
def display_patient_info(cpf, cadastro):
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=" * 50)
    print(f"{GREEN}{'INFORMAÇÕES DO PACIENTE':^50}{RESET}")
    print("=" * 50)
    print(f"CPF: {cpf}")
    print(f"DATA DE NASCIMENTO: {cadastro[cpf][1]}")
    print(f"TELEFONE: {cadastro[cpf][6]}")
    print(f"GÊNERO: {cadastro[cpf][2]}")
    print(f"PESO: {cadastro[cpf][3]} KG")
    print(f"ALTURA: {cadastro[cpf][4]}")
    print(f"IMC: {cadastro[cpf][5]}")
    print("=" * 50)
    
    print(f'''
    {GREEN}#########################{RESET}
    {GREEN}## CADASTRADO COM SUCESSO {GREEN}##{RESET}
    {GREEN}#########################{RESET}
    ''')

# Exemplo de uso
cpf = "123.456.789-00"
cadastro = {
    "123.456.789-00": [
        "Nome do Paciente",   # Índice 0
        "01/01/1990",         # Índice 1 - Data de Nascimento
        "Masculino",          # Índice 2 - Gênero
        70,                   # Índice 3 - Peso
        1.75,                 # Índice 4 - Altura
        22.86,                # Índice 5 - IMC
        "(84) 9 9619-7364"    # Índice 6 - Telefone
    ]
}

display_patient_info(cpf, cadastro)