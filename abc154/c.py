inputs = [
    '3 0',
    '1000000000 1000000000 1000000000'
]


def input():
    return inputs.pop(0)


N, K = map(int, input().split(' '))
H = list(map(int, input().split(' ')))
H = sorted(H, reverse=True)[K:]

print(sum(H))
