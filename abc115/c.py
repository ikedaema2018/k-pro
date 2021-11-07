inputs = [
    '5 3',
    '5',
    '7',
    '5',
    '7',
    '7'
]


def input():
    return inputs.pop(0)


N, K = map(int, input().split(' '))
H = []
for i in range(N):
    H.append(int(input()))
import sys
res = sys.maxsize

l = 0
r = K - 1
H = sorted(H)

while r < N:
    res = min(res, H[r] - H[l])
    r += 1
    l += 1

print(res)




