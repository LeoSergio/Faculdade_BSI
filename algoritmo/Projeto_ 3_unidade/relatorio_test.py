def gerar_relatorio_pacientes(agendamento):
    pacientes = agendamento['cpf']
    pacientes_excluidos = agendamento['cpf']
    
    relatorio = "Relatório de Pacientes\n" + "-"*23 + "\n\n"
    relatorio += f"Total de Pacientes: {len(pacientes)}\n\n"
    relatorio += "Lista de Pacientes:\n"
    for idx, paciente in enumerate(pacientes, start=1):
        relatorio += (f"{idx}. Nome: {paciente['nome']}\n"
                      f"   CPF: {paciente['cpf']}\n"
                      f"   Idade: {paciente['idade']}\n"
                      f"   Peso: {paciente['peso']}\n"
                      f"   Altura: {paciente['altura']}\n"
                      f"   Objetivo: {paciente['objetivo']}\n\n")
    
    relatorio += "Pacientes Excluídos:\n"
    for idx, paciente in enumerate(pacientes_excluidos, start=1):
        relatorio += (f"{idx}. Nome: {paciente['nome']}\n"
                      f"   CPF: {paciente['cpf']}\n"
                      f"   Idade: {paciente['idade']}\n"
                      f"   Peso: {paciente['peso']}\n"
                      f"   Altura: {paciente['altura']}\n"
                      f"   Objetivo: {paciente['objetivo']}\n\n")
    return relatorio


def gerar_relatorio_dietas(dietas):
    relatorio = "Relatório de Dietas Personalizadas\n" + "-"*36 + "\n\n"
    relatorio += f"Total de Dietas Personalizadas: {len(dietas)}\n\n"
    relatorio += "Lista de Dietas:\n"
    for idx, dieta in enumerate(dietas, start=1):
        relatorio += (f"{idx}. Nome da Dieta: {dieta['nome']}\n"
                      f"   CPF do Paciente: {dieta['cpf']}\n"
                      f"   Alergias: {dieta['alergias']}\n"
                      f"   Objetivo: {dieta['objetivo']}\n"
                      f"   Horários das Refeições: {dieta['horarios']}\n\n")
    return relatorio

def gerar_relatorio_agendamentos(agendamentos):
    relatorio = "Relatório de Agendamentos/Consultas\n" + "-"*34 + "\n\n"
    total_consultas = sum(len(horarios) for horarios in agendamentos.values())
    relatorio += f"Total de Consultas Agendadas: {total_consultas}\n\n"
    relatorio += "Lista de Agendamentos:\n"
    for data, horarios in agendamentos.items():
        for horario in horarios:
            relatorio += (f"Data da Consulta: {data}\n"
                          f"Hora da Consulta: {horario}\n\n")
    return relatorio

# Exemplo de uso
pacientes = [
    {'nome': 'João Silva', 'cpf': '12345678900', 'idade': 30, 'peso': 80, 'altura': 1.75, 'objetivo': 'Perder peso'},
    {'nome': 'Maria Souza', 'cpf': '98765432100', 'idade': 25, 'peso': 65, 'altura': 1.65, 'objetivo': 'Ganhar músculo'}
]

dietas = [
    {'nome': 'Dieta A', 'cpf': '12345678900', 'alergias': 'Nenhuma', 'objetivo': 'Perder peso', 'horarios': '08:00, 12:00, 18:00'},
    {'nome': 'Dieta B', 'cpf': '98765432100', 'alergias': 'Glúten', 'objetivo': 'Ganhar músculo', 'horarios': '09:00, 13:00, 19:00'}
]

agendamentos = {
    '01/08/2024': ['08:00', '08:30'],
    '02/08/2024': ['09:00', '09:30']
}

print(gerar_relatorio_pacientes(pacientes))
print(gerar_relatorio_dietas(dietas))
print(gerar_relatorio_agendamentos(agendamentos))
