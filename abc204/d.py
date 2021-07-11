inputs = [
    '9',
    '3 14 15 9 26 5 35 89 79'
]

def input():
    return inputs.pop(0)


import math
N = int(input())
cooks = list(map(int, input().split()))
all = sum(cooks)
half = math.floor(all / 2)

dp = [[0 for j in range(half + 1)] for i in range(N + 1)]

for i in range(N):
    for sum_t in range(half + 1):
        if sum_t - cooks[i] >= 0:
            dp1 = dp[i][sum_t - cooks[i]] + cooks[i]
        dp2 = dp[i][sum_t]
        if sum_t - cooks[i] >= 0 and dp1 > dp[i + 1][sum_t]:
            dp[i + 1][sum_t] = dp1
        if dp2 > dp[i + 1][sum_t]:
            dp[i + 1][sum_t] = dp2

print(all - dp[N][half])