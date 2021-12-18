inputs = [
    '4 5'
]


def input():
    return inputs.pop(0)


L, R = map(int, input().split(' '))
import sys
ans = sys.maxsize
for i in range(L, R):
    for j in range(i + 1, R + 1):
        amari = (i * j) % 2019
        ans = min(ans, amari)
        if ans == 0:
            break
    if ans == 0:
        break
print(ans)