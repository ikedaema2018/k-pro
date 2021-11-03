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
A = [True for _ in range(N + 1)]
for _ in range(M):
    A[int(input())] = False

dp = [0] * (N + 1)
dp[0] = 1
dp[1] = 1 if A[1] else 0

for n in range(2, N + 1):
    dp[n] = (dp[n - 1] if A[n - 1] else 0) + (dp[n - 2] if A[n - 2] else 0)
    dp[n] = dp[n] % div

print(dp[N])
