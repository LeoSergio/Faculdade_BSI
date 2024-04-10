'''
soma = 0
i = 1
while i<=3:

    i =+ 1
cara ou coroa?
'''
from random import randint
print('Jogo de cara ou coroa')
option = input('Deseja Jogar s/n')
moeda = randint(1,2)
if option == 's'or option == 'S':
    jog1 =int((input("Escolha ,Cara(1) ou coroa(2)?")))
    if jog1 == 1 and moeda == 1:
        print('Você Ganhou, deu Cara')
    elif jog1 == 1 and moeda == 2:
        print('Jogador 1 Perdeu, deu coroa')
    elif jog1 == 2 and moeda == 2:
        print('Você ganhou, deu coroa.')
    elif jog1 == 2 and moeda == 1:
        print('Você perdeu, deu Cara')
    option2 = input('Jogar novamente s/n?')

    while option2 == 's' or option2 == 's':
        jog1 =int((input("Escolha ,Cara(1) ou coroa(2)?")))
        moeda = moeda = randint(1,2)
        if jog1 == 1 and moeda == 1:
            print('Você Ganhou, deu Cara')
        elif jog1 == 1 and moeda == 2:
            print('Jogador 1 Perdeu, deu coroa')
        elif jog1 == 2 and moeda == 2:
            print('Você ganhou, deu coroa.')
        elif jog1 == 2 and moeda == 1:
            print('Você perdeu, deu Cara')
        option2 = input('Jogar novamente s/n?')
    else:
        print('Fim do programa')
        
else:
        print('Fim do programa')

    