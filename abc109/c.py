

inputs = [
    '3 81',
    '33 105 57'
]


def input():
    return inputs.pop(0)



import math
from functools import reduce
N, X = map(int, input().split(' '))
xxx = list(map(int, input().split(' ')))
new_xxx = []
for i in range(N):
    if xxx[i] != X:
        new_xxx.append(abs(xxx[i] - X))

print(reduce(lambda a, b: math.gcd(a, b), new_xxx))
