inputs = [
    '19 99',
]


def input():
    return inputs.pop(0)


A, B = map(int, input().split(' '))
import math
for c in range(1, 10000 + 1):
    if math.floor(c * 0.08) == A and math.floor(c * 0.1) == B:
        print(c)
        break
else:
    print(-1)
