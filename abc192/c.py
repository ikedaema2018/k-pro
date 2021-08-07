inputs = [
    '2',
    'FLIP',
    '6',
    '1 1 3',
    '2 0 0',
    '1 1 2',
    '1 2 3',
    '2 0 0',
    '1 1 4',
]


def input():
    return inputs.pop(0)


N = int(input())
S = input()
Q = int(input())
is_reverse = False
l_s = list(S)
for _ in range(Q):
    t, a, b = list(map(int, input().split()))
    _a = a - 1
    _b = b - 1

    if t == 1:
        if is_reverse:
            _a_r = N + _a if _a < N else _a - N
            _b_r = N + _b if _b < N else _b - N
            tmp = l_s[_a_r]
            l_s[_a_r] = l_s[_b_r]
            l_s[_b_r] = tmp
        else:
            tmp = l_s[_a]
            l_s[_a] = l_s[_b]
            l_s[_b] = tmp
    else:
        is_reverse = not is_reverse


if is_reverse:
    print(''.join(l_s[N:] + l_s[:N]))
else:
    print(''.join(l_s))
