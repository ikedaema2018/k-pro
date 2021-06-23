# https://atcoder.jp/contests/joi2010ho/tasks/joi2010ho_a
import itertools
inputs = [
    '7 5',
    '2',
    '1',
    '1',
    '3',
    '2',
    '1',
    '2',
    '-1',
    '3',
    '2',
    '-3'
]


def input():
    return inputs.pop(0)


n, m = list(map(int, input().split()))
l = [0] * (n - 1)
for i in range(n - 1):
    l[i] = int(input())
towns = [0] + list(itertools.accumulate(l))

current = 0
result = 0
for a in range(m):
    nxt = int(input()) + current
    result += abs(towns[nxt] - towns[current]) % 10**5
    current = nxt
print(result % 10**5)