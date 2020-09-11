import math
    
def sum(k):
    def a(k):
        if k == 1: 
            return 1
        return 0.5 * (math.sqrt(b(k - 1)) + 0.5 * math.sqrt(a(k - 1)))

    def b(k):
        if k == 1: 
            return 1
        return 2 * a(k - 1)**2 + b(k - 1)

    if k == 1:
        return 1
    return sum(k - 1) + (a(k) * b(k)) / math.factorial(k)

n = int(input())
print(sum(n))