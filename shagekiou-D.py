# https://atcoder.jp/contests/abc023/tasks/abc023_d
from math import ceil
import sys
inputs = [
'6',
'100 1',
'100 1',
'100 1',
'100 1',
'100 1',
'1 30'
]


def input():
    return inputs.pop(0)


N = int(input())
conditions = [tuple(map(int, input().split())) for _ in range(N)]


def ok(limit):
    limit_times = [(limit - h) / s for h, s in conditions]
    limit_times.sort()
    for i in range(N):
        if limit_times[i] < i:
            return False
    return True

low = 0
high = sys.maxsize
while low < high:
    mid = (low + high) // 2
    if ok(mid):
        high = mid
    else:
        low = mid + 1


print(low)
