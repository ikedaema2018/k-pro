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
    for j in range(2, math.floor(math.log(N, i)) + 1):
        c.append(i ** j)

print(N - len(set(c)))


