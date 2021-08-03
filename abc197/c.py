inputs = [
    '3',
    '1 5 7'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split()))
import sys
m = sys.maxsize

if len(A) == 1:
    print(A[0])
else:
    for bit in range(2 ** (N - 1)):
        i_s = []
        for i in range(N - 1):
            if (bit >> i) & 1:
                i_s.append(i + 1)
        if len(i_s) == 0:
            continue
        _or = 0
        _xor = 0
        for i in range(N):
            _or |= A[i]
            if (i + 1) in i_s:
                _xor ^= _or
                _or = 0
        _xor ^= _or
        m = min(m, _xor)
    print(m)

