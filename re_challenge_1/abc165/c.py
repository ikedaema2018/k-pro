inputs = [
    '3 4 3',
    '1 3 3 100',
    '1 2 2 10',
    '2 3 2 10'
]


def input():
    return inputs.pop(0)


N, M, Q = map(int, input().split(' '))
condition = []
for _ in range(Q):
    condition.append(list(map(int, input().split(' '))))

import itertools
A = list(itertools.combinations_with_replacement(range(1, M + 1), N))

ans = 0
for _a in A:
    result = 0
    for a, b, c, d in condition:
        if _a[b - 1] - _a[a - 1] == c:
            result += d
        ans = max(ans, result)
print(ans)
