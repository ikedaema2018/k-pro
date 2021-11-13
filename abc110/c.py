inputs = [
    'abcdefghijklmnopqrstuvwxyz',
    'ibyhqfrekavclxjstdwgpzmonu'
]


def input():
    return inputs.pop(0)


S = list(input())
T = list(input())

conditions = {}

for i in range(len(S)):
    if S[i] in conditions and conditions[S[i]] != T[i]:
        print('No')
        break
    if T[i] in conditions and conditions[T[i]] != S[i]:
        print('No')
        break
    conditions[S[i]] = T[i]
    conditions[T[i]] = S[i]
else:
    print('Yes')