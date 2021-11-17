inputs = [
    '3',
    'ABCDEF',
    '3',
    '2 0 0',
    '1 6 3',
    '1 4 2'
]


def input():
    return inputs.pop(0)


N = int(input())
S = list(input())
Q = int(input())
queries = [list(map(int, input().split(' '))) for _ in range(Q)]

is_reverse = False
for t, a, b in queries:
    if t == 2:
        is_reverse = not is_reverse
    else:
        _a = a
        _b = b
        if is_reverse:
            if a > N and b > N:
                _a = a - N
                _b = b - N
            elif a <= N and b <= N:
                _a = a + N
                _b = b + N
            else:
                _a = b - N if b > N else b + N
                _b = a - N if a > N else a + N
        tmp = S[_a - 1]
        S[_a - 1] = S[_b - 1]
        S[_b - 1] = tmp
if is_reverse:
    pos = S[N:]
    pre = S[:N]
    print("".join((pos + pre)))
else:
    print("".join(S))