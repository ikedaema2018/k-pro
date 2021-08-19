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
for i in range(N):
    for j in range(i):
        for k in range(j):
            x1, y1 = conditions[i]
            x2, y2 = conditions[j]
            x3, y3 = conditions[k]
            x1 -= x3
            x2 -= x3
            y1 -= y3
            y2 -= y3
            if x1 * y2 == x2 * y1:
                print("Yes")
                exit()
print("No")