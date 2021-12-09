inputs = [
    '198 1.10'
]


def input():
    return inputs.pop(0)


from decimal import Decimal
A, B = map(Decimal, input().split(' '))
import math
print(math.floor((A * B)))