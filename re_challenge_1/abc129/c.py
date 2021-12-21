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


N, M = map(int, input().split(' '))
dp = [0] * (N + 1)
A = [True for _ in range(N + 1)]
for _ in range(M):
    A[int(input())] = False
dp[0] = 1
dp[1] = 1 if A[1] is True else 0

for i in range(2, N + 1):
    if A[i] is False:
        dp[i] = 0
    else:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[N] % 1000000007)


