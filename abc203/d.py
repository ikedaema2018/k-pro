inputs = [
    '3 2',
    '1 7 0',
    '5 8 11',
    '10 4 2'
]

def input():
    return inputs.pop(0)

N, K = map(int, input().split())
maps = []
for _ in range(N):
    maps.append(list(map(int, input().split())))



ac = 1000000000
wa = -1

L = ((K ** 2) // 2) + 1
while wa + 1 < ac:
    wj = (wa + ac) // 2
    depth = [[0] * (N + 1) for _ in range(N + 1)]
    for i in range(N):
        for j in range(N):
            if maps[i][j] > wj:
                depth[i + 1][j + 1] = 1
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            depth[i][j] = depth[i][j - 1] + depth[i][j]
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            depth[j][i] = depth[j - 1][i] + depth[j][i]

    flag = False
    for i in range(K, N + 1):
        for j in range(K, N + 1):
            if L > (depth[i][j] - depth[i - K][j] - depth[i][j - K] + depth[i - K][j - K]):
                flag = True
    if flag:
        ac = wj
    else:
        wa = wj

print(ac)
