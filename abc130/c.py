inputs = [
    '2 2 1 1'
]


def input():
    return inputs.pop(0)


W, H, x, y = list(map(int, input().split(' ')))

print(f'{W * H / 2} {1 if W / 2 == x and H / 2 == y else 0}')