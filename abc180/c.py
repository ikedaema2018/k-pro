inputs = [
    '1000000007',
]


def input():
    return inputs.pop(0)


import math
N = int(input())
ans = []
for i in range(1, math.floor(math.sqrt(N)) + 1):
    if N % i == 0:
        ans += [i, N // i]
for i in sorted(set(ans)):
    print(i)
