import validacao
agendamento = {}
while True:
    agendado = validacao.agendar_consulta()
    if validacao.agendar_consulta():
        print()
        break
    else:
        print()
    
