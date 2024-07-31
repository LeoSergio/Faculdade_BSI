import modulo1
import modulo2
import modulo3
import validacao
import function
from datetime import datetime
from datetime import datetime, timedelta
def test(cpf,dietas):
    while True:
      # Solicitando o objetivo ao usuário
      hora = input('''Qual o horário das refeições?
                1 - Manhã
                2 - Tarde
                3 - Noite 
      ''')
      # Verificando se a entrada é válida
      if hora != '1' and hora != '2' and hora != '3':
          print('Erro no cadastro, horario inválido')
      
      # Verificando se o objetivo é válido com o IMC
      elif hora == '1':
            hora = 'manha'       
      elif hora == '2':
            hora = 'tarde'     
      elif hora == '3':
           hora = 'Noite'
      dietas[cpf] = hora 
      return hora