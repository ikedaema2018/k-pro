inputs = [
    '4 7',
    '4',
    'JIOJOIJ',
    'IOJOIJO',
    'JOIJOOI',
    'OOJJIJO',
    '3 5 4 7',
    '2 2 3 6',
    '2 2 2 2',
    '1 1 4 7'
]


def input():
    return inputs.pop(0)

M, N = list(map(int, input().split()))
K = int(input())
regions = []
for _ in range(M):
    regions.append(list(input()))

rects = []
for _ in range(K):
    rects.append(list(map(int, input().split(' '))))

for rect in rects:
    J = O = I = 0
    a, b, c, d = rect
    for i in range(min(a - 1, c - 1), max(a, c)):
        for j in range(min(b - 1, d - 1), max(b, d)):
            if regions[i][j] == 'J':
                J += 1
            elif regions[i][j] == 'O':
                O += 1
            elif regions[i][j] == 'I':
                I += 1
    print(f'{J} {O} {I}')

