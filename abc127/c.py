inputs = [
    '100000 1',
    '1 100000'
]


def input():
    return inputs.pop(0)

N, M = map(int, input().split(' '))
lrs = [list(map(int, input().split(' '))) for _ in range(M)]
ll = [''] * N
rr = [''] * N

for i in reversed(range(len(lrs))):
    lr = lrs[i]
    l, r = lr
    ll[l - 1] = 'l'
    rr[r - 1] = 'r'

l_idx = N - 1 - list(reversed(ll)).index('l')
r_idx = rr.index('r')
print(max(0, r_idx - l_idx + 1))
