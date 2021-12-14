inputs = [
    '1',
    '1'
]


def input():
    return inputs.pop(0)


N = int(input())
P = map(int, input().split(' '))

import sys
m = sys.maxsize
ans = 0
for p in P:
    if m > p:
        ans = ans + 1
        m = p
print(ans)