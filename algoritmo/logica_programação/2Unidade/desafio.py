'''
Escreva um programa no Python que simule um jogo de adivinhação,
onde o computador sorteará um valor entre 1 e 9 e o jogador terá três
chances para acertar o número.
Caso o usuário acerte na primeira tentativa, o programa deverá exibir a
mensagem “VOCÊ TEVE MUITA SORTE” e, em seguida, encerrar o
programa.
Se errar, o programa deverá fornecer uma primeira dica, dizendo “DIGITE
UM NÚMERO MENOR” ou “DIGITE UM NÚMERO MAIOR”, de acordo com o
valor fornecido.

ERROS:
mostrando duas mensagens dos ganhadores(if l20 e elif l32)


'''
import random
print('Jogo de Adivinhação')
option = input('Você deseja Jogar? s/n ')
if option.lower()=='s':
    chance = 1
    resp = int(input('Qual o número?'))
    resultado = random.randint(1,9)
        
    while(chance < 3):
        if (resultado == resp) and (chance<=1):
            print('PARABÉNS,VOCÊ TEM MUITA SORTE!')
            print(resultado)
            print("FIM DO PROGRAMA")
            chance+=1 
        elif(resultado < resp):
            print('Digite outro número!')
            print('DIGITE UM NÚMERO MENOR')
            resp = int(input('Qual o número?'))
            print('FIM DO PROGRAMA,MAIS SORTE NA PROXIMA!')
              
        elif(resultado > resp):
            print('Digite outro Número')
            print('DIGITE UM NÚMERO MAIOR!')
            resp = int(input('Qual o número?'))
            print('FIM DO PROGRAMA,MAIS SORTE NA PROXIMA!')
        elif (resultado == resp) and (chance>=2):
            print('Parabéns você acertou, teve um pouco de sorte')
            chance+=1

        else:
            print(resultado)
    chance+=1
    if chance == 3 and resultado != resp:
        print('FIM DO PROGRAMA, MAIS SORTE NA PRÓXIMA!')
        print('O número correto era:', resultado)
                   
else:
    print('FIM DO PROGRAMA')
