inputs = [
    '2',
    '1000000000 1000000000'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))

import math
import copy
pre_gcd = copy.deepcopy(A)
pos_gcd = copy.deepcopy(A)

for i in range(1, N):
    pre_gcd[i] = math.gcd(pre_gcd[i], pre_gcd[i - 1])
for i in reversed(range(N - 1)):
    pos_gcd[i] = math.gcd(pos_gcd[i + 1], pos_gcd[i])

ans = 0
for i in range(N):
    if i == 0:
        ans = max(pos_gcd[1], ans)
    elif i == (N - 1):
        ans = max(pre_gcd[N - 2], ans)
    else:
        pre = pre_gcd[i - 1]
        pos = pos_gcd[i + 1]
        ans = max(math.gcd(pre, pos), ans)
print(ans)
