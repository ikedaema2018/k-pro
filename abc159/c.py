inputs = [
    '999',
]


def input():
    return inputs.pop(0)


L = int(input())
a = L / 3
print(a ** 3)