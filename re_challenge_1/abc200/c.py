inputs = [
    '6',
    '123 223 123 523 200 2000'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))
mod200 = [0] * 200

for i in range(len(A)):
    a = A[i]
    d = a % 200
    mod200[d] += 1

result = 0
import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
for i in range(200):
    if mod200[i] >= 2:
        result += combinations_count(mod200[i], 2)

print(result)