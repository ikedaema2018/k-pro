inputs = [
    'ooo???xxxx'
]


def input():
    return inputs.pop(0)

o_l = [-1] * 10
hatena_l = [-1] * 10
x_l = [-1] * 10
S = input()

for i in range(10):
    s = S[i]
    if s == 'o':
        o_l[i] = 1
    elif s == '?':
        hatena_l[i] = 1
    elif s == 'x':
        x_l[i] = 1

import copy
result = 0
for i in [123]:
    remain_o = copy.copy(o_l)
    snum = str(i).rjust(4, '0')
    lll = list(map(int, list(snum)))
    for l in lll:
        if o_l[l] != 1 and hatena_l[l] != 1:
            break
        if remain_o[l] == 1:
            remain_o[l] = -1
    else:
        if remain_o.count(1) < 1:
            result += 1
print(result)
