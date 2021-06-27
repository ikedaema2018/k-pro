inputs = [
    '30 21'
]


def input():
    return inputs.pop(0)


N, M = list(map(int, input().split()))


def GCD(a, b):
    if b == 0:
        return a
    return GCD(b, a % b)

print(GCD(N, M))