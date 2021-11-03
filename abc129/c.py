inputs = [
    '100 5',
    '1',
    '23',
    '45',
    '67',
    '89'
]


def input():
    return inputs.pop(0)


div = 1000000007
N, M = map(int, input().split(' '))
A = [int(input()) for _ in range(M)]

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1 if 1 not in A else 0

for n in range(2, N + 1):
    dp[n] = (dp[n - 1] if n - 1 not in A else 0) + (dp[n - 2] if n - 2 not in A else 0)
    dp[n] = dp[n] % div

print(dp[N])
