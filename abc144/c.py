inputs = [
    '10000000019',
]


def input():
    return inputs.pop(0)



N = int(input())
M = int(N ** 0.5)

import sys
result = sys.maxsize
for i in range(1, M + 1):
    if N % i != 0:
        continue
    divided = int(N / i)
    result = min(divided - 1 + i - 1, result)
print(result)