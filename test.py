import modulo1
def valida_obj(cpf):
    imc = modulo1.cadastro[cpf][5]
    obj= input('''
                    Cadastrar objetivo:
                    1 - Perder peso
                    2 - Ganhar Massa Muscular
                    3 - Manutenção de Peso
                                        -->   ''')
    while True:
        if obj !=  '1' and obj!='2':
            print('Erro no cadastro, objetivo inválido')
            obj = input('''
            Qual o seu objetivo?
            1 - Perder peso
            2 - Ganhar peso
        ''')
        elif obj == '1' and imc < 18.5:
            print('OBJETIVO INVÁLIDO')
            print('Seu IMC indica que você está abaixo do peso.')
            obj = input('''
            Qual o seu objetivo?
            1 - Perder peso
            2 - Ganhar peso
        ''')
        elif obj == '2' and imc > 25:
            print('OBJETIVO INVÁLIDO')
            print('Seu IMC indica que você está acima do peso.')
            obj = input('''
            Qual o seu objetivo?
            1 - Perder peso
            2 - Ganhar peso
        ''')
        elif (obj == '3' and imc > 25) and (obj == '3' and imc < 18.5):
            print('OBJETIVO INVÁLIDO')
            print('Seu IMC está na faixa normal.')
            obj = input('''
            Qual o seu objetivo?
            1 - Perder peso
            2 - Ganhar peso
        ''')
        if obj == '1':
            obj = 'Perder peso'
        elif obj == '2':
            obj = 'Ganhar Massa muscular'
