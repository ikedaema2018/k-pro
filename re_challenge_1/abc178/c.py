inputs = [
    '869121',
]


def input():
    return inputs.pop(0)


N = int(input())
print((10 ** N - 9 ** N * 2 + 8 ** N) % (10 ** 9 + 7))



