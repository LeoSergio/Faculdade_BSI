#
imc = 11
while True:
    # Solicitando o objetivo ao usuário
    obj = input('''
    Qual o seu objetivo?
    1 - Perder peso
    2 - Ganhar peso
    3 - Manutenção de Peso 
-->    ''')
    
    # Verificando se a entrada é válida
    if obj != '1' and obj != '2' and obj != '3':
        print('Erro no cadastro, objetivo inválido')
    
    # Verificando se o objetivo é válido com base no IMC
    elif obj == '1' and imc < 18.5:
        print('OBJETIVO INVÁLIDO')
        print('Seu IMC indica que você está abaixo do peso.')
        
    elif obj == '2' and imc > 25:
        print('OBJETIVO INVÁLIDO')
        print('Seu IMC indica que você está acima do peso.')
        
    elif obj == '3' and (imc > 25 or imc < 18.5):
        print('OBJETIVO INVÁLIDO')
        print('Seu IMC está fora da faixa ideal para manutenção de peso.')
        
    else:
        # Se o objetivo for válido, saímos do loop
        break
if obj == '1':
    obj = 'Perder peso'
    print(obj)
elif obj == '2':
    obj = 'Ganhar Massa muscular'
    print(obj)
elif obj == '3':
    obj = 'Ganhar Massa muscular'
    print(obj)