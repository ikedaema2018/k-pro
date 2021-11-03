inputs = [
    '8 3',
    'ACACTACG',
    '3 7',
    '2 3',
    '1 8'
]


def input():
    return inputs.pop(0)


N, Q = map(int, input().split(' '))
S = list(input())
lrs = [list(map(int, input().split(' '))) for _ in range(Q)]

ac_count = [0] * N

for i in range(1, len(S)):
    if "".join(S[i - 1:i + 1]) == 'AC':
        ac_count[i] = 1
    before = S[i]

import itertools
acc_ac = list(itertools.accumulate(ac_count))
print(acc_ac)

for l, r in lrs:
    print(acc_ac[r - 1] - acc_ac[l - 1])
