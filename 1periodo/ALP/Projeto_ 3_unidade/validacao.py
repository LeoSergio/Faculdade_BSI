import modulo1
import modulo2
import modulo3
import validacao
import function
from datetime import datetime
from datetime import datetime, timedelta
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
def date(date_str): # PEGUEI PELO COLEGA KAIO
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
def valida_obj(cadastro,cpf,dietas,nome):
    imc = cadastro[cpf][5]
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
    dietas[nome] = obj 
    return obj
##############################################################
def plan_dieta(cadastro,cpf):
    imc = cadastro[cpf][5]
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


def hora(dietas, cpf):
    while True:
        # Solicitando o horário ao usuário
        hora = input('''Qual o horário das refeições?
                1 - Manhã
                2 - Tarde
                3 - Noite 
        ''')
        
        # Verificando se a entrada é válida
        if hora not in {'1', '2', '3'}:
            print('Erro no cadastro, horário inválido')    
            
        elif hora == '1':
            horario = 'manhã'
            break
            
        elif hora == '2':
            horario = 'tarde'
            break
        elif hora == '3':
            horario = 'noite'
            break
            
        # Adicionando o horário ao dicionário dietas
        dietas[cpf] = horario 
        return horario

def valida_nome(nome):#créditos: CHAT GPT
    # Remove espaços
    nome_sem_espacos = nome.replace(" ", "")
    
    # Verifica se o nome está vazio
    if not nome_sem_espacos:
        return None
    
    # Expressão regular para permitir apenas letras
    
    
    # Verifica se o nome corresponde ao padrão
    if (nome_sem_espacos):
        # Converte para maiúsculas
        nome_maiusculo = nome_sem_espacos.upper()
        return nome_maiusculo
    else:
        return None

# Entrada do nome do usuário
def exibir_dieta(cadastro,cpf,dietas):
    nome = input('Digite o nome da dieta: ')
    name_dieta_validado = valida_nome(nome)
    if name_dieta_validado:
        if name_dieta_validado in dietas:
            dieta_info = dietas[name_dieta_validado]
            print('NOME DA DIETA: ', name_dieta_validado)
            print('ALERGIA: ', dieta_info[0])
            print('OBJETIVO: ', dieta_info[1])
            print(validacao.plan_dieta(cadastro,cpf))
        else:
            print('Dieta não encontrada ou não cadastrada.')
    else:
        print('Nome da dieta inválido.')

#créditos: Flavius Gorgônio
def validate_phone(phone_number):
  phone_number = phone_number.replace(' ', '')
  phone_number = phone_number.replace('-', '')
  phone_number = phone_number.replace('(', '')
  phone_number = phone_number.replace(')', '')
  phone_number = phone_number.replace('+', '')
  tam = len(phone_number)
  if tam != 11:
    return False
  if not(phone_number.isdigit()):
    return False
  
  return True

#==================================#
#======== Validar Número ==========#
#==================================#
def validate_number(x):
    if x.isdigit():
        return True
    else:
        return False
    
def obter_data(): #CREDITOS: CHAT GPT
    while True:
        print()
        data_str = input('Digite a data do agendamento (dd/mm/aaaa): ')
        try:
            data = datetime.strptime(data_str, '%d/%m/%Y')
            data_atual = datetime.now()
            if data.weekday() >= 5:  
                print('Agendamentos não são permitidos nos finais de semana. Por favor, escolha uma data durante a semana.')
            elif data < data_atual:
                print('A data do agendamento não pode ser no passado. Por favor, escolha uma data futura.')
            else:
                return data
        except ValueError:
            print('Data inválida. Tente novamente.')

def obter_horario(): #CREDITOS: CHAT GPT
    while True:
        horario_str = input('Digite a hora do agendamento (hh:mm): ')
        try:
            horario = datetime.strptime(horario_str, '%H:%M').time()
            if not ((datetime.strptime('08:00', '%H:%M').time() <= horario < datetime.strptime('12:00', '%H:%M').time()) or
                    (datetime.strptime('14:00', '%H:%M').time() <= horario < datetime.strptime('18:00', '%H:%M').time())):
                print('Horário fora do horário de funcionamento (8h às 12h e 14h às 18h). Por favor, escolha um horário dentro do horário de funcionamento.')
            else:
                return horario
        except ValueError:
            print('Horário inválido. Tente novamente.')

def horario_disponivel(data, horario, agendamento): #CREDITOS: CHAT GPT
    data_str = data.strftime('%d/%m/%Y')
    if data_str in agendamento:
        for horario_agendado in agendamento[data_str]:
            horario_inicial = (datetime.combine(data, datetime.strptime(horario_agendado, '%H:%M').time()) - timedelta(minutes=30)).time()
            horario_final = (datetime.combine(data, datetime.strptime(horario_agendado, '%H:%M').time()) + timedelta(minutes=30)).time()
            
            if horario_inicial <= horario <= horario_final:
                return False
    return True

def agendar_consulta(agendamento): #CREDITOS: CHAT GPT
    data = obter_data()
    horario = obter_horario()
    
    if horario_disponivel(data, horario, agendamento):
        data_str = data.strftime('%d/%m/%Y')
        horario_str = horario.strftime('%H:%M')
        
        if data_str not in agendamento:
            agendamento[data_str] = []
        
        agendamento[data_str].append(horario_str)
        
        print('Agendamento realizado com sucesso!')
        return {'data': data_str, 'hora': horario_str}
    else:
        print('Horário indisponível. Por favor, escolha outro horário.')
        return None

# Teste das funções

    