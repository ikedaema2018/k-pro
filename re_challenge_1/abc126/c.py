inputs = [
    '100000 5',
]


def input():
    return inputs.pop(0)


N, K = map(int, input().split(" "))
import math
ans = 0

for i in range(1, N + 1):
    if K <= i:
        ans += 1
        continue
    ans += (0.5 ** math.ceil(math.log2(math.ceil(K / i))))

print(ans / N)
