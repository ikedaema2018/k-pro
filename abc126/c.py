inputs = [
    '100000 5'
]


def input():
    return inputs.pop(0)


N, K = map(int, input().split(' '))

import math
result = 0
for i in range(1, N + 1):
    init = 1 / N
    goal = math.ceil(K / i)
    pow_count = math.ceil(math.log(goal, 2))
    a = init * (0.5 ** pow_count)
    result += a
print(result)
