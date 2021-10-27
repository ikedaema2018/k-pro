inputs = [
    '99992',
]


def input():
    return inputs.pop(0)


import math
def isPrime(n):
    if n == 2:
        return False
    t = math.floor(math.sqrt(n))
    for i in range(2, int(t) + 1):
        if n % i == 0:
            return True
    return False

X = int(input())
x = X
while True:
    if not isPrime(x):
        break
    x += 1
print(x)