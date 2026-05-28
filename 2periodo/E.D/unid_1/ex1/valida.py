
'''
excluir caracteres especias para deixar apenas numero
ex: +55 (84) 91234-5678 → 5584912345678
digitos maximos: 19 com caracteres especias e espaços
DDD = de 11 à 99
'''
import re # regular expressions

def validar_tell(numero):
    numero_limpo = re.sub(r'[\s\-\(\)]', '', numero) #remove espaços, hífens e parênteses do número
    numero_limpo = re.sub(r'^\+?55', '', numero_limpo)# remove o código do país +55 se existir no início do número.

    if not numero_limpo.isdigit():#Verifica se o número tem apenas dígitos
        return {"valido": False, "erro": "O telefone deve conter apenas números."}

    if len(numero_limpo) not in (10, 11):#Verifica o tamanho do número
        return {"valido": False, "erro": "O telefone deve ter 10 dígitos (fixo) ou 11 dígitos (celular)."}

    ddd = int(numero_limpo[:2]) #Valida o DDD
    if ddd < 11 or ddd > 99:
        return {"valido": False, "erro": "DDD inválido. Deve estar entre 11 e 99."}

    if len(numero_limpo) == 11 and numero_limpo[2] != "9": #Valida celular
        return {"valido": False, "erro": "Celulares devem começar com 9 após o DDD."}

    if len(numero_limpo) == 10 and numero_limpo[2] not in "2345": #Valida telefone fixo
        return {"valido": False, "erro": "Telefones fixos devem começar com 2, 3, 4 ou 5 após o DDD."}

    tipo = "celular" if len(numero_limpo) == 11 else "fixo" #Retorna o tipo e número válido
    return {"valido": True, "tipo": tipo, "numero": numero_limpo}


import re

def validar_senha(senha):
    """
    Valida se a senha possui:
    - Pelo menos uma letra maiúscula
    - Pelo menos uma letra minúscula
    - Pelo menos um número
    - Pelo menos um caractere especial
    - Tamanho mínimo de 6 caracteres
    """
    if len(senha) < 6:
        return {"valido": False, "erro": "A senha deve ter no mínimo 6 caracteres."}
    
    if not re.search(r"[A-Z]", senha):
        return {"valido": False, "erro": "A senha deve conter pelo menos uma letra maiúscula."}
    
    if not re.search(r"[a-z]", senha):
        return {"valido": False, "erro": "A senha deve conter pelo menos uma letra minúscula."}
    
    if not re.search(r"[0-9]", senha):
        return {"valido": False, "erro": "A senha deve conter pelo menos um número."}
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return {"valido": False, "erro": "A senha deve conter pelo menos um caractere especial."}
    
    return {"valido": True, "senha": senha}


# --- Exemplos de uso ---
senhas = ["abc", "abcdef", "Abcdef", "Abcdef1", "Abcdef1!"]

for s in senhas:
    resultado = validar_senha(s)
    if resultado["valido"]:
        print(f"✅ Senha válida: {s}")
    else:
        print(f"❌ Senha inválida: {s} → {resultado['erro']}")

    