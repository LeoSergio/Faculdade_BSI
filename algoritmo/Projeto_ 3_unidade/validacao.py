#funcoes de validacao mentrer outras
'''

VALIDAÇÃO DE NOMES
VALIDACAO DE CPF
VALIDACAO DA DATA DE NASCIMENTO


'''
import datetime
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

from datetime import datetime

def validar_data_nascimento(): # Gerada pelo Chat GPT b67
    print('''
          |Data de nascimento, DIGITE APENAS NÚMEROS :|                     
          ''')

    while True:
        ano = input('Qual o ano do seu nascimento? ')
        mes = input('Qual o mês do seu nascimento? ')
        dia = input('Qual o dia do seu nascimento? ')
        
        try:
            # Converte os valores para inteiros
            ano = int(ano)
            mes = int(mes)
            dia = int(dia)
            
            # Cria a data de nascimento
            data_nascimento = datetime.datetime(ano, mes, dia)
            
            # Obtém a data atual
            data_atual = datetime.datetime.now()
            
            # Calcula a diferença em anos
            idade = data_atual.year - data_nascimento.year
            
            # Verifica se já fez aniversário este ano
            if (data_atual.month, data_atual.day) < (data_nascimento.month, data_nascimento.day):
                idade -= 1

            # Verifica se a idade é maior ou igual a 18 anos
            if idade < 18:
                print("Menor de 18 anos.")
            else:
                print("Data de nascimento válida.")
            
            break
        
        except ValueError:
            print('Data inválida. Verifique se ano, mês e dia são números válidos e formam uma data real.')

                
