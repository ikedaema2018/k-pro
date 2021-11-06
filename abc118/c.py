inputs = [
    '4',
    '2 10 8 40'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))

import fractions
import functools
a = functools.reduce(lambda x, y: fractions.gcd(x, y), A)
print(a)