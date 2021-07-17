inputs = [
    '3',
    '1 2 2',
    '3 1 2',
    '2 3 2'
]

def input():
    return inputs.pop(0)

import collections


N = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))
D = [B[c - 1] for c in C]
A_count = collections.Counter(A)
result = 0

for i in range(N):
    result += A_count[D[i]]

print(result)