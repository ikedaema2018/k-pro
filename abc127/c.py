inputs = [
    '100000 1',
    '1 100000'
]


def input():
    return inputs.pop(0)

import itertools
N, M = map(int, input().split(' '))
lrs = [list(map(int, input().split(' '))) for _ in range(M)]
acc = [0] * (N + 1)

for lr in lrs:
    l, r = lr
    acc[l - 1] += 1
    acc[r] -= 1

acc_result = list(itertools.accumulate(acc))

print(acc_result.count(M))
