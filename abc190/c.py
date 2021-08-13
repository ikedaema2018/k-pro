# inputs = [
#     '4 4',
#     '1 2',
#     '1 3',
#     '2 4',
#     '3 4',
#     '3',
#     '1 2',
#     '1 3',
#     '2 3',
# ]

# inputs = [
#     '4 4',
#     '1 2',
#     '1 3',
#     '2 4',
#     '3 4',
#     '4',
#     '3 4',
#     '1 2',
#     '2 4',
#     '2 4',
# ]

inputs = [
    '6 12',
    '2 3',
    '4 6',
    '1 2',
    '4 5',
    '2 6',
    '1 5',
    '4 5',
    '1 3',
    '1 2',
    '2 6',
    '2 3',
    '2 5',
    '5',
    '3 5',
    '1 4',
    '2 6',
    '4 6',
    '5 6'
]


def input():
    return inputs.pop(0)

# Nは皿の個数, Mは条件
N, M = map(int, input().split(' '))
ms = [list(map(int, input().split(' '))) for _ in range(M)]
K = int(input())
candidates = [list(map(int, input().split(' '))) for _ in range(K)]

ans = 0
for bit in range(2 ** K):
    selected = [0] * N
    for j in range(K):
        if (bit >> j) & 1:
            selected[candidates[j][0] - 1] += 1
        else:
            selected[candidates[j][1] - 1] += 1
    count = 0
    for m in range(M):
        if selected[ms[m][0] - 1] and selected[ms[m][1] - 1]:
            count += 1
    ans = max(count, ans)
print(ans)


