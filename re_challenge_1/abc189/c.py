inputs = [
    '6',
    '2 4 4 9 4 9'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split(' ')))

ans = 0
for i in range(N):
    _min = A[i]
    for j in range(i, N):
        _min = min(A[j], _min)
        ans = max(_min * (j - i + 1), ans)
print(ans)





