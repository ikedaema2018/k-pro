inputs = [
    '8',
    '7 3 5 4 2 1 6 8',
    '3 8 2 5 4 6 7 1'
]


def input():
    return inputs.pop(0)


N = int(input())
P = int("".join(input().split(' ')))
Q = int("".join(input().split(' ')))

import itertools
comb = list(itertools.permutations([i for i in range(1, N + 1)], N))

for i in range(len(comb)):
    num = int("".join(map(str, comb[i])))
    if num == P:
        p_count = i + 1
    if num == Q:
        q_count = i + 1

print(abs(p_count - q_count))


