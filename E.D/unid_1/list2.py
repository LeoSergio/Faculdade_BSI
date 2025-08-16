'''
Atividade 03: Numa clínica médica os pacientes são 
atendidos por ordem de chegada. Implemente esse controle:
 1. Crie uma lista representando a fila de pacientes.
 2. Adicione um paciente ao final da fila.
 3. Chame o primeiro paciente (remova da fila).
 4. Mostre a posição de um paciente específico.

'''

# Lista que representa a fila de pacientes
fila = []

# 1. Adicionar pacientes ao final da fila
def adicionar_paciente(nome):
    fila.append(nome)
    print(f"Paciente {nome} adicionado à fila.")

# 2. Chamar o primeiro paciente (remover da fila)
def chamar_paciente():
    if len(fila) > 0:
        paciente = fila.pop(0)  # remove o primeiro da lista
        print(f"Paciente {paciente} pode entrar para a consulta.")
    else:
        print("Não há pacientes na fila.")

# 3. Mostrar a posição de um paciente específico
def posicao_paciente(nome):
    if nome in fila:
        posicao = fila.index(nome) + 1  # +1 porque índice começa no 0
        print(f"O paciente {nome} está na posição {posicao} da fila.")
    else:
        print(f"O paciente {nome} não está na fila.")


adicionar_paciente("Ana")
adicionar_paciente("João")
adicionar_paciente("Maria")
adicionar_paciente("Carlos")

print("\nFila atual:", fila)

chamar_paciente()  # Ana deve sair

print("\nFila atual:", fila)

posicao_paciente("Maria")
posicao_paciente("Ana")  # já saiu da fila

