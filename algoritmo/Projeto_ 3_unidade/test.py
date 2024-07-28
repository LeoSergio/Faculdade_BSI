from datetime import datetime, timedelta
import re
agendamentos = {}
# Função para coletar e validar a data
def obter_data():
    while True:
        print()
        data_str = input('Digite a data do agendamento (dd/mm/aaaa): ')
        try:
            data = datetime.strptime(data_str, '%d/%m/%Y')
            data_atual = datetime.now()
            # Verifica se a data é um final de semana
            if data < data_atual:
                print('A data do agendamento não pode ser no passado. Por favor, escolha uma data futura.')
            elif data.weekday() >= 5:  # 5 = sábado, 6 = domingo
                print('Agendamentos não são permitidos nos finais de semana. Por favor, escolha uma data durante a semana.')
            # Verifica se a data está no passado
            
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

# Lista para armazenar agendamentos


# Função para verificar se o horário está disponível
def horario_disponivel(data, horario):
    for agendamento in agendamentos:
        if agendamento['data'] == data.strftime('%d/%m/%Y'):
            horario_agendado = datetime.strptime(agendamento['hora'], '%H:%M').time()
            horario_inicial = (datetime.combine(data, horario) - timedelta(minutes=30)).time()
            horario_final = (datetime.combine(data, horario) + timedelta(minutes=30)).time()
            
            if horario_inicial <= horario_agendado <= horario_final:
                return False
    
    return True
    

# Exemplo de uso das funções de validação
def agendar_consulta():
    data = obter_data()
    horario = obter_horario()
    
    if horario_disponivel(data, horario):
        print('Horário disponível. Você pode agendar sua consulta.')
        agendamentos.append({'data': data.strftime('%d/%m/%Y'), 'hora': horario.strftime('%H:%M')})
    else:
        print('Horário indisponível. Por favor, escolha outro horário.')
    agendamento = [data,horario]
# Teste das funções
agendar_consulta()