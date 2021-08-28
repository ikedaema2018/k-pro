inputs = [
    '6 6 8',
    '..##..',
    '.#..#.',
    '#....#',
    '######',
    '#....#',
    '#....#'
]


def input():
    return inputs.pop(0)


import copy
H, W, K = map(int, input().split())
maped = [list(input()) for i in range(H)]
ans = 0
for bit_w in range(2 ** W):
    for bit_h in range(2 ** H):
        new_maped = copy.deepcopy(maped)
        for w in range(W):
            if bit_w >> w & 1:
                # 選んだ縦一列を塗る
                for i in range(H):
                    new_maped[i][w] = '+'
        for h in range(H):
            if bit_h >> h & 1:
                # 選んだ横一列を塗る
                for j in range(W):
                    new_maped[h][j] = '+'
        count = 0
        for hh in range(H):
            for ww in range(W):
                if new_maped[hh][ww] == '#':
                    count += 1
        if count == K:
            ans += 1
print(ans)




