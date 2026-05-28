'''
Escreva um programa no Python que simule um jogo de dados disputado
entre um jogador humano e um computador, onde dois dados
eletrônicos (simulados por software, através de valores aleatórios) devem
ser lançados simultaneamente. O jogador vence se a soma dos pontos
dos dois dados for 7 ou 11, caso contrário vence o computador
Ao final da partida, o programa deverá perguntar ao usuário se o mesmo
deseja jogar novamente. O programa deverá permitir uma nova partida,
caso a resposta seja afirmativa ou encerrar em caso negativo.
'''
import random

resp = input('Deseja jogar? s/n')
if resp == 's' or 'S':
    while resp == 'S' or resp == 's':
        dado1 = random.randint(1,6)
        dado2 = random.randint(1,6)
        jog = dado1 + dado2
        soma = dado1 + dado2
        if (jog == 7 or jog ==11):
            print('Humano venceu')
            print('Resultado dos Dados é',soma)
        else:
            print('Computador venceu')
            print('Resultado dos Dados é',soma)
        resp = input('Jogar Novamente? s/n')
else:
    print('Fim do Programa')
