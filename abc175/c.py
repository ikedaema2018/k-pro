inputs = [
    '1000000000000000 1000000000000000 1000000000000000'
]


def input():
    return inputs.pop(0)


X, K, D = map(int, input().split())
x = abs(X)
need_k = x // D
if need_k >= K:
    print(x - K * D)
else:
    k = K - need_k
    if k % 2 == 0:
        print(x - need_k * D)
    else:
        print(abs(x - need_k * D - D))
