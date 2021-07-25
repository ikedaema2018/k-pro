inputs = [
    '2',
    'FLIP',
    '2',
    '2 0 0',
    '1 1 4'
]


def input():
    return inputs.pop(0)


N = int(input())
S = list(input())
Q = int(input())
queries = [list(map(int, input().split())) for z in range(Q)]
pre = S[0:N]
post = S[N:]


def change_idx(a, b):
    global pre
    global post
    _a = a % N
    _b = b % N
    if is_reverse:
        if a >= N:
            tmp = pre[_a]
            pre[_a] = pre[_b]
            pre[_b] = tmp
        elif b >= N:
            tmp = pre[_b]
            pre[_b] = post[_a]
            post[_a] = tmp
        else:
            tmp = post[_a]
            post[_a] = post[_b]
            post[_b] = tmp
    else:
        if a >= N:
            tmp = post[_a]
            post[_a] = post[_b]
            post[_b] = tmp
        elif b >= N:
            tmp = pre[_a]
            pre[_a] = post[_b]
            post[_b] = tmp
        else:
            tmp = pre[_a]
            pre[_a] = pre[_b]
            pre[_b] = tmp

is_reverse = False


for t, i_a, i_b in queries:
    if t == 1:
        change_idx(i_a - 1, i_b - 1)
    else:
        is_reverse = not is_reverse

if is_reverse:
    print("".join(post + pre))
else:
    print("".join(pre + post))