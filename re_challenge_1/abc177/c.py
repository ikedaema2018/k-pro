inputs = [
    '4',
    '141421356 17320508 22360679 244949'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))
import itertools
accum = list(itertools.accumulate(A))
ans = 0
b = accum[N - 1]
for i in range(N - 1):
    a = A[i]
    _a = accum[i]
    ans = (ans + (a * (b - _a))) % (10 ** 9 + 7)
print(ans)
