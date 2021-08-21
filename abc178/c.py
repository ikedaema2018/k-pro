inputs = [
    '869121',
]


def input():
    return inputs.pop(0)


import math
# 2つの順列の数 * 9 ** 残りの桁数
N = int(input())
if N < 2:
    print(0)
else:
    # 2つの順列の数
    a = math.factorial(N) // math.factorial(N - 2)
    print(a * 9 ** (N - 2))
