inputs = [
    '5',
    '3',
    '2',
    '4',
    '3',
    '5'
]


def input():
    return inputs.pop(0)


N = int(input())
A = int(input())
B = int(input())
C = int(input())
D = int(input())
E = int(input())

result = 4
import math
print(result + math.ceil(N / min([A, B, C, D, E])))
