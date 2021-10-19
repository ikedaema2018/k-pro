inputs = [
  '2',
  '1 4'
]


def input():
    return inputs.pop(0)


import math
N = int(input())
X = list(map(int, input().split(' ')))

result = math.inf
for p in range(1, 101):
    res = 0
    for x in X:
        res += ((x - p) ** 2)
    result = min(res, result)
print(result)