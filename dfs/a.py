inputs = [
    '4 4',
    '...s',
    '....',
    '....',
    '.g..'
]


def input():
    return inputs.pop(0)


from collections import deque
H, W = map(int, input().split())
map = [list(input()) for i in range(H)]
visited_list = [[0] * W for _ in range(H)]

_h = _w = -1
for h in range(H):
    for w in range(W):
        if map[h][w] == 's':
            _h = h
            _w = w

stack = deque([[_h, _w]])
visited_list[_h][_w] = 1
flag = False
while len(stack) != 0:
    h, w = stack.pop()
    for x, y in ([-1, 0], [1, 0], [0, -1], [0, 1]):
        n_h = h + y
        n_w = w + x
        if n_h >= H or n_h < 0 or n_w >= W or n_w < 0 or map[n_h][n_w] == '#' or visited_list[n_h][n_w] == 1:
            continue
        if map[n_h][n_w] == 'g':
            flag = True
            break
        visited_list[n_h][n_w] = 1
        stack.append([n_h, n_w])

if flag:
    print('Yes')
else:
    print('No')