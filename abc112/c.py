inputs = [
    '2',
    '0 0 100',
    '1 1 98'
]


def input():
    return inputs.pop(0)


N = int(input())
dots = sorted([list(map(int, input().split(' '))) for _ in range(N)], reverse=True, key=lambda a: a[2])

for cx in range(101):
    for cy in range(101):
        H = dots[0][2] + abs(dots[0][0] - cx) + abs(dots[0][1] - cy)
        for dot in dots[1:]:
            if dot[2] != max(0, H - abs(dot[0] - cx) - abs(dot[1] - cy)):
                break
        else:
            print(cx, cy, H)
            break


