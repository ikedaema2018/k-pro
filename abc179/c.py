inputs = [
    '100',
]


def input():
    return inputs.pop(0)


N = int(input())
ans = 0
import math
for i in range(1, N + 1):
    r = N - i
    if r == 0:
        continue
    for j in range(1, math.floor(math.sqrt(r)) + 1):
        if r % j == 0:
            k = r // j
            if k == j:
                ans += 1
            else:
                ans += 2
print(ans)

