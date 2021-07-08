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
conditions = [[] for _ in range(N)]

for _ in range(M):
    b, c = list(map(lambda x : int(x) - 1, input().split()))
    conditions[b].append(c)


def dfs(u):
    q = deque([u])
    d = [False] * N
    d[u] = True

    while q:
        n = q.popleft()
        for v in conditions[n]:
            if not d[v]:
                d[v] = True
                q.append(v)
    return d

count = 0
for i in range(N):
    count += sum(dfs(i))
print(count)