from itertools import combinations


inputs = [
    '4',
    '4 1 3 3'
]


def input():
    return inputs.pop(0)


N = int(input())
conditions = list(map(int, input().split()))

r = [{'idx': 0, 'val': 0}]
for i in range(len(conditions)):
    r.append({'idx': i + 1, 'val': r[i]['val'] + conditions[i]})



for i in range(1, N + 1):
    result = -1
    for con in combinations(r[1:], i):
        if con[-1]['idx'] - con[0]['idx'] + 1 != i:
            continue
        result = max(con[-1]['val'] - r[con[0]['idx'] - 1]['val'], result)
    print(result)