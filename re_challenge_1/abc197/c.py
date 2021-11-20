inputs = [
    '4',
    '1 3 3 1'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))
import sys
res = sys.maxsize

for bit in range(2 ** (N - 1)):
    _or = 0
    _res = 0
    for j in range(0, N - 1):
        if bit >> j & 1:
            _or |= A[j]
            _res ^= _or
            _or = 0
        else:
            _or |= A[j]
    else:
        _or |= A[N - 1]
        _res ^= _or
    res = min(res, _res)
print(res)


