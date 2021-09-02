inputs = [
    '10 10 1',
    '1 10 9 1'
]


def input():
    return inputs.pop(0)



N, M, Q = map(int, input().split())
abcds = [list(map(int, input().split())) for _ in range(Q)]


def calc(arr):
    score = 0
    for a, b, c, d in abcds:
        if arr[b - 1] - arr[a - 1] == c:
            score += d
    return score
ans = 0

# 広義単調増加
# N + (M - 1) choose M - 1
import itertools
for com in itertools.combinations(list(range(N + M - 1)), M - 1):
    init = 1
    A = []
    com_i = 0
    for i in range(N + M - 1):
        if com_i >= len(com):
            A.append(init)
        else:
            c = com[com_i]
            if c == i:
                com_i += 1
                init += 1
            else:
                A.append(init)
    ans = max(ans, calc(A))
print(ans)

