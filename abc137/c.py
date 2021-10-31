inputs = [
    '5',
    'abaaaaaaaa',
    'oneplustwo',
    'aaaaaaaaba',
    'twoplusone',
    'aaaabaaaaa'
]


def input():
    return inputs.pop(0)


N = int(input())
S = []
for _ in range(N):
    S.append(input())

counted_s = []
for s in S:
    _s = list(s)
    h = {}
    for c in _s:
        if not h.get(c):
            h[c] = 1
        else:
            h[c] += 1
    counted_s.append(h)

result = 0
from itertools import combinations

def match(_a, _b):
    a_keys = _a.keys()
    b_keys = _b.keys()
    if len(a_keys) != len(b_keys):
        return False
    for a_key in a_keys:
        if not (a_key in _b) or _a[a_key] != _b[a_key]:
            return False
    else:
        return True

result = 0
for counted_2 in combinations(counted_s, 2):
    a = counted_2[0]
    b = counted_2[1]
    if match(a, b):
        result += 1

print(result)