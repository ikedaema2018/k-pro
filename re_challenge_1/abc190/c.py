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


N, M = map(int, input().split(' '))
conditions = [list(map(int, input().split(' '))) for _ in range(M)]
K = int(input())
ans = 0

take_balls = [list(map(int, input().split(' '))) for _ in range(K)]
for bit in range(2 ** K):
    dishes = [0] * N
    for j in range(K):
        if bit >> j & 1:
            dish = take_balls[j][0] - 1
            dishes[dish] = 1
        else:
            dish = take_balls[j][1] - 1
            dishes[dish] = 1
    cnt = 0
    for condition in conditions:
        if dishes[condition[0] - 1] == 1 and dishes[condition[1] - 1] == 1:
            cnt += 1
    ans = max(ans, cnt)
print(ans)


