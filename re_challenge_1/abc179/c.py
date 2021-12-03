inputs = [
    '1000000',
]


def input():
    return inputs.pop(0)


N = int(input())
import math
lim = math.floor((N - 1) ** 0.5)
ans = 0
for i in range(1, N):
    ans += math.floor((N - 1) / i)
print(ans)
