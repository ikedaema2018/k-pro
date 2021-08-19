inputs = [
    11
]


def input():
    return inputs.pop(0)


N = int(input())
ans = 18
ss = str(N)
ls = list(ss)
for bit in range(2 ** len(ss)):
    sss = []
    for j in range(len(ss)):
        if (bit >> j) & 1:
            sss.append(ls[j])
    if len(sss) == 0:
        continue
    target = int(''.join(sss))
    if target % 3 == 0:
        ans = min(len(ss) - len(sss), ans)

if ans == 18:
    print(-1)
else:
    print(ans)


