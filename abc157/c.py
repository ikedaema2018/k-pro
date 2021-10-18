inputs = [
'3 1',
'1 0'
]


def input():
    return inputs.pop(0)


N, M = map(int, input().split(' '))
_result = [-1] * N

for _ in range(M):
    s, c = map(int, input().split(' '))
    if _result[s - 1] == -1 or _result[s - 1] == c:
        _result[s - 1] = c
    else:
        print(-1)
        break
else:
    if _result[0] == -1 and N == 1:
        _result[0] = 0
    elif _result[0] == -1:
        _result[0] = 1
    if _result[0] == 0 and N > 1:
        print(-1)
    else:
        a = ("").join(map(lambda x: '0' if x == -1 else str(x), _result))
        print(a)


