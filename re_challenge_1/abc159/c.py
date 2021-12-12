inputs = [
    '999',
]


def input():
    return inputs.pop(0)


L = int(input())
print((L / 3) ** 3)