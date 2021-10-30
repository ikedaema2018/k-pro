inputs = [
    '3',
    '500 300 200'
]


def input():
    return inputs.pop(0)


N = int(input())
V = sorted(list(map(int, input().split(' '))))

from functools import reduce
result = reduce(lambda x, y: (x + y) / 2, V)
print(result)