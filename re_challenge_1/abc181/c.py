inputs = [
    '14',
    '5 5',
    '0 1',
    '2 5',
    '8 0',
    '2 1',
    '0 0',
    '3 6',
    '8 6',
    '5 9',
    '7 9',
    '3 4',
    '9 2',
    '9 8',
    '7 2'
]


def input():
    return inputs.pop(0)


N = int(input())
conditions = [list(map(int, input().split(' '))) for _ in range(N)]
import itertools
for a, b, c in itertools.combinations(conditions, 3):
    b_x, b_y = [b[0] - a[0], b[1] - a[1]]
    c_x, c_y = [c[0] - a[0], c[1] - a[1]]
    if b_x * c_y == b_y * c_x:
        print('Yes')
        break
else:
    print('No')