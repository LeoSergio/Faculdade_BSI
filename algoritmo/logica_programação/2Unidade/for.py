'''
1.Pares menores que 20, iniciando em zero OK    
2.Ímpares entre 10 e 30  ok
3.Múltiplos de 4 entre 1 e 25 ok
4.Divisores de 30 entre 10 e 20 ok
5.Ímpares menores que x (informado pelo usuário) ok
6.Múltiplos de 7 entre a e b (informado pelo usuário) ok
7.Exiba os números de 1 até 100 substituindo os multiplos de 4 e números terminados em 4 pela palavra PIM.

print('Digite as informações que se pedem!')
a= int(input('Digite um número: '))
b= int(input('Digite um número: '))

print('INICIO DO LAÇO')

for x in range (a,b+1):
        if x % 7== 0:
            print(x)
print('FIM DO LAÇO')
'''
for x in range(1,100):
    if (x % 4 == 0) or (x%10==4):
        x='PIM'     
    print(x)