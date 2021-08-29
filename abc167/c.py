
inputs = [
    '8 5 22',
    '100 3 7 5 3 1',
    '164 4 5 2 7 8',
    '334 7 2 7 2 9',
    '234 4 7 2 8 2',
    '541 5 4 3 3 6',
    '235 4 8 6 9 7',
    '394 3 6 1 6 2',
    '872 8 4 3 7 2'
]


def input():
    return inputs.pop(0)


N, M, X = map(int, input().split())
conditions = [list(map(int, input().split())) for _ in range(N)]


import sys
ans = sys.maxsize
for bit in range(2 ** N):
    trainings = [0] * M
    m = 0
    for j in range(N):
        if (bit >> j) & 1:
            m += conditions[j][0]
            for i in range(1, len(conditions[j])):
                trainings[i - 1] += conditions[j][i]
    if all(t >= X for t in trainings):
        ans = min(ans, m)
if ans == sys.maxsize:
    print(-1)
else:
    print(ans)


