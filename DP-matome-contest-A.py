# https://atcoder.jp/contests/dp
import sys

inputs = [
    '6',
    '30 10 60 10 60 50'
]


def input():
    return inputs.pop(0)


N = int(input())
h = list(map(int, input().split()))
dp = [sys.maxsize] * N
dp[0] = 0
for i in range(1, N):
    if i > 1:
        dp[i] = min(dp[i - 2] + abs(h[i] - h[i - 2]), dp[i - 1] + abs(h[i] - h[i - 1]))
    else:
        dp[i] = dp[i - 1] + abs(h[i] - h[i - 1])


print(dp[N - 1])
