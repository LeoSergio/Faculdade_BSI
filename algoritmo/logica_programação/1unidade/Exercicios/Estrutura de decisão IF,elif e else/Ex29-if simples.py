'''
Escreva um programa em Python que leia uma data, composta por dia, mês e ano (cada um
informado separadamente) e verifique se corresponde a uma data válida. Verifique se o valor
informado para o ano é maior do que zero, se o valor informado para o mês está
compreendido entre 1 e 12 e se o dia existe naquele mês. Considere, ainda, se o ano é ou
não bissexto, lembrando que para um ano ser considerado bissexto, ele deve ser divisível
por 4 e, ao mesmo tempo, não ser divisível por 100, a menos que seja divisível por 400.
'''
import datetime
print('Digite as seguintes informações:')
day = int(input('Qual o dia atual?'))
month = int(input('Qual o mês atual?'))
year = int(input('Qual o Ano atual?'))

if( day == 29) and (month != 2) or (day == 28 and month != 2):
      print('%s / %s / %s Data inválida'%(day,month,year))
elif (day <= 31 and day >= 1) and (year > 0) and (month >= 1 and month <= 12 and month !=2):
        print('%s / %s / %s Data válida'%(day,month,year))
        
if(year % 4 == 0) and (year % 100 != 0 or year % 400 == 0):
        if (day == 29 and month == 2) and (year > 0) and (month >= 1 and month <= 12):
                print('%s / %s / %s Data válida para o mês de fevereiro'%(day,month,year))
                print('%s Ano bissexto'%(year))
elif (day <= 28 and month == 2) and (year > 0) and (month >= 1 and month <= 12):
     print('Data válida e ano não é bissexto')
else:
     print('%s o ano não é bissexto'%(year))
    

