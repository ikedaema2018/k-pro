inputs = [
    '7 8',
    '2 2',
    '4 5',
    '########',
    '#......#',
    '#.######',
    '#..#...#',
    '#..##..#',
    '##.....#',
    '########'
]


def input():
    return inputs.pop(0)


from collections import deque
gyou, retu = list(map(int, input().split()))
s_y, s_x = list(map(lambda x: int(x) - 1, input().split()))
g_y, g_x = list(map(lambda x: int(x) - 1, input().split()))

map = []
for _ in range(gyou):
    map.append(list(input()))


def bfs(_x, _y):
    q = deque()
    q.append([_x, _y])
    d = [[-1] * retu for _ in range(gyou)]
    d[_y][_x] = 0
    while q:
        x, y = q.popleft()
        jyougesayuu = []
        if y != 0:
            jyougesayuu.append([x, y - 1])
        if x != (retu - 1):
            jyougesayuu.append([x + 1, y])
        if y != (gyou - 1):
            jyougesayuu.append([x, y + 1])
        if x != 0:
            jyougesayuu.append([x - 1, y])
        for nx, ny in jyougesayuu:
            if d[ny][nx] == -1 and map[ny][nx] == '.':
                d[ny][nx] = d[y][x] + 1
                q.append([nx, ny])
    return d

d = bfs(s_x, s_y)
print(d[g_y][g_x])