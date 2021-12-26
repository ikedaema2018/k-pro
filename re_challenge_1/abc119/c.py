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


N, A, B, C = map(int, input().split(' '))
L = [int(input()) for _ in range(N)]
import sys

def dfs(idx, la, lb, lc, gc):
    if idx == N:
        if la == 0 or lb == 0 or lc == 0:
            return sys.maxsize
        return abs(A - la) + abs(B - lb) + abs(C - lc) + (gc - 3) * 10
    res = sys.maxsize
    res = min(res, dfs(idx + 1,la + L[idx], lb, lc, gc + 1))
    res = min(res, dfs(idx + 1,la, lb + L[idx], lc, gc + 1))
    res = min(res, dfs(idx + 1,la, lb, lc + L[idx], gc + 1))
    res = min(res, dfs(idx + 1,la, lb, lc, gc))
    return res
print(dfs(0, 0, 0, 0, 0))