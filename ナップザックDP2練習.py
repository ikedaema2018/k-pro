inputs = [
    '3 10',
    '15 9',
    '10 6',
    '6 4'
]


def input():
    return inputs.pop(0)

import bisect


N, W = map(int, input().split())
vw = [list(map(int, input().split())) for _ in range(N)]
V = sum(x[0] for x in vw)
INF = 1 << 60
dp = [INF] * (V + 1)
dp[0] = 0
for v, w in vw:
    dp_tmp = dp[:]
    for j in range(1, V + 1):
        idx_prev = max(0, j - v)
        dp_tmp[j] = min(dp[j], dp[idx_prev] + w)
    dp = dp_tmp
print(bisect.bisect_right(dp, W) - 1)
