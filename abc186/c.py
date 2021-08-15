inputs = [
    17
]


def input():
    return inputs.pop(0)


N = int(input())
import math
print(math.factorial(N - 1) // (math.factorial(11) * math.factorial(N - 1 - 11)))