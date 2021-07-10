# https://atcoder.jp/contests/dp

inputs = [
    '3',
    '10 40 70',
    '20 50 80',
    '30 60 90'
]


def input():
    return inputs.pop(0)


N = int(input())
dp = [[0] * 3 for _ in range(N + 1)]
dp[0][0] = dp[0][1] = dp[0][2] = 0
conditions = [list(map(int, input().split())) for _ in range(N)]

for i in range(N):
    for j in range(0, 3):
        for k in range(0, 3):
            if i >= 1:
                if j == k:
                    continue
                dp[i + 1][k] = max(dp[i][j] + conditions[i][k], dp[i + 1][k])
            else:
                dp[i + 1][k] = dp[i][j] + conditions[i][k]
print(max([dp[N][i] for i in range(3)]))
