from valida import validar_tell
from valida import validar_senha
'''
Atividade 01:  Considere um cadastro de Cliente/Usuário. 
Consulte os funções para String em 
https://www.w3schools.com/python/python_strings_metho
 ds.asp:
 1. Crie um código para verificar o TELEFONE.
 2. Crie um código para verificar a DATA de Nascimento.
 3. Crie um código para verificar se a Senha tem: uma 
maiúscula, uma minúscula, um número, um caractere 
especial e tamanho mínimo de 6
'''

def cadastrarUsuario():
    nome = input("Informe seu nome: -> ")
    telefone = obter_telefone()
    #password = input('Digite sua Senha: ')
    #senha = validar_senha(password)


    print(f"✅ Telefone válido: {telefone}")
    print(f"Usuário {nome} cadastrado com sucesso!")


def obter_telefone():
    telefone = input("Informe seu telefone: -> ")
    resultado = validar_tell(telefone)

    if resultado["valido"]:
        return resultado["numero"]
    else:
        print(f"❌ Erro: {resultado['erro']}")
        print("Tente novamente...\n")
        return obter_telefone()  # chama de novo até dar certo



