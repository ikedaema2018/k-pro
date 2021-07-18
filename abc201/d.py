inputs = [
    '1 1',
    '-'
]


def input():
    return inputs.pop(0)


def trans(s):
    if s == '+':
        return 1
    else:
        return -1
INF = 1e9


H, W = list(map(int, input().split()))
Map = [list(map(trans, list(input()))) for _ in range(H)]
dp = [[0] * (W + 1) for _ in range(H + 1)]

for i in reversed(range(H)):
    for j in reversed(range(W)):
        if (j + 1 == W) and (i + 1 == H):
            continue

        turn = ((i + j) % 2 == 0)
        if turn:
            tmp1 = tmp2 = -INF
            if i + 1 != H:
                tmp1 = dp[i + 1][j] + Map[i + 1][j]
            if j + 1 != W:
                tmp2 = dp[i][j + 1] + Map[i][j + 1]
            dp[i][j] = max([tmp1, tmp2])
        else:
            tmp1 = tmp2 = INF
            if i + 1 != H:
                tmp1 = dp[i + 1][j] + -(Map[i + 1][j])
            if j + 1 != W:
                tmp2 = dp[i][j + 1] + -(Map[i][j + 1])
            dp[i][j] = min([tmp1, tmp2])

if dp[0][0] == 0:
    print('Draw')
elif dp[0][0] > 0:
    print('Takahashi')
else:
    print('Aoki')