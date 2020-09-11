import numpy as np

def input_int(name):
    print(f'Enter {name}:', end=' ')
    return int(input())

n = input_int('n')
A = np.array([[input_int(f'A[{i}][{j}]') for j in range(n)] for i in range(n)])
Y = [[A[i].dot(A[:,j]) for j in range(n)] for i in range(n)]

print(Y)