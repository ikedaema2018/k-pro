inputs = [
    '100 0',
    ''
]


def input():
    return inputs.pop(0)


X, N = map(int, input().split(' '))
s = input()
P = [] if s == '' else list(map(int, s.split(' ')))
_P = []

for i in list(range(-1, 100 + 2)):
    if i in P:
        continue
    _P.append(i)

diff = 102
ans = -1
for i in _P:
    _diff = abs(X - i)
    if _diff < diff:
        diff = _diff
        ans = i
print(ans)
