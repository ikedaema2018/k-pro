inputs = [
    '4 4',
    '1 2',
    '2 3',
    '3 4',
    '4 1'
]

def input():
    return inputs.pop(0)

from collections import deque
N, M = list(map(int, input().split()))
conditions = [[-1] * N for _ in range(N)]

for _ in range(M):
    b, c = list(map(lambda a: int(a) - 1, input().split()))
    if c > b:
        for i in range(b, c + 1):
            conditions[b][i] = 1
    else:
        for i in range(c, b + 1):
            conditions[b][i] = 1
result = [[-1] * N for _ in range(N)]


def bfs(u):
    q = deque([u])
    d = [-1] * N

    while q:
        n = q.popleft()
        d[n] = 1
        if n != 0 and conditions[n][n - 1] == 1 and d[n - 1] == -1:
            d[n - 1] = 1
            q.append(n - 1)
        elif n != N - 1 and conditions[n][n + 1] == 1 and d[n + 1] == -1:
            d[n + 1] = 1
            q.append(n + 1)
    return d

count = 0
for i in range(N):
    count += len(list(filter(lambda x: x == 1, bfs(i))))
print(count)