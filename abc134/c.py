inputs = [
    '2',
    '5',
    '5'
]


def input():
    return inputs.pop(0)

N = int(input())
A = [int(input()) for _ in range(N)]
_A = list(reversed(sorted(A)))

for a in A:
    if a == _A[0]:
       print(_A[1])
    else:
        print(_A[0])