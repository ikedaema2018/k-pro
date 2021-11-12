inputs = [
    'abcdefghijklmnopqrstuvwxyz',
    'ibyhqfrekavclxjstdwgpzmonu'
]


def input():
    return inputs.pop(0)


S = list(input())
T = list(input())

conditions = {}
trans_s = {}

for i in range(len(S)):
    s = conditions[S[i]] if S[i] in conditions else S[i]
    if s != T[i]:
        if s in trans_s or T[i] in trans_s.values():
            print('No')
            break
        conditions[S[i]] = T[i]
        conditions[T[i]] = S[i]
        trans_s[S[i]] = T[i]
    else:
        continue
else:
    print('Yes')



