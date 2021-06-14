from itertools import combinations

inputs = [
    '7 9',
    '1 2',
    '1 3',
    '2 3',
    '4 5',
    '4 6',
    '4 7',
    '5 6',
    '5 7',
    '6 7'
]


def input():
    return inputs.pop(0)


result = 0

N, M = list(map(int, input().split()))
relations = [[0] * (N + 1) for i in range(N + 1)]
for i in range(M):
    x, y = list(map(int, input().split()))
    relations[x][y] = 1
    relations[y][x] = 1

result = 0
for bit in range(2 ** N):
    flag = 1
    group = []
    for i in range(N):
        if bit >> i & 1:
            group.append(i + 1)
    for x, y in combinations(group, 2):
        if not relations[x][y]:
            flag = 0
    if flag:
        result = max(result, len(group))

print(result)