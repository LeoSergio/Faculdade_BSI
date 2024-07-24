#funcoes de validacao mentrer outras
'''

VALIDAÇÃO DE NOMES
VALIDACAO DE CPF
VALIDACAO DA DATA DE NASCIMENTO


'''
def validaCPF(cpf):
  tam = len(cpf)
  soma = 0
  d1 = 0
  d2 = 0
  if tam != 11:
    return False
  for i in range(11):
    if (cpf[i] < '0') or (cpf[i] > '9'):
      return False
  for i in range(9):
    soma += (int(cpf[i]) * (10 - i))
  d1 = 11 - (soma % 11)
  if (d1 == 10 or d1 == 11):
    d1 = 0
  if d1 != int(cpf[9]):
    return False
  soma = 0
  for i in range(10):
    soma += (int(cpf[i]) * (11 - i))
  d2 = 11 - (soma%11)
  if (d2 == 10 or d2 == 11):
    d2 = 0
  if d2 != int(cpf[10]):
    return False

  return True



def data_nasc():
  print('DATA DE NASCIEMNTO: ')
  while True:
    print('''
          |Data de nascimento, DIGITE APENAS NÚMEROS :|                     
          ''')
    day = (input('Qual o dia do seu nascimento? '))
    month= (input('Qual o mês do seu nascimento? '))
    year= (input('Qual o ano do seu nascimento? '))
    data_nasc = day,month,year
    try: #converter a entrada para um número de ponto flutuante.
        day_float = float(day)
        month_float = float(month)
        year_float = float(year)
        data_float = day_float, month_float,year_float
        break
    except ValueError: #indica que a entrada não é um número válido.
        print('DIGITE APENAS NÚMEROS')
def name_validate():
  name = input('Digite seu nome: ')
  name_upper = name.upper()
  name = name_upper.replace(' ', '')
