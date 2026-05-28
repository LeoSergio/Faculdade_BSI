#,,,,,,,,,,PENDENCIAS,,,,,,,,,,,#
# QUERO USAR O os.system('cls') PARA LIMPAR A TELA DPS DE ALGUEM VOTAR TLGD?
# FAZER MENSAGENS DE ERRO
# FAZER OS PERCENTUAIS
# APRESENTAR OS RESULTADOS EM ORDEM DECRESCENTE (MAIOR PRO MENOR)

import os
#==================== Variáveis ====================#

pc = 0 
xbox = 0
play = 0
nint = 0 
mob = 0
nj = 0 

people = 0

resp = input("Você deseja participar da votação?(S/N):")

parar = True

#==================== Computação dos votos ====================#

while resp.upper() == "S": 

    people = people + 1

    print("\nEntrevistando a %dª pessoa:" % people)
    vote = int(input("""

    Qual plataforma você prefere jogar?        
    1. Computador       
    2. Xbox        
    3. Playstation
    4. Nintendo 
    5. Mobile               
    6. Não jogo \n
    -> """))

    if vote == 1:
        print("Você votou em Computador, obrigado pela participação!")
        print('FIM DA VOTAÇÃO')
        pc = pc + 1

    elif vote == 2:
        print("Você votou em Xbox, obrigado pela participação! ")
        print('FIM DA VOTAÇÃO')
        xbox = xbox + 1

    elif vote == 3:
        print("Você votou em Playstation, obrigado pela participação!")
        print('FIM DA VOTAÇÃO')
        play = play + 1

    elif vote == 4:
        print("Você votou em Nintendo, obrigado pela participação!")
        print('FIM DA VOTAÇÃO')
        nint = nint + 1

    elif vote == 5:
        print("Você votou em Mobile, obrigado pela participação!")
        print('FIM DA VOTAÇÃO')
        mob = mob + 1
        

    elif vote == 6:
        print("Você votou em Não jogo, obrigado pela participação")
        print('FIM DA VOTAÇÃO')
        nj = nj + 1

    else:
        print("Voto inválido!")

    #os.system('cls')

    resp = input("Você deseja participar da votação?(S/N):")
    

#==================== apresentação dos resultados ====================#

print('''
|=-=-=-=-=-> RESULTADOS <-=-=-=-=-=|     

-> Foram computados os votos de %d pessoas no total.

-> Votaram em Computador: %d Pessoas.

-> Votaram em Xbox: %d Pessoas.

-> Votaram em Playstation: %d Pessoas.

-> Votaram em Nintendo: %d Pessoas.

-> Votaram em Mobile: %d Pessoas.

-> Votaram em Não jogo: %d Pessoas.

''' %(people, pc, xbox, play, nint, mob, nj))

#|=-=-=-=-=-> PERCENTUAIS <-=-=-=-=-=|#
if people!=0:
    pc = (pc/people)*100
    xbox = (xbox/people)*100
    play = (play/people)*100
    nint = (nint/people)*100
    mob = (mob/people)*100
    nj = (nj/people)*100
    print('''
          |=-=-=-=-=-> PERCENTUAIS <-=-=-=-=-=|
-> Votaram em Computador: %d%%.

-> Votaram em Xbox: %d%% .

-> Votaram em Playstation: %d%% .

-> Votaram em Nintendo: %d%% .

-> Votaram em Mobile: %d%% .

-> Votaram em Não jogo: %d%% .

    '''%(pc, xbox, play, nint, mob, nj))
    print('FIM DO PROGRAMA')
