inputs = [
    '6',
    '200 4 4 9 4 9'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split()))

ans = 0
for i in range(N):
    for j in range(i, N):
        m = min(A[i:j + 1])
        ans = max(ans, m * (j - i + 1))

print(ans)