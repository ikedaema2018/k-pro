inputs = [
    '3',
    '0 0',
    '1 0',
    '0 1'
]


def input():
    return inputs.pop(0)


N = int(input())
l = [list(map(int, input().split())) for _ in range(N)]

import itertools
groups = list(itertools.permutations(l, N))


result = 0
for group in groups:
    before_iti = group[0]
    c = 0
    for iti in group[1:]:
        a = (before_iti[0] - iti[0]) ** 2
        b = (before_iti[1] - iti[1]) ** 2
        c += (a + b) ** 0.5
        before_iti = iti
    result += c

print(result / len(groups))