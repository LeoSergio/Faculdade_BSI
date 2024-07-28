from datetime import datetime, timedelta
import re
import validacao
import function
import main
import modulo1
import modulo2
import modulo3
import os

# Dicionário global para armazenar agendamentos
agendamentos = {}

# Função para coletar e validar a data
def obter_data():
    while True:
        print()
        data_str = input('Digite a data do agendamento (dd/mm/aaaa): ')
        try:
            data = datetime.strptime(data_str, '%d/%m/%Y')
            data_atual = datetime.now()
            # Verifica se a data é um final de semana ou no passado
            if data.weekday() >= 5:  # 5 = sábado, 6 = domingo
                print('Agendamentos não são permitidos nos finais de semana. Por favor, escolha uma data durante a semana.')
            elif data < data_atual:
                print('A data do agendamento não pode ser no passado. Por favor, escolha uma data futura.')
            else:
                return data
        except ValueError:
            print('Data inválida. Tente novamente.')

# Função para coletar e validar o horário
def obter_horario():
    while True:
        horario_str = input('Digite a hora do agendamento (hh:mm): ')
        try:
            horario = datetime.strptime(horario_str, '%H:%M').time()
            # Verifica se o horário está dentro do horário de funcionamento
            if not ((datetime.strptime('08:00', '%H:%M').time() <= horario < datetime.strptime('12:00', '%H:%M').time()) or
                    (datetime.strptime('14:00', '%H:%M').time() <= horario < datetime.strptime('18:00', '%H:%M').time())):
                print('Horário fora do horário de funcionamento (8h às 12h e 14h às 18h). Por favor, escolha um horário dentro do horário de funcionamento.')
            else:
                return horario
        except ValueError:
            print('Horário inválido. Tente novamente.')

# Função para verificar se o horário está disponível
def horario_disponivel(cpf, data, horario):
    data_str = data.strftime('%d/%m/%Y')
    if cpf in agendamentos and data_str in agendamentos[cpf]:
        for horario_agendado in agendamentos[cpf][data_str]:
            horario_inicial = (datetime.combine(data, horario) - timedelta(minutes=30)).time()
            horario_final = (datetime.combine(data, horario) + timedelta(minutes=30)).time()
            
            if horario_inicial <= horario_agendado <= horario_final:
                return False
    return True

# Função para agendar a consulta
def agendar_consulta():
    cpf = input('Digite seu CPF: ')
    if cpf in modulo1.cadastro:
        data = obter_data()
        horario = obter_horario()
    
    if horario_disponivel(cpf, data, horario):
        print('Horário disponível. Você pode agendar sua consulta.')
        data_str = data.strftime('%d/%m/%Y')
        horario_str = horario.strftime('%H:%M')
        
        # Adiciona o agendamento ao dicionário global
        if cpf not in agendamentos:
            agendamentos[cpf] = {}
        if data_str not in agendamentos[cpf]:
            agendamentos[cpf][data_str] = []
        agendamentos[cpf][data_str].append(horario)
        
        # Armazena as informações do agendamento em uma variável
        agendado = {
            'cpf': cpf, 'data': data_str, 'hora': horario_str
            }
        print('Agendamento:', agendado)
    else:
        print('Horário indisponível. Por favor, escolha outro horário.')

# Teste das funções
agendar_consulta()

# Exibe todos os agendamentos
print('Todos os agendamentos:', agendamentos)