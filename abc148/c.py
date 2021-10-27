inputs = [
    '2 3',
]


def input():
    return inputs.pop(0)

import math
def lcm(a, b):
    y = a*b / math.gcd(a, b)
    return int(y)

a, b = list(map(int, input().split(' ')))

print(lcm(a, b))
