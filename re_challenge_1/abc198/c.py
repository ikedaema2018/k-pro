inputs = [
    '3 4 4',
]


def input():
    return inputs.pop(0)


R, X, Y = map(int, input().split(' '))
distance = ((0 - X) ** 2 + (0 - Y) ** 2) ** 0.5

if distance == 0:
    print(0)
elif distance < R:
    print(2)
elif distance % R == 0:
    print(int(distance // R))
else:
    print(int(distance // R + 1))