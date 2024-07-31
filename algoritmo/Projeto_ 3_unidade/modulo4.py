import os
def my_information():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("=" * 50)
    print(" " * 15 + "MINHAS INFORMAÇÕES")
    print("=" * 50)
    print(f'''
    {f'Nome:':<15} Leandro Sérgio da Silva

    {f'Curso:':<15} Sistema de Informação

    {f'Professor:':<15} Flavius

    {f'Instituição:':<15} UFRN-CAICO/CERES

    {f'Github:':<15} Leo.sergio...

    {f'E-mail:':<15} leandro.sergio.583@gmail.com

    {f'Whatsapp:':<15} (84) 9 9619-7364

    {f'Instagram:':<15} leandro.sergio.583
    ''')
    print("=" * 50)



def project_information():

    print("=" * 50)
    print(" " * 15 + "SOBRE O PROJETO")
    print("=" * 50)
    print(f'''
    {f'Nome do Projeto:':<20} Planejamento de Dietas

    {f'Descrição:':<20} Este projeto avaliativo da 3ª unidade tem como intuito 
    {f'':<20} permitir que os pacientes tenham dietas parciais, pois não sou 
    {f'':<20} profissional na área. O foco do programa é no cadastramento do 
    {f'':<20} paciente e agendamento, com algumas dietas, mas sem aprofundamento,
    {f'':<20} pois isso é trabalho de um profissional qualificado.
    ''')
    print("=" * 50)

my_information()
project_information()