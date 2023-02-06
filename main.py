import functions

x_0 = 0
x_F = 7

X = []
F_i = -functions.p_Po(x_0-1, 2)
for x_i in range(x_0,x_F+1,1):
    p_i = functions.p_Po(x_i, 2)
    print(f'p_Po(x={x_i}) = {p_i}')
    F_i = F_i + functions.p_Po(x_i-1, 2)
    X.append((x_i, p_i, F_i))

print(X)