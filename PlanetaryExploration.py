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
J = [[0] * (N + 1) for _ in range(M + 1)]
O = [[0] * (N + 1) for _ in range(M + 1)]
I = [[0] * (N + 1) for _ in range(M + 1)]

for i in range(M):
    places = list(input())
    for j in range(N):
        if places[j] == 'J':
            J[i + 1][j + 1] = 1
        elif places[j] == 'O':
            O[i + 1][j + 1] = 1
        else:
            I[i + 1][j + 1] = 1

for i in range(M):
    for j in range(N):
        J[i + 1][j + 1] = J[i + 1][j + 1] + J[i + 1][j] + J[i][j + 1] - J[i][j]
        O[i + 1][j + 1] = O[i + 1][j + 1] + O[i + 1][j] + O[i][j + 1] - O[i][j]
        I[i + 1][j + 1] = I[i + 1][j + 1] + I[i + 1][j] + I[i][j + 1] - I[i][j]


for _ in range(K):
    a, b, c, d = list(map(int, input().split(' ')))
    a -= 1
    b -= 1
    j = J[c][d] - J[c][b] - J[a][d] + J[a][b]
    o = O[c][d] - O[c][b] - O[a][d] + O[a][b]
    i = I[c][d] - I[c][b] - I[a][d] + I[a][b]
    print(f'{j} {o} {i}')