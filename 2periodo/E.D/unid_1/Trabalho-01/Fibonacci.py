def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:        
        return fibonacci(n - 1) + fibonacci(n - 2)

def fibonacciIt(n):
    t0,t1 = 0,1
    for i in range(2,n+1):
        ti = t0 + t1
        t0 = t1
        t1 = ti 
    return t1