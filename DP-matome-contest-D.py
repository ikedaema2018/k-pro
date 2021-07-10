inputs = [
    '3 8',
    '3 30',
    '4 50',
    '5 60'
]


def input():
    return inputs.pop(0)

n, w = list(map(int,input().split()))
wv = []
for i in range(n):
    array = list(map(int, input().strip().split()))
    wv.append(array)
dp = [[0 for j in range(w + 1)]for i in range(n + 1)]

for i in range(n):
    for sum_w in range(w + 1):
        if sum_w - wv[i][0] >= 0:
            dp1 = dp[i][sum_w - wv[i][0]] + wv[i][1]
        dp2 = dp[i][sum_w]
        if sum_w - wv[i][0] >= 0 and dp1 > dp[i + 1][sum_w]:
            dp[i + 1][sum_w] = dp1
        if dp2 > dp[i + 1][sum_w]:
            dp[i + 1][sum_w] = dp2

print(dp[n][w])