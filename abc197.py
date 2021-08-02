inputs = [
    '3',
    '1 5 7'
]


def input():
    return inputs.pop(0)


N = int(input())
A = list(map(int, input().split()))
import sys
m = sys.maxsize
for i in range(2 ** (N - 1)):
    i_s = []
    for j in range(N - 1):
        if (i >> j) & 1:
            i_s.append(j + 1)
    if len(i_s) == 0:
        continue
    S = []
    pre = -1
    for j in range(len(i_s)):
        d = i_s[j]
        if pre == -1 and j == (len(i_s) - 1):
            S.append(A[0:d])
            S.append(A[d:])
        elif pre == -1:
            S.append(A[0:d])
        elif j == (N - 1):
            S.append(A[pre:d])
            S.append(A[d:])
        else:
            S.append(A[pre:d])
        pre = d
    ss = []
    for s in S:
        if len(s) == 0:
            continue
        sss = s[0]
        for ssss in s[1:]:
            sss = sss | ssss
        ss.append(sss)
    if len(ss) == 0:
        continue
    xx = ss[0]
    for x in ss[1:]:
        xx = xx ^ x
    m = min(m, xx)
print(m)

