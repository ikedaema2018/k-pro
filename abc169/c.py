inputs = [
    '1000000000000000 9.99',
]


def input():
    return inputs.pop(0)


x = input().split()
A = int(x[0])
from decimal import Decimal
B = Decimal(x[1])
print(A * B // 1)
