inputs = [
    '10 936447862',
    '854 810169801',
    '691 957981784',
    '294 687140254',
    '333 932608409',
    '832 42367415',
    '642 727293784',
    '139 870916042',
    '101 685539955',
    '853 243593312',
    '369 977358410'
]


def input():
    return inputs.pop(0)


N, W = map(int, input().split())
wv = [map(int, input().split()) for _ in range(N)]
dp = [[0] * (W + 1) for _ in range(N + 1)]

for i, (v, w) in enumerate(wv):
    for j in range(W + 1):
        dp[i + 1][j] = dp[i][j]
        if j - w >= 0:
            dp[i + 1][j] = max(dp[i + 1][j], dp[i][j - w] + v)

print(dp[-1][-1])
