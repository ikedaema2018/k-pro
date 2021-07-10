# https://atcoder.jp/contests/dp
import sys

inputs = [
    '10 4',
    '40 10 20 70 80 10 20 70 80 60'
]


def input():
    return inputs.pop(0)


N, K = list(map(int, input().split()))
h = list(map(int, input().split()))
dp = [sys.maxsize] * N
dp[0] = 0
for i in range(0, N - 1):
    for j in range(1, K + 1):
        if i + j >= N:
            break
        dp[i + j] = min(dp[i + j], dp[i] + abs(h[i] - h[i + j]))

print(dp[N - 1])