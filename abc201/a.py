inputs = [
    '5 1 3'
]

def input():
    return inputs.pop(0)


A = list(map(int, input().split()))
A = list(reversed(sorted(A)))
if (A[0] - A[1]) == (A[1] - A[2]):
    print('Yes')
else:
    print('No')