inputs = [
    '199'
]


def input():
    return inputs.pop(0)


print((int(input()) - 1) // 100 + 1)