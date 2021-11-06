inputs = [
    '5 100 90 80',
    '98',
    '40',
    '30',
    '21',
    '80'
]


def input():
    return inputs.pop(0)

import sys
N, A, B, C = map(int, input().split(' '))
ll = [int(input()) for _ in range(N)]
inf = sys.maxsize


def dfs(idx, la, lb, lc, gc):
    if idx == N:
        if la == 0 or lb == 0 or lc == 0:
            return inf
        else:
            return abs(la - A) + abs(lb - B) + abs(lc - C) + (gc - 3) * 10
    res = dfs(idx + 1, la + ll[idx], lb, lc, gc + 1)
    res = min(res, dfs(idx + 1, la, lb + ll[idx], lc, gc + 1))
    res = min(res, dfs(idx + 1, la, lb, lc + ll[idx], gc + 1))
    res = min(res, dfs(idx + 1, la, lb, lc, gc))
    return res

print(dfs(0, 0, 0, 0, 0))


