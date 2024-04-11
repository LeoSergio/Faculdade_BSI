print("Programa Operador Divisão Inteira")

a = int(input("Dividendo: "))

b = int(input("Divisor: "))

resto = a

quoc = 0

while resto >= b:
    quoc += 1     # linha 7

    resto = resto - b

print("A divisão inteira de %d por %d é %d"%(a, b, ))  # linha 9