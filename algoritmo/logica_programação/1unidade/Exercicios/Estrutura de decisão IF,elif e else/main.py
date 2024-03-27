'''
Exibindo valores em ordem crescente
Escreva um programa em Python que leia três
valores inteiros e escreva-os em ordem
crescente.
'''
print('Digite as seguintes informações:')
num1 = int(input('Número 1:'))
num2 = int(input('Número2:'))
num3 = int(input('Número3:'))
if (num1 <= num2):   
    if num2 <= num3:
        print('Ordem crescente: %i < %i < %i'%(num1,num2,num3))
elif num1 <= num3:
    print('Ordem crescente: %i < %i < %i '%(num1,num3,num2))
else:
    print('Ordem Crescente: %i < %i < %i '%())
