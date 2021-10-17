inputs = [
    '200',
]


def input():
    return inputs.pop(0)


from functools import reduce
import math

x = 0
def my_gcd(*numbers):
    return reduce(math.gcd, numbers)


k = int(input())
y = 0
result = 0
for a in range(1, k + 1):
    for b in range(1, k + 1):
        for c in range(1, k + 1):
            y += 1
            result += my_gcd(a, b, c)
print(result)
