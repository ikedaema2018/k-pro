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
conditions = [list(input()) for _ in range(H)]

ans = 0
for h in range(H - 1):
    for w in range(W - 1):
        cnt = 0
        if conditions[h][w] == '#':
            cnt += 1
        if conditions[h + 1][w] == '#':
            cnt += 1
        if conditions[h][w + 1] == '#':
            cnt += 1
        if conditions[h + 1][w + 1] == '#':
            cnt += 1

        if cnt == 1 or cnt == 3:
            ans += 1
print(ans)
