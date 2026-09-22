def h(x):
    return x+1
def g(x):
    return h(x)+2+k(x+1)
def f(x):
    return g(x)+1
def k(x):
    return x+1

def factorielle(n):
    assert n>=0
    if n==1:
        return 1
    else:
        return n*factorielle(n-1)
    
def fact_iterative(n):
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    return fact

def fact_recursive(n):
    assert n >= 0
    if n==1:
        return 1
    else:
        return n*fact_recursive(n-1)

#Q7/8/9
fact_iterative(1000)
fact_recursive(1000)
