inputs = [
    '2 2 1 1'
]


def input():
    return inputs.pop(0)


W, H, x, y = map(int, input().split(' '))
menseki = (W * H) / 2
if W / 2 == x and H / 2 == y:
    print(f'{menseki} 1')
else:
    print(f'{menseki} 0')
