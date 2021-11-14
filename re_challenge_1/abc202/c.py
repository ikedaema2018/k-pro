inputs = [
    '3',
    '2 3 3',
    '1 3 3',
    '1 1 1'
]


def input():
    return inputs.pop(0)

N = int(input())
import collections
A = collections.Counter(list(map(int, input().split(' '))))
B = list(map(int, input().split(' ')))
C = list(map(int, input().split(' ')))
result = 0
for i in range(len(C)):
    c = C[i]
    b = B[c - 1]
    result += A[b]

print(result)
