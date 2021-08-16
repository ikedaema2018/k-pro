inputs = [
    '5 5',
    '0 1 1 1 1',
    '1 0 1 1 1',
    '1 1 0 1 1',
    '1 1 1 0 1',
    '1 1 1 1 0'
]


def input():
    return inputs.pop(0)


N, K = map(int, input().split(' '))
T = []
for i in range(N):
    T.append(list(map(int, input().split(' '))))

import itertools
routes = list(itertools.permutations(list(range(1, N))))
ans = 0
for route in routes:
    distance = 0
    current = 0
    for nxt in route:
        distance += T[current][nxt]
        current = nxt
    distance += T[current][0]
    if distance == K:
        ans += 1
print(ans)
