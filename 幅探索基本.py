inputs = [
    '11 9',
    '0 1',
    '0 2',
    '1 3',
    '1 4',
    '2 5',
    '2 6',
    '3 7',
    '5 8',
    '8 9'
]


def input():
    return inputs.pop(0)

from collections import deque

n, m = list(map(int, input().split()))
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = list(map(int, input().split()))
    g[a].append(b)
    g[b].append(a)

def bfs(u):
    queue = deque([u])
    d = [None] * n
    d[u] = 0
    while queue:
        v = queue.popleft()
        for i in g[v]:
            if d[i] is None:
                d[i] = d[v] + 1
                queue.append(i)
    return d

d = bfs(0)
print(d)


