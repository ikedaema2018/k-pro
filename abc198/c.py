inputs = [
    '5 15 0',
]


def input():
    return inputs.pop(0)


import math
R, X, Y = map(int, input().split())
d = math.sqrt(X ** 2 + Y ** 2)
if d == R:
    print(1)
elif d < R:
    print(2)
else:
    print(math.ceil(d / R))
