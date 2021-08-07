inputs = [
    '100000'
]


def input():
    return inputs.pop(0)


import math
N = int(input())
sqrt = math.floor(math.sqrt(N))
c = []
for i in range(2, sqrt + 1):
    w = 2
    r = i ** w
    while r <= N:
        if r not in c:
            c.append(r)
        w += 1
        r = i ** w

print(N - len(c))


