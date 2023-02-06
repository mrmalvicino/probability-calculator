import math

def factorial(x):
    factorial = 1
    for i in range(0,x,1):
        factorial = factorial*(x-i)
    return factorial

def comb(n, m):
    comb = factorial(n)/(factorial(n-m)*factorial(m))
    return comb

def p_Bi(x_i, n, p):
    prob_x_i = comb(n,x_i)*(p**x_i)*(1-p)**(n-x_i)
    return prob_x_i

def p_G(x_i, p):
    prob_x_i = p*(1-p)**(x_i-1)
    return prob_x_i

def p_H(x_i, n, N, S):
    prob_x_i = (comb(S, x_i)*comb(N-S, n-x_i))/comb(N, n)
    return prob_x_i

def p_Po(x_i, A):
    prob_x_i = A**x_i/(math.exp(A)*factorial(x_i))
    return prob_x_i