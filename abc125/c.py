inputs = [
    '2',
    '1000000000 1000000000'
]


def input():
    return inputs.pop(0)


from fractions import gcd
N = int(input())
A = list(map(int, input().split(' ')))

from copy import copy
right = copy(A)
for i in range(1, N):
    right[i] = gcd(right[i - 1], right[i])
left = copy(A)
for i in reversed(range(0, N - 1)):
    left[i] = gcd(left[i + 1], left[i])

result = 0
for i in range(N):
    if i == 0:
        result = max(left[1], result)
    elif i == (N - 1):
        result = max(right[i - 1], result)
    else:
        a = right[i - 1]
        b = left[i + 1]
        c = gcd(a, b)
        result = max(c, result)
print(result)
