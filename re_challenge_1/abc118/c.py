inputs = [
    '4',
    '2 10 8 40'
]


def input():
    return inputs.pop(0)


N = input()
A = list(map(int, input().split(' ')))

import math
import functools
print(functools.reduce(lambda a, b: math.gcd(a, b), A))


