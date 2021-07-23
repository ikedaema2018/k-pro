inputs = [
    '8691 20'
]


def input():
    return inputs.pop(0)


N, K = list(map(int, input().split()))
for _ in range(K):
    if N % 200 == 0:
        N = N // 200
    else:
        N = int(str(N) + '200')

print(N)

