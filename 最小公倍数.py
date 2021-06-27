import math

inputs = [
    '30 21'
]


def input():
    return inputs.pop(0)

N, M = list(map(int, input().split()))

y = math.gcd(N, M)
b = int(N * M / y)
print(b)

# math.lcm(N, M)