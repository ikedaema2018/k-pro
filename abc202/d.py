inputs = [
    '30 30 118264581564861424'
]

def input():
    return inputs.pop(0)

from math import comb
A, B, K = list(map(int, input().split()))

ab = ''
a = A
b = B

while len(ab) < A + B and a > 0:
    if K <= comb(a - 1 + b, a - 1):
        a -= 1
        ab += 'a'
    else:
        K -= comb(a - 1 + b, a - 1)
        b -= 1
        ab += 'b'

ab = ab.ljust(A + B, 'b')
print(ab)
