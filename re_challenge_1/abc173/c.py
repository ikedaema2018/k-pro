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


H, W, K = map(int, input().split(' '))
M = [list(input()) for _ in range(H)]
import copy

ans= 0
for bit_w in range(2 ** W):
    for bit_h in range(2 ** H):
        m = copy.deepcopy(M)
        for i in range(W):
            if bit_w >> i & 1:
                for h in range(H):
                    m[h][i] = '.'
        for j in range(H):
            if bit_h >> j & 1:
                for w in range(W):
                    m[j][w] = '.'

        c = 0
        for i in range(W):
            for j in range(H):
                if m[j][i] == '#':
                    c += 1
        if c == K:
            ans += 1
print(ans)
