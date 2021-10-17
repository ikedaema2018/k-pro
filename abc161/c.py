inputs = [
    '2 6',
]


def input():
    return inputs.pop(0)


N, K = list(map(int, input().split(' ')))
minus_number = N // K

x = N - minus_number * K
y = abs(x - K)

print(min(x, y))