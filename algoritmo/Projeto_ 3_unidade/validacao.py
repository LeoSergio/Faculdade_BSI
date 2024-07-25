import modulo1
import modulo2
from datetime import datetime
def validaCPF(cpf): # PROF FLAVIUS
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

################################################################################
def date(date_str): #PEGUEI PELO COLEGA KAIO
    try:
        day, month, year = date_str.split("/")  # Split by '/' separator
        day, month, year = int(day), int(month), int(year)  # Convert to integers

        # Check for valid day values
        if not 1 <= day <= 31:
            return False

        # Check for valid month values and adjust day range accordingly
        if not 1 <= month <= 12:
            return False
        elif month == 2 and not is_leap_year(year):  # Handle February for non-leap years
            if day > 28:
                return False
        elif month in [4, 6, 9, 11] and day > 30:
            return False

        # Check for valid year values
        if year < 1:
            return False

        return True  # All checks passed, date is valid

    except ValueError:  # Handle invalid input format
        return False

    except Exception as e:  # Handle unexpected errors
        print(f"Error during date validation: {e}")
        return False

def is_leap_year(year): #PEGUEI PELO COLEGA KAIO

    if year % 4 != 0:
        return False
    elif year % 100 == 0 and year % 400 != 0:
        return False
    return True
#####################################################################
def valida_obj(cpf):
    imc = modulo1.cadastro[cpf][5]
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
      
      # Verificando se o objetivo é válido com o IMC
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
          # Se o objetivo for válido, sair do loop
          break
    if obj == '1':
        obj = 'Perder peso'       
    elif obj == '2':
        obj = 'Ganhar Massa muscular'     
    elif obj == '3':
        obj = 'Ganhar Massa muscular'
    modulo2.dieta[cpf] = obj 
    return obj
##############################################################
def plan_dieta(cpf):
    imc = modulo1.cadastro[cpf][5]
    print('''
    #####################################
    #         PLANO DE DIETA             #
    #####################################
    ''')
    
    if imc < 18.5:
        print('Seu IMC indica que você está abaixo do peso.')
        print('1. Coma mais frequentemente.')
        print('2. Escolha alimentos ricos em nutrientes.')
        print('3. Tente shakes e smoothies.')
    elif imc >= 18.5 and imc < 25:
        print('Seu IMC está na faixa normal.')
        print('1. Mantenha uma dieta balanceada.')
        print('2. Controle as porções.')
        print('3. Mantenha-se ativo.')
    else:
        print('Seu IMC indica que você está acima do peso.')
        print('1. Reduza calorias de forma controlada.')
        print('2. Coma mais proteínas.')
        print('3. Reduza a ingestão de carboidratos.')

################################################################

def hora(cpf):
    hora=input('''Qual o horário das refeições?
                1 - Manhâ
                2 - Tarde
                3- Cafe da tarde
                4 - Noite                                                     
                ''')
    while hora !=  '1' and hora !='2' and hora !='3' and hora !='4':
            print('Erro no cadastro, Horario inválido')
            hora = input('''Quais os horarios das refeições?
                1 - Manhâ
                2 - Tarde
                3- Cafe da tarde
                4 - Noite                                                     
                ''')
    if hora == '1':
        hora = 'Manhâ'
    elif hora == '2':
        hora = 'Tarde'
    elif hora == '3':
        hora = 'Cafe da tarde'
    elif hora == '4':
        hora = 'Noite'
    modulo2.dieta[cpf]= hora
    return hora
   