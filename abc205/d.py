from bisect import bisect_left, bisect_right

inputs = [
    '5 2',
    '1 2 3 4 5',
    '1',
    '10'
]
# 2
# 9
# 4

def input():
    return inputs.pop(0)


N, q = list(map(int, input().split()))
A = list(map(int, input().split()))
_A = []
for i in range(len(A)):
    _A.append(A[i] - i - 1)

for i in range(q):
    t = int(input())
    idx = bisect_left(_A, t)
    print(t + idx)