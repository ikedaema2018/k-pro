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


import math
def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))


N = int(input())
S = ["".join(sorted(list(input()))) for _ in range(N)]
S = sorted(S)

ans = 0
c = 1
bef = S[0]
for s in S[1:]:
    if bef == s:
        c = c + 1
    else:
        if c > 1:
            ans = ans + combinations_count(c, 2)
        c = 1
    bef = s
else:
    if c > 1:
        ans = ans + combinations_count(c, 2)

print(ans)
