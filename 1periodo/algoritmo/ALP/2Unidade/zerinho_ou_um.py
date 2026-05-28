'''
Escreva um programa no Python que simule o tradicional jogo do
ZERINHO ou UM. Nesse jogo, deve haver pelo menos três jogadores, onde
o primeiro é um jogador humano e os demais são simulados pelo
computador. Para jogar, eles devem escolher um dos valores: 0 (ZERO) ou
1 (UM). Vence aquele que apresentar um valor distinto de todos os
outros. Se todos escolherem números iguais, a partida está empatada. O
programa deve indicar se houve um vencedor ou se houve empate.
Permita ao jogador repetir o jogo, caso deseje.
'''
import random
print('Jogo do Zerinho ou Um')
resp = input('Deseja Jogar? s/n ')
if resp.lower() == 's':
    while resp.lower() == 's':
        jog = int(input('Qual o seu número? 0/1'))
        pc1 = random.randint(0,1)
        pc2 = random.randint(0,1)
        if (jog == 1) and (pc1 == 0) and (pc2 == 0):
            print('O resultado é: jogador escolheu = %i, Pc1 escolheu = %i, Pc2 escolheu = %i '%(jog,pc1,pc2))
            print('Humano venceu!')
        elif (jog == 0) and (pc1 == 1) and (pc2 == 1):
            print('O resultado é: jogador escolheu = %i, Pc1 escolheu = %i, Pc2 escolheu = %i '%(jog,pc1,pc2))
            print('Humano venceu!')
        elif (jog == 1) and (pc1 == 0) and (pc2 == 1):
             print('O resultado é: jogador escolheu = %i, Pc1 escolheu = %i, Pc2 escolheu = %i '%(jog,pc1,pc2))
             print('Pc1 venceu!')
        elif (jog == 0) and (pc1 == 1) and (pc2 == 0):
            print('O resultado é: jogador escolheu = %i, Pc1 escolheu = %i, Pc2 escolheu = %i '%(jog,pc1,pc2))
            print('Pc1 venceu!')
        elif (jog == 0) and (pc1 == 0) and (pc2 == 1):
            print('O resultado é: jogador escolheu = %i, Pc1 escolheu = %i, Pc2 escolheu = %i '%(jog,pc1,pc2))
            print('Pc2 venceu!')
        elif (jog == 1) and (pc1 == 1) and (pc2 == 0):
            print('O resultado é: jogador escolheu = %i, Pc1 escolheu = %i, Pc2 escolheu = %i '%(jog,pc1,pc2))
            print('Pc2 venceu!')
        elif(jog == 1) and (pc1 == 1) and (pc2 == 1):
            print('O resultado é EMPATE: jogador escolheu = %i, Pc1 escolheu = %i, Pc2 escolheu = %i'%(jog,pc1,pc2))
        else:
            print('ERRO, VERIFIQUE AS INFORMAÇÕES!!!')
        resp = input('Deseja jogar Novamente? s/n')
    else:
        print('FIM DO PROGRAMA')
else:
    print('FIM DO PROGRAMA')

