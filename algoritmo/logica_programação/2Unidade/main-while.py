'''
soma = 0
i = 1
while i<=3:

    i =+ 1
'''
import random

jog = random.randint(1,6)
comp = random.randint(1,6)
print("Jogador : ", jog)
print("Computador: ", comp)
if jog > comp:
 print("Jogador Ganhou!")
elif comp > jog:
 print("Computador Ganhou!")
else:
 print("Empate!")
print("Fim do Jogo!")