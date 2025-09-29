def pares_matriz(n):
    for i in range(n):
        for j in range(n):
            print(i,j)

pares_matriz(2)


def exemplo1(n):
    for i in range(n):     # L1
        print(i)           # L2


def exemplo2(n):
    for i in range(0, n, 2):   # L1
        print(i)               # L2


def exemplo3(n):
    while n > 1:        # L1
        print(n)        # L2
        n = n // 2      # L3

def ex4(n):
    i=0
    while i < n and A[i] != k:
        i += 1
    if i < n :
        return i
    return -1
