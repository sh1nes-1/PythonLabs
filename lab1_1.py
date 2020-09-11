import math

def func(a, x, k):
    return math.sin(a**k + x**k) / math.factorial(math.factorial(k))

def input_float(name):
    print(f'Enter {name}:', end=' ')
    return float(input())

x, a, e = [input_float(name) for name in ['x', 'a', 'e']]

res = func(a, x, 1)
res_prev, k = 0, 2

while res - res_prev >= e:
    res_prev = res
    res += func(a, x, k)
    k += 1

print(res)