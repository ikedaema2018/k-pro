inputs = [
    '5 5',
    '.....',
    '.###.',
    '.###.',
    '.###.',
    '.....'
]


def input():
    return inputs.pop(0)


H, W = map(int, input().split(' '))
A = [list(input()) for _ in range(H)]
ans = 0

for h in range(1, H):
    for w in range(1, W):
        cnt = 0
        for i in range(2):
            for j in range(2):
                if A[h - i][w - j] == '#':
                    cnt += 1
        if cnt % 2 == 1:
            ans += 1
print(ans)
