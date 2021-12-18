inputs = [
    '2',
    '100 1 1',
    '1 100'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))
B = list(map(int, input().split(' ')))

ans = 0
for i in range(N - 1, -1, -1):
    minus1 = min(A[i + 1], B[i])
    ans = ans + minus1
    B[i] = B[i] - minus1

    minus2 = min(A[i], B[i])
    ans = ans + minus2
    A[i] = A[i] - minus2

print(ans)

