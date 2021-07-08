inputs = [
    '9',
    '3 14 15 9 26 5 35 89 79'
]

def input():
    return inputs.pop(0)

from itertools import combinations
import math
N = int(input())
cooks = list(map(int, input().split()))
all = sum(cooks)
half = math.ceil(all / 2)

result = all
for i in range(1, N):
    conditions = combinations(cooks, i)
    for condition in conditions:
        condition_all = sum(condition)
        if half <= condition_all:
            result = min(condition_all, result)

print(result)



