'''
Escreva um programa em Python que leia dia
e mês de uma determinada data e a
localização (hemisfério) do usuário e
determine qual a estação do ano
correspondente à data.

Essas datas são fixas?
O que ocorre nos anos bissextos?
    sul
primavera
    22set - 21dez
verão
    22dez - 21 marc
outono
    22marc - 21 jun
inverno
    22jun - 21set
'''
import datetime
print("Qual a estação do ano?")

dataAtual = datetime.date.today()
day = 27
month = 12

if month >= 9:
    if month <= 11:
        print('Verão no Hemisfério Sul')
    elif month == 12:
        if day <= 21:
            print('Verão no Hemisfério Sul')
        else:
            print('Primavera no Hemisfério Sul')
elif month >= 1:
    if month <= 3:
        print('Verão no Hemisfério Sul')
    elif month == 3:
        if day <= 21:
            print('Verão no Hemisfério Sul')
        else:
            print('Outono no Hemisfério Sul')
elif month >= 4:
    if month <= 5:
        print('Outono no Hemisfério Sul')
    elif month == 6:
        if day <= 21:
            print('Outono no Hemisfério Sul')
        else:
            print('Inverno no Hemisfério Sul')
else:
    print('Inverno no Hemisfério Sul')




